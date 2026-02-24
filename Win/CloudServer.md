##### 阿里云

```
登录：root +++ A$ecret-001
```

###### 系统更新

```
sudo apt update && sudo apt upgrade -y

系统重启
sudo reboot

```

```
Tab键切换至OK
Enter确认
```

量化

```
# 检查 Python 3 版本
python3 --version

# 检查 pip 是否安装
pip3 --version

# 查看 Python 安装路径
which python3
```

###### 本地代码需要上传

**上传单个文件**

```
# 语法：scp [本地文件路径] [用户名]@[服务器IP]:[服务器目标路径]
scp /path/to/local/code.py admin@172.19.24.169:~/myproject/

# 上传整个文件夹（递归上传）
# 加上 -r 参数
scp -r /path/to/local/project_folder admin@172.19.24.169:~/myproject/

# Windows PowerShell 示例：
scp C:\Users\YourName\Code\myapp.py admin@<您的公网IP>:~/myproject/
```

示例

```
scp C:\Users\源恒\Desktop\test1.py admin@8.138.27.120:~/myproject/

scp C:\Users\源恒\Desktop\binance_ccxt.py admin@8.138.27.120:~/myproject/
```

> 问题
>

```
# 1. 先用 ssh 连接一次
ssh admin@8.138.27.120

# 出现提示时输入 yes
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

# 输入密码登录成功后，直接退出
exit
```

> 问题2
>
> 使用 SSH 密钥登录

```
# 查看本地ssh
ls C:\Users\源恒\.ssh\

# PowerShell 执行
Get-Content C:\Users\源恒\.ssh\id_rsa.pub

ssh-rsa 字符串
```

服务器配置

```
# 1. 切换到 admin 用户（如果当前是root）
su - admin

# 2. 创建 .ssh 目录
mkdir -p /home/admin/.ssh
chmod 700 /home/admin/.ssh

# 3. 编辑 authorized_keys 文件
nano /home/admin/.ssh/authorized_keys

# 5. 设置正确的权限
chmod 600 /home/admin/.ssh/authorized_keys
chown -R admin:admin /home/admin/.ssh

# 6. 验证配置
ls -la /home/admin/.ssh/
cat /home/admin/.ssh/authorized_keys
```

**测试连接**

```
# 方式 2：直接使用密钥
ssh -i C:\Users\源恒\.ssh\id_rsa admin@8.138.27.120
```

如果成功，会直接登录，不需要密码！

###### windows测试连接

```
# 1. 测试 SSH 连接
ssh -i C:\Users\源恒\.ssh\id_rsa admin@8.138.27.120

# 创建文件夹
mkdir -p ~/myproject

# 查看目录
ls -la

# 进入目录
cd ~/myproject
```

```
┌─────────────────────────────────────────────────────────────┐
│  PowerShell 窗口 1 (SSH 连接)    │  PowerShell 窗口 2 (上传)  │
├─────────────────────────────────────────────────────────────┤
│  admin@iZ7xveu1vcjrylj8ywp326Z:~$ │  PS C:\Users\源恒>        │
│  mkdir -p ~/myproject            │  scp -i ... test1.py ... │
│  cd ~/myproject                  │                          │
│  ls -l                           │                          │
│  python3 test1.py                │                          │
└─────────────────────────────────────────────────────────────┘
```

```
python3 test1.py
```

###### 创建虚拟环境

```
# 回到根目录
cd ~

# 更新软件包列表
sudo apt update

# 安装 python3-venv
sudo apt install python3.10-venv -y

# 现在请按 Tab 键选择 <Ok>，然后按 Enter 继续安装！

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 升级 pip
pip install --upgrade pip

# 配置清华镜像源（加速下载）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 进入项目目录
cd ~/myproject

# 查看项目文件
ls -l
```

###### python库安装

```
# 激活虚拟环境
source venv/bin/activate

pip install 需要安装的库
```

###### 测试python脚本

```
# 运行币安脚本
python3 binance_ccxt.py
```

###### Linux客户端运行vpn

```

```

