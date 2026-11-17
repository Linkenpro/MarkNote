# 3x-ui 部署记录

返回 [VPS](VPS.md)。保留原配置思路；面板版本、Xray 核心和客户端支持情况需在实际部署时确认。旧菜单编号不作为当前操作步骤。

## 安装与面板

安装入口见 [3x-ui 官方仓库](https://github.com/MHSanaei/3x-ui)。原记录使用官方 `install.sh` 脚本；部署前按选定版本说明检查脚本和依赖，不在笔记中固定跟随 master 的一键执行命令。

| 项目 | 记录 |
| --- | --- |
| 用户名 | `REPLACE_WITH_PANEL_USER` |
| 密码 | `REPLACE_WITH_PANEL_PASSWORD` |
| 面板端口 | `54321`，原示例，按实际设置 |
| 管理命令 | `x-ui` |
| 管理地址 | 记录实际协议、域名、端口及面板路径 |

面板端口与代理入站端口分别管理；防火墙只放行实际需要的入口。面板访问应配置 HTTPS 与访问范围。配置变更前保存面板备份，含凭据的备份不提交到仓库。

## 入站配置记录

| 方案 | 原记录字段 | 部署时需确认 |
| --- | --- | --- |
| VLESS + XHTTP + Reality | 入站端口、路径 `/abc`、目标地址、SNI、密钥对 | 核心和客户端版本、目标兼容性、双方参数 |
| VLESS + TCP + Reality | 入站端口、目标地址、SNI、密钥对 | 界面中的 TCP/RAW 名称、目标兼容性、双方参数 |
| VMess + WebSocket + TLS | 域名、路径、TLS 证书、入口端口 | TLS 终止位置、WebSocket 路径、证书与域名匹配 |

Reality 的目标地址与 SNI 应根据实际目标核验；原先列举的公共域名不作为通用可用配置。导出链接或二维码后，还需确认客户端支持相应传输，不能仅以导入成功判断连通。

## 域名与证书

DNS 配置见 [Cloudflare](../Cloudflare/Cloudflare.md)，Nginx 与证书管理见 [Web](Web.md)。

- 直连示例：域名 A/AAAA 指向 VPS；是否启用 Cloudflare 代理取决于所用传输方式。
- 面板证书和入站证书分别检查，不假设面板配置会自动应用到所有入站。
- 证书验证端口取决于验证方式，原记录的 `54300` 不是通用验证端口。
- Nginx 与入站服务不能同时占用相同地址、端口；先明确 TLS 在哪里终止。

## Nginx 转发 WebSocket

以下片段放入已有 HTTPS `server` 块：Nginx 负责 TLS，后端入站监听 `127.0.0.1:12345`，使用无 TLS 的 WebSocket，路径统一为 `/v2ray/`。

```nginx
location /v2ray/ {
    proxy_pass http://127.0.0.1:12345;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_redirect off;
}
```

`12345` 是后端入站端口，不是面板管理端口。客户端也应使用 `/v2ray/`，不要再混用旧示例 `/abb`。修改后执行 `nginx -t`，成功后加载配置。

## 历史记录

以下仅保留查阅线索，未验证当前适用性：

| 项目 | 原记录 |
| --- | --- |
| BBR 菜单 | `23 → 1` |
| 证书菜单 | `18 → 1` |
| 客户端 | Windows：Netch；Android：v2rayNG；Mac 未记录 |
| 测速工具 | CloudflareSpeedTest，运行 `CloudflareST.exe`，查看 CSV 结果 |
| 候选 HTTPS 端口 | `443`、`2053`、`2083`、`2087`、`2096`、`8443` |

旧测速 IP：`162.159.39.28`、`162.159.44.234`、`162.159.44.36`、`162.159.38.187`、`162.159.39.62`、`162.159.45.188`。原标注为“日本服务器优选 IP”，但未记录测试日期与网络环境，不能据此推断当前速度或地理位置。

若所用方案支持 CDN，客户端的连接 IP、Host 和 SNI 需分别配置；旧示例中的 Host/SNI 均为自有域名。测速结果只对测试时的网络条件有参考意义。

## 参考

- [3x-ui 官方仓库](https://github.com/MHSanaei/3x-ui)
- [Nginx WebSocket 转发](https://nginx.org/en/docs/http/websocket.html)
