##### 连接ZgoCloud

###### 获取ssh信息

```
Get-Content C:\Users\源恒\.ssh\id_rsa.pub
Get-Content C:\Users\Elin\.ssh\id_rsa.pub

ssh -i C:\Users\源恒\.ssh\id_rsa root@154.36.183.45
ssh -i C:\Users\Elin\.ssh\id_rsa root@154.36.183.45
ssh -i C:\Users\Elin\.ssh\id_rsa admin@154.36.183.45
```

```
IP:
154.36.183.1
Port:
5943
PS:
R-khwKgeOH$
```

###### 更新系统软件包

```
apt update && apt upgrade -y
```

###### 安装常用工具

```
apt install -y curl wget vim git ufw fail2ban sudo net-tools
```

###### 允许 SSH 连接 

> 防止把自己锁在外面

```
ufw allow OpenSSH
```

###### 允许 Web 服务

```
ufw allow http
ufw allow https
```

###### 启用防火墙

```
ufw enable
```

###### 设置时区

```
timedatectl set-timezone Asia/Shanghai
```

###### 设置root密码

```
passwd
```

```
ssh root@154.36.183.45
```

###### 禁用密码登录

只保留密钥

```
sudo nano /etc/ssh/sshd_config

找到 PasswordAuthentication 这一行
PasswordAuthentication no
```

删除root密码

```
sudo passwd -l root
```

###### 设置第二个ssh

```
nano /root/.ssh/authorized_keys
```

检查权限

```
chmod 700 /root/.ssh
chmod 600 /root/.ssh/authorized_keys
```

###### 修改ssh的22端口

- 修改端口前，强烈建议先开启一个新的SSH连接窗口，用于测试新端口是否生效

请**不要立即关闭**当前正在操作的旧连接，以防配置错误导致无法连接服务器

建议先备份SSH配置文件

```
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup
```

打开SSH服务的主配置文件

```
sudo nano /etc/ssh/sshd_config
```

查找并修改端口配置

> 在文件中找到以 `#Port 22` 开头的行。`#` 代表注释，需要先去掉
>
> 如果该行被注释（前面有 `#`），请删除 `#`
>
> 将后面的数字 `22` 修改为你想要的新端口号
>
> 推荐选择一个 **1024 到 65535** 之间的未被占用的端口，例如 `2022`、`12345` 或 `54321`

修改后，该行应类似于：

```
Port 2022
```

**重启SSH服务**

```
sudo systemctl restart ssh

旧的系统
sudo service ssh restart
```

**配置防火墙规则**

```
# 允许新端口
sudo ufw allow 2022/tcp

# 在确认新端口连接正常后，可以删除对22端口的允许规则
sudo ufw delete allow 22/tcp
```

**测试新端口连接**

```
ssh username@your_server_ip -p 2022
```

禁用旧的22端口在确认通过新端口可以稳定连接后再次编辑 /etc/ssh/sshd_config 文件，将 Port 22 这一行删除或在前面加上 # 注释掉，然后再次重启SSH服务，以彻底关闭22端口的监听。

#### Debian服务器

软件包管理 (APT)

###### 更新软件源列表

```
sudo apt update
```

###### 升级已安装的软件包

```
sudo apt upgrade -y
```

###### 安装软件

```
sudo apt install <package_name>
```

###### 卸载软件

```
sudo apt remove <package_name>
# 彻底卸载（包括配置文件）
sudo apt purge <package_name>
```

###### 清理无用依赖和缓存

```
sudo apt autoremove -y
sudo apt autoclean
```

##### 系统服务管理

###### 查看服务状态

```
systemctl status <service_name>
```

###### 启动/停止/重启服务

```
sudo systemctl start <service_name>
sudo systemctl stop <service_name>
sudo systemctl restart <service_name>
```

###### 设置开机自启/禁用自启

```
sudo systemctl enable <service_name>
sudo systemctl disable <service_name>
```

###### 查看服务日志 (实时查看)

```
journalctl -u <service_name> -f

journalctl -u nginx -f
```

