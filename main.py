from pathlib import Path
from collections import Counter
import parser
from rules import classify
import argparse





def main():
    # 1. 造一个"参数解析器"
    BASE = Path(__file__).parent
    p = argparse.ArgumentParser(description="这个程序用来解析命令行参数" )

    # 2. 声明"我要接收一个叫 --log 的参数"
    p.add_argument("--log",default= BASE /"resource/attack.log")
    p.add_argument("--top",type=int ,default=10)

    # 3. 真正去读命令行
    args = p.parse_args()


    path = Path(args.log)
    lines = path.read_text(encoding="utf-8").splitlines()

    entries = [parser.parse_line(l) for l in lines]

    # 把每一行变成一对：(IP, 标签)
    labeled = []
    for e in entries:
        label = classify(e.path)
        labeled.append((e.ip, label))



    # 统计 1：攻击类型
    type_counter = Counter()
    for ip, label in labeled:
        type_counter[label] += 1

    # 统计 2：可疑 IP
    ip_counter = Counter()
    for ip, label in labeled:
        if label != "NORMAL":
            ip_counter[ip] += 1

    print("========类型统计：==========")
    for name, n in type_counter.most_common(args.top):
        print(f"{name:20} {n}")
    print("========可疑 IP：==========")
    for ip, n in ip_counter.most_common(args.top):
        print(f"{ip:20} {n}")

    out_dir = BASE / "output"
    out_dir.mkdir(parents=True, exist_ok=True)


    with open(out_dir / "report.txt", "w",encoding="utf-8") as f:
        f.write("========类型统计：==========\n")
        for name, n in type_counter.most_common(args.top):
            f.write(f"{name:20} {n}\n")
        f.write("========可疑 IP：==========\n")
        for ip, n in ip_counter.most_common(args.top):
            f.write(f"{ip:20} {n}\n")


if __name__ == "__main__":
    main()


