###### 图片查看器安装

为Win10和Qin11系统，安装图片查看器

- WIN+R，输入

  ```
  regedit
  ```

- 打开注册表，查找文件夹位置，如下：

  ```
  HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows Photo Viewer/Capabilities/FileAssociations
  ```

- 新建字符串值.png	.jpg	.jpeg	.gif

  ```
  PhotoViewer.FileAssoc.Tiff
  ```

###### Win10预装软件卸载

- 以管理员身份，打开powershell
- 输入以下命令（不卸载微软商店）

```
Get-AppxPackage -allusers | Where-Object {$_.Name -notlike "*Microsoft.WindowsStore*"} | Remove-AppxPackage
```

- 安装预装软件

```
Get-AppxPackage -allusers | foreach {Add-AppxPackage -register "$($_.InstallLocation)\appxmanifest.xml" -DisableDevelopmentMode}
```

###### scp命令

**基本语法**

```
scp [options] [[user@]host1:]file1 [[user@]host2:]file2
```

options:

- -r:整个文件夹所有文件
- -P：端口

1.从服务器拉取文件

```
scp -r root@154.36.183.45:/root/binance_quant/* "C:/Users/源恒/Desktop/data/"
```

```
scp -r root@154.36.183.45:/var/www/html/work/data/bosszhipin_2026_04_18.json "C:/Users/Elin/Desktop/"
```

2.本地上传文件

```
scp "C:\Users\源恒\Desktop\0319\quant\data_app.py" root@154.36.183.45:/root/binance_quant/
```

```
scp -r "C:/Users/Elin/Desktop/work" root@154.36.183.45:/var/www/html/
```



###### Win11右键修改

- win键 + X

- Windows终端

  ```
  reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
  ```

- 回车

##### Netch使用

###### Slower订阅

- 复制链接

- 点开 `订阅` >>> `管理订阅链接`

  将订阅地址粘贴到 `链接` 一栏

  备注栏中输入 `Slower`, 点击 `添加`，关闭窗口返回

  点开 `订阅` - `从订阅链接更新服务器`

###### vmess服务器添加

```
备注：jp_vps
地址：panel.moonode.uk：443
用户ID：填写id
额外ID：0
加密方式：auto
传输协议：ws
伪装类型：none
主机：panel.moonode.uk
路径：/v2ray/
QUIC加密方式:none
QUIC加密密钥:
Mux多路复用:false
TLS底层传输安全:tls
```

##### ssh配置

###### 生成 SSH 密钥

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

###### 获取ssh信息

> PowerShell中运行

```
Get-Content C:\Users\用户名\.ssh\id_rsa.pub
```

###### 初始化连接

```
ssh -i C:\Users\用户名\.ssh\id_rsa root@服务器IP地址192.16.80.54
```

###### 日常连接

```
ssh root@服务器IP地址192.16.80.54
```

##### DNS刷新

```
# 刷新本地 DNS 解析缓存
ipconfig /flushdns

# 释放当前的 IP 租约（可选，增加成功率）
ipconfig /release

# 重新获取解析
ipconfig /renew
```

##### VS Code

###### 安装Remote-SSH插件

1. 在你的本地电脑安装 **VS Code**。

2. 安装插件：**Remote - SSH**。

3. 点击左下角的蓝色图标 `< >`，选择 **Connect to Host**。

4. 输入 `root@你的日本VPS_IP`。

5. 在 VS Code 左侧侧边栏点击 **“打开文件夹” (Open Folder)**。

   在弹出的输入框中输入：`/var/www/html`。

###### 使用内置终端

按下 **`Ctrl + ~`** (Esc 下面那个键)，你会发现 VS Code 下方弹出了一个终端。

这个终端**直接就是你的 VPS 命令行**。你不需要再开一个第三方 SSH 工具（如 Putty 或 Termius），在这里执行 `python3 quant_manager.py` 或查看 `tail -f /var/www/html/db/contact_submissions.json` 非常方便。

###### SSH配置修改

> 

###### 输入与AI提示冲突

修改 VS Code 核心设置（最有效）
打开 VS Code 设置（Ctrl + ,），搜索并修改以下两项：

> Editor: Accept Suggestion On Commit Character
>
> 操作： 取消勾选（Off）。
>

原因： 开启此项时，输入法上屏（按空格或数字）会被 VS Code 误判为确认代码补全，导致拼音直接变成英文字符。

> Editor: Suggest On Trigger Characters
>
> 操作： 取消勾选（Off）。
>
> 原因： 防止在你输入特定符号时突然弹出补全框，干扰输入法。

###### Chrome截取网页长图

1. 打开想截图的网页;
2. 按下 `F12`（或者 `Ctrl + Shift + I` / Mac 用 `Cmd + Option + I`）打开**开发者工具**;
3. 按下组合键 `Ctrl + Shift + P`（Mac 用 `Cmd + Shift + P`）打开**指令菜单**;
4. 在输入框中输入 `Capture`;
5. 在下拉选项中找到 **`Capture full size screenshot`**，选中并回车;
6. 浏览器会自动滚动并生成一张 `.png` 图片存入你的下载文件夹

##### Python自动SCP脚本

本地电脑（Windows）已经配置好了 Git Bash 或者安装了 OpenSSH，你可以直接用 Python 调用系统的 scp 命令。

- 优点：不需要安装额外的 Python 库，代码量少。
- 缺点：依赖本地环境必须有 scp 命令。

```python
import subprocess
import os

def upload_via_scp(local_file, remote_path):
    """
    local_file: 本地文件路径，例如 'jobs.csv'
    remote_path: 远程完整路径，例如 'root@1.2.3.4:/root/job_analysis/jobs.csv'
    """
    # 拼接命令
    # 注意：Windows下如果是Git Bash环境可以直接用scp，否则可能需要指定全路径
    command = f"scp {local_file} {remote_path}"
    
    print(f"🚀 正在上传: {local_file} ...")
    try:
        # shell=True 允许运行字符串形式的命令
        result = subprocess.run(command, shell=True, check=True)
        print("✅ 上传成功！")
    except subprocess.CalledProcessError as e:
        print(f"❌ 上传失败: {e}")

# 使用示例
# 建议将 remote_path 写死在配置里
REMOTE_USER = "root"
REMOTE_IP = "你的VPS_IP"
REMOTE_DIR = "/root/job_analysis/jobs.csv"

# 爬虫跑完后执行
# upload_via_scp("jobs.csv", f"{REMOTE_USER}@{REMOTE_IP}:{REMOTE_DIR}")
```



```python
import subprocess

cmd = "scp D:\\codes\\jobs.csv root@你的VPS_IP:/root/job_analysis/jobs.csv"

print(f"🚀 正在唤起 PowerShell 执行: {cmd}")

# shell=True 表示通过系统的 Shell (PowerShell) 来执行
# capture_output=True 表示捕获输出结果（成功或失败的信息）
# text=True 表示把输出结果当成文本处理（而不是乱码字节）
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

# 打印结果
if result.returncode == 0:
    print("✅ 上传成功！")
    print(result.stdout) # 打印 PowerShell 的输出
else:
    print("❌ 出错了：")
    print(result.stderr) # 打印错误信息
```