```
root@vps:~# journalctl -u nginx -f
Feb 27 23:15:49 vps systemd[1]: Reloaded nginx.service - A high performance web server and a reverse proxy server.
Mar 03 09:48:10 vps systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 03 09:48:10 vps systemd[1]: nginx.service: Deactivated successfully.
Mar 03 09:48:10 vps systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 03 09:48:10 vps systemd[1]: nginx.service: Consumed 25.426s CPU time.
Mar 03 09:57:42 vps systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 03 09:57:42 vps systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 03 11:00:16 vps systemd[1]: Reloading nginx.service - A high performance web server and a reverse proxy server...
Mar 03 11:00:16 vps nginx[132845]: 2026/03/03 11:00:16 [notice] 132845#132845: signal process started
Mar 03 11:00:16 vps systemd[1]: Reloaded nginx.service - A high performance web server and a reverse proxy server.

```

##### 网络与防火墙

###### 查看 IP 地址

```
ip addr

hostname -I
```

###### 防火墙管理 (UFW）

```
sudo ufw status
sudo ufw allow 22/tcp   # 允许 SSH
sudo ufw allow 80/tcp   # 允许 HTTP
sudo ufw enable         # 启用防火墙
```

###### 修改权限

```
chmod 755 <file_or_dir>
chown user:group <file_or_dir>
```



#### Nginx

```
软件包列表更新
sudo apt update

软件仓库直接安装
sudo apt install nginx -y
```

###### 启动并设置开机自启

```
sudo systemctl start nginx
sudo systemctl enable nginx
```

设置防火墙

```
sudo ufw allow 'Nginx Full'

或直接允许 80 端口
sudo ufw allow 80
sudo ufw allow 443
```

###### 安装Certbot

```
sudo apt install certbot python3-certbot-nginx -y
```

###### 配置https证书

将域名替换为你自己的

```
sudo certbot --nginx -d server.moonode.uk -d moonode.uk
```

###### 文件夹结构查看

```
tree

sudo apt update && sudo apt install tree -y

cd /

mkdir /root/binance_quant

网页文件整理
mkdir /root/proxy/config

# 创建网站子目录
mkdir -p /root/website/{html,assets,backup}
```



```
scp "C:\Users\源恒\Desktop\website\images\ldm.svg" root@154.36.183.45:/var/www/html/images/logo.svg

scp "C:\Users\Elin\Downloads\website\images\light_background.webp" admin@154.36.183.45:/var/www/html/images/light_background.webp
```

###### 网站站点配置

```
sudo nano /etc/nginx/sites-available/default
```

###### 错误日志

```
错误日志实时监控
sudo tail -f /var/log/nginx/error.log
```

###### 创建管理员用户

```
adduser admin
```

赋予 sudo 权限 (让他能执行管理员命令)

```
usermod -aG sudo admin
```

为admin创建ssh

```
mkdir -p /home/admin/.ssh
```

复制 root 的公钥给 admin

```
cat /root/.ssh/authorized_keys >> /home/admin/.ssh/authorized_keys
```

查看公钥列表

```
cat ~/.ssh/authorized_keys
```

###### admin用户切换root

```
sudo -i
输入密码
```

###### admin用户传文件

```
scp -r "C:\Users\源恒\Downloads\website\*" admin@154.36.183.45:/var/www/html/

scp -r "C:\Users\源恒\Downloads\website\index.html" admin@154.36.183.45:/var/www/html/

nano /var/www/html/index.html
```

`\*`表示上传该文件夹下的所有内容，而不是把这个文件夹本身也传上去

###### 网页图片问题

```
https://moonode.uk/images/logo.svg?v=test1
```

> 浏览器缓存：你的浏览器之前缓存了一个错误的 404 响应，并且死死地抓着不放，即使你后来修好了服务器，它依然直接返回缓存的 404，根本不去服务器请求。
>
> Ctrl + Shift + R

###### 利用 Nginx 静态文件服务

```
sudo nano /etc/nginx/sites-available/default
```

更新配置文件

```
sudo nginx -t
```

重新加载服务

```
sudo systemctl reload nginx
```

再次检查服务状态

```

```

修改

```
server {
    listen 80;
    server_name your-domain.com;

    # 其他配置...

    # --- 新增的日志访问配置 ---
    location /my-logs/ {
        alias /path/to/your/quant/logs/; # 注意：这里必须是绝对路径，且末尾要有斜杠
        autoindex on; # 可选：开启目录浏览，可以看到有哪些日志文件
        # 为了安全，可以设置简单的账号密码（htpasswd）
    }
}
```

```
alias /root/binance_quant/logs;
```

前端网页读取（JavaScript）

