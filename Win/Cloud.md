##### 趋势型指标

###### MA（SMA）

移动均线（Moving Average）或者简单移动平均线（Simple Moving Average）

**计算公式：**

> 算术平均
>
> N取值越大，曲线越平滑，但滞后性也越强。

$$
SMA = \frac{close_1 + close_2 + ... + close_n}{n}
$$



- close：收盘价
- n：天数、K线数

**Python实现**

```python
import talib
import numpy as np

# 假设 close_prices 是你从 SQLite 数据库读取的 BTC 收盘价数组
close_prices = np.random.random(100) 

# 计算 20 周期均线（常用于判断短期趋势）
sma_20 = talib.SMA(close_prices, timeperiod=20)

# 计算 60 周期均线（常用于判断中期趋势/牛熊分界）
sma_60 = talib.SMA(close_prices, timeperiod=60)
```

###### EMA

指数移动平均（Exponential Moving Average）

> 核心逻辑：权重（Weight）

给最近的价格分配了最大的权重，并随着时间推移，旧价格的权重呈指数级衰减。

**计算公式：**
$$
EMA_{today} = (Price_{today} - EMA_{yesterday}) \times \frac{2}{N+1} + EMA_{yesterday}
$$

- 平滑系数（Smoothing Factor）：
  $$
  \frac{2}{N+1}
  $$
  对于 $N=12$ 的均线，新价格的权重约占 15.4%。

**Python实现**

```py
import talib

# 假设 close 是你从数据库取出的 numpy 数组
# 计算 12 周期和 26 周期 EMA（这是 MACD 指标的核心基础）
ema_12 = talib.EMA(close, timeperiod=12)
ema_26 = talib.EMA(close, timeperiod=26)
```

###### MACD

指数平滑移动平均线（Moving Average Convergence / Divergence），**MACD**

差离值（DIF值）:
$$
DIF = EMA_{(close,12)} - EMA_{(close,26)}
$$
信号线（DEM值,又称MACD值):
$$
DEM = EMA_{(DIF,9)}
$$
柱形图或棒形图：
$$
OSC = DIF - DEM = DIF -MACD
$$
**Python实现**

```python
import talib
import numpy as np

# 假设 close 是从你的 crypto_data.db 读取的 BTC 收盘价 (numpy float64 数组)
# 参数：fastperiod=12, slowperiod=26, signalperiod=9
dif, dea, hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

# 获取最新的一组数据
print(f"DIF: {dif[-1]}, DEA: {dea[-1]}, Histogram: {hist[-1]}")
```

###### Bollinger Bands

布林带，布林带的结构（三条线）定义：

- 中轨（Middle Band）：

  > 通常是 **20 周期简单移动平均线（SMA 20）**。它代表了价格的中期趋势。

- 上轨（Upper Band）：

  > 中轨 + 2X标准差

- 下轨（Lower Band）：

  > 中轨 - 2X标准差

统计学意义： 根据正态分布理论，约 95% 的价格变动都会落在这个“信道”之内。

> 开口（Expansion）： 像喇叭一样打开，意味着能量释放，趋势开启。
>
> 收口（Contraction）： 轨道平行或收缩，意味着进入休整或盘整期。

**Python 实现**

```py
import talib

# 假设 close 是你从 crypto_data.db 取出的收盘价数组
# timeperiod=20, nbdevup=2, nbdevdn=2, matype=0 (SMA)
upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

# 获取最新的数值
current_upper = upper[-1]
current_lower = lower[-1]
current_price = close[-1]
```

##### 振荡型指标

###### RSI

RSI（Relative Strength Index，相对强弱指数），衡量价格涨跌动能的最常用指标之一

$$RSI = 100 - \frac{100}{1 + RS} \quad (RS = \frac{平均上涨幅度}{平均下跌幅度})$$

> **RSI > 50**：说明上涨动力强于下跌动力，市场处于多头趋势。
>
> **RSI < 50**：说明下跌动力更强，市场处于空头趋势。

**Python实现**

```python
import talib

# 假设 close 是你从 crypto_data.db 取出的收盘价数组
# timeperiod=14 是最常用的默认设置
rsi = talib.RSI(close, timeperiod=14)

# 获取最新的 RSI 数值
current_rsi = rsi[-1]
```





###### KDJ

##### 成交量型指标

###### OBV

###### VWAP

##### 波动率与形态指标

###### ATR



