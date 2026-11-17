# VPS MariaDB

返回 [VPS](VPS.md)。数据库名、表名保留原量化项目示例，密码全部使用占位符。

## 安装与管理登录

```bash
sudo apt update
sudo apt install mariadb-server
sudo systemctl enable --now mariadb
sudo systemctl status mariadb
sudo mariadb-secure-installation
sudo mariadb
```

Debian 常见安装使用 Unix socket 验证本地 root，通常无需另设数据库 root 密码。初始化向导按实际版本和现有认证配置回答，不照抄固定选项。旧版本工具可能名为 `mysql_secure_installation`。

应用和远程查询使用独立账户，不使用数据库 root。

## 数据库与查询

以下在 MariaDB 客户端执行：

```sql
SHOW VARIABLES LIKE 'datadir';
CREATE DATABASE IF NOT EXISTS binance_quant DEFAULT CHARACTER SET utf8mb4;
USE binance_quant;
SHOW TABLES;
SELECT * FROM btc_swap_5m ORDER BY BeiJing DESC LIMIT 3;
```

数据目录通常为 `/var/lib/mysql/`，以查询结果为准。最后一条语句要求表 `btc_swap_5m` 和字段 `BeiJing` 已存在。

## 只读访问账户

为通过本机 TCP / SSH 隧道进行查询创建独立账户；先替换密码：

```sql
CREATE USER 'quant_reader'@'127.0.0.1' IDENTIFIED BY 'REPLACE_WITH_STRONG_PASSWORD';
GRANT SELECT ON binance_quant.* TO 'quant_reader'@'127.0.0.1';
SHOW GRANTS FOR 'quant_reader'@'127.0.0.1';
```

该账户只能查询。采集程序写入数据库时另建写入账户，按实际操作授权。MariaDB 需监听本机 `127.0.0.1:3306`；不必向公网开放 3306。

## Windows 通过 SSH 隧道查询

在本地 PowerShell 建立隧道并保持终端运行：

```powershell
ssh -N -o ExitOnForwardFailure=yes -L 127.0.0.1:13306:127.0.0.1:3306 -p 50501 admin@vps.example.com
```

需允许该 SSH 用户进行 TCP 转发。客户端连接参数：

| 配置项 | 值 |
| --- | --- |
| 主机 | `127.0.0.1` |
| 端口 | `13306` |
| 用户 | `quant_reader` |
| 密码 | 创建账户时设置的密码 |
| 数据库 | `binance_quant` |

原笔记使用 `sshtunnel` 在 Python 中建立隧道；这里改由 OpenSSH 建立，Python 只负责查询。在另一个本地终端安装依赖并运行：

```powershell
python -m pip install pandas pymysql
```

```python
from getpass import getpass
import pandas as pd
import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    port=13306,
    user='quant_reader',
    password=getpass('MariaDB password: '),
    database='binance_quant',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)
try:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM btc_swap_5m ORDER BY BeiJing DESC LIMIT 500')
        frame = pd.DataFrame(cursor.fetchall())
    print(frame)
finally:
    connection.close()
```

## 参考

- [MariaDB 初始化工具](https://mariadb.com/docs/server/clients-and-utilities/deployment-tools/mariadb-secure-installation)
- [Unix socket 认证](https://mariadb.com/docs/server/reference/plugins/authentication-plugins/authentication-plugin-unix-socket)