```
<!DOCTYPE html>
<div>
    <h2>量化程序实时日志</h2>
    <!-- 使用 pre 标签保持日志的格式，code 标签高亮 -->
    <pre><code id="log-output">正在连接...</code></pre>
</div>

<script>
    // 每隔 3 秒刷新一次日志
    setInterval(async () => {
        try {
            // 请求你刚刚配置的那个路径下的具体日志文件
            const response = await fetch('/my-logs/app.log');
            const text = await response.text();
            
            // 获取最后 50 行（防止日志太长卡死浏览器）
            const lines = text.split('\n').slice(-50);
            document.getElementById('log-output').textContent = lines.join('\n');
        } catch (e) {
            document.getElementById('log-output').textContent = '读取失败: ' + e;
        }
    }, 3000);
</script>
```

###### nginx配置文件位置查询

该命令用于测试 Nginx 配置文件的语法是否正确，

执行时**会直接显示主配置文件的路径**

```
sudo nginx -t
```

```
/etc/nginx/nginx.conf
```

##### 量化

###### 虚拟环境

```
python3 -m venv venv
```

###### 激活虚拟环境

```
source venv/bin/activate
```

###### scp上传py文件

```
scp "C:\Users\源恒\Desktop\binance_ccxt.py" root@154.36.183.45:/root/binance_quant/

scp "C:\Users\源恒\Desktop\数据库\crypto_data.db" root@154.36.183.45:/root/binance_quant/

scp "C:\Users\源恒\Desktop\binance_test1.py" root@154.36.183.45:/root/binance_quant/

scp -r "C:\Users\源恒\Downloads\website\index.html" root@154.36.183.45:/var/www/html/
scp "C:\Users\源恒\Downloads\website\index.html" root@154.36.183.45:/var/www/html/
```

运行py文件

```
python binance_ccxt.py
```

###### 定时运行采集数据

```
timedatectl
```

配置 Crontab 定时任务

```
crontab -e
```

推荐选 nano

```
# 每天北京时间 08:30 运行量化脚本
30 8 * * * cd /root/binance_quant && source venv/bin/activate && python binance_ccxtSQL.py >> /root/binance_quant/logs/cron.log 2>&1
```

验证任务添加是否成功

```
crontab -l
```

确保定时任务守护进程正在运行

```
sudo systemctl status cron
```

查看日志文件

```
tail -n 10 /root/binance_quant/logs/cron.log
```

###### 退出venv环境

```
deactivate
```

###### 查看完整日志内容

```
cat data_fetcher.log

cat cron.log
```

###### 设置环境变量保存API

```
nano ~/.bashrc
```

文件末尾加入

```
# Binance API
export BINANCE_API_KEY="EWCgJWvOqRhnlgcYTyePlBnfVAABo2mq9PdZ6Lai2PacHyjhNM6q9k813plFtX5eq"
export BINANCE_API_SECRET="FfvRD02X1nXW3V5iNS8fFkTbwHEcriwghtSLCFPKD7ZMYJ2D66IGymTb5d7yewz2f"
```

生效

```
source ~/.bashrc
```

测试py文件

```py
import ccxt
import os

# 从环境变量读取密钥
API_KEY = os.environ.get('BINANCE_API_KEY')
API_SECRET = os.environ.get('BINANCE_API_SECRET')

if not API_KEY or not API_SECRET:
    raise ValueError("错误：未找到 BINANCE_API_KEY 或 BINANCE_API_SECRET !")

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'timeout': 10000, # 超时设置为10秒
    'enableRateLimit': True, # 必须开启，遵守速率限制，防止被封IP
    'options': {
        'defaultType': 'future',  # 指定为合约
    }
})

try:
    # 加载市场数据 (初始化)
    markets = exchange.load_markets()
    positions = exchange.fetch_positions('all') 

    print(f"{'交易对':<10} {'方向':<8} {'数量':<12} {'开仓价':<12} {'未实现盈亏':<12}")
    print("-" * 60)

    for pos in positions:
        symbol = pos['symbol']          # 交易对，例如 BTC/USDT
        side = pos['side']              # 方向：long 或 short
        amount = pos['contracts']       # 持仓数量 (合约张数)
        entry_price = pos['entryPrice'] # 开仓价格
        upl = pos['unrealizedPnl']      # 未实现盈亏

        # 只显示有实际持仓的（数量大于0）
        if amount > 0:
            print(f"{symbol:<12} {side:<8} {amount:<12} {entry_price:<12} {upl:<12}")

    # 5. 获取账户总体信息
    balance = exchange.fetch_balance()
    print(f"\n账户可用余额: {balance['USDT']['free']} USDT")
    print(f"账户总权益: {balance['USDT']['total']} USDT")

except ccxt.NetworkError as e:
    print("网络错误:", e)
except ccxt.ExchangeError as e:
    print("交易所错误:", e)
except Exception as e:
    print("其他错误:", e)
```

