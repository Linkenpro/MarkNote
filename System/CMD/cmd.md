# CMD 命令与批处理

适用于 Windows CMD 和 `.bat` 文件。示例中的路径按需替换；带空格的路径使用双引号。

## 基础操作

| 命令 | 用途 |
| --- | --- |
| `help`、`set /?` | 查看命令列表或指定命令的帮助 |
| `echo Hello World` | 输出文字 |
| `echo.` | 输出空行 |
| `@echo off` | 关闭批处理命令回显，`@` 隐藏本行命令 |
| `rem 注释内容` | 添加注释 |
| `pause` | 暂停，等待按键 |
| `pause >nul` | 暂停并隐藏提示文字 |
| `chcp 65001` | 将当前控制台代码页切换为 UTF-8 |

中文批处理可保存为 UTF-8，并配合 `chcp 65001` 使用；显示效果也受终端和程序编码影响。CMD 注释使用 `rem`，不是 `#`。

## 变量与运算

### 设置、读取与清除变量

```bat
@echo off
set "message=Hello World"
echo %message%
rem 清除变量
set "message="
```

`set` 显示环境变量；`set name` 显示名称以 `name` 开头的变量。读取指定变量的值使用 `echo %name%`。

### 整数运算

```bat
@echo off
set /a a=5, b=10
set /a c=a+b
echo %c%
set /a c=b-a
echo %c%
set /a c=b/a
echo %c%
set /a c=a*b
echo %c%
pause >nul
```

### 接受用户输入

```bat
@echo off
set "name="
set /p "name=请输入你的名字："
echo 您输入的名字是：%name%
pause >nul
```

## 文件与目录

### 查看、创建与复制

```cmd
rem 查看目录内容，并导出列表到当前目录
dir "C:\Program Files"
dir "C:\Program Files" > "lists.txt"

rem 创建目录
mkdir "D:\Example\New Folder"

rem 复制文件
copy "D:\Example\source.json" "D:\Example\copy.json"
```

`md` 与 `mkdir` 都可创建目录。`>` 将输出写入文件并覆盖原内容；`>>` 追加到文件末尾。

### 删除文件与目录

删除操作不进入回收站，执行前确认目标路径。

```cmd
rem 删除文件前逐项询问
del /p "D:\Example\Temp\*.txt"

rem 删除空目录
rmdir "D:\Example\Empty Folder"

rem 删除目录及其内容，执行时要求确认
rmdir /s "D:\Example\Temp"
```

`rmdir /s` 包含子目录和文件；加 `/q` 会取消确认提示。

## 批处理流程

### for 循环

| 场景 | 循环变量写法 |
| --- | --- |
| CMD 窗口直接输入 | `%i` |
| `.bat` 文件 | `%%i` |

命令行中递归查找 PNG 文件：

```cmd
for /r "D:\Example" %i in (*.png) do echo "%i"
```

批处理中的计数循环，参数依次为起点、步长、终点：

```bat
@echo off
for /l %%i in (1,1,5) do echo %%i
```

### goto 跳转

```bat
@echo off
goto done
echo 这一行会被跳过

:done
echo 完成
pause >nul
```

### call 调用脚本

```bat
@echo off
rem 调用当前脚本所在目录中的另一个脚本
call "%~dp0demo.bat"

rem 也可以使用完整路径
call "D:\Example\other.bat"
echo 调用完成
```

`%~dp0` 表示当前批处理文件所在的盘符和目录。被调用的批处理结束后，继续执行 `call` 后面的命令。

### exit 退出

`exit` 退出 CMD；批处理中使用 `exit /b` 返回调用者，或结束当前脚本而保留 CMD 窗口。

```bat
@echo off
echo Hello World
exit /b
```

## 程序与窗口

### start 与远程桌面

```cmd
rem 打开文件夹或文件
start "" "D:\Example"
start "" "D:\Example\notes.txt"

rem 启动程序时请求最大化或最小化窗口
start "" /max notepad.exe
start "" /min notepad.exe

rem 打开远程桌面连接
mstsc
```

`start` 的第一个带引号参数会被当作窗口标题，因此打开带引号的路径时，先写空标题 `""`。

### 自定义窗口

```cmd
title CMD Demo
mode con cols=80 lines=40
color 0E
```

`color` 的第一位指定背景色，第二位指定文字颜色；`0E` 为黑底亮黄色文字。完整颜色表用 `color /?` 查看。

## 网络与系统

### ping 与网络检查

```cmd
rem 查看本机网络配置和默认网关
ipconfig

rem 检查本机回环地址
ping 127.0.0.1

rem 检查网关，替换成实际地址
ping 192.168.1.1

rem 检查外部主机
ping www.baidu.com

rem 持续测试，按 Ctrl+C 停止
ping -t www.baidu.com

rem 查看本机名称
hostname
```

| ping 参数 | 用途 |
| --- | --- |
| `-n 4` | 发送 4 次回显请求 |
| `-l 32` | 设置发送数据大小 |
| `-w 1000` | 每次回复等待 1000 毫秒 |
| `-a` | 尝试将目标 IP 解析为主机名 |
| `-i 64` | 设置 TTL |

ping 超时不一定代表网络断开，目标或防火墙可能不响应 ICMP。

### telnet 测试 TCP 连接

需要先启用 Windows Telnet 客户端。以下示例测试指定主机的 TCP 端口：

```cmd
telnet 192.168.1.10 80
```

### 定时关机

以下命令会安排关机：

```cmd
shutdown /s /t 7200
```

表示两小时后关机。取消尚未执行的定时关机：

```cmd
shutdown /a
```

## 常用脚本

### 批量复制并按序号命名

源文件和目标目录需已存在；目标文件名为 `js1.json` 至 `js30.json`。

```bat
@echo off
chcp 65001 >nul
echo 正在复制文件……
for /l %%i in (1,1,30) do copy /-y "D:\Example\source.json" "D:\Example\js%%i.json"
pause
```

`/-y` 在覆盖已有文件前询问。

### 批量创建目录

在当前工作目录中创建名称为 `8` 至 `27` 的目录：

```bat
@echo off
for /l %%i in (8,1,27) do mkdir "%%i"
```

### 递归查找文件

```bat
@echo off
for /r "D:\Example" %%i in (*.txt) do echo "%%i"
pause >nul
```
