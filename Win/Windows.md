## 1. Windows 系统设置

### 1.1 图片查看器安装（Win10 / Win11）

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

### 1.2 Win10 预装软件卸载

以**管理员身份**运行 PowerShell：

- **卸载所有非商店应用**（保留微软商店）：
  ```powershell
  Get-AppxPackage -allusers | Where-Object {$_.Name -notlike "*Microsoft.WindowsStore*"} | Remove-AppxPackage
  ```

- **恢复所有预装软件**：
  ```powershell
  Get-AppxPackage -allusers | foreach {Add-AppxPackage -register "$($_.InstallLocation)\appxmanifest.xml" -DisableDevelopmentMode}
  ```

### 1.3 Win11 右键菜单恢复经典样式

- `Win + X` → 选择 **Windows 终端**
- 执行命令：
  ```cmd
  reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
  ```
- 重启电脑生效

### 1.4 DNS 缓存刷新

```cmd
ipconfig /flushdns   # 刷新 DNS 缓存
ipconfig /release    # 释放 IP 租约（可选）
ipconfig /renew      # 重新获取 IP
```

## 2. 网络工具与远程连接

### 2.1 SCP 命令（安全复制）

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

### 2.2 SSH 配置

**生成 SSH 密钥**（在本地）：
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

**查看本地公钥**（PowerShell）：
```powershell
Get-Content C:\Users\用户名\.ssh\id_rsa.pub
```

**首次连接**（使用密钥文件）：
```bash
ssh -i C:\Users\用户名\.ssh\id_rsa root@服务器IP
```

**日常连接**（密钥已配置后）：
```bash
ssh root@服务器IP
```

### 2.3 Netch 代理工具使用

#### Slower 订阅更新
1. 复制订阅链接
2. 打开 Netch → **订阅** → **管理订阅链接**
3. 粘贴链接，备注 `Slower`，点击添加
4. 返回后点击 **订阅** → **从订阅链接更新服务器**

#### vmess 服务器手动添加

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

## 3. 开发环境配置

### 3.1 VS Code 插件与设置

#### Remote-SSH 插件（连接 VPS）
1. 安装 **Remote - SSH** 插件
2. 点击左下角蓝色图标 `< >` → **Connect to Host**
3. 输入 `root@你的VPS_IP`
4. 连接成功后，点击 **打开文件夹**，输入 `/var/www/html`
5. 使用内置终端：`Ctrl + ~` 即可直接在 VPS 上执行命令

#### 解决中文输入与 AI 补全冲突
修改 VS Code 设置（`Ctrl + ,`）：

| 设置项                                          | 操作     | 原因                                 |
| ----------------------------------------------- | -------- | ------------------------------------ |
| `Editor: Accept Suggestion On Commit Character` | 取消勾选 | 防止输入法上屏被误判为确认补全       |
| `Editor: Suggest On Trigger Characters`         | 取消勾选 | 防止输入特定符号时弹出补全框干扰输入 |

### 3.2 SFTP 插件（VSCode）

安装插件：**SFTP**（推荐 `Natizyskunk` 版本）

**配置 `.vscode/sftp.json`**：
```json
{
    "name": "My Server",
    "host": "154.36.183.45",
    "protocol": "sftp",
    "port": 50501,
    "username": "root",
    "privateKeyPath": "C:/Users/源恒/.ssh/id_rsa", 
    "remotePath": "/var/www",
    "uploadOnSave": true,
    "downloadOnOpen": true,
    "watcher": {
        "files": "*",
        "autoUpload": true,
        "autoDelete": true
    },
    "ignore": [
    "**/.vscode/**",
    "**/.git/**",
    "**/node_modules/**",
    "**/logs/**"
]
}
```

**使用说明**：
- **自动上传**：保存文件（`Ctrl + S`）后自动同步到 VPS
- **手动上传/下载**：右键文件/文件夹 → 选择 `SFTP: Upload` 或 `Download`
- **对比差异**：右键 → `SFTP: Diff` 查看本地与远程差异

###### 手动同步

- **右键点击文件夹** -> 选择 `SFTP: Sync Remote -> Local`。
- 这会扫描 VPS 上的新文件并下载到本地

### 3.3 Python 自动 SCP 脚本

#### 方法一：调用系统 scp 命令（依赖 Git Bash 或 OpenSSH）

```python
import subprocess

def upload_via_scp(local_file, remote_path):
    command = f"scp {local_file} {remote_path}"
    print(f"🚀 正在上传: {local_file} ...")
    try:
        subprocess.run(command, shell=True, check=True)
        print("✅ 上传成功！")
    except subprocess.CalledProcessError as e:
        print(f"❌ 上传失败: {e}")

# 示例
REMOTE_USER = "root"
REMOTE_IP = "你的VPS_IP"
REMOTE_DIR = "/root/job_analysis/jobs.csv"
upload_via_scp("jobs.csv", f"{REMOTE_USER}@{REMOTE_IP}:{REMOTE_DIR}")
```

#### 方法二：直接通过 PowerShell 执行

```python
import subprocess

cmd = "scp D:\\codes\\jobs.csv root@你的VPS_IP:/root/job_analysis/jobs.csv"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print("✅ 上传成功！", result.stdout)
else:
    print("❌ 出错：", result.stderr)
```

### 3.4 OpenCode 安装（Windows）

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

## 4. 浏览器实用技巧

### Chrome 截取网页长图

文件夹内只有servicehost.ini

> 名为 `ODIS` 的文件夹的权限修改（文件夹初始设置为所有账户和组织都不能修改）
>
> 强制将 `ODIS` 文件夹的所有权转交给你的管理员账户
>
> ```
> takeown /f "C:\ProgramData\Autodesk\ODIS" /r /d y
> ```
>
> 删除整个文件夹，至此可以运行`AdODIS-installer.exe`
>
> 最新的 ODIS 安装包：https://emsfs.autodesk.com/utility/odis/1/installer/latest/AdODIS-installer.exe
>
> **以管理员身份运行**安装
>
> 安装完成后，可以运行`CAD2025安装程序`

###### 注册表修改软件安装日期（试用时间）

> 系统从注册表中读取的一个数值

1. 按下 Win + R，输入 regedit 并回车，打开注册表编辑器

2. 定位到软件信息路径，通常软件的安装信息存储在以下两个位置之一（取决于软件是为当前用户还是全系统安装的）：

   ```
   路径 A：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
   
   路径 B（64位系统下的32位软件）：HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall
   
   路径 C（仅限当前用户安装）：HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall
   ```

3. 找到对应的软件文件夹：
   在 Uninstall 文件夹下会有很多子文件夹（有些是软件名，有些是一串大括号组成的 GUID）。点击文件夹，在右侧找到 DisplayName 项，确认它是你想修改的软件。

4. 修改 InstallDate 值：

   - 在右侧列表中找到名为 **`InstallDate`** 的字符串值（REG_SZ）。

   - 双击它，将数值修改为你想要的日期。

   - **格式要求**：必须是 `YYYYMMDD`（例如，你想改为2024年5月20日，就输入 `20240520`）。

5. 查看结果

1. 打开目标网页
2. 按 `F12`（或 `Ctrl+Shift+I`）打开**开发者工具**
3. 按 `Ctrl+Shift+P`（Mac: `Cmd+Shift+P`）打开**指令菜单**
4. 输入 `Capture`，选择 **`Capture full size screenshot`** 并回车
5. 浏览器自动生成长截图并保存为 `.png` 到下载文件夹