自动脚本

```
auto
```

#### vps代理搭建

###### 更新系统软件包

```
# Debian
apt update && apt upgrade -y
```

###### 安装必要依赖

```
apt install curl socat -y
```

###### 一键安装3x-ui面板

```
bash <(curl -Ls https://raw.githubusercontent.com/MHSanaei/3x-ui/master/install.sh)
```

脚本会询问是否确认安装，输入 `y`

设置账号密码：安装最后会要求你设置面板的 用户名、密码 和 端口（默认 2053）

```
Username:
YIeFe1Azor
Password:
UmilnrjKjn
Port:
54321
WebBasePath:
fdowFIwF2GE5CHWs3o
Access URL:
https://moonode.uk:54321/fdowFIwF2GE5CHWs3o
https://154.36.183.45:54321/fdowFIwF2GE5CHWs3o
```

恢复nginx

```
systemctl start nginx
```

###### VPS 内部防火墙

```
# 54321
ufw allow 54321/tcp  
ufw reload
```

##### 入站列表

###### 推荐配置 (VLESS + Reality)

1. 点击左侧 **“入站列表” (Inbounds)** -> **“添加入站” (Add Inbound)**。

2. 基本设置:

   - **备注 (Remark)**: 随便填，例如 `My-VLESS-Reality`。
   - **协议 (Protocol)**: 选择 `VLESS`。
   - **端口 (Port)**: 填写一个未被占用的端口（例如 `443` 或其他随机高位端口，**注意去安全组放行该端口**）。*建议不要用 54321，那是面板端口。*
   - **传输协议 (Transport)**: 选择 `Reality`。

3. Reality 设置:

   - **目标网站 (Dest)**: 填写一个国外的大型网站，如 `www.microsoft.com:443` 或 `www.apple.com:443` (作为伪装)。

   - **私钥 (Private Key)**: 点击旁边的 **“生成” (Generate)** 按钮自动生成。

     ```
     5lEremOipQStSuigDleyikd2peJoc-8AHtMFgVg_UgE
     ```

     ```
     uDPj5lkgewc2l_ANI_H-Sr5RzaLMkk90FQRaNOVtp2I
     ```

   - **短 ID (Short ID)**: 点击 **“生成”** 自动生成。

     ```
     8cd216db6485,9c,f0856d39,8e7c,1966e055edf22bdf,d0b6f0b458,d9ee89,7b9ed21969cb2c
     ```

   - **Xver**: 保持默认 `0`。

4. 用户设置:

   - 点击 **“添加用户”**，生成一个 **UUID** (也可以手动复制一个)。

5. 点击底部的 **“确定” (OK)** 保存。

###### VMess + WS + TLS（需要域名）

1. 点击 **“添加入站”**。
2. 基本设置:
   - **协议**: `VMess`。
   - **端口**: `443` (或者其他端口)。
   - **传输协议**: `WS` (WebSocket)。
3. WS 设置:
   - **路径 (Path)**: 填写一个随机路径，例如 `/mysecretroad` (客户端也要填一样的)。
4. TLS 设置:
   - 开启 **TLS** 开关。
   - **域名**: 填写 `moonode.uk`。
   - **证书/私钥**: 同面板设置，填入之前的 `.cer` 和 `.key` 路径，或者选择“自动”（如果脚本已配置好）。
5. **用户设置**: 添加用户，生成 UUID。
6. 点击 **“确定”**。

##### Nginx 反向代理

Nginx 统一管理流量，甚至可以让 3x-ui 的面板隐藏在你的二级目录或特定域名下，增加安全性

> **端口 80/443**：由 Nginx 监听（个人网页）。
>
> **127.0.0.1:2053**：3x-ui 面板（限制仅本地访问，通过 Nginx 转发，更安全）。
>
> **量化程序端口**：保持独立，或通过 Nginx 监控其 API 状态

修改 3x-ui 面板监听地址

> 在 3x-ui 的“面板设置”中，将监听 IP 从 0.0.0.0 改为 127.0.0.1。
>
> 这样别人就无法通过 IP:2053 直接访问你的面板，必须通过你的 Nginx 域名转发才能进入

Nginx 配置示例

