```
git config --global user.name "yh-cocanie"
git config --global user.email cocanadalope@gmail.com
```

```
You don't have any public SSH keys in your GitHub account. You can add a new public key, or try cloning this repository via HTTPS.
```

1. cmd命令行

```
# 如果系统不支持ED25519，使用RSA
ssh-keygen -t rsa -b 4096 -C "cocanadalope@gmail.com"
```

```
Your identification has been saved in C:\Users\源恒/.ssh/id_rsa
Your public key has been saved in C:\Users\源恒/.ssh/id_rsa.pub

```

###### 启动SSH代理并添加密钥

```
# 启动SSH代理
eval "$(ssh-agent -s)"

# 添加SSH私钥到代理
ssh-add ~/.ssh/id_ed25519
```

###### 查看生成的公钥

```
cat ~/.ssh/id_rsa.pub

查看生成的公钥
在本地文件夹下打开git bash
```

###### 在 Github 中添加公钥

```

```

###### 测试链接

```
ssh -T git@github.com
```

```
git clone git@github.com:Linkenpro/MarkNote.git
```

```
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
```

###### 暂存文件

```
# 或者添加所有修改的文件
git add .
```

###### 提交文件

```
git commit -m "Add new feature"
```

#### git配置

###### 设置用户名

```
git config user.name "用户名"
```

###### 设置邮箱

```
git config user.email "你的邮箱"
```

###### 检查信息

```
git config -l
```

###### 检查状态

```
git status
```

###### 加载当前目录

```
git add .
```

###### 提交本地仓库

```
git conmmit -m "2023年03月29日21时28分"
```

第三方SSH

###### 生成sshkey

```
ssh-keygen -t rsa -C "2421814924@qq.com"
```

###### 查看公钥

```
cat ~/.ssh/id_rsa.pub
```

###### 粘贴ssh

###### 终端

```
ssh -T git@github.com
```

#### 问题处理

###### 连接超时

问题处理
连接超时22
————
vim ~/.ssh/config
写入
Host github.com
Hostname ssh.github.com
Port 443
保存
:wq

> 按ESC键切换到下面输入，按I切换上页输入

###### 自动提交脚本

> 日常使用状态下
>
> git add .
>
> git commit -m '提交的信息'
>
> git push

bat脚本自动化

```bash
@echo off
:: 放弃 UTF-8，回归原生中文编码以解决命令识别错误
chcp 936 >nul

:: 1. 强制使用短路径格式 (PROGRA~1 这种逻辑) 
:: 这里的 C:\Users\源恒 对应的短路径通常可以直接用绝对字符串
set "KEY=C:/Users/源恒/.ssh/id_rsa"

:: 2. 告诉 Git 使用指定的 SSH 钥匙，并禁止它去写 known_hosts
set GIT_SSH_COMMAND=ssh -i "%KEY%" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null

:: 3. 执行同步
cd /d "D:\MarkNote"

echo [1/3] Adding files...
git add .

echo [2/3] Committing...
git commit -m "Auto-sync %date% %time%"

echo [3/3] Pushing to GitHub...
:: 直接推送，不再打印带中文的提示信息，防止脚本崩溃
git push

if %errorlevel% equ 0 (
    echo Sync Success!
) else (
    echo Sync Failed. Check your SSH Key on GitHub.
)

pause >nul
```

