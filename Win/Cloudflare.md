##### 域名解析

添加DNS记录

###### A 记录 (最核心)

- DNS>>>Records
- 点击 + **Add record**

- 添加根域名记录（@）:

  > **Type**: A
  > **Name**: @ (代表根域名 moonode.uk)
  > **Content**: 你的云服务器公网 IP (例如 47.100.xx.xx)
  > **Proxy status**:
  > ⚪ DNS Only (灰色): 推荐用于量化交易 API、SSH、数据库连接。延迟最低，无中间人干扰。
  > 🟠 Proxied (橙色): 推荐用于公开的博客、监控大屏。有 CDN 加速和防攻击功能，但可能增加延迟。
  >
  > **TTL**: `Auto`

###### CNAME 记录 (别名)

##### 静态页面

静态网站生成器 (Static Site Generator) + Cloudflare Pages

适用工具：Hugo (最快), Hexo (插件多), Jekyll, Astro

Hugo：

Windows: `choco install hugo -confirm` (需先装 Chocolatey) 或下载二进制文件

创建网站

```
hugo new site my-portfolio
cd my-portfolio
git init
# 下载一个喜欢的主题 (例如 PaperMod，很适合技术博客)
git clone https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

3.配置主题：修改 hugo.toml，填入你的域名 moonode.uk 和标题

4.撰写内容

```
hugo new content posts/my-first-quant-strategy.md
# 编辑生成的 md 文件，写你的文章
```

5.在 GitHub 创建一个新仓库，将代码 push 上去

6.连接 Cloudflare Pages：

- 登录 Cloudflare Dashboard -> Workers & Pages -> Create Application -> Pages -> Connect to Git
- 选择你的仓库
- Build settings:
  Framework preset: Hugo
  Build command: hugo --minify
  Build output directory: public

- 点击 Save and Deploy

绑定域名：

- 在 Pages 项目设置中，点击 Custom Domains，输入 moonode.uk。
- Cloudflare 会自动配置 DNS，几分钟后即可访问

###### 连接ZgoCloud

```
Get-Content C:\Users\源恒\.ssh\id_rsa.pub
Get-Content C:\Users\Elin\.ssh\id_rsa.pub

ssh -i C:\Users\源恒\.ssh\id_rsa root@154.36.183.45
ssh -i C:\Users\Elin\.ssh\id_rsa root@154.36.183.45
```

```
IP:
154.36.183.1
Port:
5943
Password:
-khwKgeOH
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

##### Nginx

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
```

