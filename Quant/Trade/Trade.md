# 交易技术指标

以按时间从早到晚排列的 K 线为输入。公式中的 $C_t$ 表示第 $t$ 根 K 线的收盘价，$N$ 表示 K 线条数。例如 5 分钟 K 线的 SMA(20) 使用最近 20 根 K 线。库的安装和数据准备见 [TA-Lib](../TA-lib/TA-lib.md)。

## 趋势与波动

### SMA 简单移动平均线

最近 $N$ 根 K 线收盘价的算术平均。窗口越大，曲线通常越平滑，对价格变化的反应也越慢。

$$
\operatorname{SMA}_t(N)=\frac{1}{N}\sum_{i=0}^{N-1}C_{t-i}
$$

### EMA 指数移动平均线

近期收盘价的权重更高，越早的数据权重衰减越多。周期为 12 时，最新收盘价的权重约为 15.4%。

$$
\alpha=\frac{2}{N+1},\qquad
\operatorname{EMA}_t(N)=\alpha C_t+(1-\alpha)\operatorname{EMA}_{t-1}(N)
$$

### MACD 指数平滑异同移动平均线

常用参数为 12、26、9。DIF 是短期与长期 EMA 的差，DEA 是 DIF 的 EMA，柱值是 DIF 减 DEA 的有符号差值。

$$
\begin{aligned}
\mathrm{DIF}_t &= \operatorname{EMA}_t(C,12)-\operatorname{EMA}_t(C,26) \\
\mathrm{DEA}_t &= \operatorname{EMA}_t(\mathrm{DIF},9) \\
\mathrm{Hist}_t &= \mathrm{DIF}_t-\mathrm{DEA}_t
\end{aligned}
$$

TA-Lib 按 DIF、DEA、柱值的顺序返回结果。和其他软件对照时，先核对柱值是否有额外倍率。

### BBANDS 布林带

常用设置以 20 周期 SMA 为中轨，上下轨由同一窗口内收盘价的标准差 $\sigma_t$ 决定。

$$
\mathrm{Upper}_t=\mathrm{SMA}_t(20)+2\sigma_t,\qquad
\mathrm{Lower}_t=\mathrm{SMA}_t(20)-2\sigma_t
$$

带宽扩大表示滚动窗口内价格离散程度上升，收窄表示离散程度下降。带宽本身不判断方向，布林带也没有固定的 95% 价格覆盖率。

## 动量

### RSI 相对强弱指数

RSI 衡量近期上涨幅度与下跌幅度的相对强弱，常用周期为 14。TA-Lib 使用 Wilder 平滑处理平均涨幅和平均跌幅。

$$
RS=\frac{\text{平均涨幅}}{\text{平均跌幅}},\qquad RSI=100-\frac{100}{1+RS}
$$

在平均涨跌幅均有定义的情况下，RSI 高于 50 表示平滑后的涨幅大于跌幅，低于 50 则相反。50 可以作为观察动量的中线，仍需结合价格走势判断趋势。

## Python 示例

下面用一组固定的模拟收盘价演示各指标的调用和返回顺序。使用真实数据时，传入按时间升序排列的数值数组。

```python
import numpy as np
import talib

close = 100 + np.linspace(0, 20, 100) + 3 * np.sin(np.arange(100) / 4)

sma20 = talib.SMA(close, timeperiod=20)
sma60 = talib.SMA(close, timeperiod=60)
ema12 = talib.EMA(close, timeperiod=12)
ema26 = talib.EMA(close, timeperiod=26)
dif, dea, hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
upper, middle, lower = talib.BBANDS(
    close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=talib.MA_Type.SMA
)
rsi14 = talib.RSI(close, timeperiod=14)

print(f"DIF={dif[-1]:.3f}, DEA={dea[-1]:.3f}, 柱值={hist[-1]:.3f}")
print(f"收盘={close[-1]:.2f}, 上轨={upper[-1]:.2f}, 下轨={lower[-1]:.2f}")
```

TA-Lib 的输出通常与输入等长，开头会有用于预热的 NaN。比较不同软件的结果时，先核对输入、周期、平滑方式和初始值。

## 参考

- [TA-Lib 指标列表](https://ta-lib.github.io/ta-lib-python/funcs.html)
- [TA-Lib Python 文档](https://github.com/TA-Lib/ta-lib-python)
