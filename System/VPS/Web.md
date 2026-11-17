# VPS 网站部署

返回 [VPS](VPS.md)。服务器命令以 Debian 为例，域名和目录均需替换。

## Nginx 与 HTTPS

```bash
sudo apt update
sudo apt install nginx certbot python3-certbot-nginx
sudo systemctl enable --now nginx
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

在 `/etc/nginx/sites-available/default` 配置实际 `server_name`、站点目录或上游服务。域名先解析到服务器，供应商防火墙需允许验证流量。申请证书前确认 HTTP 站点可访问：

```bash
sudo nginx -t
sudo systemctl reload nginx
sudo certbot --nginx -d example.com -d www.example.com
sudo certbot renew --dry-run
```

仅在配置检查成功后 reload；证书中的每个域名都需满足验证条件。另检查安装方式对应的自动续期任务。

可在 `nginx.conf` 的 `http` 块设置 `server_tokens off;` 隐藏版本号；这不会修复漏洞。

## 上传与下载

以下在本地 PowerShell 执行。服务器上 `/home/admin/upload` 须预先创建，上传后再由管理员部署到站点目录。

```powershell
# 上传整个 site 目录
scp -r -P 50501 "C:/Projects/site" admin@vps.example.com:/home/admin/upload/
# 下载站点到本地当前目录
scp -r -P 50501 admin@vps.example.com:/var/www/example.com .
```

SSH 使用小写 `-p`，SCP 使用大写 `-P`，远程路径前使用英文冒号。

## 文件权限

对纯静态站点，Nginx 通常只需读取文件和进入目录，不必拥有整个 `/var/www`。以下仅适用于已确认的静态站点目录：

```bash
sudo find /var/www/example.com -type d -exec chmod 755 {} \;
sudo find /var/www/example.com -type f -exec chmod 644 {} \;
```

应用代码、`.env`、私钥及上传目录需单独设置权限，不套用上述批量命令。需要写入时只授权对应的数据目录。

## Node.js 与 PM2

使用运行应用的普通用户，按 [nvm 官方说明](https://github.com/nvm-sh/nvm#installing-and-updating)安装 nvm，重新打开 Bash 或加载其初始化文件。原笔记的 `v0.39.7` 安装地址属于旧版记录。

```bash
nvm install --lts
node -v
npm -v
npm install -g pm2
cd /var/www/html/work
pm2 start app.js --name my-website
pm2 startup
```

先执行 `pm2 startup` 输出的系统配置命令，再保存当前进程列表：

```bash
pm2 save
pm2 status
pm2 logs my-website
```

示例假设 `app.js` 与项目依赖已经就绪。PM2 管理 Node.js 进程，Nginx 将请求转发到应用监听的本地端口，两者需分别配置。升级 nvm 管理的 Node.js 后，检查并重新生成 PM2 自启配置。

## 日志与配置检查

```bash
sudo nginx -t
sudo tail -f /var/log/nginx/error.log
sudo journalctl -u nginx -f
```

修改配置时先检查，再执行 `sudo systemctl reload nginx`。

## 参考

- [PM2 开机启动](https://pm2.keymetrics.io/docs/usage/startup/)
- [数据库部署](MariaDB.md)
