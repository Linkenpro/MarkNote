# Windows

系统设置、远程连接与开发工具备忘。代码块注明运行环境；示例中的服务器地址、用户名和路径需按实际配置替换。

## 系统设置

### 传统照片查看器

历史方法：为已存在的 Windows 照片查看器补充文件关联，不是安装查看器组件；不同 Windows 版本可能不适用。

使用 `Win + R → regedit` 打开注册表，修改前导出目标项备份。

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations
```

在该项下添加字符串值：

| 名称 | 数值数据 |
| --- | --- |
| `.png` | `PhotoViewer.FileAssoc.Tiff` |
| `.jpg` | `PhotoViewer.FileAssoc.Tiff` |
| `.jpeg` | `PhotoViewer.FileAssoc.Tiff` |
| `.gif` | `PhotoViewer.FileAssoc.Tiff` |

### 预装应用管理

优先在 Windows 设置中卸载指定应用。使用 PowerShell 时，先确认包名，再针对单个包操作：

```powershell
Get-AppxPackage | Select-Object Name, PackageFullName

# 将占位符替换成上一步确认的完整包名
Remove-AppxPackage -Package '<PackageFullName>'
```

默认针对当前用户。原笔记中“排除 Microsoft Store 后批量卸载”的命令会匹配大量应用，不等于只卸载第三方软件，因此不保留为日常操作。

已有应用文件但注册异常时，可针对实际存在的清单重新注册：

```powershell
Add-AppxPackage -Register 'C:\实际安装目录\AppxManifest.xml' -DisableDevelopmentMode
```

重新注册不等于重新下载安装，不能保证恢复已删除的全部应用。

### Windows 11 经典右键菜单

以下是历史注册表技巧，是否有效取决于系统版本。修改前备份对应注册表项。

```cmd
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

重启后检查效果。需要恢复时，还原修改前的注册表备份。

## 网络与远程连接

### DNS 与 DHCP

在 CMD 中执行：

```cmd
rem 刷新 DNS 缓存
ipconfig /flushdns
```

DHCP 租约异常时再使用下列命令；释放租约会暂时中断对应网络连接，不是刷新 DNS 的必要步骤。

```cmd
ipconfig /release
ipconfig /renew
```

### SSH 密钥与连接配置

以下在 PowerShell 中执行，保留原笔记的 RSA 4096 位密钥示例：

```powershell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Get-Content "$env:USERPROFILE\.ssh\id_rsa.pub"
```

将公钥配置到服务器目标用户的 `~/.ssh/authorized_keys`，私钥保留在本机。连接前确认服务器主机指纹。

编辑 `%USERPROFILE%\.ssh\config`，例如：

```sshconfig
Host my-vps
    HostName 服务器IP
    User root
    Port 50501
    IdentityFile ~/.ssh/id_rsa
```

`50501` 为原笔记中的自定义 SSH 端口示例，需与服务器一致。配置后连接：

```powershell
ssh my-vps
```

### SCP 文件传输

使用上面的 SSH 别名，可复用服务器地址、端口和密钥设置：

```powershell
# 下载目录到本地；目标目录需存在
scp -r my-vps:/root/binance_quant "$env:USERPROFILE/Desktop/data/"

# 上传单个文件
scp "$env:USERPROFILE/Desktop/quant/data_app.py" my-vps:/root/binance_quant/

# 上传整个目录
scp -r "$env:USERPROFILE/Desktop/work" my-vps:/var/www/html/
```

`-r` 递归复制目录；不使用 SSH 别名时，可通过大写 `-P` 指定端口。

### Netch 代理配置

历史配置记录，界面名称以安装版本为准。

订阅更新：在“订阅 → 管理订阅链接”添加链接，再从订阅链接更新服务器。

原 vmess 节点参数整理如下，需与服务端一致：

| 字段 | 示例值 |
| --- | --- |
| 备注 | `jp_vps` |
| 地址 / 端口 | `panel.moonode.uk` / `443` |
| 用户 ID | 服务端配置的 UUID |
| 额外 ID | `0` |
| 加密方式 | `auto` |
| 传输协议 | `ws` |
| 伪装类型 | `none` |
| 主机 | `panel.moonode.uk` |
| 路径 | `/v2ray/` |
| TLS | `tls` |
| Mux | `false` |

原配置使用 WebSocket，QUIC 字段无需另填。

### Git HTTP 代理

以下端口 `2801` 来自原笔记，使用前改为本机代理实际监听的 SOCKS5 端口：

```powershell
git config --global http.proxy socks5h://127.0.0.1:2801
git config --global https.proxy socks5h://127.0.0.1:2801
```

