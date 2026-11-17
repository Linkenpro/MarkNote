# macOS

开发环境、网站同步与远程访问备忘。命令注明执行位置；服务器地址、端口、用户名和路径按实际环境替换。

## 开发环境

### Homebrew

按 [Homebrew 官网](https://brew.sh/) 的安装说明操作，安装后执行终端提示的 `brew shellenv` 配置。Apple Silicon 与 Intel Mac 的默认安装路径不同，不统一写死为 `/opt/homebrew`。

原环境使用本机 HTTP 代理端口 `7892`，仅在代理确实监听此端口时设置：

```bash
export https_proxy=http://127.0.0.1:7892
export http_proxy=http://127.0.0.1:7892
```

取消当前终端的代理环境变量：

```bash
unset https_proxy http_proxy
```

### OpenCode 接入 DeepSeek

在 [DeepSeek 开放平台](https://platform.deepseek.com/) 创建 API Key，保存在本机凭据配置中，不写入项目或笔记。

原接入流程：在项目目录运行 `opencode`，输入 `/connect`，选择 DeepSeek 并填写 Key。供应商入口和模型名称以所装版本及账户可用列表为准，不固定旧笔记中的模型名称。

## 网站文件与 Git

### 从 VPS 拉取文件

以下在 Mac 终端执行。`50501` 为原环境的 SSH 端口示例：

```bash
mkdir -p ~/openCode
scp -r -P 50501 root@服务器IP:/var/www/html ~/openCode/
cd ~/openCode/html
```

复制目录后，本地项目位于 `~/openCode/html`。先确认本地没有需要保留的同名文件。

### 初始化仓库

先创建忽略规则，再暂存和提交，避免把日志或环境变量文件提交进去。

项目根目录的 `.gitignore` 示例；已有文件时合并规则：

```gitignore
# 项目日志
quant/cron.log
quant/logs/*.json
*.log

# 系统与编辑器文件
.DS_Store
*.swp
*.swo
*~

# 临时文件、环境变量与构建输出
*.tmp
.env
.env.local
dist/
build/
```

在项目目录执行：

```bash
git init
git config user.name "你的名字"
git config user.email "your_email@example.com"
git status
git add .
git diff --cached --stat
git commit -m "Initial commit - pull from VPS"
```

这里的用户配置仅影响当前仓库。`.gitignore` 不会自动取消跟踪已经提交的文件。

### 修正最近一次提交作者

仅在需要修改最近一次提交时使用，会改写该提交；已共享的提交应先与协作者协调。

```bash
git commit --amend --reset-author --no-edit
```

## 文件同步

### rsync 手动推送

在 Mac 上先预览变更，再上传：

```bash
rsync -avzn --exclude='.git/' --exclude='.env*' -e "ssh -p 50501" ~/openCode/html/ root@服务器IP:/var/www/html/
rsync -avz --exclude='.git/' --exclude='.env*' -e "ssh -p 50501" ~/openCode/html/ root@服务器IP:/var/www/html/
```

`-n` 只预览；源目录末尾 `/` 表示同步目录内的内容。这里不使用 `--delete`，不会因本地缺少文件而删除远程多余文件。rsync 不会自动读取 `.gitignore`，其他日志和构建目录需按项目补充排除规则。

### fswatch 监听推送

先完成一次手动同步，并确认 SSH 认证可正常使用。以下在 Mac 前台运行，按 `Ctrl+C` 停止：

```bash
brew install fswatch
fswatch -o ~/openCode/html | while read -r event; do
  rsync -avz --exclude='.git/' --exclude='.env*' -e "ssh -p 50501" ~/openCode/html/ root@服务器IP:/var/www/html/
done
```

这是单向上传，不是双向同步或冲突合并；本地保存会触发上传到目标网站目录。

### VS Code SFTP

通过 `Cmd + Shift + P` 打开命令面板，选择 `SFTP: Sync Local -> Remote` 上传。

先核对 `.vscode/sftp.json` 中的目标路径和同步选项，避免启用删除远程多余文件的配置。同步命令并不等于只进行差异预览。基础配置见 [Windows 笔记](../Windows/Windows.md)。

## RustDesk 远程桌面

### VPS 服务端

RustDesk OSS 服务端包含两个组件：

| 组件 | 用途 |
| --- | --- |
| `hbbs` | ID 注册、连接协调与信令 |
| `hbbr` | 无法直连时转发中继流量 |

原笔记只安装了 `rustdesk-server-hbbs` 的 `1.1.15 amd64` 包，不能据此视为中继服务已完整部署。

从 [服务端 Releases](https://github.com/rustdesk/rustdesk-server/releases) 选择适合 VPS 系统和架构的版本，按 [官方部署说明](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/install/) 安装两个组件，并配置所需端口。

使用原笔记的 Debian 包部署方式时，可检查服务；名称和公钥路径需以实际安装结果为准：

```bash
systemctl status rustdesk-hbbs rustdesk-hbbr
systemctl cat rustdesk-hbbs
cat /var/lib/rustdesk-server/id_ed25519.pub
```

服务参数需要调整时，使用 systemd override，避免直接修改软件包自带的单元文件。公钥取自实际服务器，不复用示例 Key。

### Mac 被控端与其他客户端

安装 [RustDesk](https://rustdesk.com/zh/)，在网络配置中填写：

| 字段 | 值 |
| --- | --- |
| ID 服务器 | VPS 地址 |
| 中继服务器 | 实际 hbbr 地址 |
| Key | 服务端生成的公钥 |

按客户端提示授予 macOS 所需权限。其他设备配置同一服务端后，使用 Mac 的设备 ID，并通过被控端确认或配置的访问认证建立连接。

## FRP 内网穿透

公网 VPS 运行 `frps`，Mac 运行 `frpc`。以下示例将 VPS 的 `6000` 端口转发到 Mac 的 SSH `22` 端口。

### 前置条件

- 在 Mac 的“系统设置 → 通用 → 共享”中开启“远程登录”，选择允许登录的用户。
- 确认本地 SSH 服务和密钥登录正常，再配置公网转发。
- 两端使用兼容的 FRP 版本和相同认证令牌。

原笔记中的明文令牌已替换。若仍在使用，需在两端同步更换；编辑笔记不会撤销旧令牌或清除 Git 历史。

### VPS 安装与配置

从 [FRP Releases](https://github.com/fatedier/frp/releases) 下载与 VPS 系统和架构匹配的包。原笔记使用 `v0.68.1 linux_amd64`，此处作为历史版本记录，不代表最新版本。

在解压目录执行：

```bash
sudo install -m 755 frps /usr/local/bin/frps
sudo mkdir -p /etc/frp
sudo nano /etc/frp/frps.toml
```

写入配置，并将占位符替换为新生成的令牌：

```toml
bindPort = 7000
auth.method = "token"
auth.token = "<FRP_TOKEN>"
```

配置直接用编辑器填写。如果使用 shell heredoc，应采用 `<<'EOF'`，避免令牌中的 `$` 被当成变量展开。

创建 `/etc/systemd/system/frps.service`：

```ini
[Unit]
Description=FRP Server
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/frps -c /etc/frp/frps.toml
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

验证并启动：

```bash
sudo frps verify -c /etc/frp/frps.toml
sudo systemctl daemon-reload
sudo systemctl enable --now frps
sudo systemctl status frps
```

配置修改后执行 `sudo systemctl restart frps`。如使用 UFW，放行所需端口，并同步检查云安全组：

```bash
sudo ufw allow 7000/tcp
sudo ufw allow 6000/tcp
sudo ufw status
```

`7000` 用于 FRP 客户端连接；`6000` 是外部 SSH 入口。能确定来源地址时，应限制允许访问的来源。

### Mac 客户端

安装并编辑 Homebrew 服务使用的配置文件，统一手动测试与后台启动的配置路径：

```bash
brew install frpc
frpc -v
mkdir -p "$(brew --prefix)/etc/frp"
nano "$(brew --prefix)/etc/frp/frpc.toml"
```

已有配置时先备份，再合并以下内容：

```toml
serverAddr = "服务器IP"
serverPort = 7000
auth.method = "token"
auth.token = "<FRP_TOKEN>"

[[proxies]]
name = "mac-ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
```

令牌必须与服务端一致。验证后在前台测试：

```bash
frpc verify -c "$(brew --prefix)/etc/frp/frpc.toml"
frpc -c "$(brew --prefix)/etc/frp/frpc.toml"
```

登录成功只说明客户端连上 frps，还需从其他设备验证 SSH 转发：

```bash
ssh -p 6000 Mac用户名@服务器IP
```

前台测试结束后按 `Ctrl+C`，再启用后台服务，避免重复运行：

```bash
brew services start frpc
brew services list
```

修改配置后使用 `brew services restart frpc`；停止使用 `brew services stop frpc`。

### 转发其他服务

例如在客户端追加以下配置，将 Mac 的 `3000` 端口映射到 VPS 的 `8000` 端口，并在 VPS 放行对应端口：

```toml
[[proxies]]
name = "mac-web"
type = "tcp"
localIP = "127.0.0.1"
localPort = 3000
remotePort = 8000
```

### 排查顺序

| 现象 | 检查项 |
| --- | --- |
| 连接 frps 超时 | VPS 地址、7000 端口、防火墙、安全组、frps 状态 |
| 认证失败 | 两端令牌是否一致、配置是否被 shell 展开 |
| frpc 登录成功但 SSH 不通 | 代理注册结果、6000 端口、Mac 远程登录与本机 22 端口 |
| 后台启动后失效 | `brew services list`、服务读取的配置路径、Mac 是否休眠 |

## Mac SSH 与系统维护

### 授权密钥

在 Mac 目标登录用户下编辑授权公钥文件：

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

将连接方的公钥追加为单独一行，保留已有密钥。查看连接方公钥的示例：

```bash
# Mac / Linux 终端
cat ~/.ssh/id_ed25519.pub
```

```powershell
# Windows PowerShell
Get-Content "$env:USERPROFILE\.ssh\id_rsa.pub"
```

### 仅允许密钥登录

先在另一个终端成功测试密钥登录，并保留本机操作方式。检查 `/etc/ssh/sshd_config` 的 Include 设置后，再添加自定义配置片段，例如 `/etc/ssh/sshd_config.d/100-macos.conf`：

```sshconfig
PasswordAuthentication no
KbdInteractiveAuthentication no
AuthenticationMethods publickey
```

检查语法和有效配置：

```bash
sudo /usr/sbin/sshd -t
sudo /usr/sbin/sshd -T | grep -E 'passwordauthentication|kbdinteractiveauthentication|authenticationmethods'
```

文件名排序不代表一定覆盖其他配置，以实际输出为准。原笔记使用 `launchctl unload/load` 重启系统 SSH 服务；此方法不作为跨版本通用步骤。需要重新启用服务时，在 Mac 本机通过“远程登录”开关操作，再测试新连接。

### 电源与防火墙

```bash
# 查看电池状态
pmset -g batt

# 查看应用防火墙状态
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

原笔记的休眠开关如下，属于持续性的电源设置变更，适用性需在当前机型和系统上验证：

```bash
# 禁用休眠
sudo pmset -a disablesleep 1

# 重新允许休眠
sudo pmset -a disablesleep 0
```

保持唤醒工具的原记录为 Amphetamine；是否适合长期运行需按机器使用场景决定。

### Mole 清理工具

原有命令速查，具体功能以安装版本的帮助信息为准：

```bash
brew install mole
mo uninstall
mo clean
mo analyze
```

分别用于卸载、清理和磁盘分析；执行清理或卸载前查看交互界面列出的目标。

### 卸载 Anaconda 与 Python

卸载前先确认安装来源和目录，保留仍需要的环境与依赖记录。

| 软件 | 原笔记中的位置 | 整理要点 |
| --- | --- | --- |
| Anaconda | `~/opt/anaconda3` | 先退出 conda 环境，确认实际安装目录，再按对应安装方式卸载；清理 shell 中对应的 conda 初始化段 |
| python.org Python 3.11 | `/Library/Frameworks/Python.framework/Versions/3.11`、`/Applications/Python 3.11/` | 仅处理确认属于该版本的文件，不混用 Homebrew 或系统 Python 的卸载方式 |

检查 shell 配置：

```bash
nano ~/.zshrc
```

原笔记使用解析 `ls` 输出并批量删除 `/usr/local/bin` 链接的方法，已改为人工确认每个符号链接的目标后再移除，避免误删其他版本的命令。

## 参考

- [Mac 远程登录](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)
- [Homebrew frpc 配置路径](https://formulae.brew.sh/formula/frpc)
- [FRP 认证](https://gofrp.org/en/docs/features/common/authentication/)
- [FRP 配置检查](https://gofrp.org/en/docs/features/common/configure/)
