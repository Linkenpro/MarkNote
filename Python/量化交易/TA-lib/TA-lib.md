# TA-Lib库

> TA-Lib 是一个 Python 金融指数处理库，基于 Cython 而不是 SWIG，提供丰富的技术分析指标，是量化交易的必备工具。
>

##### 安装
```python
# 安装 TA-Lib
pip install TA-Lib
```

##### 函数 API (常用)
```python
import talib
import numpy as np

# 生成模拟数据
close = np.random.random(100)

# 计算简单移动平均线(SMA)
sma = talib.SMA(close, timeperiod=20)

# 计算布林带
upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2)

# 计算动量指标
mom = talib.MOM(close, timeperiod=5)
```

##### 抽象 API (更灵活)
```python
from talib.abstract import *

# 创建输入数据
inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}

# 计算移动平均线
sma = SMA(inputs, timeperiod=20)

# 计算布林带
upper, middle, lower = BBANDS(inputs, 20, 2, 2)

# 计算相对强度指数(RSI)
rsi = RSI(inputs, timeperiod=14)

# 计算MACD
macd, macd_signal, macd_hist = MACD(inputs, fastperiod=12, slowperiod=26, signalperiod=9)
```

## 量化交易常用指标

### 1. 重叠研究 (Overlap Studies)
**均线指标** - 量化交易最基础的指标
- `SMA` (简单移动平均线): `talib.SMA(close, timeperiod=20)`
- `EMA` (指数移动平均线): `talib.EMA(close, timeperiod=20)`
- `WMA` (加权移动平均线): `talib.WMA(close, timeperiod=20)`
- `BBANDS` (布林带): `talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2)`

**使用场景**：趋势判断、支撑/阻力位识别

### 2. 动量指标 (Momentum Indicators)
**核心指标** - 量化交易最常用的动量指标
- `RSI` (相对强弱指标): `talib.RSI(close, timeperiod=14)`
  - 0-30: 超卖, 70-100: 超买
- `MACD` (指数平滑异同移动平均线): `talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)`
  - MACD线与信号线交叉是主要交易信号
- `STOCH` (随机指标): `talib.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowd_period=3)`
  - 20以下超卖, 80以上超买

**使用场景**：趋势强度判断、超买超卖识别

### 3. 波动性指标 (Volatility Indicators)
**关键指标** - 量化交易风险管理的核心
- `ATR` (平均真实波幅): `talib.ATR(high, low, close, timeperiod=14)`
  - 衡量市场波动性，用于设置止损、仓位大小
- `TRANGE` (真实波幅): `talib.TRANGE(high, low, close)`

**使用场景**：止损设置、仓位管理、波动率交易

### 4. 形态识别 (Pattern Recognition)
**实用指标** - 识别K线形态，辅助交易决策
- `CDLHAMMER` (锤子线): `talib.CDLHAMMER(open, high, low, close)`
- `CDLDOJI` (十字星): `talib.CDLDOJI(open, high, low, close)`
- `CDLENGULFING` (吞没形态): `talib.CDLENGULFING(open, high, low, close)`
- `CDL3WHITESOLDIERS` (三白兵): `talib.CDL3WHITESOLDIERS(open, high, low, close)`

**使用场景**：K线形态识别，预判市场反转

## 量化交易常用指标组合策略

### 策略1: 均线交叉策略
```python
# 计算短期和长期均线
short_ma = talib.SMA(close, timeperiod=50)
long_ma = talib.SMA(close, timeperiod=200)

# 金叉买入，死叉卖出
buy_signal = (short_ma > long_ma) & (short_ma.shift(1) <= long_ma.shift(1))
sell_signal = (short_ma < long_ma) & (short_ma.shift(1) >= long_ma.shift(1))
```

### 策略2: RSI超买超卖策略
```python
# 计算RSI
rsi = talib.RSI(close, timeperiod=14)

# 超买卖出，超卖买入
buy_signal = (rsi < 30) & (rsi.shift(1) >= 30)
sell_signal = (rsi > 70) & (rsi.shift(1) <= 70)
```

### 策略3: MACD + RSI组合策略
```python
# 计算MACD
macd_line, signal_line, _ = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

# 计算RSI
rsi = talib.RSI(close, timeperiod=14)

# MACD金叉且RSI超卖买入
buy_signal = (macd_line > signal_line) & (rsi < 30)

# MACD死叉且RSI超买卖出
sell_signal = (macd_line < signal_line) & (rsi > 70)
```

## 重要提示

1. **数据长度**：TA-Lib 需要至少 `timeperiod` 长度的数据才能计算指标
2. **数据格式**：输入必须是 numpy 数组，且长度一致
3. **参数调整**：不同品种、不同时间周期需要调整指标参数
4. **回测验证**：所有指标策略必须经过严格回测验证

## 常用指标参数参考

| 指标    | 常用周期    | 说明                                    |
| ------- | ----------- | --------------------------------------- |
| SMA/EMA | 20, 50, 200 | 短期/中期/长期趋势                      |
| RSI     | 14          | 标准周期，超买超卖参考                  |
| MACD    | 12,26,9     | 标准周期，12日快线，26日慢线，9日信号线 |
| ATR     | 14          | 波动率参考，常用止损设置                |

TA-Lib 是量化交易的基石工具，熟练掌握这些常用指标的使用，能极大提升策略开发效率和质量。建议结合回测框架（如Backtrader、Zipline）进行策略开发和验证。
