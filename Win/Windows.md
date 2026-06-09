#### 1. Windows 系统设置

##### Win10/Win11图片查看器安装

为系统安装传统 Windows 照片查看器：

1. `Win + R` 输入 `regedit` 打开注册表
2. 定位到：
   ```
   HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows Photo Viewer/Capabilities/FileAssociations
   ```
3. 新建字符串值，名称分别为 `.png` `.jpg` `.jpeg` `.gif`，数值数据均填写：
   ```
   PhotoViewer.FileAssoc.Tiff
   ```

##### Win10 预装软件卸载

以**管理员身份**运行 PowerShell：

- **卸载所有非商店应用**（保留微软商店）：
  ```powershell
  Get-AppxPackage -allusers | Where-Object {$_.Name -notlike "*Microsoft.WindowsStore*"} | Remove-AppxPackage
  ```

- **恢复所有预装软件**：
  ```powershell
  Get-AppxPackage -allusers | foreach {Add-AppxPackage -register "$($_.InstallLocation)\appxmanifest.xml" -DisableDevelopmentMode}
  ```

##### Win11右键菜单恢复经典样式

- `Win + X` → 选择 **Windows 终端**
- 执行命令：
  ```cmd
  reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
  ```
- 重启电脑生效

##### DNS 缓存刷新

```cmd
ipconfig /flushdns   # 刷新 DNS 缓存
ipconfig /release    # 释放 IP 租约（可选）
ipconfig /renew      # 重新获取 IP
```

#### 2. 网络工具与远程连接

##### SCP命令

**基本语法**：
```
scp [options] [[user@]host1:]file1 [[user@]host2:]file2
```
常用选项：
- `-r`：复制整个文件夹
- `-P`：指定端口（大写 P）

**从服务器拉取文件**：
```bash
scp -r root@154.36.183.45:/root/binance_quant/* "C:/Users/源恒/Desktop/data/"
scp -r root@154.36.183.45:/var/www/html/work/data/bosszhipin_2026_04_18.json "C:/Users/Elin/Desktop/"
```

**本地上传文件**：

```bash
scp "C:\Users\源恒\Desktop\0319\quant\data_app.py" root@154.36.183.45:/root/binance_quant/
scp -r "C:/Users/Elin/Desktop/work" root@154.36.183.45:/var/www/html/
```

##### SSH 配置

生成 SSH 本地密钥：
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

查看本地公钥：
```powershell
Get-Content C:\Users\用户名\.ssh\id_rsa.pub
```

首次连接
```bash
ssh -i C:\Users\用户名\.ssh\id_rsa root@服务器IP
```

日常连接（配置后）：
```bash
ssh root@服务器IP
```

##### Netch 代理工具使用

###### Slower 订阅更新
- 复制订阅链接
- 打开 Netch → **订阅** → **管理订阅链接**
- 粘贴链接，备注 `Slower`，点击添加
- 返回后点击 **订阅** → **从订阅链接更新服务器**

###### vmess 服务器手动添加

| 字段            | 值                   |
| --------------- | -------------------- |
| 备注            | jp_vps               |
| 地址            | panel.moonode.uk:443 |
| 用户ID          | （填写你的 ID）      |
| 额外ID          | 0                    |
| 加密方式        | auto                 |
| 传输协议        | ws                   |
| 伪装类型        | none                 |
| 主机            | panel.moonode.uk     |
| 路径            | /v2ray/              |
| QUIC加密方式    | none                 |
| QUIC加密密钥    | （留空）             |
| Mux多路复用     | false                |
| TLS底层传输安全 | tls                  |

#### 3. 开发环境配置

##### Remote-SSH 插件连接VPS
1. 安装 **Remote - SSH** 插件
2. 点击左下角蓝色图标 `< >` → **Connect to Host**
3. 输入 `root@你的VPS_IP`
4. 连接成功后，点击 **打开文件夹**，输入 `/var/www/html`
5. 使用内置终端：`Ctrl + ~` 即可直接在 VPS 上执行命令

##### SFTP同步插件

插件作者： `Natizyskunk` 版本

> 文件设置："C:\Users\源恒\.ssh\config"

```
Host my-vps
    HostName 154.36.183.45
    User root
    Port 50501
    # 正确路径
    IdentityFile C:\Users\源恒\.ssh\id_rsa
```

