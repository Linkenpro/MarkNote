##### 量化

###### 量化交易时间漂移

币安 API 要求客户端请求的时间戳与服务器时间的偏差不能超过 5000毫秒（5秒）（默认 recvWindow）。
结合你刚才修改系统时间的操作，这个问题通常由以下两种情况引起：
时间不同步：你的 VPS 系统时间与币安服务器时间偏差超过 5 秒。虽然你手动设置了时间，但如果没有开启 NTP 同步，VPS 的硬件时钟可能走得快或慢，导致几分钟后又偏了。
代码逻辑问题：你的 Python 代码在生成签名时，使用的时间戳不是“当前实时时间”，而是硬编码的、过期的或者逻辑错误的时间。

- 安装并启用 chrony

  ```
  apt update
  apt install -y chrony
  ```

- 设置开机启动

  ```
  systemctl start chrony
  systemctl enable chrony
  ```

- 强制立即同步时间

  ```
  # 停止 chrony 服务以便强制步进时间
  systemctl stop chrony
  
  # 强制立即校准时间
  chronyd -q 'server pool.ntp.org iburst'
  
  # 重新启动服务
  systemctl start chrony
  ```

- 验证状态

  ```
  timedatectl status
  ```

  > `System clock synchronized: yes`
  >
  > `NTP service: active`

##### 量化Systemd守护进程

###### 1.创建 Service 配置文件

```
sudo nano /etc/systemd/system/quant.service
```

粘贴内容

```
[Unit]
Description=Binance_quant
After=network.target

[Service]
# 设置工作目录
WorkingDirectory=/root/quant/binance/
# 推荐使用绝对路径执行python
ExecStart=/root/quant/venv/bin/python main.py
# 确保程序异常退出后自动重启，延迟 5 秒
Restart=always
RestartSec=5
User=root
# 统一将日志存放在工作目录下，确保文件夹权限
StandardOutput=append:/root/quant/binance/log/trading.log
StandardError=append:/root/quant/binance/log/error.log

[Install]
WantedBy=multi-user.target
```

###### 2.加载并启动服务

重载 Systemd 配置，每次修改 .service 文件后必须执行

```
sudo systemctl daemon-reload
```

设置开机自启动

```
sudo systemctl enable quant
```

启动服务命令

```
sudo systemctl start quant
```

**日常管理**

查看状态，是否在跑，以及最近的报错信息

```
sudo systemctl status quant
```

停止运行

```
sudo systemctl stop quant
```

重启服务（更新main.py)

```
sudo systemctl restart quant
```

实时查看日志,代替原来的 tail -f

```
journalctl -u quant -f
```

##### 管理quant文件夹

拉取文件

```
scp -r -P 50501 root@154.36.183.45:/root/quant/binance/* "D:\Python\Program\quant"
```

回传文件

```
scp -r -P 50501 "D:\Python\Program\quant\*" root@154.36.183.45:/root/quant/binance/
```

```
scp -r -P 50501 "D:\Python\Program\quant\report\*" root@154.36.183.45:/root/quant/binance/report/
```

回传

```
scp -r -P 50501 "D:\Python\Program\quant\trade\*" root@154.36.183.45:/root/quant/binance/trade/
```

只拉取数据库

```
scp -r -P 50501 root@154.36.183.45:/root/quant/binance/db/* "D:\Python\Program\quant\db"
```

