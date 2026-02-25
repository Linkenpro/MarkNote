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

ssh -i C:\Users\源恒\.ssh\id_rsa root@154.36.183.45
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