**配置 `.vscode/sftp.json`**：
```json
{
    "name": "My Server",
    "host": "154.36.183.45",
    "protocol": "sftp",
    "port": 50501,
    "username": "root",
    "privateKeyPath": "C:/Users/源恒/.ssh/id_rsa",
    "remotePath": "/root/quant/binance",
    "uploadOnSave": false,
    "logLevel": "info",
    "keepaliveInterval": 0,
    "sshConfig": {
        "KeepAlive": true
    },
    "ignore": [
        "**/.vscode/**",
        "**/.git/**",
        "**/__pycache__/**"
    ]
}
```

**使用说明**：
- 手动同步下载： `SFTP: Sync Remote -> Local`
- 手动同步上传： `SFTP: Sync Local -> Remote`

###### Nodejs版本不兼容

尝试将远程文件同步到本地时，与其底层的 SSH 依赖库（ssh2）发生了严重的 Node.js 版本不兼容问题

**手动修复插件源码**

源码位置

```
C:\Users\Elin\.vscode\extensions\natizyskunk.sftp-1.16.3\node_modules\ssh2\lib\protocol\SFTP.js
```

第2492行

```js
if ((typeof attrs.atime === 'number' || isDate(attrs.atime))
        && (typeof attrs.mtime === 'number' || isDate(attrs.mtime))) {
      const atime = toUnixTimestamp(attrs.atime);
      const mtime = toUnixTimestamp(attrs.mtime);
      flags |= ATTR.ACMODTIME;
      // Big Endian
      ATTRS_BUF[nb++] = atime >>> 24;
      ATTRS_BUF[nb++] = atime >>> 16;
      ATTRS_BUF[nb++] = atime >>> 8;
      ATTRS_BUF[nb++] = atime;
      ATTRS_BUF[nb++] = mtime >>> 24;
      ATTRS_BUF[nb++] = mtime >>> 16;
      ATTRS_BUF[nb++] = mtime >>> 8;
      ATTRS_BUF[nb++] = mtime;
    }
    // TODO: extended attributes
  } 
```

把

```js
if ((typeof attrs.atime === 'number' || isDate(attrs.atime))
        && (typeof attrs.mtime === 'number' || isDate(attrs.mtime))) {
```

修改成

```js
if ((typeof attrs.atime === 'number' || attrs.atime instanceof Date)
        && (typeof attrs.mtime === 'number' || attrs.mtime instanceof Date)) {
```

彻底重启一次 VS Code 让插件重新加载

##### 安装OpenCode

1. 安装 Node.js
2. **以管理员身份运行 PowerShell**，执行：
   
   ```powershell
   Set-ExecutionPolicy RemoteSigned
   ```
   输入 `Y` 确认
3. 使用命令提示符（CMD）安装：
   ```cmd
   npm i -g opencode-ai
   ```

#### 4. 浏览器实用技巧

###### Chrome截取网页长图

- 查看结果

- 打开目标网页
- 按 `F12`（或 `Ctrl+Shift+I`）打开**开发者工具**
- 按 `Ctrl+Shift+P`（Mac: `Cmd+Shift+P`）打开**指令菜单**
- 输入 `Capture`，选择 **`Capture full size screenshot`** 并回车
- 浏览器自动生成长截图并保存为 `.png` 到下载文件夹

#### 5.Autodesk

###### Autodesk CAD安装报错问题解决

文件夹内只有servicehost.ini

> 名为 `ODIS` 的文件夹的权限修改（文件夹初始设置为所有账户和组织都不能修改）
>

- 强制将 `ODIS` 文件夹的所有权转交给你的管理员账户

```
takeown /f "C:\ProgramData\Autodesk\ODIS" /r /d y
```

- 删除整个文件夹，至此可以运行`AdODIS-installer.exe`


- 最新的 ODIS 安装包：https://emsfs.autodesk.com/utility/odis/1/installer/latest/AdODIS-installer.exe


- **以管理员身份运行**安装

- 安装完成后，可以运行`CAD2025安装程序`

#### 6.Git

###### git bash窗口代理

> 解决git bash上传下载速度慢

```
git config --global http.proxy socks5://127.0.0.1:2801
git config --global https.proxy socks5://127.0.0.1:2801
```