```
server {
    listen 443 ssl;
    server_name yourdomain.com; # 你的域名

    # 你的个人网页配置
    location / {
        root /var/www/html;
        index index.html;
    }

    # 3x-ui 面板的反向代理
    location /mysecureadmin/ {
        proxy_pass http://127.0.0.1:54321;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

```
location / {
        proxy_pass http://127.0.0.1:54321;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
```

**SSL 证书共用**： 由于 Nginx 已经占用了 80/443，3x-ui 就不要再尝试去申请 80 端口的证书了（会冲突导致 Nginx 启动失败）。建议让 Nginx 处理所有证书，或者 3x-ui 使用 **Reality 协议**（不需要证书，也不占 443 端口）。

**防火墙策略（关键）**： 因为 Nginx 在前台，你只需要在 VPS 防火墙（ufw/iptables）开启：

- `80/443` (Nginx)
- `你的代理协议端口` (比如 Reality 用的 40000+)
- **关闭** `2053` (面板端口)，因为它已经通过 Nginx 转发了，没必要暴露在公网被扫。

**资源限制**： 量化程序最怕交换内存（Swap）导致的毫秒级延迟。

- 运行 `top` 或 `htop` 观察内存。
- 如果内存吃紧，建议给 3x-ui 限制日志记录大小，防止日志塞满硬盘影响量化程序的数据库写入。

###### 子域名反向代理

**添加一条 A 记录**

- **主机记录 (Host/Name)**: `panel` (或者你想要的任何前缀，如 `admin`, `xui`)
- **记录值 (Value/IP)**: 你的 **VPS 公网 IP**
- **TTL**: 自动或默认
- **代理状态 (Cloudflare)**: 建议先设为 **灰色 (DNS Only)**。如果后续需要 CDN 加速或隐藏 IP，再开启橙色云朵（但开启橙色云朵可能需要额外配置 WebSocket 支持）。

**申请子域名的 SSL 证书**

x-ui 面板强制要求 HTTPS

安装了 acme.sh，ssh中

```
# 停止 Nginx 以释放 80 端口 (防止冲突)
sudo systemctl stop nginx

# 申请证书 (将 panel.moonode.uk 替换为你实际的子域名)
~/.acme.sh/acme.sh --issue -d panel.moonode.uk --standalone

# 申请成功后，重新启动 Nginx
sudo systemctl start nginx
```

> 如果提示证书已存在或需要强制重新申请，可以加 --force 参数

记住证书路径（通常如下）：

- 全链证书：`/root/.acme.sh/panel.moonode.uk_ecc/fullchain.cer`
- 私钥：`/root/.acme.sh/panel.moonode.uk_ecc/panel.moonode.uk.key`

创建一个新的 Nginx 配置文件专门用于这个子域名

```
sudo nano /etc/nginx/sites-available/panel.moonode.uk
```

填入以下配置

```
server {
    listen 80;
    server_name panel.moonode.uk;
    # 强制将所有 HTTP 请求重定向到 HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name panel.moonode.uk;

    # --- SSL 证书路径 (替换为你刚才申请的子域名证书路径) ---
    ssl_certificate /root/.acme.sh/panel.moonode.uk_ecc/fullchain.cer;
    ssl_certificate_key /root/.acme.sh/panel.moonode.uk_ecc/panel.moonode.uk.key;

    # --- SSL 优化配置 (推荐) ---
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location / {
        # --- 反向代理到 x-ui 面板内部端口 (默认是 54321，如果你改过请修改这里) ---
        proxy_pass http://127.0.0.1:54321;

        # --- 必要的 Header 设置 (保持连接和获取真实 IP) ---
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # --- WebSocket 支持 (x-ui 面板可能用到 WS) ---
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        
        # 增加超时时间，防止长时间操作断开
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

启用配置：
创建软链接到 sites-enabled 目录

```
sudo ln -s /etc/nginx/sites-available/panel.moonode.uk /etc/nginx/sites-enabled/
```

检查并重载 Nginx

```
# 1. 检查语法
sudo nginx -t

# 2. 如果语法正确，重载服务
sudo systemctl reload nginx
```

**调整 x-ui 面板设置** (可选但推荐)

1. 暂时通过 IP:端口 (`https://IP:54321`) 登录面板。
2. 进入 **“面板设置”**。
3. 确保 **“面板 URL 根路径”** 是空的（即为 `/`）。如果你在 Nginx 里配置的是 `location /`，这里必须为空。
4. 保存。

**测试访问**

打开浏览器访问：
**`https://panel.moonode.uk`**
