# E:\PythonProject1\W4\rules.py
# 2026-09-26 | W4-D5 | 状态：5条规则表已经建立 | 覆盖边界：unquote 解码（规则表未写）
from urllib.parse import unquote
import re

# ---- Step 1：解码（先不做分类）----
CASES = [
    "/search.php?q=%3Cscript%3Ealert(1)%3C/script%3E",
    "/ping.php?ip=127.0.0.1%3Bcat%20/etc/passwd",
    "/download.php?file=..%2f..%2f..%2fetc%2fpasswd",
    "/index.html",
]

RULES = [
    ("SQL_INJECTION",      r"union\s+select|(or|and)\s+'?\w'?\s*=\s*'?\w|\bsleep\s*\(|information_schema|extractvalue|drop\s+table|'\s*--|'\s*#|union\s+(all\s+)?select|\(\s*select"),   # 你测过的
    ("XSS",                r"<\w+|on\w+=|javascript:"),
    ("COMMAND_INJECTION",  r"cat\s+/|whoami|wget|nc\s+-|&&|`\w+`|;(?!\w+=)"),   # 先把你现在这版放进去
    ("PATH_TRAVERSAL",     r"/etc/passwd|/etc/shadow|windows/win\.ini|windows/boot\.ini|/proc/self|/var/log/|(\.\./){3,}|(\.\.\\){3,}"),
    ("SCANNER",            r"phpmyadmin|\.env|wp-login|\.git|wp-config|phpinfo\.|manager|\.sql|\.aws|/solr|admin\.php|\.bak|xmlrpc\.php|backup|adminer\.php"),
]

def classify(path):
    """给一条路径打标签；都没命中返回 'NORMAL'"""
    decoded = unquote(path)
    for name, pattern in RULES:
        if re.search(pattern, decoded, re.IGNORECASE):
            return name
    return "NORMAL"



if __name__ == "__main__":
    for c in CASES:
        print(f"原样: {c}")
        print(f"解码: {unquote(c)}")
        print()
