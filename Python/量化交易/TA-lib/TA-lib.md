# TA-Lib库

> TA-Lib 是一个 Python 金融指数处理库，基于 Cython 而不是 SWIG，提供丰富的技术分析指标，是量化交易的必备工具。
>

##### 安装
```python
# 安装 TA-Lib
pip install TA-Lib
```

#####  `TA-Lib` 库安装

###### 安装 C 底层库

> 确保系统具备编译 C 代码的环境

```
sudo apt update
sudo apt install build-essential wget -y
```

下载并解压

```
wget https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz
tar -xzf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4/
```

配置和编译

> 只有 1GB 内存，不要使用 make -j（多线程编译），直接用单线程 make 最稳妥。

```
./configure --prefix=/usr
make
sudo make install
```

###### 安装 Python 绑定库

```
pip install TA-Lib
```
