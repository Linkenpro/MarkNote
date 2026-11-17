# VPS 运行维护

以 Debian + systemd 为例。除标注为本地 PowerShell 的命令外，均在服务器执行。`vps.example.com` 为占位域名，`50501` 为统一的 SSH 端口示例。

## 专题入口

| 内容 | 笔记 |
| --- | --- |
| 基础命令 | [Debian](../Debian/Debian.md) |
| 网站、Nginx、HTTPS、Node.js | [Web](Web.md) |
| 数据库与远程读取 | [MariaDB](MariaDB.md) |
| Python 与定时采集 | [Python](Python.md) |
| 代理服务 | [3x-ui](3x-ui.md) |
| 容器安装与运行 | [Docker](../Docker/Docker.md) |

## 初始化

首次使用已有管理员或供应商提供的 root 账户登录；root 环境中可省略 sudo。若最小系统未安装 sudo，先由 root 安装。

```bash
sudo apt update
sudo apt upgrade
sudo apt install sudo curl wget nano git ufw
sudo timedatectl set-timezone Asia/Shanghai
timedatectl
```

Fail2ban 为可选工具，安装后还需确认 SSH jail、日志来源及实际端口配置，不能把安装成功当作已生效。

## 管理员与公钥

服务器创建管理员：

```bash
sudo adduser admin
sudo usermod -aG sudo admin
sudo install -d -m 700 -o admin -g admin /home/admin/.ssh
sudo nano /home/admin/.ssh/authorized_keys
```

在本地 PowerShell 查看已有公钥，并将完整一行粘贴到上面的文件中；文件名按实际密钥替换：

```powershell
Get-Content "$env:USERPROFILE/.ssh/id_ed25519.pub"
```

服务器设置权限：

```bash
sudo chown admin:admin /home/admin/.ssh/authorized_keys
sudo chmod 600 /home/admin/.ssh/authorized_keys
```

新增密钥时追加一行，保留仍在使用的密钥。另开终端测试 admin 登录及 `sudo -i`，成功后再收紧 SSH 配置。

## SSH

### 密钥登录

编辑 `/etc/ssh/sshd_config`，同时检查其 Include 引入的配置文件和 Match 条件。以下为仅使用公钥的示例设置：

```text
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin prohibit-password
```

`prohibit-password` 保留 root 公钥登录；若不需要 root 远程登录可改为 `no`。锁定 root 密码不是配置 SSH 公钥登录的必要步骤。

保存后先检查，再加载：

```bash
sudo /usr/sbin/sshd -t
sudo /usr/sbin/sshd -T
sudo systemctl reload ssh
```

仅在语法检查成功后执行 reload；`sshd -T` 用于检查生效配置，有 Match 条件时还需结合目标用户、地址核对。保留当前会话，另开终端验证公钥登录。

### 更换端口

先在供应商防火墙与 UFW 放行 `50501/tcp`，保留原端口。编辑 SSH 配置，迁移期间同时监听：

```text
Port 22
Port 50501
```

```bash
sudo ufw allow 50501/tcp
sudo /usr/sbin/sshd -t
sudo systemctl reload ssh
sudo ss -tlnp
```

语法检查通过后再加载。本地新建连接：

```powershell
ssh -p 50501 admin@vps.example.com
```

确认新连接及 sudo 可用后，删除 SSH 配置中的 `Port 22`，再次检查并加载，最后删除旧防火墙规则。上述流程适用于 `ssh.service` 管理的监听；使用 `ssh.socket` 的系统需另行核对 socket 配置。更换端口不能替代密钥认证。

## 防火墙

启用前先确认当前 SSH 端口已放行；以下假设首次连接仍使用 22：

```bash
sudo ufw allow 22/tcp
sudo ufw enable
sudo ufw status verbose
```

按服务需要开放 Web 端口：

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ss -tulpn
```

SSH 完成迁移后，按实际存在的规则删除旧放行项：

```bash
sudo ufw status numbered
sudo ufw delete allow 22/tcp
# 仅在原先添加过 OpenSSH 应用规则时删除该项
sudo ufw delete allow OpenSSH
sudo ufw status verbose
```

供应商安全组也需同步检查。Docker 发布端口与 UFW 的交互见 [Docker](../Docker/Docker.md#debian-服务器)。

## 日常维护

常用软件包与服务命令见 [Debian](../Debian/Debian.md)。

```bash
sudo journalctl -u ssh -f
df -h
sudo du -xhd1 /var /root 2>/dev/null | sort -hr | head -n 15
sudo journalctl --disk-usage
```

`/root` 是 root 用户的主目录，文件系统根目录是 `/`。若系统配置了相应日志输出，也可查看 `/var/log/auth.log`。

确认清理范围后使用：

```bash
sudo apt clean
sudo apt autoremove
# 删除超过 3 天的已归档 journal 日志，会丢失相应排查记录
sudo journalctl --vacuum-time=3d
```

限制持久化 journal 占用时，在 `/etc/systemd/journald.conf` 的 `[Journal]` 节中设置：

```ini
[Journal]
SystemMaxUse=200M
```

```bash
sudo systemctl restart systemd-journald
```

该选项针对持久化 journal；临时 journal 对应 `RuntimeMaxUse`，其他文本日志另行管理。pip 缓存使用对应 Python 环境的 `python -m pip cache purge` 清理；VS Code Server 旧版本先确认不再使用，再按具体版本处理。

## 参考

- [OpenSSH 服务端配置](https://man.openbsd.org/sshd_config)
- [journald 配置](https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html)