该设置用于 Git 的 HTTP(S) 传输，不会自动给 `git@github.com:...` 形式的 SSH 连接配置代理。

取消设置：

```powershell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 开发工具

### VS Code Remote - SSH

安装 **Remote - SSH** 插件，通过命令面板执行 `Remote-SSH: Connect to Host`，选择 `my-vps`。

连接后打开远程目录（如 `/var/www/html`）；集成终端中的命令在远程服务器执行。

### VS Code SFTP 同步

原笔记使用 `Natizyskunk` 的 SFTP 插件。Remote - SSH 用于直接编辑远程文件；SFTP 用于同步本地与远程副本。

在项目中创建 `.vscode/sftp.json`，以下为基本配置示例：

```json
{
    "name": "My Server",
    "host": "服务器IP",
    "protocol": "sftp",
    "port": 50501,
    "username": "root",
    "privateKeyPath": "C:/Users/用户名/.ssh/id_rsa",
    "remotePath": "/root/quant/binance",
    "uploadOnSave": false,
    "ignore": [
        "**/.vscode/**",
        "**/.git/**",
        "**/__pycache__/**"
    ]
}
```

| 操作 | 命令面板入口 |
| --- | --- |
| 下载远程文件到本地 | `SFTP: Sync Remote -> Local` |
| 上传本地文件到远程 | `SFTP: Sync Local -> Remote` |

同步前确认方向与远程路径。上面的配置显式填写连接参数，不依赖插件自动读取 SSH 别名。

### OpenCode 安装

原笔记使用 npm 安装。安装 Node.js 后，在 CMD 中执行：

```cmd
npm i -g opencode-ai
opencode --version
```

这是原有安装方式的记录，更新方法参见 [OpenCode 文档](https://opencode.ai/docs)。CMD 下执行 npm 无需修改 PowerShell 执行策略。

## 浏览器技巧

### Chrome 网页长截图

打开目标网页，按 `F12` 或 `Ctrl + Shift + I` 打开开发者工具，再按 `Ctrl + Shift + P` 打开命令菜单。

输入 `Capture`，选择 `Capture full size screenshot`，保存生成的 PNG。

### Edge IE 模式

用于需要旧版 IE 兼容的网站；是否可用取决于 Edge 配置和组织策略。

- 打开 `edge://settings/defaultBrowser`，将“允许在 Internet Explorer 模式下重新加载网站”设为允许，按提示重启。
- 打开目标网站，从菜单选择“在 Internet Explorer 模式下重新加载”。入口位置可能随版本变化。
- 如果入口不可用，检查组织策略或按官方说明配置 IE 模式站点列表。

IE 模式不会解除网站服务端的图片大小限制。

## 故障记录

### SFTP 1.16.3 日期类型判断补丁

原记录将故障归因为 Node.js 与 `ssh2` 依赖兼容问题，但未保存报错堆栈，暂不能确认根因。以下仅保留为旧版本修复记录，不作为通用安装步骤。

文件位置：

```text
%USERPROFILE%\.vscode\extensions\natizyskunk.sftp-1.16.3\node_modules\ssh2\lib\protocol\SFTP.js
```

备份文件后搜索以下判断，不依赖固定行号：

```javascript
if ((typeof attrs.atime === 'number' || isDate(attrs.atime))
    && (typeof attrs.mtime === 'number' || isDate(attrs.mtime))) {
```

原记录改为：

```javascript
if ((typeof attrs.atime === 'number' || attrs.atime instanceof Date)
    && (typeof attrs.mtime === 'number' || attrs.mtime instanceof Date)) {
```

保存后完全退出并重启 VS Code。插件更新可能覆盖手动修改。

### Autodesk 安装器 ODIS 异常

原记录：安装 CAD 2025 时，`C:\ProgramData\Autodesk\ODIS` 中仅有 `servicehost.ini`，曾通过处理该目录权限并重装 ODIS 排障。仅凭该现象不能确认故障原因。

优先按 Autodesk 官方说明卸载、重装 Installer 组件。原记录中的强制接管并删除目录属于特定环境操作，不作为默认处理步骤。

- [Autodesk 安装器无法启动的排障说明](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/When-launching-Autodesk-Installer-nothing-happens-and-no-user-interface-appears.html)
- [AdODIS 安装程序](https://emsfs.autodesk.com/utility/odis/1/installer/latest/AdODIS-installer.exe)

## 参考

- [Remove-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/remove-appxpackage)
- [Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage)
- [Edge IE 模式本地站点列表](https://learn.microsoft.com/deployedge/edge-ie-mode-local-site-list)
