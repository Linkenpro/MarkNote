#### 个人网页服务

##### 更新网页文件

###### 从服务器拉取

```
scp -r -P 50501 root@154.36.183.45:/var/www/html/quant/* "C:/Users/源恒/Desktop/file/"
```

```
scp -r root@154.36.183.45:/var/www/html/* "C:/Users/Elin/Desktop/file/"
```

###### 移除vps的所有文件

```
rm -rf /var/www/html/*
```

###### 回传文件

```
scp -r "C:/Users/源恒/Desktop/0322/*" root@154.36.183.45:/var/www/html/
scp -r -P 50501 "C:\Users\源恒\Downloads\index.html" root@154.36.183.45:/var/www/html/
```

```
scp -r "C:/Users/Elin/Desktop/0315/*" root@154.36.183.45:/var/www/html/
```

###### 权限修复三件套

```
chown -R www-data:www-data /var/www/html && find /var/www/html -type d -exec chmod 755 {} \; && find /var/www/html -type f -exec chmod 644 {} \;
```

其他命令

```
cd /var/www/html
```

```
cd /root/binance_quant && source venv/bin/activate
```

```
cat /var/www/html/quant/logs/cron.log
```



##### Nginx安装配置

###### 安装nginx

```
sudo apt update

sudo apt install nginx -y
```

###### 启动并设置开机自启

```
sudo systemctl start nginx
sudo systemctl enable nginx
```

###### 设置Nginx的防火墙端口

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

文件夹结构查看

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

###### 网站个人配置

```
sudo nano /etc/nginx/sites-available/default
```

查看配置

```
cat /etc/nginx/sites-available/default
```

###### 错误日志

```
错误日志实时监控
sudo tail -f /var/log/nginx/error.log
```

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

###### nginx配置文件位置查询

该命令用于测试 Nginx 配置文件的语法是否正确，

执行时**会直接显示主配置文件的路径**

```
sudo nginx -t
```

```
/etc/nginx/nginx.conf
```

###### 检查nginx本地日志

```
tail -n 20 /var/log/nginx/access.log
```

###### 隐藏nginx版本号

修改Nginx 配置隐藏版本号

```
nano /etc/nginx/nginx.conf
```

为了让扫描器觉得你的服务器“不好下口”，建议在 nginx.conf 的 http 块中加入：

```
server_tokens off;
```

##### 网页数据库配置

###### 安装数据库以支持登录功能

一键安装命令

```
sudo apt update && sudo apt install mariadb-server -y
```

检查状态

```
sudo systemctl status mariadb
```

###### 安全初始化

```
sudo mysql_secure_installation
```

- 提示 `Enter current password for root`: 直接按 **Enter** (初始没有密码)。
- `Switch to unix_socket authentication`: 输入 **n** (否)。
- `Change the root password?`: 输入 **y** (是)，然后设置一个强密码（请记好，后面配置 PHP 要用）。`·96$ecret`
- `Remove anonymous users?`: **y**
- `Disallow root login remotely?`: **y**
- `Remove test database and access to it?`: **y**
- `Reload privilege tables now?`: **y**

##### Flask后端服务API

###### 守护进程创建

让 API 在后台稳定运行，断线也不停

```
sudo nano /etc/systemd/system/quant_api.service
```

填写内容

```
[Unit]
Description=Binance Quant API Service
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/root/binance_quant
# 确保使用虚拟环境的 python
Environment="PATH=/root/binance_quant/venv/bin"
ExecStart=/root/binance_quant/venv/bin/python app.py
Restart=always
RestartSec=5
# 日志输出到 journalctl
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

启动服务：

```
sudo systemctl daemon-reload
sudo systemctl start quant_api
sudo systemctl enable quant_api
sudo systemctl status quant_api  # 确认状态为 active (running)
```

#### Debian服务器

##### 用户管理

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

##### 软件包管理 (APT)

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

##### 网路防火墙

###### 查看正在监听的端口

> 此命令更实用

```
sudo ss -tulpn
```

###### ufw简化防火墙

> ufw当前详细状态

```
sudo ufw status verbose
```

###### 启用防火墙

```
sudo ufw enable
```

###### ufw放行端口

```
# 1. 允许SSH
sudo ufw allow 22/tcp

