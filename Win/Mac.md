## 1. DeepSeek API 接入

### 1.1 获取 API Key

1. 访问 [DeepSeek 开放平台](https://platform.deepseek.com/) 并登录
2. 进入 **API Keys** 页面，点击 **Create new API key**
3. 创建后**立即复制并保存**（通常以 `sk-` 开头）

### 1.2 接入 OpenCode（代码编辑器插件）

- 在项目目录下运行 `opencode`
- 输入 `/connect` 并回车
- 供应商列表中选择 `deepseek`
- 粘贴 API Key 并确认
- 选择模型（如 `DeepSeek-V4-Pro`）完成配置

## 2. 文件拉取与 Git 初始化

### 2.1 从远程 VPS 拉取网站文件

```bash
scp -r -P 50501 root@154.36.183.45:"/var/www/html/*" ~/openCode/
```

### 2.2 初始化 Git 仓库

```bash
git init
git status
git add .
git commit -m "Initial commit - pull from VPS"
touch .gitignore
```

### 2.3 配置 .gitignore（静态网站项目）

```bash
cat > .gitignore << 'EOF'
# 日志文件（量化交易产生的日志）
quant/cron.log
quant/logs/*.json

# 本地编辑器/系统文件
.DS_Store
*.swp
*.swo
*~

# 临时文件
*.tmp
*.log

# 环境变量
.env
.env.local

# 构建输出（如果有）
dist/
build/
EOF
```

### 2.4 设置 Git 用户信息并修正提交作者

```bash
git config --global user.name "MyMacBookPro"
git config --global user.email "2421814924@qq.com"
git commit --amend --reset-author
```

## 3. 文件同步（rsync）

### 3.1 手动推送

```bash
rsync -avz -e "ssh -p 50501" ~/openCode/html/ root@154.36.183.45:/var/www/html/
```

### 3.2 自动保存推送（监听文件变化）

```bash
# 安装 fswatch
brew install fswatch

# 放到后台运行
fswatch -o ~/openCode/html | xargs -n1 -I{} rsync -avz -e "ssh -p 50501" ~/openCode/html/ root@154.36.183.45:/var/www/html/ &
```

> `fswatch -o` – 文件变动时输出一次  
> `xargs` – 触发 rsync 同步

## 4. RustDesk 自建中继服务器

### 4.1 在 VPS 上搭建中转服务器

**服务端**：https://github.com/rustdesk/rustdesk-server/releases

```bash
sudo apt update && sudo apt install -y wget
wget https://github.com/rustdesk/rustdesk-server/releases/download/1.1.15/rustdesk-server-hbbs_1.1.15_amd64.deb
sudo dpkg -i rustdesk-server-hbbs_1.1.15_amd64.deb

# 修改 hbbs 启动参数以指定中继服务器
systemctl show -p FragmentPath rustdesk-hbbs.service
sudo nano /lib/systemd/system/rustdesk-hbbs.service
# 保存后重载并重启
sudo systemctl daemon-reload
sudo systemctl restart rustdesk-hbbs

# 查看 Key
cat /var/lib/rustdesk-server/id_ed25519.pub
# 示例 Key: EAXTJZFoTSHQoPpHHtddhmSY9ybYatouEB546BQ2CkE=

# 检查 hbbs 是否带 IP 运行
systemctl status rustdesk-hbbs
```

### 4.2 配置 Mac 被控端

- 下载 [RustDesk macOS 版](https://rustdesk.com/zh/)
- 点击菜单 (≡) → **网络**
- **ID 服务器**：`154.36.183.45`
- **中继服务器**：`154.36.183.45`
- **Key**：粘贴上面 `cat` 出的长字符串
- 点击 **确认**

### 4.3 从外部连接

在其他设备（Windows/Mac/iPad/手机）上安装 RustDesk，配置相同的 VPS 地址，输入 Mac 的设备 ID 即可远程控制。

## 5. FRP 内网穿透服务

### 5.1 架构说明

- 公网 VPS 运行服务端 `frps`
- 内网 Mac 运行客户端 `frpc`

### 5.2 VPS 服务端部署

```bash
cd /tmp
wget https://github.com/fatedier/frp/releases/download/v0.68.1/frp_0.68.1_linux_amd64.tar.gz
tar -xzf frp_0.68.1_linux_amd64.tar.gz
cd frp_0.68.1_linux_amd64

sudo cp frps /usr/local/bin/
sudo mkdir -p /etc/frp
sudo cp frps.toml /etc/frp/
```

**创建 systemd 服务**

```bash
sudo tee /etc/systemd/system/frps.service > /dev/null <<EOF
[Unit]
Description=FRP Server
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/frps -c /etc/frp/frps.toml
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
```

**配置 frps.toml**

```bash
sudo tee /etc/frp/frps.toml > /dev/null <<EOF
bindPort = 7000
auth.token = "9016$ecTon"
EOF
```

**启动服务**

```bash
sudo systemctl daemon-reload
sudo systemctl start frps
sudo systemctl enable frps
sudo systemctl status frps
```

**配置防火墙（UFW）**

```bash
sudo ufw allow 7000/tcp
sudo ufw allow 6000/tcp
sudo ufw reload
```

### 5.3 Mac 客户端部署

#### 安装 Homebrew（如未安装）

```bash
export https_proxy=http://127.0.0.1:7892 http_proxy=http://127.0.0.1:7892
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 添加环境变量（根据终端提示执行类似命令）
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"
```

#### 安装 frpc

```bash
brew install frpc
frpc -v
```

#### 配置客户端 frpc.toml

```bash
mkdir -p ~/frp
cd ~/frp
cat > frpc.toml <<EOF
serverAddr = "154.36.183.45"   # 替换为你的 VPS IP
serverPort = 7000
auth.token = "9016$ecTon"

[[proxies]]
name = "mac-ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
EOF
```

#### 测试连接

```bash
frpc -c ~/frp/frpc.toml
```

看到 `login to server success` 即表示成功。

#### 备用：修改全局配置（可选）

```bash
sudo nano /opt/homebrew/etc/frp/frpc.toml
```

### 5.4 连接测试

从任意网络通过 VPS SSH 连接 Mac：

```bash
ssh <Mac用户名>@<VPS公网IP> -p 6000
```

### 5.5 Mac 电源管理（保持唤醒）

```bash
# 禁用休眠
sudo pmset -a disablesleep 1

# 恢复
sudo pmset -a disablesleep 0
```

推荐安装 **Amphetamine** 应用。

### 5.6 进阶配置

#### 客户端后台自启

```bash
brew services start frpc
# 管理命令：restart / stop
```

#### 暴露更多本地服务（示例）

```toml
[[proxies]]
name = "mac-web"
type = "tcp"
localIP = "127.0.0.1"
localPort = 3000
remotePort = 8000
```

### 5.7 常见问题排查

| 问题                       | 可能原因与解决                                               |
| -------------------------- | ------------------------------------------------------------ |
| `Connection refused`       | VPS 防火墙未放行 6000 端口；Mac 未开启“远程登录”             |
| `i/o timeout`              | VPS 防火墙/安全组未放行 7000 端口                            |
| `authentication failed`    | 客户端与服务端的 `auth.token` 不一致                         |
| Mac 客户端重启后未自动连接 | 执行 `brew services list` 检查状态，`brew services restart frpc` |

## 6. Mac 系统配置与优化

### 6.1 SSH 密钥管理

查看/编辑授权密钥：

```bash
nano ~/.ssh/authorized_keys
```

查看各平台公钥：

```bash
# Windows
type C:\Users\Elin\.ssh\id_rsa.pub

# VPS
cat ~/.ssh/id_ed25519.pub
```

### 6.2 彻底禁用 SSH 密码登录（仅允许密钥）

```bash
sudo nano /etc/ssh/sshd_config.d/100-macos.conf
```

写入：

```
PasswordAuthentication no
KbdInteractiveAuthentication no
AuthenticationMethods publickey
```

检查配置并重启服务：

```bash
sudo sshd -t
sudo launchctl unload -w /System/Library/LaunchDaemons/ssh.plist
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

### 6.3 防火墙管理

```bash
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

### 6.4 Mole 智能卸载与系统优化

```bash
brew install mole
mo uninstall    # 交互式卸载菜单
mo clean        # 深度清理系统垃圾
mo analyze      # 可视化磁盘分析
```

### 6.5 查看电池电量

```bash
pmset -g batt
```

### 6.6 软件卸载示例

#### 卸载 Anaconda

```bash
conda deactivate
rm -rf ~/opt/anaconda3
nano ~/.zshrc   # 删除 conda 初始化代码段
source ~/.zshrc
```

#### 删除官方 Python 3.11

```bash
sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.11
sudo rm -rf "/Applications/Python 3.11/"
cd /usr/local/bin && ls -l | grep '../Frameworks/Python.framework/Versions/3.11' | awk '{print $9}' | sudo xargs rm -f
```

## 7. SFTP 手动比对同步（VSCode）

1. 打开命令面板：`Cmd + Shift + P`
2. 输入并选择 `SFTP: Sync Local -> Remote`
3. 执行同步（确保配置文件中未启用 `"syncOption": { "delete": true }` 以免删除远程多余文件）
