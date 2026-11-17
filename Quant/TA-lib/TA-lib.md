# TA-Lib

TA-Lib 用于计算金融时间序列的技术指标。Python 包名为 `TA-Lib`，导入名为 `talib`，底层计算由 TA-Lib C 库完成。

## 安装与验证

在项目的 Python 虚拟环境中运行：

```shell
python -m pip install TA-Lib
python -c "import talib; print(talib.__version__)"
```

Python 包从 0.6.5 起为受支持的平台提供自带 C 库的 wheel。pip 能找到与当前 Python 版本、系统和架构匹配的 wheel 时，直接安装即可。若只想检查能否使用 wheel，可运行 `python -m pip install --only-binary=:all: TA-Lib`。

## Debian VPS 源码安装备忘

仅在找不到合适的 wheel、需要从源码构建 Python 绑定时使用。下面保留原笔记中 C 库 0.6.4 的构建流程。该示例对应 Python 绑定 0.6.x 和 NumPy 2。其他版本先查官方兼容表，再选对应的 C 库版本。

```bash
sudo apt update
sudo apt install build-essential wget python3-dev

wget https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz
tar -xzf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4
./configure --prefix=/usr
make
sudo make install
```

原 VPS 只有 1 GB 内存，编译时使用单任务 `make`。这里的 `python3-dev` 对应 Debian 自带的 Python，其他 Python 版本需要匹配的开发头文件。

在项目虚拟环境中构建绑定并检查：

```bash
python -m pip install --no-binary=TA-Lib "TA-Lib>=0.6,<0.7"
python -c "import talib; print(talib.__version__)"
```

若 C 库装在自定义目录，构建时用 `TA_INCLUDE_PATH` 和 `TA_LIBRARY_PATH` 指定头文件和库文件的位置。

## 常用指标

| 函数 | 输入 | 输出 |
| --- | --- | --- |
| `SMA` / `EMA` | 收盘价 | 简单 / 指数移动均线 |
| `RSI` | 收盘价 | 相对强弱指标 |
| `MACD` | 收盘价 | MACD 线、信号线、柱值 |
| `BBANDS` | 收盘价 | 上轨、中轨、下轨 |
| `ATR` | 最高价、最低价、收盘价 | 平均真实波幅 |

`timeperiod` 按数据条数计算。例如使用 5 分钟 K 线时，`SMA(timeperiod=20)` 使用 20 根 K 线。

## K 线计算示例

`candles.csv` 包含 `timestamp`、`high`、`low`、`close` 四列。时间戳使用 ISO 8601 字符串。如果数据来自 CCXT，Unix 毫秒时间戳应改用 `pd.to_datetime(df["timestamp"], unit="ms", utc=True)`。示例需另装 `pandas`。

```python
import numpy as np
import pandas as pd
import talib

df = pd.read_csv("candles.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
df = df.sort_values("timestamp")

high = df["high"].to_numpy(dtype="float64", na_value=np.nan)
low = df["low"].to_numpy(dtype="float64", na_value=np.nan)
close = df["close"].to_numpy(dtype="float64", na_value=np.nan)
if not all(np.isfinite(values).all() for values in (high, low, close)):
    raise ValueError("请先处理 K 线价格中的缺失值或无穷值")

df["sma_20"] = talib.SMA(close, timeperiod=20)
df["rsi_14"] = talib.RSI(close, timeperiod=14)
df["atr_14"] = talib.ATR(high, low, close, timeperiod=14)
df["macd"], df["macd_signal"], df["macd_hist"] = talib.MACD(
    close, fastperiod=12, slowperiod=26, signalperiod=9
)

print(df.tail())
```

指标开头通常会有一段 `NaN`，因为可用历史不足。回测时从所需指标均有效的行开始，不把预热值填成 0。计算前检查时间戳是否重复，以及 K 线是否缺段。若策略在收盘后产生信号，回测需按信号实际可用的时点模拟成交。

## 参考

- [Python 包安装、版本兼容和 NaN 说明](https://github.com/TA-Lib/ta-lib-python)
- [官方指标列表](https://ta-lib.github.io/ta-lib-python/funcs.html)
- [TA-Lib C 库安装](https://ta-lib.org/install/)