# 2. 允许Web服务 (Nginx)
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# 3. 允许Xray代理端口
sudo ufw allow 12345/tcp
```

###### 删除端口

```
sudo ufw delete allow 2053/tcp
```



##### 服务器ssh

###### 在服务器上配置

```
Get-Content C:\Users\你的用户名\.ssh\id_rsa.pub
```

登录远程服务器

```
ssh root@服务器IP
```

创建 .ssh 目录

```
mkdir -p ~/.ssh
```

将公钥写入`authorized_keys`文件

```
nano ~/.ssh/authorized_keys
```

设置正确的权限

```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chown -R $USER:$USER ~/.ssh
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

挑选一个“隐蔽”的端口

```
sudo ufw allow 50501/tcp
```

检查状态

```
sudo ufw status
```

修改 SSH 配置文件

```
sudo nano /etc/ssh/sshd_config
```

> 找到 `#Port 22` 这一行。
>
> 去掉前面的 `#` 号。
>
> 在下面紧接着添加一行 `Port 28443`（**先保留 22 端口，等测试成功再删**）

按 `Ctrl + O` 保存，`Enter` 确认，`Ctrl + X` 退出

```
ssh -p 50501 root@154.36.183.45
```

彻底关掉 22 端口

```
sudo nano /etc/ssh/sshd_config
```

> 确保里面只有 Port 50501。
>
> 删除或注释掉（加 #） Port 22。
>

保存退出后重启服务

```
sudo systemctl restart ssh
```

执行 UFW 命令删掉旧规则

```
sudo ufw delete allow 22/tcp
```

彻底关门的正确命令

```
# 删除基于应用配置的规则
sudo ufw delete allow OpenSSH
```

执行完后，再次查看状态验证

```
sudo ufw status verbose
```

端口攻击查看

```
tail -f /var/log/auth.log
```

###### ssh配置

```
cat /etc/ssh/sshd_config
```

 `PermitRootLogin yes` 允许 Root 直接通过密钥登录

可以改为 `PermitRootLogin prohibit-password`。它的作用是显式声明：**允许 Root 登录，但绝对不允许用密码**

```
ssh -p 50501 root@154.36.183.45
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

###### 关闭端口

```
sudo ufw delete allow 8443/tcp
```

###### 开放端口

```
sudo ufw allow 2053/tcp

# 重新加载防火墙规则
sudo ufw reload

