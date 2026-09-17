##### Windows 环境准备

下载地址：https://www.docker.com/products/docker-desktop/

- Windows 10/11
- 启用 WSL2（推荐） 或 Hyper-V

> 安装后重启，确保右下角托盘出现 Docker鲸鱼图标

| 设置项                       | 建议值                   | 说明                       |
| ---------------------------- | ------------------------ | -------------------------- |
| **General → Use WSL 2**      | 勾选                     | 性能更好，兼容性更强       |
| **Resources → Memory**       | ≥ 4GB                    | Python 项目建议 4~8GB      |
| **Resources → File Sharing** | 添加项目所在盘（如 C:\） | 允许容器挂载本地目录       |
| **Experimental Features**    | 可开启（可选）           | 如 `Use Docker Compose V2` |

##### Python项目 Docker化核心步骤

###### 项目结构示例

```
my-python-app/
├── app.py                 # 主程序
├── requirements.txt       # 依赖列表
├── Dockerfile             # 镜像构建文件
├── docker-compose.yml     # （可选）多服务编排
└── .dockerignore          # 忽略文件（类似 .gitignore）
```

###### 编写Dockerfile

```dockerfile
# 使用官方 Python 镜像（指定版本！）
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件（利用 Docker 层缓存）
COPY requirements.txt .

# 安装依赖（--no-cache-dir 减小镜像体积）
RUN pip install --no-cache-dir -r requirements.txt

# 复制源代码
COPY . .

# 暴露端口（如 Flask 默认 5000）
EXPOSE 5000

# 启动命令（开发时可覆盖）
CMD ["python", "app.py"]
```

> 固定 Python 版本（避免 latest）
> 先复制 requirements.txt 再安装，加速缓存复用
> 使用 slim 镜像减小体积

###### .dockerignore

> 避免无用文件进镜像

```
__pycache__/
*.pyc
.git
.env
venv/
.idea/
.vscode/
*.log
```

