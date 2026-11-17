# Docker

Windows 使用 Docker Desktop；Debian 服务器使用 Docker Engine。包含 Python 项目打包与运行示例。

## Windows 环境准备

下载并安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)，系统要求以安装页面为准。

使用 WSL 2 后端时，在 `Settings → General` 中启用 `Use WSL 2 based engine`；部分安装环境默认启用，不显示此选项。需要从 WSL 发行版运行 Docker 时，再配置对应的 WSL Integration。

启动 Docker Desktop 后，在终端检查：

```powershell
docker version
docker compose version
```

`docker version` 应能显示客户端和服务端信息。资源与文件共享设置随后端而异，不必照搬固定的内存或共享盘配置。

## Python 项目结构

| 文件 | 用途 |
| --- | --- |
| `app.py` | 程序入口 |
| `requirements.txt` | Python 依赖 |
| `Dockerfile` | 镜像构建步骤 |
| `.dockerignore` | 排除构建上下文中的无关文件 |
| `docker-compose.yml` | 可选，用于声明服务配置 |

以下示例假设这些文件位于同一项目目录，程序提供端口为 `5000` 的 Web 服务。

## 编写 Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 先安装依赖，便于复用构建缓存
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

- `3.11-slim` 是示例版本，按项目兼容性选择；该标签不会锁定补丁版本或镜像内容。
- `EXPOSE` 声明容器使用的端口，实际访问还需要在运行时配置端口映射。
- Web 程序需监听容器内的 `0.0.0.0:5000`。普通脚本可去掉 `EXPOSE` 和下方运行命令的 `-p` 参数。

## 排除无关文件

在项目根目录创建 `.dockerignore`：

```text
__pycache__/
*.pyc
.git/
.env
venv/
.venv/
.idea/
.vscode/
*.log
```

它控制哪些文件进入构建上下文，不影响容器运行时的目录挂载。

## 构建与运行

在项目根目录执行：

```powershell
# 构建镜像，末尾的点表示当前目录为构建上下文
docker build -t my-python-app .

# 后台运行，端口仅绑定本机地址
docker run -d --name my-python-app -p 127.0.0.1:5000:5000 my-python-app
```

程序启动后，通过 `http://localhost:5000` 访问。镜像名与容器名可以相同；同名容器已存在时，需先移除旧容器或使用其他名称。

## 查看与停止容器

| 命令 | 用途 |
| --- | --- |
| `docker ps` | 查看正在运行的容器 |
| `docker ps -a` | 查看所有容器，包括已退出的容器 |
| `docker logs -f my-python-app` | 持续查看日志，按 Ctrl+C 结束查看 |
| `docker stop my-python-app` | 停止容器 |
| `docker start my-python-app` | 重新启动已有容器 |
| `docker rm my-python-app` | 删除已停止的容器，容器内未持久化的数据会丢失 |

修改代码后需要重新构建镜像，并用新镜像创建容器；`docker start` 不会更新已有容器的代码。

## Debian 服务器

由 [VPS 笔记](../VPS/VPS.md)归并。服务器按 [Docker 官方 Debian 安装说明](https://docs.docker.com/engine/install/debian/)配置软件源，再安装 Engine 与 Compose 插件；不要在未配置官方源时直接假定这些包可用。

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker
sudo docker version
sudo docker compose version
```

原笔记使用的便捷脚本保留为测试环境备选；官方不建议用于生产环境：

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
# 查看并确认脚本内容及安装目标后再执行
sudo sh get-docker.sh
```

### 停止与自启

先查看并按需停止业务容器，再停止服务；服务停止会影响容器管理及相关业务：

```bash
sudo docker ps
sudo docker stop my-python-app
sudo systemctl stop docker.service docker.socket
```

禁止开机自动启动：

```bash
sudo systemctl disable docker.service docker.socket
```

恢复时使用 `sudo systemctl enable --now docker.service docker.socket`。不使用按进程名批量 `pkill` 的方式关闭 Docker 或 containerd。

Docker 发布的容器端口可能绕过 UFW 的规则；需结合绑定地址及 Docker 防火墙机制核对对外暴露范围，不能只检查 `ufw status`。

## 参考

- [Docker Desktop WSL 2 后端](https://docs.docker.com/desktop/features/wsl/)
- [端口声明与映射](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)
- [构建上下文与 .dockerignore](https://docs.docker.com/build/concepts/context/)
