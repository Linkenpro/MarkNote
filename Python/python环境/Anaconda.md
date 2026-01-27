### Anaconda使用备忘笔记

在cmd命令行状态下

```shell
conda
```

查看conda现有的环境

```shell
conda env list
```

新建python虚拟环境（使用不同版本的python虚拟环境，某些库文件在某些版本才能使用/稳定性）

```shell
conda create -n tradevnpy python=3.7
# 格式 conda create -n 环境名 python=版本号
```

使用VPN会导致创建环境不成功

启动虚拟环境
```shell
conda activate vnpytrade
# 格式 conda activate 环境名
```

虚拟安装第三方库
```shell
# 在conda的虚拟环境下
# cd转到下载好的解压包目录下
# 使用命令
python.exe setup.py install
# 即可安装
```

更新anaconda软件的命令

- 不能挂梯子vpn

```shell
conda update conda
```

## Python安装第三方库

默认方式
```shell
pip install 库名
```

安装下载好的库
```shell
python setup.py install
python.exe setup.py install
```

## Jupyter

安装插件——Jupyter页面目录
```shell
conda install -c conda-forge jupyter_contrib_nbextensions
```
