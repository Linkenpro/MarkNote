# Debian 命令速查

适用于 Debian 终端。示例中的路径、包名和用户名按实际替换；管理命令需 root 或 sudo 权限。部署流程见 [VPS](../VPS/VPS.md)。

## 文件与目录

| 命令 | 用途 |
| --- | --- |
| `ls -lah` | 列出文件，包括隐藏文件 |
| `cd /var/log` / `cd ..` | 切换目录 / 返回上级 |
| `pwd` | 显示当前目录 |
| `mkdir -p ~/demo/logs` | 创建目录及缺少的父目录 |
| `cp notes.txt notes.bak` | 复制文件 |
| `cp -r demo demo-backup` | 复制目录 |
| `mv old.txt new.txt` | 移动或重命名 |
| `touch notes.txt` | 创建空文件，或更新已有文件的时间 |
| `rm -i notes.bak` | 确认后删除文件 |
| `rmdir empty-dir` | 删除空目录 |
| `cat notes.txt` | 查看文件内容 |
| `less /var/log/dpkg.log` | 分页查看，按 q 退出 |
| `head -n 20 notes.txt` | 查看前 20 行 |
| `tail -n 20 notes.txt` | 查看后 20 行 |
| `tail -f app.log` | 持续查看新增日志 |

## 软件包

| 命令 | 用途 |
| --- | --- |
| `sudo apt update` | 刷新软件包索引，不执行升级 |
| `sudo apt upgrade` | 升级可升级的软件包 |
| `sudo apt install nginx` | 安装软件 |
| `sudo apt install ./package.deb` | 安装本地包并处理依赖 |
| `sudo dpkg -i package.deb` | 直接安装本地包；依赖问题需另行处理 |
| `sudo apt remove nginx` | 卸载软件，保留配置 |
| `sudo apt purge nginx` | 卸载软件并删除包管理的配置 |
| `sudo apt autoremove` | 检查并移除不再需要的自动安装依赖 |
| `sudo apt clean` | 清理下载的软件包缓存 |
| `apt search keyword` | 搜索软件包 |
| `apt show nginx` | 查看软件包信息 |

软件源配置可能位于 `/etc/apt/sources.list` 或 `/etc/apt/sources.list.d/`；修改后运行 `apt update`。

## 用户与权限

| 命令 | 用途 |
| --- | --- |
| `whoami` / `id` | 当前用户名 / 用户及组信息 |
| `sudo -i` / `su -` | 经 sudo / root 密码进入 root 登录环境 |
| `sudo adduser demo` | 创建用户 |
| `sudo deluser demo` | 删除用户，默认保留主目录 |
| `sudo passwd demo` | 设置用户密码 |
| `sudo usermod -aG sudo demo` | 将用户加入 sudo 组 |
| `chmod 600 .env` | 仅所有者可读写 |
| `chmod 755 script.sh` | 所有者可写，所有用户可读及执行 |
| `sudo chown demo:demo notes.txt` | 修改文件所属用户和组 |

## 服务与日志

| 命令 | 用途 |
| --- | --- |
| `systemctl status ssh` | 查看服务状态 |
| `sudo systemctl start ssh` / `sudo systemctl stop ssh` | 启动 / 停止服务 |
| `sudo systemctl restart ssh` | 重启服务 |
| `sudo systemctl enable ssh` / `sudo systemctl disable ssh` | 启用 / 禁用开机自启，不改变当前运行状态 |
| `sudo journalctl -u ssh -f` | 持续查看服务日志 |
| `hostnamectl` | 查看主机信息 |
| `timedatectl` | 查看时间、时区与同步状态 |
| `sudo reboot` / `sudo shutdown -h now` | 重启 / 立即关机 |

## 网络

| 命令 | 用途 |
| --- | --- |
| `ip addr` / `hostname -I` | 查看网络地址 |
| `ip route` | 查看路由 |
| `sudo ss -tulpn` | 查看 TCP/UDP 监听端口及进程 |
| `ping -c 4 example.com` | 测试连通性；不响应不一定代表服务不可达 |
| `curl -I https://example.com` | 查看 HTTP 响应头 |
| `wget https://example.com/file.zip` | 下载文件 |
| `sudo ufw status verbose` | 查看 UFW 状态，需先安装 |
| `sudo nft list ruleset` | 查看 nftables 规则，需相应工具及权限 |

网络由 ifupdown 管理时查看 `/etc/network/interfaces`；使用 NetworkManager 时使用 `nmcli`，不要混用配置方式。远程防火墙操作见 [VPS](../VPS/VPS.md#防火墙)。

## 资源监控

| 命令 | 用途 |
| --- | --- |
| `top` / `htop` | 交互查看进程，htop 需另行安装 |
| `ps aux` | 查看进程快照 |
| `kill PID` | 请求进程退出，替换 PID 为实际数字 |
| `kill -9 PID` | 强制终止，不执行正常清理；仅在正常退出失败时使用 |
| `free -h` | 查看内存 |
| `df -h` | 查看文件系统空间 |
| `du -sh /var/log` | 查看目录占用 |
