###### 连接ZgoCloud

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
Password:
-khwKgeOH$
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
    raise ValueError("❌ 错误：未找到环境变量 BINANCE_API_KEY 或 BINANCE_API_SECRET")

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'timeout': 10000, # 超时设置为10秒
    'enableRateLimit': True, # 必须开启，遵守速率限制，防止被封IP
    'options': {
        'defaultType': 'future',  # 指定为 'future' (合约/期货)
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

