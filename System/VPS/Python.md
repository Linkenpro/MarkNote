# VPS Python 与定时采集

返回 [VPS](VPS.md)。保留原项目路径 `/root/quant`；下面的项目操作和 crontab 均由 root 执行。改用普通用户部署时，应一并调整路径、所有权及任务所属用户。

## 虚拟环境

```bash
sudo apt install python3-venv cron
mkdir -p /root/quant/logs
cd /root/quant
python3 -m venv venv
/root/quant/venv/bin/python -m pip install -r requirements.txt
```

`requirements.txt` 需由项目提供。交互式 Bash 中可激活环境：

```bash
source /root/quant/venv/bin/activate
python binance_ccxt.py
```

定时任务直接使用虚拟环境的 Python，避免依赖激活脚本。

## API 配置

在 `/root/quant/.env` 保存配置，不提交到 Git：

```dotenv
BINANCE_API_KEY=REPLACE_WITH_API_KEY
BINANCE_SECRET=REPLACE_WITH_API_SECRET
```

```bash
chmod 600 /root/quant/.env
/root/quant/venv/bin/python -m pip install python-dotenv
```

在程序初始化时显式加载：

```python
import os
from dotenv import load_dotenv

load_dotenv('/root/quant/.env')
api_key = os.environ['BINANCE_API_KEY']
api_secret = os.environ['BINANCE_SECRET']
```

权限 `600` 只允许文件所有者读写，仍需核对所有者是否是运行程序的用户。不要依靠 cron 自动读取 `.bashrc`，也不要在 `.bashrc` 内加入对自身的 `source`。

## 定时采集

先手动确认脚本及依赖可运行：

```bash
cd /root/quant
/root/quant/venv/bin/python /root/quant/binance_ccxtSQL.py
sudo systemctl enable --now cron
timedatectl
crontab -e
```

当服务器时区为 `Asia/Shanghai` 时，以下任务每天北京时间 08:30 执行：

```cron
30 8 * * * cd /root/quant && /root/quant/venv/bin/python /root/quant/binance_ccxtSQL.py >> /root/quant/logs/cron.log 2>&1
```

Debian cron 默认使用 `/bin/sh`；直接调用解释器即可，不需要 `source`。如果服务器保留 UTC，应换算执行时间。日志目录必须事先存在并可写。

## 检查与排错

```bash
crontab -l
sudo systemctl status cron
sudo journalctl -u cron --since today
tail -n 50 /root/quant/logs/cron.log
```

| 现象 | 检查项 |
| --- | --- |
| 手动可运行，定时失败 | 用户、工作目录、解释器路径、环境变量 |
| 没有日志文件 | 日志目录存在与否、权限、任务是否触发 |
| API 认证失败 | `.env` 加载、权限配置、系统时间同步 |
| 数据时间不一致 | 系统时区、程序时区、数据库字段约定 |

项目日志 `data_fetcher.log` 按脚本实际写入位置查看；运行日志应另设轮转，避免无限增长。

## 本地传输

原项目位于 `/root`，下列 PowerShell 示例要求服务器保留 root 公钥登录：

```powershell
scp -P 50501 root@vps.example.com:/root/quant/binance_ccxtSQL.py .
scp -P 50501 ./btc5min.py root@vps.example.com:/root/quant/
```

普通用户部署时同时替换登录用户和项目路径。数据库访问见 [MariaDB](MariaDB.md)。

## 参考

- [Debian crontab 手册](https://manpages.debian.org/bookworm/cron/crontab.5.en.html)
