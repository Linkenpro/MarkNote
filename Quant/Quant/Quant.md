# 量化项目运维

记录 Debian VPS 上币安量化项目的时间同步、后台服务与文件传输。项目目录保留原部署路径，服务器地址用占位域名。

| 项目 | 示例 |
| --- | --- |
| SSH 地址和端口 | `root@vps.example.com:50501` |
| 项目目录 | `/root/quant/binance` |
| Python 解释器 | `/root/quant/venv/bin/python` |
| 本地目录 | `D:/Python/Program/quant` |

## 币安签名请求时间偏差

币安现货签名请求的 `recvWindow` 默认是 5000 毫秒，用于限制请求可接受的滞后时间。请求时间戳还必须早于服务器时间加 1 秒，因此允许的偏差并非正负各 5 秒。若使用 USDⓈ-M 合约，按对应接口文档核对签名参数。

遇到时间戳报错，先确认 VPS 系统时钟是否同步，再检查程序是否在签名前生成当前时间戳，以及是否误把秒当成毫秒或复用了旧请求时间。程序可用 `time.time_ns() // 1_000_000` 生成毫秒级 Unix 时间戳。系统时区只影响时间的显示方式。

### 在 Debian 检查同步

如果机器已配置可用的时间同步服务，先检查现有服务。以下以 chrony 为例。

```bash
sudo apt update
sudo apt install chrony
sudo systemctl enable --now chrony
timedatectl status
chronyc tracking
chronyc sources -v
```

在 `chronyc sources -v` 中检查是否已选中时间源（通常标记为 `^*`），再用 `chronyc tracking` 查看剩余校正量。若偏差很大且必须立即校准，确认同步源可用后，可在维护窗口运行 `sudo chronyc makestep`。系统时间会立即跳变，先暂停对时间敏感的任务，校准后再复查。

## 用 systemd 运行服务

以下示例适用于常驻进程。定时采集任务见 [VPS Python 与定时采集](../../System/VPS/Python.md)。

确认入口脚本、虚拟环境和应用配置就绪后，按下方内容创建 `/etc/systemd/system/quant.service`。

```ini
[Unit]
Description=Binance quant service
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/quant/binance
ExecStart=/root/quant/venv/bin/python -u /root/quant/binance/main.py
Restart=on-failure
RestartSec=5s
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

示例沿用原部署的 root 用户及目录。改用普通用户时，需一并迁移项目目录、虚拟环境及配置文件，并核对权限。这里仅在异常退出时尝试自动重启。若程序需要外部网络，仍需按程序自身的连接和重试逻辑处理断线。

### 启动与维护

```bash
sudo systemd-analyze verify /etc/systemd/system/quant.service
sudo systemctl daemon-reload
sudo systemctl enable --now quant.service
sudo systemctl status quant.service
sudo journalctl -u quant.service -n 50
```

| 命令 | 用途 |
| --- | --- |
| `sudo systemctl restart quant.service` | 更新代码后重启 |
| `sudo systemctl stop quant.service` | 停止当前进程 |
| `sudo journalctl -u quant.service -f` | 持续查看标准输出和错误输出 |

修改服务配置后，先验证，再执行 `daemon-reload` 并重启。若已有工具仍读取原先的 `log/trading.log` 和 `log/error.log`，可以保留原服务中两条 `append:` 配置，并提前创建日志目录。此时用 `tail -f` 查看这两个文件，并单独安排日志轮转。

## 在 Windows 传输文件

以下命令在本地 PowerShell 执行。`scp` 使用大写 `-P` 指定 SSH 端口。示例要求 VPS 已允许对应账户通过 SSH 登录，并且目标目录已存在。

```powershell
# 下载项目目录的可见文件
scp -r -P 50501 "root@vps.example.com:/root/quant/binance/*" "D:/Python/Program/quant/"

# 仅上传指定子目录的内容
scp -r -P 50501 "D:/Python/Program/quant/report/*" "root@vps.example.com:/root/quant/binance/report/"
scp -r -P 50501 "D:/Python/Program/quant/trade/*" "root@vps.example.com:/root/quant/binance/trade/"
```

整目录回传使用同样的格式，把本地源改为 `D:/Python/Program/quant/*`、远程目标改为 `/root/quant/binance/`。执行前检查同名文件和待传输范围，避免覆盖服务器配置、数据库或报告。

### 下载 SQLite 数据

服务正在写入 SQLite 时，先通过 SQLite 的备份机制生成一致性快照，再下载快照。以下假设服务器已安装 `sqlite3`，库文件名和备份路径按实际替换。

在 VPS 上生成备份。

```bash
sqlite3 /root/quant/binance/db/crypto_data.db ".backup /root/quant/crypto_data-backup.db"
```

在本地 PowerShell 下载。

```powershell
scp -P 50501 "root@vps.example.com:/root/quant/crypto_data-backup.db" "D:/Python/Program/quant/db/"
```

## 参考

- [Binance 现货请求签名](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/request-security)
- [Binance USDⓈ-M 合约接口](https://developers.binance.com/docs/derivatives/usds-margined-futures/general-info)
- [chronyc 手册](https://chrony-project.org/doc/4.6/chronyc.html)
- [systemd 服务配置](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [SQLite 在线备份](https://www.sqlite.org/backup.html)