# 确认修改结果
sudo ufw status
```

##### 系统清理

清理系统无用缓存

```
# 清理已下载的软件包安装包
apt-get clean
# 卸载不再需要的依赖包
apt-get autoremove -y
```



#### 量化项目

###### 虚拟环境

```
python3 -m venv venv
```

###### 激活虚拟环境

```
source venv/bin/activate
```

运行py文件

```
python binance_ccxt.py
```

##### 项目一：定时采集

###### 配置 Crontab 定时任务

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

###### 查看完整日志内容

```
cat data_fetcher.log
```

###### API与密钥保存

设置环境变量保存API

```
nano ~/.bashrc
```

文件末尾加入

```
source ~/.bashrc
```

###### 拉取py程序

```
scp -r root@154.36.183.45:/root/binance_quant/binance_ccxtSQL.py "C:/Users/源恒/Desktop/"
```

```
scp -r "C:/Users/源恒/Desktop/btc5min.py" root@154.36.183.45:/root/binance_quant/
```

##### 量化问题处理

###### VPS系统时间与量化采集



###### API权限与定时任务读取

```
nano .env
```

```
BINANCE_API_KEY=你的真实API_KEY
BINANCE_SECRET=你的真实API_SECRET
```

为了防止其他用户窃取你的密钥，必须限制该文件的权限，仅允许 root 读写：

```
chmod 600 /root/binance_quant/.env
ls -l .env
# 输出应该是: -rw------- 1 root root ... .env
```

使用 python-dotenv 库

```
pip install python-dotenv
```

1

#### 代理加速

- 更新系统软件包

```
apt update && apt upgrade -y
```

- 安装必要依赖

```
apt install curl socat -y
```

- 一键安装3x-ui面板

```
bash <(curl -Ls https://raw.githubusercontent.com/MHSanaei/3x-ui/master/install.sh)
```

脚本会询问是否确认安装，输入 `y`

询问是否给面板分配随机端口

> yes

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

##### 3X-UI面板使用

###### vps管理面板

```
x-ui
```

开启面板BBR

```
23

1
```

##### 入站列表

- 协议
- 传输
- 安全 Reality和TLS

###### 第一种：Vless+XHTTP+Reality

1. 备注：随便填

2. 协议：选择vless

3. 端口：随机分配

4. 传输：选择XHTTP

5. 路径：填写正斜杠+随机字符

   ```
   /abc
   ```

6. 安全选Reality

   Target：填写

   SNI:

   ```
   microsoft.com
   apple.com
   tesla.com
   ```

7. 点击创建公钥和私钥

8. 点击创建

9. 点击左侧加号，点击二维码，用V2ray，小火箭，Clash扫码添加节点

   点击二维码图片自动复制链接

###### 第二种：Vless+TCP+Reality

1. 传输选择TCP

2. 安全选Reality

3. Target：填写

   SNI:

   ```
   microsoft.com
   apple.com
   tesla.com
   ```

4. 点击创建公钥和私钥

##### 用域名搭建节点

1. 准备一个域名
2. 托管到Cloudflare

###### 添加解析记录

```
A记录
名称填test
ip地址vps的ip，关闭代理
点击保存
```

ping刚才的域名

```
ping 域名
```

##### vps操作

###### 安装ssl证书

```
18

1 获得ssl证书

填写自己的域名
panel.moonode.uk

填写一个端口54300

ACEM脚本：
选择n

对面板安装证书：y

保存至记事本
```

###### 第三种节点Vmess+WS+TLS

1. 名称随便填

2. 协议：vmess

3. 传输选Websocket

4. 主机：填自己的域名

   ```
   panel.moonode.uk
   ```

5. 路径：/abb

6. 安全选TLS

   建议端口：443、2053、2083、2087、2096、8443

7. SNI：填自己的域名

8. 公钥私钥：从面板设置证书

9. 点击创建

###### 软件

Windows：V2rayN

Mac：

安卓：V2rayNG

###### Nginx文件配置

```

```



```
location /v2ray/ {
    proxy_redirect off;
    proxy_pass http://127.0.0.1:12345; # 对应 x-ui 节点端口
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
}
```

##### 防火墙端口

```

    location /v2ray/ {
        if ($http_upgrade != "websocket") { 
            return 404; #如果不是WS请求，直接返回404
        }
        proxy_redirect off;
        proxy_pass http://127.0.0.1:12345; #转发至3x-ui端口
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        # 传递真实 IP，方便你在面板看日志
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
```

###### 端口连接-延迟测试

```
https://ping.pe/
```

##### 优选IP

###### 寻找最优 IP

> 目前最流行的是 CloudflareSpeedTest（开源项目）

解压后运行`CloudflareST.exe`

工具会自动测试几千个 Cloudflare 的 IP，并按 延迟 和 下载速度 排序

测试结束后，你会得到一个列表。

选一个延迟最低（比如 50-100ms）且下载速度最快的 IP（例如 162.159.x.x 或 104.x.x.x）。

###### 修改代理客户端设置

需要把“假 IP”填进去，但告诉服务器“真域名”

地址 (Address)：填入你刚才优选出来的 IP（例如 104.16.123.45）。

伪装域名 (Host / HTTP Host)：填入你的域名 panel.moonode.uk。

SNI (Server Name Indication)：必须填 panel.moonode.uk。

端口：依然是 443。

```
日本服务器优选ip
162.159.39.28
162.159.44.234
```

##### ip测试

###### ping检测

```
ping.pe
```

###### ip欺诈分

```
https://scamalytics.com/
```

#### Docker安装

```
# 1. 更新系统索引并安装必要的 HTTPS 传输组件
sudo apt update && sudo apt install -y curl

# 2. 下载并运行 Docker 官方安装脚本
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 3. 启动并设置开机自启
sudo systemctl enable --now docker
```

安装 Docker Compose (插件版)

```
sudo apt install -y docker-compose-plugin

验证安装
docker compose version
```

禁止自启动

```
sudo systemctl disable docker
sudo systemctl disable docker.socket
```

临时停止服务

```
sudo systemctl stop docker
sudo systemctl stop docker.socket
```

彻底“杀死”残留进程

```
sudo pkill -f docker && sudo pkill -f containerd
```

