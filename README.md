# 攻击日志分析工具

## 一句话说明
一个用 Python 写的 Web 访问日志分析工具：从日志中识别 5 类常见 Web 攻击，统计攻击类型分布，并定位可疑来源 IP。

## 功能
1. 统计攻击类型 
2. 检测可疑 IP
3. 结果同时打印到终端，并写入 `output/report.txt`（目录会自动创建）。

## 环境要求
- 已在 Python 3.13 测试
- 本项目零第三方依赖
- 无需 `pip install`

## 运行
`python main.py`

## 参数
| 参数  | 默认值              | 说明             |
|-------|---------------------|------------------|
| --log | resource/attack.log | 攻击日志默认位置 |
| --top | 10                  | 输出Top N        |

## 输出示例
以下是 `python main.py --top 3` 的输出：
```
========类型统计：==========
NORMAL               39
SQL_INJECTION        18
SCANNER              15
========可疑 IP：==========
203.0.113.201        13
203.0.113.45         11
91.240.118.172       11
```
## 支持的攻击类型
| 类型              | 命中特征                                                                                                                                                   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SQL_INJECTION     | UNION SELECT 联合查询注入；OR '1'='1 布尔盲注；SLEEP( 时间盲注；'-- / '# 注释截断；(SELECT 子查询                                                          |
| XSS               | 任意 HTML 标签（`<script>`、`<img>` 等，即 < 后紧跟字母）；onerror=、onload= 等 on 开头的属性；javascript: 伪协议                                          |
| COMMAND_INJECTION | ; 与 && 命令拼接；反引号命令替换；cat /、whoami、wget、nc - 等命令名                                                                                       |
| PATH_TRAVERSAL    | 读取 `/etc/passwd`、`/etc/shadow` 等敏感系统文件；访问 `/proc/self`、`/var/log`；≥3 组`../`或`..\`多层向上跳目录                                           |
| SCANNER           | 访问 phpmyadmin、admin.php 等后台；`.env/.git/.bak`源码 / 配置备份；wp-login、xmlrpc.php 等 WordPress 敏感路径；phpinfo、sql 备份、solr、aws 凭证、adminer |  


## 文件说明
| 文件                | 作用           |
|---------------------|----------------|
| main.py             | 入口           |
| rules.py            | 攻击特征规则表 |
| parser.py           | 日志行解析     |
| resource/attack.log | 示例数据       |
