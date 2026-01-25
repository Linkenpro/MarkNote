```python
# 导入方式
import os
```

##### 路径操作

| 功能               | 语法                      | 说明                                        |
| :----------------- | :------------------------ | :------------------------------------------ |
| 拼接路径           | `os.path.join(dir, file)` | 跨平台安全拼接（自动处理 `/` 或 `\`）       |
| 获取绝对路径       | `os.path.abspath(path)`   | 返回绝对路径                                |
| 规范化路径         | `os.path.normpath(path)`  | 清理 `.`、`..`、多余分隔符                  |
| 分离目录和文件名   | `os.path.split(path)`     | 返回 `(dir, basename)` 元组                 |
| 获取文件名         | `os.path.basename(path)`  | 如 `os.path.basename('/a/b.txt') → 'b.txt'` |
| 获取目录名         | `os.path.dirname(path)`   | 如 `os.path.dirname('/a/b.txt') → '/a'`     |
| 分离文件名和扩展名 | `os.path.splitext(path)`  | 如 `('file', '.txt')`                       |

```python
path = os.path.join("data", "input.txt")  # data/input.txt（Linux）或 data\input.txt（Windows）
full_path = os.path.abspath("test.py")
name, ext = os.path.splitext("report.pdf")  # name='report', ext='.pdf'
```

##### 文件与目录操作

| 操作                            | 语法                                   | 说明                                              |
| ------------------------------- | -------------------------------------- | ------------------------------------------------- |
| 判断路径是否存在                | `os.path.exists(path)`                 | 文件或目录存在返回 `True`                         |
| 判断是否为文件                  | `os.path.isfile(path)`                 | 是文件返回 `True`                                 |
| 判断是否为目录                  | `os.path.isdir(path)`                  | 是目录返回 `True`                                 |
| 创建单层目录                    | `os.mkdir(path)`                       | 父目录不存在会报错                                |
| 创建多层目录                    | `os.makedirs(path, exist_ok=True)`     | 类似 `mkdir -p`，`exist_ok=True` 避免已存在时报错 |
| 删除文件                        | `os.remove(path)` 或 `os.unlink(path)` | 删除单个文件                                      |
| 删除空目录                      | `os.rmdir(path)`                       | 目录非空会报错                                    |
| 删除非空目录（需配合 `shutil`） | `shutil.rmtree(path)`                  | `os` 本身不支持递归删除                           |
| 重命名/移动                     | `os.rename(src, dst)`                  | 可跨目录（相当于移动）                            |
| 获取文件大小                    | `os.path.getsize(path)`                | 返回字节数                                        |

```python
if not os.path.exists("logs"):
    os.makedirs("logs", exist_ok=True)

if os.path.isfile("config.ini"):
    print("文件大小:", os.path.getsize("config.ini"), "字节")
```

##### 工作目录操作

| 操作             | 语法             |
| ---------------- | ---------------- |
| 获取当前工作目录 | `os.getcwd()`    |
| 切换工作目录     | `os.chdir(path)` |

```python
print("当前目录:", os.getcwd())
os.chdir("/home/user/project")
```

##### 环境变量

| 操作             | 语法                                                    |
| ---------------- | ------------------------------------------------------- |
| 获取环境变量     | `os.getenv("VAR_NAME")` 或 `os.environ.get("VAR_NAME")` |
| 设置环境变量     | `os.environ["VAR_NAME"] = "value"`                      |
| 获取所有环境变量 | `os.environ`（类似字典）                                |

```python
home = os.getenv("HOME")  # Linux/macOS
python_path = os.environ.get("PYTHONPATH", "未设置")
os.environ["MY_APP_MODE"] = "production"
```

##### 其他实用功能

| 功能                       | 语法                                 |
| -------------------------- | ------------------------------------ |
| 获取文件状态（如修改时间） | `os.stat(path)`                      |
| 获取换行符                 | `os.linesep`（如 `\n` 或 `\r\n`）    |
| 获取路径分隔符             | `os.sep`（Linux: `/`, Windows: `\`） |
| 获取系统名称               | `os.name`（如 `'posix'`, `'nt'`）    |
| 退出程序                   | `os.exit(code)`                      |