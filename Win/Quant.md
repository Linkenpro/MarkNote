量化

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