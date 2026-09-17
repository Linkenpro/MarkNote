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

##### R2对象存储

```
输入你的 VPS IP: 

```

```
AccessKeyID:
ba7b2833fdbe2139cb7b390aa901cec7
SecretAccessKey：
1db360808c1e94f47446b9d0ac498f7f90e99fca6e9cb2881cbf8f3ecbe759be
TokenValue：
qd-Te7ChTCPiRLvDM5IiNVAru-a6LY0edhlaup18
Use jurisdiction-specific endpoints for S3 clients:
https://aa1c3a307afbd92707ebce24c756c620.r2.cloudflarestorage.com
```

###### 安装rclone

```
curl https://rclone.org/install.sh | sudo bash
```

配置向导

```
rclone config
```

New remote

- n

name

- r2

Storage>

- s3

provider>

- Cloudflare

env_auth>

- false

access_key_id>

> 粘贴Cloudflare 后台复制的 Access Key ID

secret_access_key>

> 粘贴你刚才在 Cloudflare 后台复制的 Secret Access Key

region>

> auto

endpoint>

> 例如：https://a1b2c3d4e5f6g7h8i9j0.r2.cloudflarestorage.com

location_constraint>

> 回车

acl>

> 回车

Edit advanced config>

> n

Yes this is OK>

> y

###### 测试连接

```
rclone ls r2:moonode-backups
```

```
echo "R2 Backup Test Successful!" > test-r2.txt

rclone copy test-r2.txt r2:moonode-backups/

rclone ls r2:moonode-backups/
```

###### 备份量化数据至R2

```
crontab -e
```

文件末尾

```
# 每天 09:00 自动备份量化数据库和日志到 R2
0 9 * * * /bin/bash -c "cd /root/binance_quant && tar -czf backup-\$(date +\%F).tar.gz crypto_data.db logs/cron.log && rclone copy backup-\$(date +\%F).tar.gz r2:moonode-backups/backups/\$(date +\%Y)/\$(date +\%m)/ && find . -name 'backup-*.tar.gz' -mtime +7 -delete" >> /root/binance_quant/logs/cron.log 2>&1
```

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

