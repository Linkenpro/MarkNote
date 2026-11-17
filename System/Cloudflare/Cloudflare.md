# Cloudflare

## DNS 域名解析

在 `DNS → Records → Add record` 添加记录。

### A 记录

| 配置项 | 填写值 |
| --- | --- |
| Type | `A` |
| Name | `@`（根域名，如 `moonode.uk`） |
| Content | VPS 公网 IP |
| Proxy status | 按下表选择 |
| TTL | `Auto` |

### 代理模式

| 模式 | 用途 |
| --- | --- |
| DNS Only（灰云） | 仅解析到源站，例如 SSH、数据库连接 |
| Proxied（橙云） | 网站流量经过 Cloudflare，用于博客、网页监控面板等 |

## R2 对象存储

### 连接参数

| 参数 | 值 |
| --- | --- |
| rclone remote 名称 | `r2` |
| 存储桶 | `moonode-backups` |
| Access Key ID | `<ACCESS_KEY_ID>` |
| Secret Access Key | `<SECRET_ACCESS_KEY>` |
| S3 endpoint | 从 R2 后台复制，通常为 `https://<ACCOUNT_ID>.r2.cloudflarestorage.com` |
| 量化项目目录 | `/root/binance_quant` |

密钥只在本机配置中填写，不存入笔记。原笔记中的明文凭据需在后台撤销并重新生成；修改本文不会清除 Git 历史中的旧值。

### 安装与配置 rclone

在 VPS 上执行：

```bash
curl https://rclone.org/install.sh | sudo bash
rclone config
```

按向导填写：

| 配置项 | 填写值 |
| --- | --- |
| New remote | `n` |
| name | `r2` |
| Storage | `s3` |
| provider | `Cloudflare` |
| env_auth | `false` |
| access_key_id | 后台生成的 Access Key ID |
| secret_access_key | 后台生成的 Secret Access Key |
| region | `auto` |
| endpoint | 上表中的 S3 endpoint |
| location_constraint / acl | 回车，保留默认值 |
| Edit advanced config | `n` |
| Yes this is OK | `y` |

### 上传与连接测试

```bash
# 查看桶内文件
rclone ls r2:moonode-backups/

# 上传测试文件，再确认结果
echo "R2 Backup Test Successful!" > test-r2.txt
rclone copy test-r2.txt r2:moonode-backups/
rclone ls r2:moonode-backups/
```

### 定时备份

原有方案：每天打包数据库与日志，上传到 R2 的 `backups/年/月/`，上传成功后清理项目目录中超过 7 天的本地备份包。

以下命令保留原笔记的备份逻辑，尚未在服务器验证。将脚本保存为 `/root/binance_quant/backup-r2.sh`：

```bash
#!/usr/bin/env bash
set -e

cd /root/binance_quant
archive="backup-$(date +%F).tar.gz"
remote="r2:moonode-backups/backups/$(date +%Y)/$(date +%m)/"

tar -czf "$archive" crypto_data.db logs/cron.log
rclone copy "$archive" "$remote"
find . -name 'backup-*.tar.gz' -mtime +7 -delete
```

执行 `crontab -e`，添加：

```cron
0 9 * * * /bin/bash /root/binance_quant/backup-r2.sh >> /root/binance_quant/logs/backup-r2.log 2>&1
```

`09:00` 按服务器 cron 使用的时区解释。该脚本是部署示例；整理笔记不会安装定时任务。

## Pages 静态网站

流程：Hugo 创建网站 → 推送 GitHub → 连接 Cloudflare Pages → 绑定域名。

### 创建 Hugo 项目

Windows 已安装 Chocolatey 时：

```powershell
choco install hugo --confirm
```

创建项目并下载 PaperMod 主题：

```bash
hugo new site my-portfolio
cd my-portfolio
git init
git clone https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

### 配置主题与撰写内容

编辑 `hugo.toml`，设置主题、站点标题和域名 `moonode.uk`。

```bash
hugo new content posts/my-first-quant-strategy.md
```

编辑生成的 Markdown 文件，再将项目推送到 GitHub 仓库。

### 部署到 Pages

在 Cloudflare 的 `Workers & Pages` 中创建 Pages 项目并连接 GitHub 仓库。

| 构建配置 | 值 |
| --- | --- |
| Framework preset | `Hugo` |
| Build command | `hugo --minify` |
| Build output directory | `public` |

保存并部署。

### 绑定域名

在 Pages 项目的 `Custom Domains` 中添加 `moonode.uk`，按页面提示完成 DNS 配置。
