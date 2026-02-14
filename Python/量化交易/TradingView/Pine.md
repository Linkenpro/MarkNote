# 内置变量

###### ask

> 当前tick的ask价，代表活跃卖家以当前价值接受该商品的最低价格
>

此信息仅在“1T”时间周期内可用

在其他时间周期内，变量的值为`na`

- 类型:`series float`


> 如果bid/ask值自最后一tick发生变化，但没有进行新的交易，则这些变化将不会反映在此变量的值中。它仅在新的tick上更新。
>

###### bar_index

> 目前的价格棒指数
>
> 编号从零开始，第一个条的索引为`0`

类型：`series int`

```js
//@version=6
indicator("bar_index")
plot(bar_index)
plot(bar_index > 5000 ? close : 0)
```

> - **bar_index**已替换版本4中的**n**变量。
> - K线索引从第一根历史K线起算为0。
>
> - 使用此变量/函数可能会导致指标重新绘制。
>

###### barstate.isconfirmed

如果脚本正在计算当前k线的最后(关闭)更新，则返回`true`。 

下一个脚本将在新K线数据上计算

类型:`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算
>

不建议在`request.security()`表达式中使用`barstate.isconfirmed`。 从`request.security()`请求的它的值是不可预测的。

###### barstate.isfirst

如果当前k线为k线组的第一条k线，则返回`true`，否则返回`false`

类型：`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算
>
> 使用此变量/函数可能会导致指标重新绘制

###### barstate.ishistory

如果当前k线为历史k线，则返回`true`，否则返回`false`

类型:`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算
>

###### barstate.islast

如果当前k线为k线组的最后一条k线，则返回`true`，否则返回`false`

类型:`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算

###### barstate.islastconfirmedhistory

如果市场收盘时脚本在数据集的最后一根K线上执行，或者脚本正在实时K线之前的K线上执行，

如果市场开盘，则返回`true`。否则返回`false`

类型:`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算
>

###### barstate.isnew

如果脚本目前在新k线上计算着，则返回`true`，否则返回`false`。

类型:`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算
>

###### barstate.isrealtime

如果当前k线为实时k线，则返回`true`，否则返回`false`。

类型:`series bool`

> 使用此变量的Pine Script®代码可以对历史数据和实时数据进行不同的计算。
>

###### bid

当前tick的bid价，代表活跃买家愿意以当前价值为该商品支付的最高价格。

> 此信息仅在“1T”时间周期内可用。在其他时间周期内，变量的值为`na`

类型:`series float`

> 如果bid/ask值自最后一tick发生变化，但没有进行新的交易，则这些变化将不会反映在此变量的值中。
>
> 它仅在新的tick上更新

###### box.all

返回一个数组，其中填充了脚本绘制的所有当前box。

类型：`array<box>`



```js
//@version=6
indicator("box.all")
//delete all boxes
box.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time, border_style=line.style_dashed)
a_allBoxes = box.all
if array.size(a_allBoxes) > 0
    for i = 0 to array.size(a_allBoxes) - 1
        box.delete(array.get(a_allBoxes, i))
```

> 该阵列是只读的。阵列的索引零是图表上最旧对象的ID。
>

###### chart.bg_color

从“图表设置/外观/背景”字段返回图表背景的颜色。选择渐变时，返回渐变的中点。

类型:`input color`

###### chart.fg_color

返回与`chart.bg_color]`提供最佳对比度的颜色。

类型:`input color`

###### chart.is_heikinashi

类型:`simple bool`

> 返回值
>
> 如果图表类型是平均K线图，则返回`true]`，否则返回`false`
>

###### chart.is_kagi

类型:`simple bool`

返回值

如果图表类型是卡吉图，则返回`true`，否则返回`false`

###### chart.is_linebreak

类型:`simple bool`

> 返回值
>
> 如果图表类型是新价线，则返回`true`，否则返回`false`
>

###### chart.is_pnf

类型:`simple bool`

返回值

> 如果图表类型是点数图，则返回`true`，否则返回`false`。
>

###### chart.is_range

类型:`simple bool`

返回值

> 如果图表类型是Range图，则返回`true`，否则返回`false`
>

###### chart.is_renko

类型:`simple bool`

> 返回值
>
> 如果图表类型是砖形图，则返回`true`，否则返回`false`
>

###### chart.is_standard

类型:`simple bool`

返回值

如果图表类型不是以下之一，则返回`true`：砖形图、卡吉图、新价线、点数图、范围图、平均K线图；否则，返回`false`

###### chart.left_visible_bar_time

图表上当前可见的最左侧K线的`time`

类型:`input int`

> 当其值更新以反映图表中的变化时，使用此变量的脚本将自动重新执行，这可能是由用户滚动图表或新的实时K线引起的。
>
> 在包含此变量的脚本上创建的警报，将仅使用警报创建时分配给该变量的值，无论该值随后是否发生变化，这可能会导致重新绘制。
>

###### chart.right_visible_bar_time

图表上当前可见的最右侧K线的`time`

类型`input int`

> 当其值更新以反映图表中的变化时，使用此变量的脚本将自动重新执行，这可能是由用户滚动图表或新的实时K线引起的。
>
> 在包含此变量的脚本上创建的警报，将仅使用警报创建时分配给该变量的值，无论该值随后是否发生变化，这可能会导致重新绘制。
>

###### close

当前K线关闭时的收盘价，或尚未完成的实时K线的最后交易价格

类型:`series float`

可使用方括号运算符 []来访问以前的值

###### dayofmonth

根据K线的开盘UNIX时间戳计算得出的交易所时区月份天数

类型:`series int`

> 该变量始终引用与K线开盘时间相对应的一天。因此，对于具有隔夜时段的商品（例如“ Eurusd”，“星期一”会议从周日的17:00开始，以交易所时间开始），该价值可能是从上一周起的一天，而不是时段的主要交易日。
>

###### dayofweek

根据K线的开盘UNIX时间戳计算得出的交易所时区的周天数

类型:`series int`

该变量始终引用与K线开盘时间相对应的一天。

因此，对于具有隔夜时段的商品（例如“ Eurusd”，“星期一”会议从周日的17:00开始，以交易所时间开始），该价值可能是从上一周起的一天，而不是时段的主要交易日。

###### dividends.future_amount

以当前工具的货币返回即将到来的股息的支付金额，如果此数据不可用，则返回`na`

类型:`series float`

> 该值在脚本初始计算期间仅获取一次。该变量将返回相同的值，直到重新计算脚本为止，即使在下一次股息的预期支付日期之后也是如此
>

###### dividends.future_ex_date

返回当前工具下次股息支付的除息日期(Ex-date)，如果此数据不可用，则返回`na`。除息日表示投资者不再有权从最近的股息中获得派息。

只有在这一天之前购买股票的人才有资格获得股息。

类型:`series int`

返回值

UNIX时间，以毫秒表示

> 该值在脚本初始计算期间仅获取一次。该变量将返回相同的值，直到重新计算脚本为止，即使在下一次股息的预期支付日期之后也是如此
>

###### dividends.future_pay_date

返回当前工具下次股息支付的支付日期（支付日），如果此数据不可用，则返回`na`。支付日是指合格投资者收到股息的日期。

类型:`series int`

返回值

UNIX时间，以毫秒表示。

> 该值在脚本初始计算期间仅获取一次。该变量将返回相同的值，直到重新计算脚本为止，即使在下一次股息的预期支付日期之后也是如此。
>

###### earnings.future_eps

返回以商品货币表示的下一份收益报告的估计每股收益，如果此数据不可用，则返回`na`

类型:`series float`

> 该值在脚本初始计算期间仅获取一次。该变量将返回相同的值，直到重新计算脚本为止，即使在下一次收益报告的预期时间之后也是如此
>

###### earnings.future_period_end_time

检查下一份收益报告的数据，并返回这些收益所涵盖的财务期间结束当天的UNIX时间戳，如果此数据不可用，则返回`na`

类型:`series int`

返回值

UNIX时间，以毫秒表示。

> 该值在脚本初始计算期间仅获取一次。该变量将返回相同的值，直到重新计算脚本为止，即使在下一次收益报告的预期时间之后也是如此。
>

###### earnings.future_revenue

返回以商品货币表示的下一份收益报告的预计收入，如果此数据不可用，则返回`na`。

类型:`series float`

> 该值在脚本初始计算期间仅获取一次。该变量将返回相同的值，直到重新计算脚本为止，即使在下一次收益报告的预期时间之后也是如此
>

###### earnings.future_time

返回UNIX时间戳，指示下一次收益报告的预期时间；如果此数据不可用，则返回`na`

类型:`series int`

返回值

UNIX时间，以毫秒表示。

> 该值在脚本初始计算期间仅获取一次
>
> 该变量将返回相同的值，直到重新计算脚本为止，即使在下一次收益报告的预期时间之后也是如此

###### high

当前最高价

类型:`series float`

> 可使用方括号运算符 []来访问以前的值，例如。 高[1]，高[2]。
>

###### hl2

是(最高价 + 最低价)/2的快捷键

类型:`series float`

###### hlc3

是(最高价+最低价+收盘价)/3的快捷键

类型:`series float`

###### hlcc4

是(高+低+收+收)/4的快捷键

类型:`series float`

###### hour

交易所时区的当前小时k线。

类型:`series int`

###### label.all

返回一个阵列，其中填充了脚本绘制的所有当前标签。

类型:`array<label>`



```js
//@version=6
indicator("label.all")
//delete all labels
label.new(bar_index, close)
a_allLabels = label.all
if array.size(a_allLabels) > 0
    for i = 0 to array.size(a_allLabels) - 1
        label.delete(array.get(a_allLabels, i))
```

> 该阵列是只读的。阵列的索引零是图表上最旧对象的ID
>

###### last_bar_index

最后一根图表K线的索引

K线索引以第一根K线为零开始

类型:`series int`



```js
//@version=6
strategy("Mark Last X Bars For Backtesting", overlay = true, calc_on_every_tick = true)
lastBarsFilterInput = input.int(100, "Bars Count:")

var lastbar = last_bar_index

allowedToTrade = (lastbar - bar_index <= lastBarsFilterInput) or barstate.isrealtime
bgcolor(allowedToTrade ? color.new(color.green, 80) : na)
```

返回值

收盘的最后历史K线索引，或开盘的实时K线索引。

> 请注意，使用此变量可能会导致[指标重绘]
>

###### last_bar_time

最后一根图表K线的UNIX格式的时间。

它是自1970年1月1日00:00:00 UTC以来经过的毫秒数。

类型:`series int`

> 使用此变量/函数可能会导致[指标重新绘制]
>
> 此变量根据K线的开盘时间返回时间戳。

###### line.all

返回一个数组，其中填充了脚本绘制的所有当前线条。

类型:`array<line>`

```js
//@version=6
indicator("line.all")
//delete all lines
line.new(bar_index - 10, close, bar_index, close)
a_allLines = line.all
if array.size(a_allLines) > 0
    for i = 0 to array.size(a_allLines) - 1
        line.delete(array.get(a_allLines, i))
```

> 该阵列是只读的阵列的索引零是图表上最旧对象的ID
>

###### linefill.all

返回一个由脚本绘制的所有当前linefill对象填充的阵列

类型:`array<linefill>`

> 该阵列是只读的。阵列的索引零是图表上最旧对象的ID。
>

###### low

当前最低价

类型:`series float`

可使用方括号运算符 []来访问以前的值，例如。 低[1]，低[2]。

###### minute

交易所时区的当前分钟k线。

类型:`series int`

###### month

交易所时区的当前月k线。

类型:`series int`

> 此变量根据K线的打开时间返回月份。
>
> 对于隔夜交易时段（例如EURUSD，其周一交易时段从周日17:00开始），该值可以比交易日的月份低1。

###### na

表示“不可用”的关键字，表示变量没有赋值。

类型:`simple na`

```js
//@version=6
indicator("na")

plot(bar_index < 10 ? na : close)

float a = na
if bar_index >= 10
    a := close
plot(a)

plot(na(close[1` ? close : close[1`

plot(nz(close[1], close))
```

> 请勿将此变量与[比较运算符]一起使用来测试`na`的值，因为这可能会导致意外行为。
>
> 相反，请使用`na()`函数。请注意，当初始化语句还指定变量的类型时，可以使用`na`来初始化变量。

###### ohlc4

是(开盘价 + 最高价 + 最低价 + 收盘价)/4的快捷键

类型:`series float`

###### open

当前开盘价

类型:`series float`

> 可使用方括号运算符 []来访问以前的值，例如。 开[1]，开[2]。
>

###### polyline.all

返回一个数组，其中包含脚本绘制的所有当前[polyline]实例。

类型:`array<polyline>`

> 该数组是只读的
>
> 数组的索引零引用图表上最旧的折线对象的ID

###### second

交易所时区的当前秒k线。

类型:`series int`

###### session.isfirstbar

如果当前K线是当天交易时段的第一根K线，则返回`true`，否则返回`false`。

如果使用延长交易时段信息，则仅在盘前K线的第一根K线上返回`true`。

类型:`series bool`

```js
//@version=6
strategy("`session.isfirstbar` Example", overlay = true)
longCondition = year >= 2022

if session.isfirstbar and longCondition
    strategy.entry("Long", strategy.long)

if session.islastbar and barstate.isconfirmed
    strategy.close("Long", immediately = true)
```

###### session.isfirstbar_regular

在当天的第一根常规交易时段K线返回`true`，否则返回`false`。

无论是否使用延长交易时段信息，结果都是相同的。

类型:`series bool`

```js
//@version=6
strategy("`session.isfirstbar_regular` Example", overlay = true)
longCondition = year >= 2022
// Place a long order at the `close` of the trading session's first bar.
if session.isfirstbar and longCondition
    strategy.entry("Long", strategy.long)
// Close the long position at the `close` of the trading session's last bar.
if session.islastbar_regular and barstate.isconfirmed
    strategy.close("Long", immediately = true)
```

###### session.islastbar

如果当前K线是当天交易时段的最后一根K线，则返回`true`，否则返回`false`。

 如果使用延长交易时段信息，则仅在盘后K线的最后一根K线上返回`true`。

类型:`series bool`

```js
//@version=6
strategy("`session.islastbar` Example", overlay = true)
longCondition = year >= 2022

if session.islastbar and longCondition
    strategy.entry("Long", strategy.long)

if session.islastbar and barstate.isconfirmed
    strategy.close("Long", immediately = true)
```

> 此变量不能保证在每个时段中返回一次`true`，因为如果在时段的最后一根K线期间没有发生任何交易，则时段的最后一根K线可能不存在。
>

此变量不能保证在非标准图表类型上按预期工作，例如Renko图。

###### session.islastbar_regular

在当天的最后一根常规交易时段K线返回`true`，否则返回`false`。无论是否使用延长交易时段信息，结果都是相同的。

类型:`series bool`

```js
//@version=6
strategy("`session.islastbar_regular` Example", overlay = true)
longCondition = year >= 2022

if session.isfirstbar and longCondition
    strategy.entry("Long", strategy.long)

if session.islastbar_regular and barstate.isconfirmed
    strategy.close("Long", immediately = true)
```

> 此变量不能保证在每个时段中返回一次`true`，因为如果在时段的最后一根K线期间没有发生任何交易，则时段的最后一根K线可能不存在。
>

此变量不能保证在非标准图表类型上按预期工作，例如Renko图。

###### session.ismarket

如果当前K线是常规交易时段（即市场时段）的一部分，则返回`true`，否则返回`false`。

类型:`series bool`

###### session.ispostmarket

如果当前K线是盘后市场的一部分，则返回`true`，否则返回`false`。

在非日内图表上始终返回`false`。

类型:`series bool`

###### session.ispremarket

如果当前K线是盘前市场的一部分，则返回`true`，否则返回`false`。在非日内图表上始终返回`false`。

类型:`series bool`

#### strategy

###### strategy.account_currency

返回用于计算结果的货币，可以在策略的属性中设置。

类型:`simple string`

###### strategy.avg_losing_trade

返回每笔亏损交易的平均损失金额。

计算方式为亏损总和除以亏损交易数量。

类型:`series float`

###### strategy.avg_losing_trade_percent

返回每笔亏损交易的平均亏损百分比。计算方法为亏损百分比总和除以亏损交易数量。

类型:`series float`

###### strategy.avg_trade

返回每笔交易的平均盈利或亏损金额。计算方式为所有利润和损失的总和除以已平仓交易的数量。

类型:`series float`

###### strategy.avg_trade_percent

返回每笔交易的平均收益或损失百分比。计算方式为所有盈亏百分比之和除以已平仓交易数量。

类型:`series float`

###### strategy.avg_winning_trade

返回每笔获利交易获得的平均金额。计算方式为利润总和除以获利交易数量。

类型:`series float`

###### strategy.avg_winning_trade_percent

返回每笔获利交易的平均收益百分比。计算方式为利润百分比总和除以获利交易数量。

类型:`series float`

###### strategy.closedtrades

整个交易区间内平仓交易数量。

类型:`series int`

###### strategy.closedtrades.first_index

交易列表中列出的第一笔（最早）交易的索引或交易编号。此数字通常为零。

如果已关闭的交易数量超过允许的限制，则最旧的交易将被删除，此数字是剩余最早交易的索引。

类型:`series int`

###### strategy.equity

当前权益`strategy.initial_capital` + `strategy.netprofit` + `strategy.openprofit`

类型:`series float`

###### strategy.eventrades

整个交易区间的盈亏平衡交易数量。

类型:`series int`

###### strategy.grossloss

所有已完成亏损交易的总货币价值。

类型:`series float`

###### strategy.grossloss_percent

所有已完成的亏损交易的总价值，以初始资本的百分比表示。

类型:`series float`

###### strategy.grossprofit

所有已完成赢利交易的总货币价值。

类型:`series float`

###### strategy.grossprofit_percent

所有已完成的盈利交易的总货币价值，以初始资本的百分比表示。

类型:`series float`

###### strategy.initial_capital

策略属性中设定的初始资本金额。

类型:`series float`

###### strategy.losstrades

整个交易范围内无盈利交易次数。

类型:`series int`

###### strategy.margin_liquidation_price

当策略中使用保证金时，返回将发生模拟追加保证金通知的价格点，并清算足够的仓位以满足保证金要求。

类型:`series float`

```js
//@version=6
strategy("Margin call management", overlay = true, margin_long = 25, margin_short = 25,
  default_qty_type = strategy.percent_of_equity, default_qty_value = 395)

float maFast = ta.sma(close, 14)
float maSlow = ta.sma(close, 28)

if ta.crossover(maFast, maSlow)
    strategy.entry("Long", strategy.long)

if ta.crossunder(maFast, maSlow)
    strategy.entry("Short", strategy.short)

changePercent(v1, v2) =>
    float result = (v1 - v2) * 100 / math.abs(v2)

if math.abs(changePercent(close, strategy.margin_liquidation_price)) <= 10
    strategy.close("Long")
    strategy.close("Short")
```

> 如果策略不使用边距，即`strategy()`声明语句未指定`margin_long`或`margin_short`参数的参数，则变量返回`na`。
>

###### strategy.max_contracts_held_all

整个交易范围内一次交易的最大合约/股票/手/单位数量

类型:`series float`

###### strategy.max_contracts_held_long

整个交易范围内一次多头交易的最大合约/股票/手/单位数量。

类型:`series float`

###### strategy.max_contracts_held_short

整个交易范围内一次短头交易的最大合约/股票/手/单位数量。

类型:`series float`

###### strategy.max_drawdown

整个交易范围内的最大股权回撤值

类型:`series float`

###### strategy.max_drawdown_percent

整个交易区间的最大股权回撤值，以百分比表示，计算公式为：`Lowest Value During Trade / (Entry Price x Quantity) * 100`。

类型:`series float`

###### strategy.max_runup

整个交易区间的最大股权上涨值

类型:`series float`

###### strategy.max_runup_percent

整个交易区间的最大股权上涨值，以百分比表示，计算公式为：`Highest Value During Trade / (Entry Price x Quantity) * 100`。

类型:`series float`

###### strategy.netprofit

所有已完成交易的总货币价值。

类型:`series float`

###### strategy.netprofit_percent

所有已完成交易的总价值，以初始资本的百分比表示。

类型:`series float`

###### strategy.openprofit

所有未平仓位的当前未实现损益。

类型:`series float`

###### strategy.openprofit_percent

所有未平仓位的当前未实现利润或损失，以百分比表示，并按公式计算：`openPL / realizedEquity * 100`。

类型:`series float`

###### strategy.opentrades

未关闭或者继续持有的交易数量。如果没有，则显示0.

类型:`series int`

###### strategy.opentrades.capital_held

返回未平仓交易当前持有的资本金额。

类型:`series float`

```js
//@version=6
strategy(
   "strategy.opentrades.capital_held example", overlay=false, margin_long=50, margin_short=50,
   default_qty_type = strategy.percent_of_equity, default_qty_value = 100
 )

if barstate.isfirst
    strategy.entry("Short", strategy.short)

plot(strategy.opentrades.capital_held, "Capital held")
bgcolor(bar_index > 0 and strategy.opentrades.capital_held == 0 ? color.new(color.red, 60) : na)
```

> 如果策略未使用假设账户的一部分模拟资金交易，即如果[strategy()] 函数不包含非零`margin_long`或`margin_short`参数，则此变量返回`na`。
>

###### strategy.position_avg_price

当前市场定位平均入场价。 如果市场地位平滑，则“NaN”就会退回。

类型:`series float`

###### strategy.position_entry_name

最初开立当前市场仓位的订单名称。

类型:`series string`

###### strategy.position_size

目前市场仓位的方向和规模。 如果值> 0，则市场仓位较长。 

如果值<0，则市场仓位较短。 绝对值是交易中的合同/股/手/单位数(仓位大小)。

类型:`series float`

###### strategy.wintrades

整个交易范围内盈利交易数量

类型:`series int`

#### syminfo

###### syminfo.basecurrency

如果商品是外汇或加密货币对或基于此类货币对的衍生品，则返回包含代表商品基础货币（即交易货币或代币）的代码字符串。 否则，它返回一个空字符串。

> 例如，此变量对“EURJPY”返回“EUR”，对“BTCUSDT”返回“BTC”，对“CME:6C1!”返回“CAD”，对“NASDAQ:AAPL”返回“”。

类型:`simple string`

###### syminfo.country

返回商品所在国家/地区的两个字母代码，格式为[ISO 3166-1 alpha-2]；如果交易所未直接关联到特定国家/地区，则返回`na`。

> 例如，在“NASDAQ:AAPL”上它将返回“US”，在“LSE:AAPL”上它将返回“GB”，在“BITSTAMP:BTCUSD”上它将返回`na`。

类型:`simple string`

###### syminfo.currency

返回一个字符串，其中包含代表商品价格的货币代码。

> 例如，此变量对“NASDAQ:AAPL”返回“USD”，对“EURJPY”返回“JPY”。

类型:`simple string`

###### syminfo.current_contract

如果当前代码为连续期货合约，则为标的合约的股票代码标识符；否则为`na`。

类型:`simple string`

###### syminfo.description

当前商品的描述。

类型:`simple string`

###### syminfo.employees

公司现有员工人数。

类型:`simple int`

```js
//@version=6
indicator("syminfo simple")

var result_table = table.new(position = position.top_right, columns = 2, rows = 5, border_width = 1)
if barstate.islastconfirmedhistory

    table.cell(table_id = result_table, column = 0, row = 0, text = "name")
    table.cell(table_id = result_table, column = 1, row = 0, text = "value")

    table.cell(table_id = result_table, column = 0, row = 1, text = "employees")
    table.cell(table_id = result_table, column = 1, row = 1, text = str.tostring(syminfo.employees))

    table.cell(table_id = result_table, column = 0, row = 2, text = "shareholders")
    table.cell(table_id = result_table, column = 1, row = 2, text = str.tostring(syminfo.shareholders))

    table.cell(table_id = result_table, column = 0, row = 3, text = "shares_outstanding_float")
    table.cell(table_id = result_table, column = 1, row = 3, text = str.tostring(syminfo.shares_outstanding_float))

    table.cell(table_id = result_table, column = 0, row = 4, text = "shares_outstanding_total")
    table.cell(table_id = result_table, column = 1, row = 4, text = str.tostring(syminfo.shares_outstanding_total))
```

###### syminfo.expiration_date

表示当前期货合约最后一天开始时间的UNIX时间戳。

该变量仅与非连续期货品种兼容。对于其它商品，它返回`na`。

类型:`simple int`

###### syminfo.industry

返回商品的行业，如果商品没有行业，则返回`na`。

例如：“互联网软件/服务”、“软件组装”、“综合石油”、“机动车辆”等。这些与图表的“商品信息”窗口中可以看到的值相同。

类型:`simple string`

> 板块是经济数据中的泛指。行业是一个较窄的分类。
>
> 以NASDAQ:CAT（Caterpillar, Inc.）为例，属于“生产者制造”板块和“卡车/建筑/农用机械”行业

###### syminfo.isin

此字段包含一个字符串，表示某个证券代码关联的国际证券识别码 (ISIN)；如果该代码没有ISIN信息，则此字段为空字符串。ISIN是一个12位字母数字代码，用于在全球范围内唯一标识证券。与可能因交易所而异的股票代码不同，证券的ISIN在所有交易所都是一致的。因此，程序员可以使用ISIN来识别基础金融工具，而无需考虑交易所或交易所列出的代码名称。

> 例如，NASDAQ:AAPL和GETTEX:APC的ISIN为US0378331005，因为这两个代码都指Apple Inc.的普通股。相比之下，TSX:AAPL的ISIN为CA03785Y1007，因为该代码指的是不同的金融工具：Apple Inc.加拿大存托凭证 (CDR)。
>

类型:`simple string`

###### syminfo.main_tickerid

表示当前图表商品的股票代码标识符。该值包含交易所前缀和商品名称，以冒号分隔（例如“NASDAQ:AAPL”）。它还可以包含有关数据修改的信息，

> 例如股息调整、非标准图表类型、货币转换等。与`syminfo.tickerid`不同，此变量的值在`request.*()`函数调用的`expression`参数中使用时不会改变。

类型:`simple string`

###### syminfo.mincontract

当前商品可交易的最小数量。此限制由交易所设置。对于加密货币，它通常小于1个代币。对于大多数其他类型的资产，它通常为1。

类型:`simple float`

###### syminfo.minmove

返回一个整数，用于计算商品价格变动之间的最小增量`syminfo.mintick`。它是`syminfo.mintick`公式中的分子：`syminfo.minmove / syminfo.pricescale = syminfo.mintick`。

类型:`simple int`

###### syminfo.mintick

当前品种的最小刻度值。

类型:`simple float`

###### syminfo.pointvalue

证券的图表价格乘以点值等于交易证券的实际价格。

对于除期货以外的所有类型的证券，点值通常等于1，因此可以忽略不计。对于期货，图表上显示的价格要么是单张期货合约的成本，在这种情况下点值为1；要么是标的商品的单个单位价格，在这种情况下点值代表单张合约中包含的单位数量。

> “COMEX:GC1!”黄金期货图表的价格反映的是一金衡盎司黄金的价格。然而，根据COMEX交易所的定义，一份GC期货合约包含100金衡盎司。因此，当“GC1!”图表上的价格为2000美元时，一份合约的成本为2000美元*100金衡盎司=200,000美元。这一计算在回测中非常重要，因为策略引擎会考虑点值，如果资金不足，就不会开仓。
>

点值也会显示在给定资产的“商品信息”窗口。

类型:`simple float`

###### syminfo.prefix

当前商品名称的简码(即'CME_EOD:TICKER'简码为'CME_EOD')。

类型:`simple string`

```js
//@version=6
indicator("syminfo.prefix")

if barstate.islastconfirmedhistory
    label.new(bar_index, high, text=syminfo.prefix)
```

###### syminfo.pricescale

返回一个整数，用于计算商品价格变动之间的最小增量`syminfo.mintick`。它是`syminfo.mintick`公式中的分母：`syminfo.minmove / syminfo.pricescale = syminfo.mintick`。

类型:`simple int`

###### syminfo.recommendations_buy

给予当前商品“买入”评级的分析师数量。

类型:`series int`

```js
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.recommendations_buy_strong

给予当前商品“强力买入”评级的分析师数量。

类型:`series int`

```js
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.recommendations_date

当前商品最后一组建议的开始日期。

类型:`series int`

```js
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.recommendations_hold

给予当前商品“持有”评级的分析师数量。

类型:`series int`

```js
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.recommendations_sell

给予当前商品“卖出”评级的分析师数量。

类型:`series int`

```
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.recommendations_sell_strong

给予当前商品“强力卖出”评级的分析师数量。

类型:`series int`

```js
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.recommendations_total

当前商品的推荐总数。

类型:`series int`

```js
//@version=6
indicator("syminfo recommendations", overlay = true)
//@variable A table containing information about analyst recommendations.
var table ratings = table.new(position.top_right, 8, 2, frame_color = #000000)
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    // Add header cells.
    table.cell(ratings, 0, 0, "Start Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 0, "End Date", bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 0, "Buy", bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 0, "Strong Buy", bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 0, "Sell", bgcolor = color.maroon, text_color = #000000, text_size = size.large)
    table.cell(ratings, 5, 0, "Strong Sell", bgcolor = color.red, text_color = #000000, text_size = size.large)
    table.cell(ratings, 6, 0, "Hold", bgcolor = color.orange, text_color = #000000, text_size = size.large)
    table.cell(ratings, 7, 0, "Total", bgcolor = color.silver, text_color = #000000, text_size = size.large)
    // Recommendation strings
    string startDate         = str.format_time(syminfo.recommendations_date, "yyyy-MM-dd")
    string endDate           = str.format_time(YTD, "yyyy-MM-dd")
    string buyRatings        = str.tostring(syminfo.recommendations_buy)
    string strongBuyRatings  = str.tostring(syminfo.recommendations_buy_strong)
    string sellRatings       = str.tostring(syminfo.recommendations_sell)
    string strongSellRatings = str.tostring(syminfo.recommendations_sell_strong)
    string holdRatings       = str.tostring(syminfo.recommendations_hold)
    string totalRatings      = str.tostring(syminfo.recommendations_total)
    // Add value cells
    table.cell(ratings, 0, 1, startDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 1, 1, endDate, bgcolor = color.gray, text_color = #000000, text_size = size.large)
    table.cell(ratings, 2, 1, buyRatings, bgcolor = color.teal, text_color = #000000, text_size = size.large)
    table.cell(ratings, 3, 1, strongBuyRatings, bgcolor = color.lime, text_color = #000000, text_size = size.large)
    table.cell(ratings, 4, 1, sellRatings, bgcolor = color.maroon, text_color = #000000, text_size = size.large)
```

###### syminfo.root

期货合约等衍生品的根源。对于其他品种，返回与`syminfo.ticker`相同的值。

类型:`simple string`

```js
//@version=6
indicator("syminfo.root")

if barstate.islastconfirmedhistory
    label.new(bar_index, high, syminfo.root)
```

###### syminfo.sector

返回商品的板块，如果商品没有板块，则返回`na`。

例如：“电子技术”、“技术服务”、“能源矿物”、“耐用消费品”等。这些值与图表的“商品信息”窗口中看到的值相同

类型:`simple string`

> 板块是经济数据中的泛指。行业是一个较窄的分类。以NASDAQ:CAT（Caterpillar, Inc.）为例，属于“生产者制造”板块和“卡车/建筑/农用机械”行业。
>

###### syminfo.session

图表主要系列的时段类型。 可能值为`session.regular`，`session.extended`

类型:`simple string`

###### syminfo.shareholders

公司现有股东人数。

类型:`simple int`

```js
//@version=6
indicator("syminfo simple")
//@variable A table containing information about a company's employees, shareholders, and shares.
var result_table = table.new(position = position.top_right, columns = 2, rows = 5, border_width = 1)
if barstate.islastconfirmedhistory
    // Add header cells
    table.cell(table_id = result_table, column = 0, row = 0, text = "name")
    table.cell(table_id = result_table, column = 1, row = 0, text = "value")
    // Add employee info cells.
    table.cell(table_id = result_table, column = 0, row = 1, text = "employees")
    table.cell(table_id = result_table, column = 1, row = 1, text = str.tostring(syminfo.employees))
    // Add shareholder cells.
    table.cell(table_id = result_table, column = 0, row = 2, text = "shareholders")
    table.cell(table_id = result_table, column = 1, row = 2, text = str.tostring(syminfo.shareholders))
    // Add float shares outstanding cells.
    table.cell(table_id = result_table, column = 0, row = 3, text = "shares_outstanding_float")
    table.cell(table_id = result_table, column = 1, row = 3, text = str.tostring(syminfo.shares_outstanding_float))
    // Add total shares outstanding cells.
    table.cell(table_id = result_table, column = 0, row = 4, text = "shares_outstanding_total")
    table.cell(table_id = result_table, column = 1, row = 4, text = str.tostring(syminfo.shares_outstanding_total))
```

###### syminfo.shares_outstanding_float

公司现有已发行股票总数，不包括任何限制性股票。

类型:`simple float`

```js
//@version=6
indicator("syminfo simple")
//@variable A table containing information about a company's employees, shareholders, and shares.
var result_table = table.new(position = position.top_right, columns = 2, rows = 5, border_width = 1)
if barstate.islastconfirmedhistory
    // Add header cells
    table.cell(table_id = result_table, column = 0, row = 0, text = "name")
    table.cell(table_id = result_table, column = 1, row = 0, text = "value")
    // Add employee info cells.
    table.cell(table_id = result_table, column = 0, row = 1, text = "employees")
    table.cell(table_id = result_table, column = 1, row = 1, text = str.tostring(syminfo.employees))
    // Add shareholder cells.
    table.cell(table_id = result_table, column = 0, row = 2, text = "shareholders")
    table.cell(table_id = result_table, column = 1, row = 2, text = str.tostring(syminfo.shareholders))
    // Add float shares outstanding cells.
    table.cell(table_id = result_table, column = 0, row = 3, text = "shares_outstanding_float")
    table.cell(table_id = result_table, column = 1, row = 3, text = str.tostring(syminfo.shares_outstanding_float))
    // Add total shares outstanding cells.
    table.cell(table_id = result_table, column = 0, row = 4, text = "shares_outstanding_total")
    table.cell(table_id = result_table, column = 1, row = 4, text = str.tostring(syminfo.shares_outstanding_total))
```

###### syminfo.shares_outstanding_total

公司现有流通股总数，包括内部人士、大股东和员工持有的限制性股票。

类型:`simple int`

```js
//@version=6
indicator("syminfo simple")
//@variable A table containing information about a company's employees, shareholders, and shares.
var result_table = table.new(position = position.top_right, columns = 2, rows = 5, border_width = 1)
if barstate.islastconfirmedhistory
    // Add header cells
    table.cell(table_id = result_table, column = 0, row = 0, text = "name")
    table.cell(table_id = result_table, column = 1, row = 0, text = "value")
    // Add employee info cells.
    table.cell(table_id = result_table, column = 0, row = 1, text = "employees")
    table.cell(table_id = result_table, column = 1, row = 1, text = str.tostring(syminfo.employees))
    // Add shareholder cells.
    table.cell(table_id = result_table, column = 0, row = 2, text = "shareholders")
    table.cell(table_id = result_table, column = 1, row = 2, text = str.tostring(syminfo.shareholders))
    // Add float shares outstanding cells.
    table.cell(table_id = result_table, column = 0, row = 3, text = "shares_outstanding_float")
    table.cell(table_id = result_table, column = 1, row = 3, text = str.tostring(syminfo.shares_outstanding_float))
    // Add total shares outstanding cells.
    table.cell(table_id = result_table, column = 0, row = 4, text = "shares_outstanding_total")
    table.cell(table_id = result_table, column = 1, row = 4, text = str.tostring(syminfo.shares_outstanding_total))
```

###### syminfo.target_price_average

分析师预测的该商品最新年度价格目标的平均值

类型:`series float`

```js
//@version=6
indicator("syminfo target_price")
if barstate.islastconfirmedhistory

    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000

    highLine = line.new(time, close, YTD, syminfo.target_price_high, color = color.green, xloc = xloc.bar_time)

    lowLine = line.new(time, close, YTD, syminfo.target_price_low, color = color.red, xloc = xloc.bar_time)

    medianLine = line.new(time, close, YTD, syminfo.target_price_median, color = color.gray, xloc = xloc.bar_time)

    averageLine = line.new(time, close, YTD, syminfo.target_price_average, color = color.orange, xloc = xloc.bar_time)

    linefill.new(lowLine, medianLine, color.new(color.red, 90))
    linefill.new(medianLine, highLine, color.new(color.green, 90))

    string estimatesText = str.format("Number of estimates: {0}", syminfo.target_price_estimates)
    label.new(bar_index, close, estimatesText, textcolor = color.white, size = size.large)
```

> 如果分析师在市场收盘时提供目标，则该变量可以返回`na`，直到市场开盘。
>

###### syminfo.target_price_date

当前商品的最新价格目标预测的开始日期。

类型:`series int`

```js
//@version=6
indicator("syminfo target_price")
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    //@variable A line connecting the current `close` to the highest yearly price estimate.
    highLine = line.new(time, close, YTD, syminfo.target_price_high, color = color.green, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the lowest yearly price estimate.
    lowLine = line.new(time, close, YTD, syminfo.target_price_low, color = color.red, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the median yearly price estimate.
    medianLine = line.new(time, close, YTD, syminfo.target_price_median, color = color.gray, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the average yearly price estimate.
    averageLine = line.new(time, close, YTD, syminfo.target_price_average, color = color.orange, xloc = xloc.bar_time)
    // Fill the space between targets
    linefill.new(lowLine, medianLine, color.new(color.red, 90))
    linefill.new(medianLine, highLine, color.new(color.green, 90))
    // Create a label displaying the total number of analyst estimates.
    string estimatesText = str.format("Number of estimates: {0}", syminfo.target_price_estimates)
    label.new(bar_index, close, estimatesText, textcolor = color.white, size = size.large)
```

> 如果分析师在市场收盘时提供目标，则该变量可以返回`na`，直到市场开盘。
>

###### syminfo.target_price_estimates

当前商品的最新价格目标预测总数。

类型:`series float`

```js
//@version=6
indicator("syminfo target_price")
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    //@variable A line connecting the current `close` to the highest yearly price estimate.
    highLine = line.new(time, close, YTD, syminfo.target_price_high, color = color.green, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the lowest yearly price estimate.
    lowLine = line.new(time, close, YTD, syminfo.target_price_low, color = color.red, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the median yearly price estimate.
    medianLine = line.new(time, close, YTD, syminfo.target_price_median, color = color.gray, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the average yearly price estimate.
    averageLine = line.new(time, close, YTD, syminfo.target_price_average, color = color.orange, xloc = xloc.bar_time)
    // Fill the space between targets
    linefill.new(lowLine, medianLine, color.new(color.red, 90))
    linefill.new(medianLine, highLine, color.new(color.green, 90))
    // Create a label displaying the total number of analyst estimates.
    string estimatesText = str.format("Number of estimates: {0}", syminfo.target_price_estimates)
    label.new(bar_index, close, estimatesText, textcolor = color.white, size = size.large)
```

如果分析师在市场收盘时提供目标，则该变量可以返回`na`，直到市场开盘。

###### syminfo.target_price_high

分析师预测的该商品最新的最高年度价格目标。

类型:`series float`

```js
//@version=6
indicator("syminfo target_price")
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    //@variable A line connecting the current `close` to the highest yearly price estimate.
    highLine = line.new(time, close, YTD, syminfo.target_price_high, color = color.green, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the lowest yearly price estimate.
    lowLine = line.new(time, close, YTD, syminfo.target_price_low, color = color.red, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the median yearly price estimate.
    medianLine = line.new(time, close, YTD, syminfo.target_price_median, color = color.gray, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the average yearly price estimate.
    averageLine = line.new(time, close, YTD, syminfo.target_price_average, color = color.orange, xloc = xloc.bar_time)
    // Fill the space between targets
    linefill.new(lowLine, medianLine, color.new(color.red, 90))
    linefill.new(medianLine, highLine, color.new(color.green, 90))
    // Create a label displaying the total number of analyst estimates.
    string estimatesText = str.format("Number of estimates: {0}", syminfo.target_price_estimates)
    label.new(bar_index, close, estimatesText, textcolor = color.white, size = size.large)
```

如果分析师在市场收盘时提供目标，则该变量可以返回`na`，直到市场开盘

###### syminfo.target_price_low

分析师预测的该商品最新的最低年度价格目标。

类型:`series float`

```js
//@version=6
indicator("syminfo target_price")
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    //@variable A line connecting the current `close` to the highest yearly price estimate.
    highLine = line.new(time, close, YTD, syminfo.target_price_high, color = color.green, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the lowest yearly price estimate.
    lowLine = line.new(time, close, YTD, syminfo.target_price_low, color = color.red, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the median yearly price estimate.
    medianLine = line.new(time, close, YTD, syminfo.target_price_median, color = color.gray, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the average yearly price estimate.
    averageLine = line.new(time, close, YTD, syminfo.target_price_average, color = color.orange, xloc = xloc.bar_time)
    // Fill the space between targets
    linefill.new(lowLine, medianLine, color.new(color.red, 90))
    linefill.new(medianLine, highLine, color.new(color.green, 90))
    // Create a label displaying the total number of analyst estimates.
    string estimatesText = str.format("Number of estimates: {0}", syminfo.target_price_estimates)
    label.new(bar_index, close, estimatesText, textcolor = color.white, size = size.large)
```

> 如果分析师在市场收盘时提供目标，则该变量可以返回`na`，直到市场开盘。
>

###### syminfo.target_price_median

分析师预测的该商品去年价格目标的中位数。

类型:`series float`

```
//@version=6
indicator("syminfo target_price")
if barstate.islastconfirmedhistory
    //@variable The time value one year from the date of the last analyst recommendations.
    int YTD = syminfo.target_price_date + timeframe.in_seconds("12M") * 1000
    //@variable A line connecting the current `close` to the highest yearly price estimate.
    highLine = line.new(time, close, YTD, syminfo.target_price_high, color = color.green, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the lowest yearly price estimate.
    lowLine = line.new(time, close, YTD, syminfo.target_price_low, color = color.red, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the median yearly price estimate.
    medianLine = line.new(time, close, YTD, syminfo.target_price_median, color = color.gray, xloc = xloc.bar_time)
    //@variable A line connecting the current `close` to the average yearly price estimate.
    averageLine = line.new(time, close, YTD, syminfo.target_price_average, color = color.orange, xloc = xloc.bar_time)
    // Fill the space between targets
    linefill.new(lowLine, medianLine, color.new(color.red, 90))
    linefill.new(medianLine, highLine, color.new(color.green, 90))
    // Create a label displaying the total number of analyst estimates.
    string estimatesText = str.format("Number of estimates: {0}", syminfo.target_price_estimates)
    label.new(bar_index, close, estimatesText, textcolor = color.white, size = size.large)
```

> 如果分析师在市场收盘时提供目标，则该变量可以返回`na`，直到市场开盘。
>

###### syminfo.ticker

无交易所前缀的商品代码，例如 'MSFT'。

类型:`simple string`

###### syminfo.tickerid

表示图表商品或请求商品的股票代码标识符，具体取决于脚本如何使用它。当在`request.*()`函数调用的`expression`参数中使用时，变量的值表示请求数据集的股票代码ID。否则，它表示图表的股票代码ID。该值包含交易所前缀和商品名称，以冒号分隔（例如“NASDAQ:AAPL”）。它还可以包含有关数据修改的信息，例如股息调整、非标准图表类型、货币转换等。

类型:`simple string`

> 因为这个变量的值并不总是使用简单的“prefix:ticker”格式，所以它不适合用于布尔比较或字符串操作函数。在这些情况下，通过 [ticker.standard()] 运行变量的结果来净化它。这将删除任何无关信息并返回使用“prefix:ticker”结构统一格式化的代码ID。
>

要始终访问脚本的主股票代码ID，即使在另一种情况下，请使用[syminfo.main_tickerid]变量。

###### syminfo.timezone

图表主要系列的交换时区。 可能的值见`timestamp()`

类型:`simple string`

###### syminfo.type

商品所属的市场类型。

> 为"stock"、"fund"、"dr"、"right"、"bond"、"warrant"、"structured"、"index"、"forex"、"futures"、"spread"、"economic"、"fundamental"、"crypto"、"spot"、"swap"、"option"、"commodity"。

类型:`simple string`

###### syminfo.volumetype

当前商品的交易量类型。

可能的值有：“base”表示基础货币，“quote”表示报价货币，“tick”表示交易数量，“n/a”表示没有交易量或其类型未指定。

类型:`simple string`

> 只有一些数据馈送供应商提供信息合格成交量。因此，该变量将仅在某些商品上返回一个值，主要是在加密领域。
>

#### ta

###### ta.accdist

累积/分布指数

类型:`series float`

###### ta.iii

盘中强度指数。

类型:`series float`

```js
//@version=6
indicator("Intraday Intensity Index")
plot(ta.iii, color=color.yellow)

f_iii() =>
    (2 * close - high - low) / ((high - low) * volume)

plot(f_iii())
```

###### ta.nvi

负量指标。

类型:`series float`

```js
//@version=6
indicator("Negative Volume Index")

plot(ta.nvi, color=color.yellow)

f_nvi() =>
    float ta_nvi = 1.0
    float prevNvi = (nz(ta_nvi[1], 0.0) == 0.0) ? 1.0 : ta_nvi[1]
    if nz(close, 0.0) == 0.0 or nz(close[1], 0.0) == 0.0
        ta_nvi := prevNvi
    else
        ta_nvi := (volume < nz(volume[1], 0.0)) ? prevNvi + ((close - close[1` / close[1` * prevNvi : prevNvi
    result = ta_nvi

plot(f_nvi())
```

###### ta.obv

能量潮指标

类型:`series float`

```js
//@version=6
indicator("On Balance Volume")
plot(ta.obv, color=color.yellow)

f_obv() =>
    ta.cum(math.sign(ta.change(close)) * volume)

plot(f_obv())
```

###### ta.pvi

正量指标

类型:`series float`

```
//@version=6
indicator("Positive Volume Index")

plot(ta.pvi, color=color.yellow)

// the same on pine
f_pvi() =>
    float ta_pvi = 1.0
    float prevPvi = (nz(ta_pvi[1], 0.0) == 0.0) ? 1.0 : ta_pvi[1]
    if nz(close, 0.0) == 0.0 or nz(close[1], 0.0) == 0.0
        ta_pvi := prevPvi
    else
        ta_pvi := (volume > nz(volume[1], 0.0)) ? prevPvi + ((close - close[1` / close[1` * prevPvi : prevPvi
    result = ta_pvi

plot(f_pvi())
```

###### ta.pvt

价量趋势指标

类型:`series float`

```js
//@version=6
indicator("Price-Volume Trend")
plot(ta.pvt, color=color.yellow)

// the same on pine
f_pvt() =>
    ta.cum((ta.change(close) / close[1` * volume)

plot(f_pvt())
```

###### ta.tr

真实范围，相当于`ta.tr(handle_na = false)`。

其计算方式为`math.max(high - low, math.abs(high - close[1`, math.abs(low - close[1`)`。

类型:`series float`

###### ta.vwap

成交量加权平均价格。

> 它使用[hlc3]作为它的源系列

类型:`series float`

###### ta.wad

威廉多空力度线。

类型:`series float`

```js
//@version=6
indicator("Williams Accumulation/Distribution")
plot(ta.wad, color=color.yellow)

// the same on pine
f_wad() =>
    trueHigh = math.max(high, close[1`
    trueLow = math.min(low, close[1`
    mom = ta.change(close)
    gain = (mom > 0) ? close - trueLow : (mom < 0) ? close - trueHigh : 0
    ta.cum(gain)

plot(f_wad())
```

###### ta.wvad

威廉变异离散量

类型:`series float`

```js
//@version=6
indicator("Williams Variable Accumulation/Distribution")
plot(ta.wvad, color=color.yellow)

// the same on pine
f_wvad() =>
    (close - open) / (high - low) * volume

plot(f_wvad())
```

###### table.all

返回一个阵列，其中填充了脚本绘制的所有当前表格

类型:`array<table>`

```js
//@version=6
indicator("table.all")
//delete all tables
table.new(position = position.top_right, columns = 2, rows = 1, bgcolor = color.yellow, border_width = 1)
a_allTables = table.all
if array.size(a_allTables) > 0
    for i = 0 to array.size(a_allTables) - 1
        table.delete(array.get(a_allTables, i))
```

> 该阵列是只读的
>
> 阵列的索引零是图表上最旧对象的ID。

###### time

UNIX格式的当前k线时间。 这是自1970年1月1日00:00:00 UTC以来的毫秒数

类型:`series int`

> 请注意，此变量返回基于K线开盘时间的时间戳。因此，对于隔夜交易时段（例如EURUSD，周一交易时段于周日17:00开始），此变量可以返回交易日指定日期之前的时间。例如，对于EURUSD，`dayofmonth(time)`可以比交易日的日期低1，因为当天的K线实际上在前一天开盘。
>

###### time_close

当前K线的收盘时间，以UNIX格式表示。它表示自1970年1月1日00:00:00 UTC以来经过的毫秒数。

在tick图标和基于价格的图表，例如砖形图、新价线、卡吉图、点数图和范围图上，此变量的序列保存最新实时K线的`na`时间戳（因为未来的收盘时间不可预测），但所有之前的K线的时间戳均有效。

类型:`series int`

###### time_tradingday

表示当前K线所属交易日00:00 UTC的时间戳，采用UNIX格式（自1970年1 月1日00:00:00 UTC以来经过的毫秒数）。

类型:`series int`

```js
//@version=6
indicator("Friday session")

//@variable The day of week, based on the current `time_tradingday` value. 
//          Uses "UTC+0" to return the daily session's timestamp at 00:00 UTC. 
int tradingDayOfWeek = dayofweek(time_tradingday, "UTC+0")

//@variable Returns `true` if the `dayofweek` represents Friday, in exchange time.
//          It might never return `true` on overnight symbols, depending on the timeframe, since the Friday session
//          starts on Thursday.
bool isFriday = dayofweek == dayofweek.friday
//@variable Returns `true` if the `tradingDayOfWeek` is Friday. 
//          Differs from `isFriday` on symbols with overnight sessions and for timeframes > "1D" on others.
bool isFridaySession = tradingDayOfWeek == dayofweek.friday

// Create a horizontal line at the `dayofweek.friday` value.
hline(dayofweek.friday, "Friday value", color.gray, hline.style_dashed, 2)
// Plot the `dayofweek` and `tradingDayOfWeek` for comparison.
plot(dayofweek, "Day of week", color.blue, 2)
plot(tradingDayOfWeek, "Trading day", color.teal, 3)
// Highlight the background when `isFriday` and `isFridaySession` occur.
bgcolor(isFriday ? color.new(color.blue, 90) : na, title = "isFriday highlight")
bgcolor(isFridaySession ? color.new(color.teal, 80) : na, title = "isFridaySession highlight")
```

此变量在处理隔夜交易时段非常有用，因为当日交易时段可以从前一个日历日开始。

> 例如，对于“FXCM:EURUSD”商品，周一交易时段从周日交易时段17:00开始。与 `time`返回周一日线上周日17:00 的时间戳不同，`time_tradingday`返回周一00:00 UTC的时间戳。当用于高于“1D”的时间周期时，`time_tradingday`返回该日线内最后一个交易日的时间戳（例如，在“1W”时间周期内，它返回当周内最后一个交易日的时间戳）

[time_close]

###### timeframe.isdaily

如果当前分辨率是每日分辨率，则返回`true`，否则返回`false`

类型:`simple bool`

###### timeframe.isdwm

如果当前分辨率是每日或每周或每月分辨率，则返回`true`，否则返回`false`

类型:`simple bool`

###### timeframe.isintraday

如果当前周期是日内（分钟或秒）周期，则返回`true`，否则返回`false`

类型:`simple bool`

###### timeframe.isminutes

如果当前周期是分钟周期，则返回`true`，否则返回`false`。

类型:`simple bool`

###### timeframe.ismonthly

如果当前分辨率是每月分辨率，则返回`true`，否则返回`false`

类型:`simple bool`

###### timeframe.isseconds

如果当前周期是秒，则返回true，否则返回false。

类型:`simple bool`

###### timeframe.isticks

如果当前时间周期是tick周期，则返回true，否则返回false。

类型:`simple bool`

###### timeframe.isweekly

如果当前分辨率是每周分辨率，则返回`true`，否则返回`false`。

类型:`simple bool`

###### timeframe.main_period

脚本主时间周期的字符串表示。如果脚本是[indicator()]，并在其声明语句中指定了`timeframe`值，则此变量将保存该值。否则，其值表示图表的时间范围。与[timeframe.period]不同，此变量的值在`request.*()`函数调用的`expression`参数中使用时不会改变。

字符串的格式为“<quantity>[<unit>]”，其中 <unit> 为“T”表示tick、“S”表示秒、“D”表示天、“W”表示周、“M”表示月，但分钟没有。小时没有<unit>：小时时间周期以分钟表示。

该变量的值为：“10S”表示10秒，“30”表示30分钟，“240”表示4小时，“1D”表示1天，“2W”表示两周，“3M”表示一个季度。

类型:`simple string`

###### timeframe.multiplier

时间周期乘数

> 例如 '60' - 60，'D' - 1，'5D' - 5，'12M' - 12。

类型:`simple int`

###### timeframe.period

脚本主时间周期或请求时间周期的字符串表示，具体取决于脚本如何使用它。变量的值在`request.*()`函数调用的`expression`参数中使用时表示请求数据集的时间周期。否则，其值表示脚本的主时间周期`timeframe.main_period`，等于[indicator()]声明语句的`timeframe`参数或图表的时间周期。

字符串的格式为“<quantity>[<unit>]”，其中 <unit> 为“T”表示tick、“S”表示秒、“D”表示天、“W”表示周、“M”表示月，但分钟没有。小时没有<unit>：小时时间周期以分钟表示。

该变量的值为：“10S”表示10秒，“30”表示30分钟，“240”表示4小时，“1D”表示1天，“2W”表示两周，“3M”表示一个季度。

类型:`simple string`

> 为了始终访问脚本的主时间周期，即使在另一种情况下，也可以使用[timeframe.main_period]变量。
>

###### timenow

UNIX格式的当前时间。 这是自1970年1月1日00:00:00 UTC以来的毫秒数。

类型:`series int`

> 请注意，使用此变量/函数可能会导致[指标重新绘制]。
>

###### volume

当前K线成交量

类型:`series float`

> 可使用方括号运算符 []来访问以前的值，例如。 成交量[1]，成交量[2]。
>

###### weekofyear

根据K线的开盘UNIX时间戳计算得出的交易所时区一年的周数。

类型:`series int	

> 该变量始终引用与K线开盘时间相对应的周数。因此，对于具有隔夜时段的商品（例如，“EURUSD”，其中“星期一”交易时段于星期日17:00开始，以交易时间为准），该价值可能代表上一个日历周，而不是时段的主要交易日的一周。
>

###### year

交换时区的当前年k线

类型:`series int`

> 请注意，此变量根据K线的打开时间返回年份。对于隔夜交易时段（例如EURUSD，其周一交易时段从周日17:00开始），该值可以比交易日的年份低1。
>

# 常数

###### adjustment.dividends



常数股息调整（应用股息调整）。

类型

const string

另见

[adjustment.none][adjustment.splits][ticker.new()]

###### adjustment.none



无调整类型的常量（不应用调整）。

类型

const string

另见

[adjustment.splits][adjustment.dividends][ticker.new()]

###### adjustment.splits



分割调整类型的常量（应用分割调整）。

类型

const string

另见

[adjustment.none][adjustment.dividends][ticker.new()]

###### alert.freq_all



与alert()函数的 `freq` 参数一起使用的命名常数。

所有函数调用触发警报。

类型

const string

另见

[alert()]

###### alert.freq_once_per_bar



与alert()函数的 `freq` 参数一起使用的命名常数。

K线中的第一个函数调用触发警报。

类型

const string

另见

[alert()]

###### alert.freq_once_per_bar_close



与alert()函数的 `freq` 参数一起使用的命名常数。

该函数调用仅在实时K线的最后一个脚本迭代期间发生时，在关闭时触发警报。

类型

const string

另见

[alert()]

###### backadjustment.inherit



用于指定[ticker.new()]和[ticker.modify()]函数中`backadjustment`参数值的常量。

类型

const backadjustment

另见

[ticker.new()][ticker.modify()][backadjustment.on][backadjustment.off]

###### backadjustment.off



用于指定[ticker.new()]和[ticker.modify()]函数中`backadjustment`参数值的常量。

类型

const backadjustment

另见

[ticker.new()][ticker.modify()][backadjustment.on][backadjustment.inherit]

###### backadjustment.on



用于指定[ticker.new()]和[ticker.modify()]函数中`backadjustment`参数值的常量。

类型

const backadjustment

另见

[ticker.new()][ticker.modify()][backadjustment.inherit][backadjustment.off]

###### barmerge.gaps_off



合并所请求数据的策略。 数据不间断地合并，所有的差距都以先前最近的现有值填满。

类型

const barmerge_gaps

另见

[request.security()][barmerge.gaps_on]

###### barmerge.gaps_on



给所请求的数据合并策略。 数据与可能的差距(`na`值)合并。

类型

const barmerge_gaps

另见

[request.security()][barmerge.gaps_off]

###### barmerge.lookahead_off



合并所请求数据位置的策略。 所请求的条形图与当前的条形图按照k线收盘时间合并。 这种合并策略禁止从“未来”获取数据计算历史的影响。

类型

const barmerge_lookahead

另见

[request.security()][barmerge.lookahead_on]

###### barmerge.lookahead_on



合并所请求数据位置的策略。 请求的条形图与当前的条形图按照k线开盘时间合并。 这种合并策略可能导致从“未来”获取数据计算历史的不良影响。 这在回溯测试策略中不被接受，但在指标中可使用。

类型

const barmerge_lookahead

另见

[request.security()][barmerge.lookahead_off]

###### color.aqua



是#00BCD4颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.orange]

###### color.black



是#363A45颜色的命名常量。

类型

const color

另见

[color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.blue



是 #2962ff 颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.teal][color.aqua][color.orange]

###### color.fuchsia



是#E040FB颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.gray



是#787B86颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.green



是#4CAF50颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.lime



是#00E676颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.maroon



为 ＃880E4F 颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.navy



是#311B92颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.blue][color.teal][color.aqua][color.orange]

###### color.olive



是#808000颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.orange



是#FF9800颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua]

###### color.purple



是#9C27B0颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.red



是#F23645颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.silver



为 #B2B5BE 颜色的命名常量。

类型

const color

另见

[color.black][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.teal



是#089981颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.aqua][color.orange]

###### color.white



是#FFFFFF颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.yellow][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### color.yellow



是#FDD835颜色的命名常量。

类型

const color

另见

[color.black][color.silver][color.gray][color.white][color.maroon][color.red][color.purple][color.fuchsia][color.green][color.lime][color.olive][color.navy][color.blue][color.teal][color.aqua][color.orange]

###### currency.AED



阿联酋迪拉姆。

类型

const string

另见

[strategy()]

###### currency.ARS



阿根廷比索。

类型

const string

另见

[strategy()]

###### currency.AUD



澳元。

类型

const string

另见

[strategy()]

###### currency.BDT



孟加拉塔卡。

类型

const string

另见

[strategy()]

###### currency.BHD



巴林第纳尔。

类型

const string

另见

[strategy()]

###### currency.BRL



巴西雷亚尔。

类型

const string

另见

[strategy()]

###### currency.BTC



比特币。

类型

const string

另见

[strategy()]

###### currency.CAD



加元

类型

const string

另见

[strategy()]

###### currency.CHF



瑞士法郎

类型

const string

另见

[strategy()]

###### currency.CLP



智利比索。

类型

const string

另见

[strategy()]

###### currency.CNY



人民币。

类型

const string

另见

[strategy()]

###### currency.COP



哥伦比亚比索。

类型

const string

另见

[strategy()]

###### currency.CZK



捷克克朗。

类型

const string

另见

[strategy()]

###### currency.DKK



丹麦克朗。

类型

const string

另见

[strategy()]

###### currency.EGP



埃及镑。

类型

const string

另见

[strategy()]

###### currency.ETH



以太坊。

类型

const string

另见

[strategy()]

###### currency.EUR



欧元.

类型

const string

另见

[strategy()]

###### currency.GBP



英镑。

类型

const string

另见

[strategy()]

###### currency.HKD



港币

类型

const string

另见

[strategy()]

###### currency.HUF



匈牙利福林。

类型

const string

另见

[strategy()]

###### currency.IDR



印尼盾。

类型

const string

另见

[strategy()]

###### currency.ILS



以色列新谢克尔。

类型

const string

另见

[strategy()]

###### currency.INR



印度卢比。

类型

const string

另见

[strategy()]

###### currency.ISK



冰岛克朗。

类型

const string

另见

[strategy()]

###### currency.JPY



日元

类型

const string

另见

[strategy()]

###### currency.KES



肯尼亚先令。

类型

const string

另见

[strategy()]

###### currency.KRW



韩元。

类型

const string

另见

[strategy()]

###### currency.KWD



科威特第纳尔。

类型

const string

另见

[strategy()]

###### currency.LKR



斯里兰卡卢比。

类型

const string

另见

[strategy()]

###### currency.MAD



摩洛哥迪拉姆。

类型

const string

另见

[strategy()]

###### currency.MXN



墨西哥比索。

类型

const string

另见

[strategy()]

###### currency.MYR



马来西亚林吉特。

类型

const string

另见

[strategy()]

###### currency.NGN



尼日利亚奈拉。

类型

const string

另见

[strategy()]

###### currency.NOK



挪威克朗

类型

const string

另见

[strategy()]

###### currency.NONE



未指明的货币。

类型

const string

另见

[strategy()]

###### currency.NZD



新西兰元

类型

const string

另见

[strategy()]

###### currency.PEN



秘鲁索尔。

类型

const string

另见

[strategy()]

###### currency.PHP



菲律宾比索。

类型

const string

另见

[strategy()]

###### currency.PKR



巴基斯坦卢比。

类型

const string

另见

[strategy()]

###### currency.PLN



波兰兹罗提。

类型

const string

另见

[strategy()]

###### currency.QAR



卡塔尔里亚尔。

类型

const string

另见

[strategy()]

###### currency.RON



罗马尼亚利奥。

类型

const string

另见

[strategy()]

###### currency.RSD



塞尔维亚第纳尔。

类型

const string

另见

[strategy()]

###### currency.RUB



俄罗斯卢布

类型

const string

另见

[strategy()]

###### currency.SAR



沙特里亚尔。

类型

const string

另见

[strategy()]

###### currency.SEK



瑞典克朗

类型

const string

另见

[strategy()]

###### currency.SGD



新加坡元

类型

const string

另见

[strategy()]

###### currency.THB



泰铢。

类型

const string

另见

[strategy()]

###### currency.TND



突尼斯第纳尔。

类型

const string

另见

[strategy()]

###### currency.TRY



土耳其里拉

类型

const string

另见

[strategy()]

###### currency.TWD



新台币。

类型

const string

另见

[strategy()]

###### currency.USD



美元

类型

const string

另见

[strategy()]

###### currency.USDT



Tether。

类型

const string

另见

[strategy()]

###### currency.VES



委内瑞拉玻利瓦尔。

类型

const string

另见

[strategy()]

###### currency.VND



越南盾。

类型

const string

另见

[strategy()]

###### currency.ZAR



南非兰特

类型

const string

另见

[strategy()]

###### dayofweek.friday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.sunday][dayofweek.monday][dayofweek.tuesday][dayofweek.wednesday][dayofweek.thursday][dayofweek.saturday]

###### dayofweek.monday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.sunday][dayofweek.tuesday][dayofweek.wednesday][dayofweek.thursday][dayofweek.friday][dayofweek.saturday]

###### dayofweek.saturday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.sunday][dayofweek.monday][dayofweek.tuesday][dayofweek.wednesday][dayofweek.thursday][dayofweek.friday]

###### dayofweek.sunday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.monday][dayofweek.tuesday][dayofweek.wednesday][dayofweek.thursday][dayofweek.friday][dayofweek.saturday]

###### dayofweek.thursday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.sunday][dayofweek.monday][dayofweek.tuesday][dayofweek.wednesday][dayofweek.friday][dayofweek.saturday]

###### dayofweek.tuesday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.sunday][dayofweek.monday][dayofweek.wednesday][dayofweek.thursday][dayofweek.friday][dayofweek.saturday]

###### dayofweek.wednesday



是[dayofweek()]函数的返回值和[dayofweek]变量的值的命名常量。

类型

const int

另见

[dayofweek.sunday][dayofweek.monday][dayofweek.tuesday][dayofweek.thursday][dayofweek.friday][dayofweek.saturday]

###### display.all



与`plot*()`、`input*()`、[fill()]、[bgcolor()]、[barcolor()]和[hline()]函数的`display`参数一起使用的命名常量。指定值或视觉对象默认出现在所有可能的位置。

类型

const plot_simple_display

备注

`display.*`常量支持[+]和[-]操作，支持自定义显示设置组合。例如，`display.all - display.data_window`指定输入或绘图的数据出现在除数据窗口之外的所有可能位置。

在脚本的“设置/样式”标签页选中未选中的绘图会更改其显示设置，使绘制的数据出现在所有可用的图表位置。要恢复脚本中编写的显示设置，请从“设置”对话框底部的“默认”下拉菜单中选择“重置设置”。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### display.data_window



与`plot*()`和`input*()`函数的`display`参数一起使用的命名常量。指定默认情况下在数据窗口中可用的值。点击图表右侧边栏中的“对象树和数据窗口”图标即可访问“数据窗口”标签页。

类型

const plot_display

备注

`display.*`常量支持[+]和[-]操作，从而支持自定义显示设置组合。例如，`display.data_window + display.status_line`指定输入或绘图的数据显示在数据窗口和脚本的状态行中，而`display.all - display.data_window`指定数据显示在除数据窗口之外的所有可能位置。

在脚本的“设置/样式”标签页选中未选中的绘图会更改其显示设置，使绘制的数据出现在所有可用的图表位置。要恢复脚本中编写的显示设置，请从“设置”对话框底部的“默认”下拉菜单中选择“重置设置”。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### display.none



与`plot*()`、`input*()`、[fill()]、[bgcolor()]、[barcolor()]和[hline()]函数的`display`参数一起使用的命名常量。指定默认情况下不在任何地方显示值或视觉效果。

类型

const plot_simple_display

备注

在脚本的“设置/样式”标签页选中未选中的绘图会更改其显示设置，使绘制的数据出现在所有可用的图表位置。要恢复脚本中编写的显示设置，请从“设置”对话框底部的“默认”下拉菜单中选择“重置设置”。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### display.pane



与`plot*()`函数的`display`参数一起使用的命名常量。指定绘制的值默认显示在图表窗格中。

类型

const plot_display

备注

`display.*`常量支持[+]和[-]操作，从而支持自定义显示设置组合。例如，`display.pane + display.data_window`指定绘图值显示在图表窗格和数据窗口中，`display.all - display.pane`指定绘图值显示在除图表窗格之外的所有可能位置。

在脚本的“设置/样式”标签页选中未选中的绘图会更改其显示设置，使绘制的数据出现在所有可用的图表位置。要恢复脚本中编写的显示设置，请从“设置”对话框底部的“默认”下拉菜单中选择“重置设置”。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### display.pine_screener



与[plot()]函数的`display`参数一起使用的命名常量。指定当用户将指标应用于所选自选表时，[Pine Screener]默认显示一列绘图值。

类型

const plot_display

备注

`display.*`常量支持[+]和[-]操作，从而支持自定义显示设置组合。例如，`display.data_window + display.pine_screener`指定绘制的值显示在数据窗口和Pine筛选器，而`display.all - display.pine_screener`指定值显示在除Pine筛选器之外的所有可能位置。

Pine筛选器默认仅显示脚本中前10个已启用图表的列。如果图表的默认显示设置未包含筛选器，或者筛选器已显示脚本中其他10个图表的列，则用户可以使用表头最右侧的“管理列”菜单，将筛选器配置为显示该图表的列。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### display.price_scale



与`plot*()`函数的`display`参数一起使用的命名常量。指定价格坐标是否显示绘图数据的标签，但前提是图表设置允许。

类型

const plot_display

备注

`display.*`常量支持[+]和[-]操作，从而支持自定义显示设置组合。例如，`display.price_scale + display.data_window`指定绘图数据显示在价格坐标和数据窗口中；`display.all - display.price_scale`指定数据显示在除价格坐标之外的所有可能位置。

在脚本的“设置/样式”标签页选中未选中的绘图会更改其显示设置，使绘制的数据出现在所有可用的图表位置。要恢复脚本中编写的显示设置，请从“设置”对话框底部的“默认”下拉菜单中选择“重置设置”。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### display.status_line



与`plot*()`和`input*()`函数的`display`参数一起使用的命名常量。指定只有在图表设置允许的情况下，值才可在脚本的状态行中使用。

类型

const plot_display

备注

`display.*`常量支持[+]和[-]操作，从而支持自定义显示设置组合。例如，`display.data_window + display.status_line`指定输入或绘图的数据显示在数据窗口和脚本的状态行中，而`display.all - display.status_line`指定数据显示在除状态行之外的所有可能位置。

在脚本的“设置/样式”标签页选中未选中的绘图会更改其显示设置，使绘制的数据出现在所有可用的图表位置。要恢复脚本中编写的显示设置，请从“设置”对话框底部的“默认”下拉菜单中选择“重置设置”。

另见

[plot()][plotshape()][plotchar()][plotarrow()][plotbar()][plotcandle()]

###### dividends.gross



[request.dividends()]函数的命名常数。用于请求扣除前的股息回报。

类型

const string

另见

[request.dividends()]

###### dividends.net



[request.dividends()]函数的命名常数。用于请求扣除后的股息回报。

类型

const string

另见

[request.dividends()]

###### earnings.actual



[request.earnings()]函数的命名常数。用于请求所报告的收益值。

类型

const string

另见

[request.earnings()]

###### earnings.estimate



[request.earnings()]函数的命名常数。用于请求预估收益值。

类型

const string

另见

[request.earnings()]

###### earnings.standardized



[request.earnings()]函数的命名常量。用于请求标准化收益值。

类型

const string

另见

[request.earnings()]

###### extend.both



[line.new()]和[line.set_extend()]函数的命名常量。

类型

const string

另见

[line.new()][line.set_extend()][extend.none][extend.left][extend.right]

###### extend.left



[line.new()]和[line.set_extend()]函数的命名常量。

类型

const string

另见

[line.new()][line.set_extend()][extend.none][extend.right][extend.both]

###### extend.none



[line.new()]和[line.set_extend()]函数的命名常量。

类型

const string

另见

[line.new()][line.set_extend()][extend.left][extend.right][extend.both]

###### extend.right



[line.new()]和[line.set_extend()]函数的命名常量。

类型

const string

另见

[line.new()][line.set_extend()][extend.none][extend.left][extend.both]

###### false



表示[bool]值的文字，以及比较操作的结果。

备注

请参阅[比较运算符]和[逻辑运算符]的用户手册。

另见

[bool]

###### font.family_default



[box.new()], [box.set_text_font_family()], [label.new()], [label.set_text_font_family()], [table.cell()]和[table.cell_set_text_font_family()]功能的默认文本字体

类型

const string

另见

[box.new()][box.set_text_font_family()][label.new()][label.set_text_font_family()][table.cell()][table.cell_set_text_font_family()][font.family_monospace]

###### font.family_monospace



[box.new()], [box.set_text_font_family()], [label.new()], [label.set_text_font_family()], [table.cell()]和[table.cell_set_text_font_family()]功能的等宽文本字体

类型

const string

另见

[box.new()][box.set_text_font_family()][label.new()][label.set_text_font_family()][table.cell()][table.cell_set_text_font_family()][font.family_default]

###### format.inherit



是一个命名常量，用于从[indicator()]函数中的父系列中选择脚本输出值的格式。

类型

const string

另见

[indicator()][format.price][format.volume][format.percent]

###### format.mintick



是与[str.tostring()]函数一起使用的命名常量。使用此参数将数字传递给[str.tostring()]会将数字四舍五入到可以除以[syminfo.mintick]的最接近的值，不带余数，并且向上舍入，并返回带尾随零的所述值的字符串版本。

类型

const string

另见

[indicator()][format.inherit][format.price][format.volume]

###### format.percent



是一个命名常量，用于在指标函数中以百分比形式选择脚本输出值的格式。它在值后添加一个百分号。

类型

const string

备注

无论图表本身的精度如何，默认精度均为2。这可以通过[indicator()]函数的'precision'参数来更改。

另见

[indicator()][format.inherit][format.price][format.volume]

###### format.price



是一个命名常量，用于在[indicator()]函数中选择脚本输出值的格式作为价格。

类型

const string

备注

如果format是format.price，则设置默认精度值。您可以使用指标函数的precision参数来更改精度值。

另见

[indicator()][format.inherit][format.volume][format.percent]

###### format.volume



是一个命名常量，用于在[indicator()]函数中选择脚本输出格式为成交量，例如 '5183'将被格式化为'5.183K'。

该变量定义的小数精度规则优先于其他精度设置。当[indicator()]、[strategy()]或`plot*()`调用使用此`format`选项时，函数的`precision`参数不会影响结果。

类型

const string

另见

[indicator()][format.inherit][format.price][format.percent]

###### hline.style_dashed



是[hline()]函数的点划线样式的命名常量。

类型

const hline_style

另见

[hline.style_solid][hline.style_dotted]

###### hline.style_dotted



是[hline()]函数的点虚线样式的命名常量。

类型

const hline_style

另见

[hline.style_solid][hline.style_dashed]

###### hline.style_solid



是[hline()]函数的实心线型的命名常量。

类型

const hline_style

另见

[hline.style_dotted][hline.style_dashed]

###### label.style_arrowdown



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_arrowup



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_circle



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_cross



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_diamond



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square]

###### label.style_flag



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_center



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_square][label.style_diamond]

###### label.style_label_down



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_left



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_lower_left



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_lower_right



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_right



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_up



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_upper_left



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_label_upper_right



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_none



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_square



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_diamond]

###### label.style_text_outline



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_triangledown



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangleup][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_triangleup



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_xcross][label.style_cross][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_lower_left][label.style_label_lower_right][label.style_label_upper_left][label.style_label_upper_right][label.style_label_center][label.style_square][label.style_diamond]

###### label.style_xcross



[label.new()]和[label.set_style()]函数的标签样式。

类型

const string

另见

[label.new()][label.set_style()][label.set_textalign()][label.style_none][label.style_cross][label.style_triangleup][label.style_triangledown][label.style_flag][label.style_circle][label.style_arrowup][label.style_arrowdown][label.style_label_up][label.style_label_down][label.style_label_left][label.style_label_right][label.style_label_center][label.style_square][label.style_diamond]

###### line.style_arrow_both



[line.new()]和[line.set_style()]函数的线条样式。 两点上带箭头的实线。

类型

const string

另见

[line.new()][line.set_style()][line.style_solid][line.style_dotted][line.style_dashed][line.style_arrow_left][line.style_arrow_right]

###### line.style_arrow_left



[line.new()]和[line.set_style()]函数的线条样式。 第一点带箭头的实线。

类型

const string

另见

[line.new()][line.set_style()][line.style_solid][line.style_dotted][line.style_dashed][line.style_arrow_right][line.style_arrow_both]

###### line.style_arrow_right



[line.new()]和[line.set_style()]函数的线条样式。 第二点带箭头的实线。

类型

const string

另见

[line.new()][line.set_style()][line.style_solid][line.style_dotted][line.style_dashed][line.style_arrow_left][line.style_arrow_both]

###### line.style_dashed



[line.new()]和[line.set_style()]函数的线条样式。

类型

const string

另见

[line.new()][line.set_style()][line.style_solid][line.style_dotted][line.style_arrow_left][line.style_arrow_right][line.style_arrow_both]

###### line.style_dotted



[line.new()]和[line.set_style()]函数的线条样式。

类型

const string

另见

[line.new()][line.set_style()][line.style_solid][line.style_dashed][line.style_arrow_left][line.style_arrow_right][line.style_arrow_both]

###### line.style_solid



[line.new()]和[line.set_style()]函数的线条样式。

类型

const string

另见

[line.new()][line.set_style()][line.style_dotted][line.style_dashed][line.style_arrow_left][line.style_arrow_right][line.style_arrow_both]

###### location.abovebar



[plotshape()]，[plotchar()]功能的位置值。 形状绘制在主系列k线上方。

类型

const string

另见

[plotshape()][plotchar()][location.belowbar][location.top][location.bottom][location.absolute]

###### location.absolute



[plotshape()]，[plotchar()]功能的位置值。 形状在图表上绘制，使用指标值作为价格坐标。

类型

const string

另见

[plotshape()][plotchar()][location.abovebar][location.belowbar][location.top][location.bottom]

###### location.belowbar



[plotshape()]，[plotchar()]功能的位置值。 形状绘制在主要系列k线下方。

类型

const string

另见

[plotshape()][plotchar()][location.abovebar][location.top][location.bottom][location.absolute]

###### location.bottom



[plotshape()]，[plotchar()]功能的位置值。 形状绘制在底部图表边框附近。

类型

const string

另见

[plotshape()][plotchar()][location.abovebar][location.belowbar][location.top][location.absolute]

###### location.top



[plotshape()]，[plotchar()]功能的位置值。 形状绘制在顶部图表边框附近。

类型

const string

另见

[plotshape()][plotchar()][location.abovebar][location.belowbar][location.bottom][location.absolute]

###### math.e



是[欧拉数`的命名常数。它等于2.7182818284590452。

类型

const float

另见

[math.phi][math.pi][math.rphi]

###### math.phi



是[黄金分割]的命名常数。等于1.6180339887498948。

类型

const float

另见

[math.e][math.pi][math.rphi]

###### math.pi



是[阿基米德常数]的命名常数。它等于3.1415926535897932。

类型

const float

另见

[math.e][math.phi][math.rphi]

###### math.rphi



是[黄金分割率]的命名常数。它等于0.6180339887498948。

类型

const float

另见

[math.e][math.pi][math.phi]

###### order.ascending



确定阵列从最小到最大的排序顺序。

类型

const sort_order

另见

[array.new_float()][array.sort()]

###### order.descending



确定阵列从最大到最小的排序顺序。

类型

const sort_order

另见

[array.new_float()][array.sort()]

###### plot.linestyle_dashed



与[plot()]函数的`linestyle`参数一起使用的命名常量，用于修改绘制线条的外观。如果函数调用的`style`参数指定了显示线条的绘图样式，则使用此常量作为`linestyle`参数将指定绘制的线条为虚线。

类型

const plot_line_style

另见

[plot()][plot.linestyle_solid][plot.linestyle_dotted]

###### plot.linestyle_dotted



与[plot()]函数的`linestyle`参数一起使用的命名常量，用于修改绘制线条的外观。如果函数调用的`style`参数指定了显示线条的绘图样式，则使用此常量作为`linestyle`参数将指定绘制的线条为虚线。

类型

const plot_line_style

另见

[plot()][plot.linestyle_dashed][plot.linestyle_solid]

###### plot.linestyle_solid



与[plot()]函数的`linestyle`参数一起使用的命名常量，用于修改绘制线条的外观。如果函数调用的`style`参数指定了显示线条的绘图样式，则使用此常量作为`linestyle`参数将指定绘制的线条为实线。

类型

const plot_line_style

另见

[plot()][plot.linestyle_dashed][plot.linestyle_dotted]

###### plot.style_area



'Area'样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_areabr



'Area With Breaks'样式的命名常量，用作[plot()]函数中`style`参数的参数。 与[plot.style_area]类似，只是不填充数据中的空白。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_circles



“Circles”样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_columns



'Columns' 样式的命名常量，用作[plot()]函数中的`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_cross



'Cross' 样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_histogram



'Histogram'样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_line



'Line'样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_linebr



'Line With Breaks'样式的命名常量，用作[plot()]函数中`style`参数的参数。类似于[plot.style_line]，除了数据中的空白没有被填充。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_stepline



'Step Line'样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline_diamond][plot.style_steplinebr]

###### plot.style_stepline_diamond



'Step Line With Diamonds'样式的命名常量，用作[plot()]函数中`style`参数的参数。类似于[plot.style_stepline]，除了数据变化也用菱形标记。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_steplinebr]

###### plot.style_steplinebr



“Step line with Breaks”样式的命名常量，用作[plot()]函数中`style`参数的参数。

类型

const plot_style

另见

[plot()][plot.style_line][plot.style_linebr][plot.style_histogram][plot.style_cross][plot.style_area][plot.style_areabr][plot.style_columns][plot.style_circles][plot.style_stepline][plot.style_stepline_diamond]

###### position.bottom_center



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到底边居中。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.top_right][position.middle_left][position.middle_center][position.middle_right][position.bottom_left][position.bottom_right]

###### position.bottom_left



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到屏幕的左下角。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.top_right][position.middle_left][position.middle_center][position.middle_right][position.bottom_center][position.bottom_right]

###### position.bottom_right



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到屏幕的右下角。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.top_right][position.middle_left][position.middle_center][position.middle_right][position.bottom_left][position.bottom_center]

###### position.middle_center



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到屏幕中央。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.top_right][position.middle_left][position.middle_right][position.bottom_left][position.bottom_center][position.bottom_right]

###### position.middle_left



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到屏幕左侧。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.top_right][position.middle_center][position.middle_right][position.bottom_left][position.bottom_center][position.bottom_right]

###### position.middle_right



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到屏幕右侧。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.top_right][position.middle_left][position.middle_center][position.bottom_left][position.bottom_center][position.bottom_right]

###### position.top_center



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到顶边居中。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_right][position.middle_left][position.middle_center][position.middle_right][position.bottom_left][position.bottom_center][position.bottom_right]

###### position.top_left



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到左上角。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_center][position.top_right][position.middle_left][position.middle_center][position.middle_right][position.bottom_left][position.bottom_center][position.bottom_right]

###### position.top_right



在[table.new()]、[table.cell()]函数中使用的表格位置。

将表格绑定到右上角。

类型

const string

另见

[table.new()][table.cell()][table.set_position()][position.top_left][position.top_center][position.middle_left][position.middle_center][position.middle_right][position.bottom_left][position.bottom_center][position.bottom_right]

###### scale.left



一个用于[indicator()]和[strategy()]声明语句中`scale`参数的命名常量。它指定脚本的价格坐标位于窗格的左侧。如果脚本覆盖在主图表窗格或其他脚本的窗格上，它会在窗格左侧添加一个新的价格坐标，并独立缩放其视觉效果以适应窗格的视觉空间。

类型

const scale_type

另见

[indicator()]

###### scale.none



A named constant for use as the `scale` argument in [indicator()] and [strategy()] declaration statements. A declaration statement can use this constant only if its `overlay` argument is `true`. Specifies that the script scales its visuals independently to fit the visual space of the main chart pane or another script's pane without displaying a separate scale. The script displays plotted numbers directly on the pane's existing price scale if the chart's settings allow it. If the user moves the script to a new pane, the script displays the values on a new scale to the left or right of that pane, depending on the chart's "Scales placement" setting.

类型

const scale_type

另见

[indicator()]

###### scale.right



一个用于[indicator()]和[strategy()]声明语句中`scale`参数的命名常量。它指定脚本的价格坐标位于窗格的右侧。如果脚本覆盖在主图表窗格或其他脚本的窗格上，它会在窗格右侧添加一个新的价格坐标，并独立缩放其视觉效果以适应窗格的视觉空间。

类型

const scale_type

另见

[indicator()]

###### session.extended



延长时段类型的常数(有延长时段数据)。

类型

const string

另见

[session.regular][syminfo.session]

###### session.regular



常规时段类型的常数(无延长时段数据)。

类型

const string

另见

[session.extended][syminfo.session]

###### settlement_as_close.inherit



用于指定[ticker.new()]和[ticker.modify()]函数中`settlement_as_close`参数值的常量。

类型

const settlement

另见

[ticker.new()][ticker.modify()][settlement_as_close.on][settlement_as_close.off]

###### settlement_as_close.off



用于指定[ticker.new()]和[ticker.modify()]函数中`settlement_as_close`参数值的常量。

类型

const settlement

另见

[ticker.new()][ticker.modify()][settlement_as_close.on][settlement_as_close.inherit]

###### settlement_as_close.on



用于指定[ticker.new()]和[ticker.modify()]函数中`settlement_as_close`参数值的常量。

类型

const settlement

另见

[ticker.new()][ticker.modify()][settlement_as_close.inherit][settlement_as_close.off]

###### shape.arrowdown



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.arrowup



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.circle



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.cross



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.diamond



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.flag



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.labeldown



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.labelup



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.square



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.triangledown



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.triangleup



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### shape.xcross



[plotshape()]功能的形状样式。

类型

const string

另见

[plotshape()]

###### size.auto



一个常量，用于指定[plotchar()]、[plotshape()]、[label.new()]和[box.new()]绘图的大小。自动调整绘图的大小。

类型

const string

另见

[plotshape()][plotchar()][label.set_size()][size.tiny][size.small][size.normal][size.large][size.huge]

###### size.huge



一个常量，用于指定[plotchar()]、[plotshape()]、[label.new()]、[box.new()]和[table.cell()]绘图的大小。设置大小为巨大。

类型

const string

另见

[plotshape()][plotchar()][label.set_size()][size.auto][size.tiny][size.small][size.normal][size.large]

###### size.large



一个常量，用于指定[plotchar()]、[plotshape()]、[label.new()]、[box.new()]和[table.cell()]绘图的大小。设置大小为大。

类型

const string

另见

[plotshape()][plotchar()][label.set_size()][size.auto][size.tiny][size.small][size.normal][size.huge]

###### size.normal



一个常量，用于指定[plotchar()]、[plotshape()]、[label.new()]、[box.new()]和[table.cell()]绘图的大小。设置大小为正常。

类型

const string

另见

[plotshape()][plotchar()][label.set_size()][size.auto][size.tiny][size.small][size.large][size.huge]

###### size.small



一个常量，用于指定[plotchar()]、[plotshape()]、[label.new()]、[box.new()]和[table.cell()]绘图的大小。设置大小为小。

类型

const string

另见

[plotshape()][plotchar()][label.set_size()][size.auto][size.tiny][size.normal][size.large][size.huge]

###### size.tiny



一个常量，用于指定[plotchar()]、[plotshape()]、[label.new()]、[box.new()]和[table.cell()]绘图的大小。设置大小为微小。

类型

const string

另见

[plotshape()][plotchar()][label.set_size()][size.auto][size.small][size.normal][size.large][size.huge]

###### splits.denominator



[request.splits()]函数的命名常数。用于请求拆分的分母（分数行下方的数字）。

类型

const string

另见

[request.splits()]

###### splits.numerator



[request.splits()]函数的命名常量。用于请求拆分的分子（分数行上方的数字）。

类型

const string

另见

[request.splits()]

###### strategy.cash



这是可以提供给 [strategy()] 声明语句中的 `default_qty_type` 参数的参数之一。仅当[strategy.entry()]或[strategy.order()]函数调用中的‘qty’参数未使用值时才相关。它指定 `strategy.account_currency` 中的一定数量的现金将用于进入交易。

类型

const string



```
//@version=6
strategy("strategy.cash", overlay = true, default_qty_value = 50, default_qty_type = strategy.cash, initial_capital = 1000000)

if bar_index == 0
    // As ‘qty’ is not defined, the previously defined values for the `default_qty_type` and `default_qty_value` parameters are used to enter trades, namely 50 units of cash in the currency of `strategy.account_currency`.
    // `qty` is calculated as (default_qty_value)/(close price). If current price is $5, then qty = 50/5 = 10.
    strategy.entry("EN", strategy.long)
if bar_index == 2
    strategy.close("EN")
```

另见

[strategy()]

###### strategy.commission.cash_per_contract



订单佣金类型。 以每份合约的账户货币显示金额

类型

const string

另见

[strategy()]

###### strategy.commission.cash_per_order



订单佣金类型。 按每个订单的账户货币显示金额。

类型

const string

另见

[strategy()]

###### strategy.commission.percent



订单佣金类型。 现金订单量的百分比。

类型

const string

另见

[strategy()]

###### strategy.direction.all



允许既可以做多又可以做空的策略

类型

const string

另见

[strategy.risk.allow_entry_in()]

###### strategy.direction.long



只能做多的策略

类型

const string

另见

[strategy.risk.allow_entry_in()]

###### strategy.direction.short



只能做空的策略

类型

const string

另见

[strategy.risk.allow_entry_in()]

###### strategy.fixed



这是可以提供给[strategy()]声明语句中的 `default_qty_type` 参数的参数之一。仅当[strategy.entry()]或[strategy.order()]函数调用中的‘qty’参数未使用值时才相关。它指定将使用一些合约/股票/手数来进行交易。

类型

const string



```
//@version=6
strategy("strategy.fixed", overlay = true, default_qty_value = 50, default_qty_type = strategy.fixed, initial_capital = 1000000)

if bar_index == 0
    // As ‘qty’ is not defined, the previously defined values for the `default_qty_type` and `default_qty_value` parameters are used to enter trades, namely 50 contracts.
    // qty = 50
    strategy.entry("EN", strategy.long)
if bar_index == 2
    strategy.close("EN")
```

另见

[strategy()]

###### strategy.long



与[strategy.entry()]和[strategy.order()]命令的`direction`参数一起使用的命名常量。它指定该命令创建买入订单。

类型

const strategy_direction

另见

[strategy.entry()][strategy.exit()][strategy.order()]

###### strategy.oca.cancel



与[strategy.entry()]和[strategy.order()]命令的`oca_type`参数一起使用的命名常量。它指定当另一个具有相同`oca_name`和`oca_type`的订单执行时，策略会取消未完成的订单。

类型

const string

备注

如果策略在同一时间执行，则无法取消或减少来自OCA组的挂单。例如，如果市场价格触发了来自[strategy.order()]调用的两个具有相同`oca_*`参数的止损订单，则该策略无法全部或部分取消任何一个。

另见

[strategy.entry()][strategy.exit()][strategy.order()]

###### strategy.oca.none



与[strategy.entry()]和[strategy.order()]命令的`oca_type`参数一起使用的命名常量。它指定订单独立于所有其他订单执行，包括具有相同`oca_name`的订单。

类型

const string

另见

[strategy.entry()][strategy.exit()][strategy.order()]

###### strategy.oca.reduce



与[strategy.entry()]和[strategy.order()]命令的`oca_type`参数一起使用的命名常量。它指定当另一个具有相同`oca_name`和`oca_type`的订单执行时，该策略会将未成交订单减少该订单的大小。如果未成交订单的大小在减少后达到0，则与完全取消订单相同。

类型

const string

备注

如果策略在同一时间执行，则无法取消或减少来自OCA组的挂单。例如，如果市场价格触发了来自[strategy.order()]调用的两个具有相同`oca_*`参数的止损订单，则该策略无法全部或部分取消任何一个。

来自[strategy.exit()]的订单自动使用此OCA类型，并且它们默认属于同一个OCA组。

另见

[strategy.entry()][strategy.exit()][strategy.order()]

###### strategy.percent_of_equity



这是可以提供给[strategy()]声明语句中的 `default_qty_type` 参数的参数之一。仅当[strategy.entry()]或[strategy.order()]函数调用中的 ‘qty’ 参数未使用值时才相关。它指定一定百分比(0-100)的净值将用于进入交易。

类型

const string



```
//@version=6
strategy("strategy.percent_of_equity", overlay = false, default_qty_value = 100, default_qty_type = strategy.percent_of_equity, initial_capital = 1000000)

// As ‘qty’ is not defined, the previously defined values for the `default_qty_type` and `default_qty_value` parameters are used to enter trades, namely 100% of available equity.
if bar_index == 0
    strategy.entry("EN", strategy.long)
if bar_index == 2
    strategy.close("EN")
plot(strategy.equity)

 // The ‘qty’ parameter is set to 10. Entering position with fixed size of 10 contracts and entry market price = (10 * close).
if bar_index == 4
    strategy.entry("EN", strategy.long, qty = 10)
if bar_index == 6
    strategy.close("EN")
```

另见

[strategy()]

###### strategy.short



与[strategy.entry()]和[strategy.order()]命令的`direction`参数一起使用的命名常量。它指定该命令创建卖单。

类型

const strategy_direction

另见

[strategy.entry()][strategy.exit()][strategy.order()]

###### text.align_bottom



[box.new()]、[box.set_text_valign()]、[table.cell()]和[table.cell_set_text_valign()]函数的垂直文本对齐。

类型

const string

另见

[table.cell()][table.cell_set_text_valign()][text.align_center][text.align_left][text.align_right]

###### text.align_center



[box.new()]、[box.set_text_halign()]、[box.set_text_valign()]、[label.new()]和[label.set_textalign()]函数的文本对齐。

类型

const string

另见

[label.new()][label.set_style()][text.align_left][text.align_right]

###### text.align_left



[box.new()]、[box.set_text_halign()]、[label.new()]和[label.set_textalign()]函数的水平文本对齐。

类型

const string

另见

[label.new()][label.set_style()][text.align_center][text.align_right]

###### text.align_right



[box.new()]、[box.set_text_halign()]、[label.new()]和[label.set_textalign()]函数的水平文本对齐。

类型

const string

另见

[label.new()][label.set_style()][text.align_center][text.align_left]

###### text.align_top



[box.new()]、[box.set_text_valign()]、[table.cell()]和[table.cell_set_text_valign()]函数的垂直文本对齐。

类型

const string

另见

[table.cell()][table.cell_set_text_valign()][text.align_center][text.align_left][text.align_right]

###### text.format_bold



与`label.new()`、`box.new()`、`table.cell()`和`*set_text_formatting()`函数的`text_formatting`参数一起使用的命名常量。使文本变为粗体。

类型

const text_format

另见

[label.new()][box.new()][table.cell()]

###### text.format_italic



与`label.new()`、`box.new()`、`table.cell()` 和 `*set_text_formatting()`函数的`text_formatting`参数一起使用的命名常量。将文本设为斜体。

类型

const text_format

另见

[label.new()][box.new()][table.cell()]

###### text.format_none



与`label.new()`、`box.new()`、`table.cell()`和`*set_text_formatting()`函数的`text_formatting`参数一起使用的命名常量。表示无特殊文本格式。

类型

const text_format

另见

[label.new()][box.new()][table.cell()]

###### text.wrap_auto



[box.new()]和[box.set_text_wrap()]函数的自动换行模式。

类型

const string

另见

[box.new()][box.set_text()][box.set_text_wrap()]

###### text.wrap_none



禁用[box.new()]和[box.set_text_wrap()]函数的换行模式。

类型

const string

另见

[box.new()][box.set_text()][box.set_text_wrap()]

###### true



表示[bool]变量可以保存的值之一的文字，或者当表达式使用比较或逻辑运算符时可以计算的值。

备注

请参阅[比较运算符]和[逻辑运算符]的用户手册。

另见

[bool]

###### xloc.bar_index



一个常量，指定创建和修改Pine绘图的函数如何解释x坐标。如果为`xloc = xloc.bar_index`，则绘图对象将每个x坐标视为`bar_index`值。

类型

const string

另见

[xloc.bar_time][line.new()][label.new()][box.new()][polyline.new()][line.set_xloc()][label.set_xloc()]

###### xloc.bar_time



一个常量，指定创建和修改Pine绘图的函数如何解释x坐标。如果为`xloc = xloc.bar_time`，则绘图对象将每个x坐标视为UNIX时间戳，以毫秒表示。

类型

const string

另见

[xloc.bar_index][line.new()][label.new()][box.new()][polyline.new()][line.set_xloc()][label.set_xloc()][xloc.bar_index]

###### yloc.abovebar



一个命名常量，指定函数[label.new()]中y值的解释算法。

类型

const string

另见

[label.new()][label.set_yloc()][yloc.price][yloc.belowbar]

###### yloc.belowbar



一个命名常量，指定函数[label.new()]中y值的解释算法。

类型

const string

另见

[label.new()][label.set_yloc()][yloc.price][yloc.abovebar]

###### yloc.price



一个命名常量，指定函数[label.new()]中y值的解释算法。

类型

const string

另见

[label.new()][label.set_yloc()][yloc.abovebar][yloc.belowbar]

#### 功能

###### alert()



在最新的实时K线调用时，以指定的频率为指标或策略创建警报触发。要为包含对此函数的调用的脚本激活警报，请打开“创建警报”对话框，然后在“条件”部分中选择脚本名称和“任何 alert() 函数调用”。



```
alert(message, freq) → void
```

参数

**message (series string)** 警报出现时发送的消息。

**freq (input string)** 可选。确定允许的警报触发频率。可能的值有：[alert.freq_all]（允许在任何实时更新时发出警报）、[alert.freq_once_per_bar]（仅允许在每根实时K线的第一次执行时发出警报）或 [alert.freq_once_per_bar_close]（仅允许在实时K线关闭时发出警报）。默认值为[alert.freq_once_per_bar]。



```
//@version=6
indicator("`alert()` example", "", true)
ma = ta.sma(close, 14)
xUp = ta.crossover(close, ma)
if xUp
    // Trigger the alert the first time a cross occurs during the real-time bar.
    alert("Price (" + str.tostring(close) + ") crossed over MA (" + str.tostring(ma) + ").", alert.freq_once_per_bar)
plot(ma)
plotchar(xUp, "xUp", "▲", location.top, size = size.tiny)
```

备注

`alert()`函数不会在图表上显示信息。

与[alertcondition()]不同，对此函数的调用不计入脚本的绘图计数。此外`alert()`调用允许在本地范围内进行，包括导出库函数的范围。

请参阅帮助中心的[这篇文章]，了解有关激活`alert()`调用警报的更多信息。

另见

[alertcondition()]

###### alertcondition()



创建警报条件，可在“创建警报”对话框中使用。请注意，[alertcondition()]不会创建警报，它只是在“创建警报”对话框中为您提供更多选项。此外，[alertcondition()]效果在图表上不可见。



```
alertcondition(condition, title, message) → void
```

参数

**condition (series bool)** 用于警报的系列布尔值。 True值代表警报触发，false - 无警报。 必要参数。

**title (const string)** 警报条件的标题。 可选参数。

**message (const string)** 当警报触发时显示消息。可选参数。



```
//@version=6
indicator("alertcondition", overlay=true)
alertcondition(close >= open, title='Alert on Green Bar', message='Green Bar!')
```

备注

请注意，alertcondition调用会生成一个额外的图。当我们计算每个脚本的输出系列数时，所有这些调用都会被考虑在内。

另见

[alert()]

###### array.abs()

2过载



返回一个阵列，其中包含原始阵列中每个元素的绝对值。

语法和重载

[`array.abs(id) → array`][`array.abs(id) → array`]

参数

**id (array<int/float>)** 阵列对象。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.avg()

2过载



该函数返回阵列元素的均值。

语法和重载

[`array.avg(id) → series float`][`array.avg(id) → series int`]

参数

**id (array<int/float>)** 阵列对象。



```
//@version=6
indicator("array.avg example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.avg(a))
```

返回值

阵列元素的均值。

备注

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.max()][array.min()][array.stdev()]

###### array.binary_search()



该函数返回值的索引，如果未找到该值，则返回-1。要搜索的阵列必须按升序排序。



```
array.binary_search(id, val) → series int
```

参数

**id (array<int/float>)** 阵列对象。

**val (series int/float)** 在阵列中搜索的值。



```
//@version=6
indicator("array.binary_search")
a = array.from(5, -2, 0, 9, 1)
array.sort(a) // [-2, 0, 1, 5, 9]
position = array.binary_search(a, 0) // 1
plot(position)
```

备注

二进制搜索适用于按升序预先排序的阵列。它首先将阵列中间的元素与目标值进行比较。如果元素与目标值匹配，则返回其在阵列中的位置。如果元素的值大于目标值，则在阵列的下半部分继续搜索。如果元素的值小于目标值，则在阵列的上半部分继续搜索。通过递归地执行此操作，该算法逐渐消除了阵列中目标值不能位于的越来越小的部分。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.binary_search_leftmost()



如果找到值，该函数将返回该值的索引。当未找到值时，该函数返回下一个最小元素的索引，如果它在阵列中，则在值所在位置的左侧。要搜索的阵列必须按升序排序。



```
array.binary_search_leftmost(id, val) → series int
```

参数

**id (array<int/float>)** 阵列对象。

**val (series int/float)** 在阵列中搜索的值。



```
//@version=6
indicator("array.binary_search_leftmost")
a = array.from(5, -2, 0, 9, 1)
array.sort(a) // [-2, 0, 1, 5, 9]
position = array.binary_search_leftmost(a, 3) // 2
plot(position)
```



```
//@version=6
indicator("array.binary_search_leftmost, repetitive elements")
a = array.from(4, 5, 5, 5)
// Returns the index of the first instance.
position = array.binary_search_leftmost(a, 5)
plot(position) // Plots 1
```

备注

二进制搜索适用于按升序预先排序的阵列。它首先将阵列中间的元素与目标值进行比较。如果元素与目标值匹配，则返回其在阵列中的位置。如果元素的值大于目标值，则在阵列的下半部分继续搜索。如果元素的值小于目标值，则在阵列的上半部分继续搜索。通过递归地执行此操作，该算法逐渐消除了阵列中目标值不能位于的越来越小的部分。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.binary_search_rightmost()



如果找到该值，该函数将返回该值的索引。当未找到该值时，该函数返回该值在阵列中所在位置右侧的元素的索引。阵列必须按升序排序。



```
array.binary_search_rightmost(id, val) → series int
```

参数

**id (array<int/float>)** 阵列对象。

**val (series int/float)** 在阵列中搜索的值。



```
//@version=6
indicator("array.binary_search_rightmost")
a = array.from(5, -2, 0, 9, 1)
array.sort(a) // [-2, 0, 1, 5, 9]
position = array.binary_search_rightmost(a, 3) // 3
plot(position)
```



```
//@version=6
indicator("array.binary_search_rightmost, repetitive elements")
a = array.from(4, 5, 5, 5)
// Returns the index of the last instance.
position = array.binary_search_rightmost(a, 5)
plot(position) // Plots 3
```

备注

二进制搜索按升序对已排序的阵列起作用。它首先将阵列中间的元素与目标值进行比较。如果元素与目标值匹配，则返回其在阵列中的位置。如果元素的值大于目标值，则在阵列的下半部分继续搜索。如果元素的值小于目标值，则在阵列的上半部分继续搜索。通过递归地执行此操作，该算法逐渐消除了阵列中目标值不能位于的越来越小的部分。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.clear()



该函数从阵列中删除所有元素。



```
array.clear(id) → void
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.clear example")
a = array.new_float(5,high)
array.clear(a)
array.push(a, close)
plot(array.get(a,0))
plot(array.size(a))
```

另见

[array.new_float()][array.insert()][array.push()][array.remove()][array.pop()]

###### array.concat()



该函数用于合并两个阵列。它将所有元素从第二个阵列推送到第一个阵列，然后返回第一个阵列。



```
array.concat(id1, id2) → array<type>
```

参数

**id1 (any array type)** 第一个阵列对象。

**id2 (any array type)** 第二个阵列对象。



```
//@version=6
indicator("array.concat example")
a = array.new_float(0,0)
b = array.new_float(0,0)
for i = 0 to 4
    array.push(a, high[i`
    array.push(b, low[i`
c = array.concat(a,b)
plot(array.size(a))
plot(array.size(b))
plot(array.size(c))
```

返回值

第一个阵列具有来自第二个阵列的合并元素。

另见

[array.new_float()][array.insert()][array.slice()]

###### array.copy()



该函数创建现有阵列的副本。



```
array.copy(id) → array<type>
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.copy example")
length = 5
a = array.new_float(length, close)
b = array.copy(a)
a := array.new_float(length, open)
plot(array.sum(a) / length)
plot(array.sum(b) / length)
```

返回值

阵列的副本。

另见

[array.new_float()][array.get()][array.slice()][array.sort()]

###### array.covariance()



该函数返回两个阵列的协方差。



```
array.covariance(id1, id2, biased) → series float
```

参数

**id1 (array<int/float>)** 阵列对象。

**id2 (array<int/float>)** 阵列对象。

**biased (series bool)** 确定应该使用哪个估计。可选。默认值为true。



```
//@version=6
indicator("array.covariance example")
a = array.new_float(0)
b = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
    array.push(b, open[i`
plot(array.covariance(a, b))
```

返回值

两个阵列的协方差。

备注

如果`biased`为`true`，函数将使用对整个总体的有偏估计进行计算；如果`false`，则使用对样本的无偏估计进行计算。如果两个数组均为空，则返回`na`。

另见

[array.new_float()][array.max()][array.stdev()][array.avg()][array.variance()]

###### array.every()



如果`id`数组的所有元素均为`true`，则返回`true`，否则返回`false`。



```
array.every(id) → series bool
```

参数

**id (array<bool>)** 阵列对象。

备注

此函数还适用于[int]和[float]类型的阵列，在这种情况下，零值被视为`false`，所有其它值被视为`true`。

另见

[array.some()][array.get()]

###### array.fill()



该函数将阵列的元素设置为单个值。如果未指定索引，则设置所有元素。如果仅提供起始索引（默认为0），则设置从该索引开始的元素。如果同时使用两个索引参数，则会设置从开始索引到但不包括结束索引的元素（默认值为na）。



```
array.fill(id, value, index_from, index_to) → void
```

参数

**id (any array type)** 阵列对象。

**value (series <type of the array's elements>)** 用于填充阵列的值。

**index_from (series int)** 起始索引，默认为0。

**index_to (series int)** 结束索引，默认为na。必须大于要设置的最后一个元素的索引。



```
//@version=6
indicator("array.fill example")
a = array.new_float(10)
array.fill(a, close)
plot(array.sum(a))
```

另见

[array.new_float()][array.set()][array.slice()]

###### array.first()



返回阵列的第一个元素。如果阵列为空，则抛出运行时错误。



```
array.first(id) → series <type>
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.first example")
arr = array.new_int(3, 10)
plot(array.first(arr))
```

另见

[array.last()][array.get()]

###### array.from()

12过载



该函数采用以下类型之一的可变数量的参数：int、float、bool、string、label、line、color、box、table、linefill，并返回相应类型的阵列。

语法和重载

[`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`][`array.from(arg0, arg1, ...) → array`]

参数

**arg0, arg1, ... (<arg..._type>)** 数组参数。



```
//@version=6
indicator("array.from_example", overlay = false)
arr = array.from("Hello", "World!") // arr (array<string>) will contain 2 elements: {Hello}, {World!}.
plot(close)
```

返回值

阵列元素的值。

备注

此函数最多可接受4,000 个“int”、“float”、“bool”或“color”参数。对于所有其它类型，包括用户定义类型，限制为999。

###### array.get()



该函数返回指定索引处元素的值。



```
array.get(id, index) → series <type>
```

参数

**id (any array type)** 阵列对象。

**index (series int)** 要返回其值的元素的索引。



```
//@version=6
indicator("array.get example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i] - open[i`
plot(array.get(a, 9))
```

返回值

阵列元素的值。

备注

如果索引为正数，则函数从数组的开头向前计数到结尾。第一个元素的索引为0，最后一个元素的索引为`array.size() - 1`。如果索引为负数，则函数从数组的结尾向后计数到开头。在这种情况下，最后一个元素的索引为-1，第一个元素的索引为负数`array.size()`。例如，对于包含三个元素的数组，以下所有元素都是`index`参数的有效参数：0、1、2、-1、-2、-3。

另见

[array.new_float()][array.set()][array.slice()][array.sort()]

###### array.includes()



如果在阵列中找到该值，则该函数返回true，否则返回false。



```
array.includes(id, value) → series bool
```

参数

**id (any array type)** 阵列对象。

**value (series <type of the array's elements>)** 要在阵列中搜索的值。



```
//@version=6
indicator("array.includes example")
a = array.new_float(5,high)
p = close
if array.includes(a, high)
    p := open
plot(p)
```

返回值

如果在阵列中找到该值，则为true，否则为false。

另见

[array.new_float()][array.indexof()][array.shift()][array.remove()][array.insert()]

###### array.indexof()



此函数返回值首次出现的索引。如果找不到该值，则返回 -1。



```
array.indexof(id, value) → series int
```

参数

**id (any array type)** 阵列对象。

**value (series <type of the array's elements>)** 要在阵列中搜索的值。



```
//@version=6
indicator("array.indexof example")
a = array.new_float(5,high)
index = array.indexof(a, high)
plot(index)
```

返回值

元素的索引。

另见

[array.lastindexof()][array.get()][array.lastindexof()][array.remove()][array.insert()]

###### array.insert()



该函数通过在适当位置添加新元素来更改阵列的内容。



```
array.insert(id, index, value) → void
```

参数

**id (any array type)** 阵列对象。

**index (series int)** 插入值的索引。

**value (series <type of the array's elements>)** 要添加到阵列的值。



```
//@version=6
indicator("array.insert example")
a = array.new_float(5, close)
array.insert(a, 0, open)
plot(array.get(a, 5))
```

备注

如果索引为正数，则函数从数组的开头向前计数到结尾。第一个元素的索引为0，最后一个元素的索引为`array.size() - 1`。如果索引为负数，则函数从数组的结尾向后计数到开头。在这种情况下，最后一个元素的索引为-1，第一个元素的索引为负数`array.size()`。例如，对于包含三个元素的数组，以下所有元素都是`index`参数的有效参数：0、1、2、-1、-2、-3。

另见

[array.new_float()][array.set()][array.push()][array.remove()][array.pop()][array.unshift()]

###### array.join()



该函数通过连接阵列的所有元素来建立并返回新字符串，用指定的分隔符字符串分隔。



```
array.join(id, separator) → series string
```

参数

**id (array<int/float/string>)** 阵列对象。

**separator (series string)** 用于分隔每个阵列元素的字符串。



```
//@version=6
indicator("array.join example")
a = array.new_float(5, 5)
label.new(bar_index, close, array.join(a, ","))
```

另见

[array.new_float()][array.set()][array.insert()][array.remove()][array.pop()][array.unshift()]

###### array.last()



返回阵列的最后一个元素。如果阵列为空，则抛出运行时错误。



```
array.last(id) → series <type>
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.last example")
arr = array.new_int(3, 10)
plot(array.last(arr))
```

另见

[array.first()][array.get()]

###### array.lastindexof()



此函数返回值最后一次出现的索引。如果找不到该值，则返回 -1。



```
array.lastindexof(id, value) → series int
```

参数

**id (any array type)** 阵列对象。

**value (series <type of the array's elements>)** 要在阵列中搜索的值。



```
//@version=6
indicator("array.lastindexof example")
a = array.new_float(5,high)
index = array.lastindexof(a, high)
plot(index)
```

返回值

元素的索引。

另见

[array.new_float()][array.set()][array.push()][array.remove()][array.insert()]

###### array.max()

2过载



该函数返回最大值，或给定阵列中的第n个最大值。

语法和重载

[`array.max(id, nth) → series float`][`array.max(id, nth) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**nth (series int)** 返回的第n个最大值，其中0是最大值。可选。默认为零。



```
//@version=6
indicator("array.max")
a = array.from(5, -2, 0, 9, 1)
thirdHighest = array.max(a, 2) // 1
plot(thirdHighest)
```

返回值

阵列中的最大值或第n个最大值。

备注

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.min()][array.sum()]

###### array.median()

2过载



该函数返回阵列元素的中位数。

语法和重载

[`array.median(id) → series float`][`array.median(id) → series int`]

参数

**id (array<int/float>)** 阵列对象。



```
//@version=6
indicator("array.median example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.median(a))
```

返回值

阵列元素的中位数。

备注

如果`id`数组为空，则返回`na`。

另见

[array.median()][array.avg()][array.variance()][array.min()]

###### array.min()

2过载



该函数返回最小值，或给定序列中的第n个最小值。

语法和重载

[`array.min(id, nth) → series float`][`array.min(id, nth) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**nth (series int)** 要返回的第n个最小值，其中0是最小值。可选。默认为零。



```
//@version=6
indicator("array.min")
a = array.from(5, -2, 0, 9, 1)
secondLowest = array.min(a, 1) // 0
plot(secondLowest)
```

返回值

阵列中的最小值或第n个最小值。

备注

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.max()][array.sum()]

###### array.mode()

2过载



该函数返回阵列元素的模式。如果有多个具有相同频率的值，则返回最小值。

语法和重载

[`array.mode(id) → series float`][`array.mode(id) → series int`]

参数

**id (array<int/float>)** 阵列对象。



```
//@version=6
indicator("array.mode example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.mode(a))
```

返回值

`id` 阵列中出现频率最高的值。如果不存在，则返回最小值。

备注

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][ta.mode()][matrix.mode()][array.avg()][array.variance()][array.min()]

###### array.new_bool()



此函数创建一个由bool类型的元素组成的新阵列对象。



```
array.new_bool(size, initial_value) → array<bool>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series bool)** 所有数组元素的初始值。可选。默认值为“false”。



```
//@version=6
indicator("array.new_bool example")
length = 5
a = array.new_bool(length, close > open)
plot(array.get(a, 0) ? close : open)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()][array.sort()]

###### array.new_box()



该函数创建一个新的box类型元素的阵列对象。



```
array.new_box(size, initial_value) → array<box>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series box)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_box example")
boxes = array.new_box()
array.push(boxes, box.new(time, close, time+2, low, xloc=xloc.bar_time))
plot(1)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()]

###### array.new_color()



该函数创建一个由color类型的元素组成的新阵列对象。



```
array.new_color(size, initial_value) → array<color>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series color)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_color example")
length = 5
a = array.new_color(length, color.red)
plot(close, color = array.get(a, 0))
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()][array.sort()]

###### array.new_float()



此函数创建一个新的浮点型元素阵列对象。



```
array.new_float(size, initial_value) → array<float>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series int/float)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_float example")
length = 5
a = array.new_float(length, close)
plot(array.sum(a) / length)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_color()][array.new_bool()][array.get()][array.slice()][array.sort()]

###### array.new_int()



该函数创建一个由int类型的元素组成的新阵列对象。



```
array.new_int(size, initial_value) → array<int>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series int)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_int example")
length = 5
a = array.new_int(length, int(close))
plot(array.sum(a) / length)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()][array.sort()]

###### array.new_label()



该函数创建一个标签类型元素的新阵列对象。



```
array.new_label(size, initial_value) → array<label>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series label)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_label example", overlay = true, max_labels_count = 500)

//@variable The number of labels to show on the chart.
int labelCount = input.int(50, "Labels to show", 1, 500)

//@variable An array of `label` objects.
var array<label> labelArray = array.new_label()

//@variable A `chart.point` for the new label.
labelPoint = chart.point.from_index(bar_index, close)
//@variable The text in the new label.
string labelText = na
//@variable The color of the new label.
color labelColor = na
//@variable The style of the new label.
string labelStyle = na

// Set the label attributes for rising bars.
if close > open
    labelText  := "Rising"
    labelColor := color.green
    labelStyle := label.style_label_down
// Set the label attributes for falling bars.
else if close < open
    labelText  := "Falling"
    labelColor := color.red
    labelStyle := label.style_label_up

// Add a new label to the `labelArray` when the chart bar closed at a new value.
if close != open
    labelArray.push(label.new(labelPoint, labelText, color = labelColor, style = labelStyle))
// Remove the first element and delete its label when the size of the `labelArray` exceeds the `labelCount`.
if labelArray.size() > labelCount
    label.delete(labelArray.shift())
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()]

###### array.new_line()



该函数创建一个线型元素的新阵列对象。



```
array.new_line(size, initial_value) → array<line>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series line)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_line example")
// draw last 15 lines
var a = array.new_line()
array.push(a, line.new(bar_index - 1, close[1], bar_index, close))
if array.size(a) > 15
    ln = array.shift(a)
    line.delete(ln)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()]

###### array.new_linefill()



该函数创建一个新的linefill类型元素的阵列对象。



```
array.new_linefill(size, initial_value) → array<linefill>
```

参数

**size (series int)** 阵列的初始大小。

**initial_value (series linefill)** 所有阵列元素的初始值。

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

###### array.new_string()



该函数创建一个字符串类型元素的新阵列对象。



```
array.new_string(size, initial_value) → array<string>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series string)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new_string example")
length = 5
a = array.new_string(length, "text")
label.new(bar_index, close, array.get(a, 0))
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()]

###### array.new_table()



该函数创建一个表类型元素的新阵列对象。



```
array.new_table(size, initial_value) → array<table>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (series table)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("table array")
tables = array.new_table()
array.push(tables, table.new(position = position.top_left, rows = 1, columns = 2, bgcolor = color.yellow, border_width=1))
plot(1)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

另见

[array.new_float()][array.get()][array.slice()]

###### array.new<type>()



该函数创建一个新的<type>元素阵列对象。



```
array.new<type>(size, initial_value) → array<type>
```

参数

**size (series int)** 序列的初始大小。可选。默认值为0。

**initial_value (<array_type>)** 所有序列元素的初始值。可选。默认值为“na”。



```
//@version=6
indicator("array.new<string> example")
a = array.new<string>(1, "Hello, World!")
label.new(bar_index, close, array.get(a, 0))
```



```
//@version=6
indicator("array.new<color> example")
a = array.new<color>()
array.push(a, color.red)
array.push(a, color.green)
plot(close, color = array.get(a, close > open ? 1 : 0))
```



```
//@version=6
indicator("array.new<float> example")
length = 5
var a = array.new<float>(length, close)
if array.size(a) == length
    array.remove(a, 0)
    array.push(a, close)
plot(array.sum(a) / length, "SMA")
```



```
//@version=6
indicator("array.new<line> example")
// draw last 15 lines
var a = array.new<line>()
array.push(a, line.new(bar_index - 1, close[1], bar_index, close))
if array.size(a) > 15
    ln = array.shift(a)
    line.delete(ln)
```

返回值

可与其他阵列一起使用的阵列对象的ID。*（）函数。

备注

阵列索引从0开始。

如果要初始化一个阵列并同时指定其所有元素，请使用函数array.from。

另见

[array.from()][array.push()][array.get()][array.size()][array.remove()][array.shift()][array.sum()]

###### array.percentile_linear_interpolation()

2过载



返回数组值的指定百分比（百分位数）小于或等于它的值，使用线性插值。

语法和重载

[`array.percentile_linear_interpolation(id, percentage) → series float`][`array.percentile_linear_interpolation(id, percentage) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**percentage (series int/float)** 必须等于或小于返回值的值的百分比。

备注

在统计数据中，百分位数是出现或低于特定分数的排名项目的百分比。该测量表明，标准频率分布中得分的百分比低于要测量的百分位排名。线性插值估计两个等级之间的值。

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.percentile_nearest_rank()

2过载



使用最近秩方法返回指定百分比的数组值（百分位数）小于或等于它的值。

语法和重载

[`array.percentile_nearest_rank(id, percentage) → series float`][`array.percentile_nearest_rank(id, percentage) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**percentage (series int/float)** 必须等于或小于返回值的值的百分比。

备注

在统计数据中，百分位是出现在某个分数或低于某个分数的排名项目的百分比。 此测量显示低于您正在测量的百分排名的标准频率分布中的分数百分比。

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.percentrank()

2过载



返回指定`index`处元素的百分位数排名。

语法和重载

[`array.percentrank(id, index) → series float`][`array.percentrank(id, index) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**index (series int)** 应计算百分位等级的元素的索引。

备注

百分位等级是数组中小于或等于参考值的元素的数量，以百分比表示。

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.pop()



该函数从阵列中删除最后一个元素并返回其值。



```
array.pop(id) → series <type>
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.pop example")
a = array.new_float(5,high)
removedEl = array.pop(a)
plot(array.size(a))
plot(removedEl)
```

返回值

被删除元素的值。

另见

[array.new_float()][array.set()][array.push()][array.remove()][array.insert()][array.shift()]

###### array.push()



该函数将一个值附加到阵列。



```
array.push(id, value) → void
```

参数

**id (any array type)** 阵列对象。

**value (series <type of the array's elements>)** 添加到阵列末尾的元素值。



```
//@version=6
indicator("array.push example")
a = array.new_float(5, 0)
array.push(a, open)
plot(array.get(a, 5))
```

另见

[array.new_float()][array.set()][array.insert()][array.remove()][array.pop()][array.unshift()]

###### array.range()

2过载



该函数返回给定数组的最小值和最大值之间的差。

语法和重载

[`array.range(id) → series float`][`array.range(id) → series int`]

参数

**id (array<int/float>)** 阵列对象。



```
//@version=6
indicator("array.range example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.range(a))
```

返回值

数组中最小值和最大值之间的差。

备注

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.min()][array.max()][array.sum()]

###### array.remove()



该函数通过删除具有指定索引的元素来更改阵列的内容。



```
array.remove(id, index) → series <type>
```

参数

**id (any array type)** 阵列对象。

**index (series int)** 要删除的元素索引。



```
//@version=6
indicator("array.remove example")
a = array.new_float(5,high)
removedEl = array.remove(a, 0)
plot(array.size(a))
plot(removedEl)
```

返回值

被删除元素的值。

备注

如果索引为正数，则函数从数组的开头向前计数到结尾。第一个元素的索引为0，最后一个元素的索引为`array.size() - 1`。如果索引为负数，则函数从数组的结尾向后计数到开头。在这种情况下，最后一个元素的索引为-1，第一个元素的索引为负数`array.size()`。例如，对于包含三个元素的数组，以下所有元素都是`index`参数的有效参数：0、1、2、-1、-2、-3。

另见

[array.new_float()][array.set()][array.push()][array.insert()][array.pop()][array.shift()]

###### array.reverse()



此函数反转阵列。第一个阵列元素变成最后一个，最后一个阵列元素变成第一个。



```
array.reverse(id) → void
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.reverse example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.get(a, 0))
array.reverse(a)
plot(array.get(a, 0))
```

另见

[array.new_float()][array.sort()][array.push()][array.set()][array.avg()]

###### array.set()



该函数将元素的值设置为指定的索引。



```
array.set(id, index, value) → void
```

参数

**id (any array type)** 阵列对象。

**index (series int)** 要修改元素的索引。

**value (series <type of the array's elements>)** 要设置的新值。



```
//@version=6
indicator("array.set example")
a = array.new_float(10)
for i = 0 to 9
    array.set(a, i, close[i`
plot(array.sum(a) / 10)
```

备注

如果索引为正数，则函数从数组的开头向前计数到结尾。第一个元素的索引为0，最后一个元素的索引为`array.size() - 1`。如果索引为负数，则函数从数组的结尾向后计数到开头。在这种情况下，最后一个元素的索引为-1，第一个元素的索引为负数`array.size()`。例如，对于包含三个元素的数组，以下所有元素都是`index`参数的有效参数：0、1、2、-1、-2、-3。

另见

[array.new_float()][array.get()][array.slice()]

###### array.shift()



该函数删除阵列的第一个元素并返回其值。



```
array.shift(id) → series <type>
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.shift example")
a = array.new_float(5,high)
removedEl = array.shift(a)
plot(array.size(a))
plot(removedEl)
```

返回值

被删除元素的值。

另见

[array.unshift()][array.set()][array.push()][array.remove()][array.includes()]

###### array.size()



该函数返回阵列中元素的数量。



```
array.size(id) → series int
```

参数

**id (any array type)** 阵列对象。



```
//@version=6
indicator("array.size example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
// note that changes in slice also modify original array
slice = array.slice(a, 0, 5)
array.push(slice, open)
// size was changed in slice and in original array
plot(array.size(a))
plot(array.size(slice))
```

返回值

阵列中元素的数量。

另见

[array.new_float()][array.sum()][array.slice()][array.sort()]

###### array.slice()



Creates an array representing a slice of an existing array. Setting a slice's element to a new value changes the corresponding element in the original array to that value. Likewise, inserting or removing an element in the slice inserts or removes an element in the original array at the index range covered by the slice.



```
array.slice(id, index_from, index_to) → array<type>
```

参数

**id (any array type)** The reference (ID) of the array from which to create a new slice.

**index_from (series int)** The `id` array index corresponding to the start of the slice.

**index_to (series int)** The `id` array index corresponding to the end of the slice. The index is non-inclusive; the resulting slice contains all the original array's elements from `index_from` to `index_to - 1`.



```
//@version=6
indicator("array.slice example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
// take elements from 0 to 4
// *note that changes in slice also modify original array
slice = array.slice(a, 0, 5)
plot(array.sum(a) / 10)
plot(array.sum(slice) / 5)
```

返回值

The ID of an array representing a slice of the `id` array.

备注

The indices in the resulting slice range from zero to one less than the slice's size. These indices do not directly represent the same element indices as the original array. For example, if the `index_from` value is 5, the slice's element at index 1 refers to the `id` array's element at index 6.

Scripts cannot modify the elements of a historical array. Therefore, they cannot modify historical array slices created by this function. Instead of modifying an array referenced by an ID retrieved with the [[\]] operator, use [array.copy()] to create a shallow copy of the historical array, then modify the copy or a slice of that copy instead.

另见

[array.new_float()][array.get()][array.sort()]

###### array.some()



如果`id`数组中至少有一个元素是`true`，则返回`true`，否则返回`false`。



```
array.some(id) → series bool
```

参数

**id (array<bool>)** 阵列对象。

备注

此函数还适用于[int]和[float]类型的阵列，在这种情况下，零值被视为`false`，所有其它值被视为`true`。

另见

[array.every()][array.get()]

###### array.sort()



该函数对阵列的元素进行排序。



```
array.sort(id, order) → void
```

参数

**id (array<int/float/string>)** 阵列对象。

**order (series sort_order)** 排序顺序：order.ascending（默认）或order.descending。



```
//@version=6
indicator("array.sort example")
a = array.new_float(0,0)
for i = 0 to 5
    array.push(a, high[i`
array.sort(a, order.descending)
if barstate.islast
    label.new(bar_index, close, str.tostring(a))
```

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.sort_indices()



返回一个索引阵列，当用于索引原始阵列时，将按其排序顺序访问其元素。它不会修改原始阵列。



```
array.sort_indices(id, order) → array<int>
```

参数

**id (array<int/float/string>)** 阵列对象。

**order (series sort_order)** 排序顺序：order.ascending 或 order.descending。可选。默认值为 order.ascending。



```
//@version=6
indicator("array.sort_indices")
a = array.from(5, -2, 0, 9, 1)
sortedIndices = array.sort_indices(a) // [1, 2, 4, 0, 3]
indexOfSmallestValue = array.get(sortedIndices, 0) // 1
smallestValue = array.get(a, indexOfSmallestValue) // -2
plot(smallestValue)
```

另见

[array.new_float()][array.insert()][array.slice()][array.reverse()][order.ascending][order.descending]

###### array.standardize()

2过载



该函数返回标准化元素的阵列。

语法和重载

[`array.standardize(id) → array`][`array.standardize(id) → array`]

参数

**id (array<int/float>)** 阵列对象。



```
//@version=6
indicator("array.standardize example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
b = array.standardize(a)
plot(array.min(b))
plot(array.max(b))
```

返回值

标准化元素的阵列。

另见

[array.max()][array.min()][array.mode()][array.avg()][array.variance()][array.stdev()]

###### array.stdev()

2过载



该函数返回阵列元素的标准差。

语法和重载

[`array.stdev(id, biased) → series float`][`array.stdev(id, biased) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**biased (series bool)** 确定应该使用哪个估计。可选。默认值为true。



```
//@version=6
indicator("array.stdev example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.stdev(a))
```

返回值

阵列元素的标准差。

备注

如果`biased`为真，则该函数使用对整个总体的有偏估计进行计算。如果`biased`为假，则使用对样本的无偏估计进行计算。

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.max()][array.min()][array.avg()]

###### array.sum()

2过载



该函数返回阵列元素的总和。

语法和重载

[`array.sum(id) → series float`][`array.sum(id) → series int`]

参数

**id (array<int/float>)** 阵列对象。



```
//@version=6
indicator("array.sum example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.sum(a))
```

返回值

阵列元素的总和。

备注

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.max()][array.min()]

###### array.unshift()



该函数将值插入阵列的初始位置。



```
array.unshift(id, value) → void
```

参数

**id (any array type)** 阵列对象。

**value (series <type of the array's elements>)** 要添加到阵列初始位置的值。



```
//@version=6
indicator("array.unshift example")
a = array.new_float(5, 0)
array.unshift(a, open)
plot(array.get(a, 0))
```

另见

[array.shift()][array.set()][array.insert()][array.remove()][array.indexof()]

###### array.variance()

2过载



该函数返回阵列元素的方差。

语法和重载

[`array.variance(id, biased) → series float`][`array.variance(id, biased) → series int`]

参数

**id (array<int/float>)** 阵列对象。

**biased (series bool)** 确定应该使用哪个估计。可选。默认值为true。



```
//@version=6
indicator("array.variance example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i`
plot(array.variance(a))
```

返回值

阵列元素的方差。

备注

如果`biased`为true，函数将使用对整个总体的有偏估计进行计算，如果为false - 对样本的无偏估计。

如果`id`数组为空，则返回`na`。

另见

[array.new_float()][array.stdev()][array.min()][array.avg()][array.covariance()]

###### barcolor()



设置K线颜色



```
barcolor(color, offset, editable, show_last, title, display) → void
```

参数

**color (series color)** K线颜色。您可以使用如“red”或“＃ff001a”的常量，以及如 'close >= open ? green : red'的复杂表达式。必要参数。

**offset (simple int)** 在k线特定数量上向左或向右移动颜色系列。 默认值为0。

**editable (input bool)** 如果为true，则barcolor样式可在格式对话框中编辑。 默认值为true。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**title (const string)** Barcolor标题。可选参数。

**display (input plot_simple_display)** 控制K线颜色的显示位置。可能的值为：[display.none]、[display.all]。默认为[display.all]。



```
//@version=6
indicator("barcolor example", overlay=true)
barcolor(close < open ? color.black : color.white)
```

另见

[bgcolor()][plot()][fill()]

###### bgcolor()



用指定颜色填充K线的背景



```
bgcolor(color, offset, editable, show_last, title, display, force_overlay) → void
```

参数

**color (series color)** 填充背景的颜色。 您可以使用如“red”或“＃ff001a”的常量以及像 'close >= open ? green : red'的复杂表达式。必要参数。

**offset (simple int)** 在k线特定数量上向左或向右移动颜色系列。 默认值为0。

**editable (input bool)** 如果为true，则bgcolor样式可在格式对话框中编辑。 默认值为true。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**title (const string)** bgcolor的标题。 可选参数。

**display (input plot_simple_display)** 控制背景颜色的显示位置。可能的值为：[display.none]、[display.all]。默认为[display.all]。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("bgcolor example", overlay=true)
bgcolor(close < open ? color.new(color.red,70) : color.new(color.green, 70))
```

另见

[barcolor()][plot()][fill()]

###### bool()

4过载



将`x`值转换为[bool]值。如果`x`是 `na`、`false`或 [int]/[float]值且等于0，则返回`false`。对于所有其他可能的值，则返回`true`。

语法和重载

[`bool(x) → const bool`][`bool(x) → input bool`][`bool(x) → simple bool`][`bool(x) → series bool`]

参数

**x (simple int/float/bool)** 要转换为指定类型的值，通常为`na`。

返回值

转换为bool后参数的值。

另见

[float()][int()][color()][string()][line()][label()]

###### box()



转换na为box。



```
box(x) → series box
```

参数

**x (series box)** 要转换为指定类型的值，通常为`na`。

返回值

转换为box后参数的值。

另见

[float()][int()][bool()][color()][string()][line()][label()]

###### box.copy()



克隆box对象。



```
box.copy(id) → series box
```

参数

**id (series box)** Box对象。



```
//@version=6
indicator('Last 50 bars price ranges', overlay = true)
LOOKBACK = 50
highest = ta.highest(LOOKBACK)
lowest = ta.lowest(LOOKBACK)
if barstate.islastconfirmedhistory
    var BoxLast = box.new(bar_index[LOOKBACK], highest, bar_index, lowest, bgcolor = color.new(color.green, 80))
    var BoxPrev = box.copy(BoxLast)
    box.set_lefttop(BoxPrev, bar_index[LOOKBACK * 2], highest[50`
    box.set_rightbottom(BoxPrev, bar_index[LOOKBACK], lowest[50`
    box.set_bgcolor(BoxPrev, color.new(color.red, 80))
```

另见

[box.new()][box.delete()]

###### box.delete()



删除指定的box对象。如果它已经被删除，则什么都不做。



```
box.delete(id) → void
```

参数

**id (series box)** 要删除的box对象。

另见

[box.new()]

###### box.get_bottom()



返回box底部边框的价格值。



```
box.get_bottom(id) → series float
```

参数

**id (series box)** 一个box对象。

返回值

价格值。

另见

[box.new()][box.set_bottom()]

###### box.get_left()



返回box左边框的K线索引或UNIX时间（取决于用于'xloc'的最后一个值）。



```
box.get_left(id) → series int
```

参数

**id (series box)** 一个box对象。

返回值

K线索引或UNIX时间戳（以毫秒为单位）。

另见

[box.new()][box.set_left()]

###### box.get_right()



返回box右边框的K线索引或UNIX时间（取决于用于'xloc'的最后一个值）。



```
box.get_right(id) → series int
```

参数

**id (series box)** 一个box对象。

返回值

K线索引或UNIX时间戳（以毫秒为单位）。

另见

[box.new()][box.set_right()]

###### box.get_top()



返回box顶部边框的价格值。



```
box.get_top(id) → series float
```

参数

**id (series box)** 一个box对象。

返回值

价格值。

另见

[box.new()][box.set_top()]

###### box.new()

2过载



创建一个新的box对象。

语法和重载

[`box.new(top_left, bottom_right, border_color, border_width, border_style, extend, xloc, bgcolor, text, text_size, text_color, text_halign, text_valign, text_wrap, text_font_family, force_overlay, text_formatting) → series box`][`box.new(left, top, right, bottom, border_color, border_width, border_style, extend, xloc, bgcolor, text, text_size, text_color, text_halign, text_valign, text_wrap, text_font_family, force_overlay, text_formatting) → series box`]

参数

**top_left (chart.point)** 一个[chart.point]对象，指定box的左上角位置。

**bottom_right (chart.point)** 一个[chart.point]对象，指定box的右下角位置。

**border_color (series color)** 四条边框的颜色。可选。默认值为[color.blue]。

**border_width (series int)** 四条边框的宽度，以像素为单位。可选默认值为1像素。

**border_style (series string)** 四个边框的样式。可能的值：[line.style_solid]、[line.style_dotted]、[line.style_dashed]。可选。默认值为[line.style_solid]。

**extend (series string)** 当使用[extend.none]时，水平边框从左边框开始，到右边框结束。使用[extend.left]或[extend.right]，水平边框分别无限延伸到框的左侧或右侧。 使用[extend.both]，水平边框在两侧延伸。可选。默认值为[extend.none]。

**xloc (series string)** 确定“left”和“right”的参数是K线索引还是时间值。如果xloc = [xloc.bar_index]，则参数必须是K线索引。如果xloc = [xloc.bar_time]，则参数必须是UNIX时间。可能的值：[xloc.bar_index]和[xloc.bar_time]。可选。默认值为[xloc.bar_index]。

**bgcolor (series color)** box的背景颜色。可选。默认值为[color.blue]。

**text (series string)** 要在框内显示的文本。可选。默认为空字符串。

**text_size (series int/string)** 可选。框文本大小。大小可以是任意正整数，也可以是`size.*`内置常量字符串之一。常量字符串及其等效整数值为：[size.auto] (0)、[size.tiny] (8)、[size.small] (10)、[size.normal] (14)、[size.large] (20)、[size.huge] (36)。默认值为[size.auto]或0。

**text_color (series color)** 文字的颜色。可选。默认值为[color.black]。

**text_halign (series string)** Box文本的水平对齐方式。可选。默认值为[text.align_center]。 可能的值：[text.align_left]、[text.align_center]、[text.align_right]。

**text_valign (series string)** Box文本的垂直对齐方式。可选。默认值为[text.align_center]。可能的值：[text.align_top]、[text.align_center]、[text.align_bottom]。

**text_wrap (series string)** 可选。是否换行。换行的文本到达框边时会另起一行。低于框底部的换行文本不会显示。未换行的文本会保留在一行上，如果太长则会*显示*超出框的宽度。如果 `text_size` 为0或[text.wrap_auto]，则此设置无效。默认值为[text.wrap_none]。可能的值：[text.wrap_none]、[text.wrap_auto]。

**text_font_family (series string)** 文本的字体系列。可选。默认值为[font.family_default]。可能的值：[font.family_default]、[font.family_monospace]。

**force_overlay (const bool)** 如果是`true`，则绘图将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。

**text_formatting (const text_format)** 显示文本的格式。格式选项支持添加。例如，`text.format_bold + text.format_italic`将使文本同时变为粗体和斜体。可能的值：[text.format_none]、[text.format_bold]、[text.format_italic]。可选。默认值为[text.format_none]。



```
//@version=6
indicator("box.new")
var b = box.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time, border_style=line.style_dashed)
box.set_lefttop(b, time, 100)
box.set_rightbottom(b, time + 60 * 60 * 24, 500)
box.set_bgcolor(b, color.green)
```

返回值

可以在box.set_*()和box.get_*()函数中使用的box对象的ID。

另见

[box.delete()][box.get_left()][box.get_top()][box.get_right()][box.get_bottom()][box.set_top_left_point()][box.set_left()][box.set_top()][box.set_bottom_right_point()][box.set_right()][box.set_bottom()][box.set_border_color()][box.set_bgcolor()][box.set_border_width()][box.set_border_style()][box.set_extend()][box.set_text()][box.set_text_formatting()][box.set_xloc()]

###### box.set_bgcolor()



设置box的背景颜色。



```
box.set_bgcolor(id, color) → void
```

参数

**id (series box)** 一个box对象。

**color (series color)** 新的背景颜色。

另见

[box.new()]

###### box.set_border_color()



设置box的边框颜色。



```
box.set_border_color(id, color) → void
```

参数

**id (series box)** 一个box对象。

**color (series color)** 新的边框颜色。

另见

[box.new()]

###### box.set_border_style()



设置box的边框样式。



```
box.set_border_style(id, style) → void
```

参数

**id (series box)** 一个box对象。

**style (series string)** 新的边框样式。

另见

[box.new()][line.style_solid][line.style_dotted][line.style_dashed]

###### box.set_border_width()



设置box的边框宽度。



```
box.set_border_width(id, width) → void
```

参数

**id (series box)** 一个box对象。

**width (series int)** 四条边框的宽度，以像素为单位。

另见

[box.new()]

###### box.set_bottom()



设置box的底边坐标。



```
box.set_bottom(id, bottom) → void
```

参数

**id (series box)** 一个box对象。

**bottom (series int/float)** 底部边框的价格值。

另见

[box.new()][box.get_bottom()]

###### box.set_bottom_right_point()



设置`id`box的右下角位置为`point`。



```
box.set_bottom_right_point(id, point) → void
```

参数

**id (series box)** 一个[box]对象。

**point (chart.point)** 一个[chart.point]对象。

###### box.set_extend()



设置此box对象边框的扩展类型。 当使用[extend.none]时，水平边框从左边框开始，到右边框结束。使用[extend.left]或[extend.right]，水平边框分别无限地扩展到方框的左侧或右侧。使用[extend.both]，水平边框在两侧扩展。



```
box.set_extend(id, extend) → void
```

参数

**id (series box)** 一个box对象。

**extend (series string)** 新的扩展类型。

另见

[box.new()][extend.none][extend.right][extend.left][extend.both]

###### box.set_left()



设置box的左边坐标。



```
box.set_left(id, left) → void
```

参数

**id (series box)** 一个box对象。

**left (series int)** 左边框的K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象不能在未来绘制超过500根K线。

另见

[box.new()][box.get_left()]

###### box.set_lefttop()



设置box的左边坐标和上边坐标。



```
box.set_lefttop(id, left, top) → void
```

参数

**id (series box)** 一个box对象。

**left (series int)** 左边框的K线索引或K线时间。

**top (series int/float)** 顶部边框的价格值。

另见

[box.new()][box.get_left()][box.get_top()]

###### box.set_right()



设置box的右边坐标。



```
box.set_right(id, right) → void
```

参数

**id (series box)** 一个box对象。

**right (series int)** 右边框的K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象不能在未来绘制超过500根K线。

另见

[box.new()][box.get_right()]

###### box.set_rightbottom()



设置box的右边坐标和底边坐标。



```
box.set_rightbottom(id, right, bottom) → void
```

参数

**id (series box)** 一个box对象。

**right (series int)** 右边框的K线索引或K线时间。

**bottom (series int/float)** 底部边框的价格值。

另见

[box.new()][box.get_right()][box.get_bottom()]

###### box.set_text()



该函数设置框内的文本。



```
box.set_text(id, text) → void
```

参数

**id (series box)** 一个box对象。

**text (series string)** 要在框内显示的文本。

另见

[box.set_text_color()][box.set_text_size()][box.set_text_valign()][box.set_text_halign()][box.set_text_formatting()]

###### box.set_text_color()



该函数设置框内文本的颜色。



```
box.set_text_color(id, text_color) → void
```

参数

**id (series box)** 一个box对象。

**text_color (series color)** 文字颜色。

另见

[box.set_text()][box.set_text_size()][box.set_text_valign()][box.set_text_halign()]

###### box.set_text_font_family()



该函数设置框内文本的字体系列。



```
box.set_text_font_family(id, text_font_family) → void
```

参数

**id (series box)** 一个box对象。

**text_font_family (series string)** 文本的字体系列。可能的值：[font.family_default]、[font.family_monospace]。



```
//@version=6
indicator("Example of setting the box font")
if barstate.islastconfirmedhistory
    b = box.new(bar_index, open-ta.tr, bar_index-50, open-ta.tr*5, text="monospace")
    box.set_text_font_family(b, font.family_monospace)
```

另见

[box.new()][font.family_default][font.family_monospace]

###### box.set_text_formatting()



设置绘图应用于显示文本的格式属性。



```
box.set_text_formatting(id, text_formatting) → void
```

参数

**id (series box)** 一个box对象。

**text_formatting (const text_format)** 显示文本的格式。格式选项支持添加。例如，`text.format_bold + text.format_italic`将使文本同时变为粗体和斜体。可能的值：[text.format_none]、[text.format_bold]、[text.format_italic]。可选。默认值为[text.format_none]。

另见

[box.set_text_color()][box.set_text_size()][box.set_text_valign()][box.set_text_halign()][box.set_text()]

###### box.set_text_halign()



该函数设置框文本的水平对齐方式。



```
box.set_text_halign(id, text_halign) → void
```

参数

**id (series box)** 一个box对象。

**text_halign (series string)** 框文本的水平对齐方式。可能的值：[text.align_left]、[text.align_center]、[text.align_right]。

另见

[box.set_text()][box.set_text_size()][box.set_text_valign()][box.set_text_color()]

###### box.set_text_size()



该函数设置框文本的大小。



```
box.set_text_size(id, text_size) → void
```

参数

**id (series box)** 一个box对象。

**text_size (series int/string)** 框文本大小。大小可以是任意正整数，也可以是`size.*`内置常量字符串之一。常量字符串及其等效整数值为：[size.auto] (0)、[size.tiny] (8)、[size.small] (10)、[size.normal] (14)、[size.large] (20)、[size.huge] (36)。

另见

[box.set_text()][box.set_text_color()][box.set_text_valign()][box.set_text_halign()]

###### box.set_text_valign()



该函数设置框文本的垂直对齐方式。



```
box.set_text_valign(id, text_valign) → void
```

参数

**id (series box)** 一个box对象。

**text_valign (series string)** 框文本的垂直对齐方式。可能的值：[text.align_top]、[text.align_center]、[text.align_bottom]。

另见

[box.set_text()][box.set_text_size()][box.set_text_color()][box.set_text_halign()]

###### box.set_text_wrap()



该函数设置框内文本的换行模式。



```
box.set_text_wrap(id, text_wrap) → void
```

参数

**id (series box)** 一个box对象。

**text_wrap (series string)** 是否换行。换行的文本到达框边时会另起一行。低于框底部的换行文本不会显示。未换行的文本会保留在一行上，如果文本太长，则会*显示*超出框的宽度。如果`text_size`为0或[text.wrap_auto]，则此设置无效。可能的值：[text.wrap_none]、[text.wrap_auto]。

另见

[box.set_text()][box.set_text_size()][box.set_text_valign()][box.set_text_halign()][box.set_text_color()]

###### box.set_top()



设置box的顶边坐标。



```
box.set_top(id, top) → void
```

参数

**id (series box)** 一个box对象。

**top (series int/float)** 顶部边框的价格值。

另见

[box.new()][box.get_top()]

###### box.set_top_left_point()



设置`id`框的左上角位置为`point`。



```
box.set_top_left_point(id, point) → void
```

参数

**id (series box)** 一个[box]对象。

**point (chart.point)** 一个[chart.point]对象。

###### box.set_xloc()



设置[box]的左边框和右边框并更新其`xloc`属性。



```
box.set_xloc(id, left, right, xloc) → void
```

参数

**id (series box)** 要更新的box对象的ID。

**left (series int)** box左边框的K线索引或时间戳。

**right (series int)** box右边框的K线索引或时间戳。

**xloc (series string)** 确定框是否将`left`和`right`参数视为K线索引或时间戳。可能的值：[xloc.bar_index]和[xloc.bar_time]。如果值为[xloc.bar_index]，则参数表示K线索引。如果为[xloc.bar_time]，则参数表示[UNIX timestamps]。

另见

[box.new()][xloc.bar_index][xloc.bar_time]

###### chart.point.copy()



使用指定的`id`创建[chart.point]对象的副本。



```
chart.point.copy(id) → chart.point
```

参数

**id (chart.point)** 一个[chart.point]对象。

###### chart.point.from_index()



返回一个[chart.point]对象，其中`index`作为其x坐标，`price`作为其y坐标。



```
chart.point.from_index(index, price) → chart.point
```

参数

**index (series int)** 点的x坐标，表示为K线索引值。

**price (series int/float)** 点的y坐标。

备注

从此函数返回的[chart.point]实例的`time`字段值将为`na`，这意味着将`xloc`值设置为`xloc.bar_time`的绘图对象将无法使用它们。

###### chart.point.from_time()



返回一个[chart.point]对象，其中`time`作为其x坐标，`price`作为其y坐标。



```
chart.point.from_time(time, price) → chart.point
```

参数

**time (series int)** 点的x坐标，表示为UNIX时间值。

**price (series int/float)** 点的y坐标。

备注

从此函数返回的[chart.point]实例的`index`字段值将为`na`，这意味着将`xloc`值设置为`xloc.bar_index`的绘图对象将无法使用它们。

###### chart.point.new()



使用指定的`time`、`index`和`price`创建新的[chart.point]对象。



```
chart.point.new(time, index, price) → chart.point
```

参数

**time (series int)** 点的x坐标，表示为UNIX时间值。

**index (series int)** 点的x坐标，表示为K线索引值。

**price (series int/float)** 点的y坐标。

备注

绘图对象是否使用点的`time`或`index`字段作为x坐标，取决于返回绘图的函数调用中使用的`xloc`类型。

请务必注意，此函数不会验证`time`和`index`值是否指的是同一根K线。

另见

[polyline.new()]

###### chart.point.now()



返回一个以`price`作为y坐标的[chart.point]对象



```
chart.point.now(price) → chart.point
```

参数

**price (series int/float)** 点的y坐标。可选。默认值为[close]。

备注

从此函数返回的[chart.point]实例记录其执行K线上的`index`和`time`字段的值，使其适合与任何`xloc`类型的绘图对象一起使用。

###### color()

4过载



施放na颜色

语法和重载

[`color(x) → const color`][`color(x) → input color`][`color(x) → simple color`][`color(x) → series color`]

参数

**x (const color)** 要转换为指定类型的值，通常为`na`。

返回值

转换为颜色后参数的值。

另见

[float()][int()][bool()][string()][line()][label()]

###### color.b()

4过载



检索颜色的蓝色调的值。

语法和重载

[`color.b(color) → const float`][`color.b(color) → input float`][`color.b(color) → simple float`][`color.b(color) → series float`]

参数

**color (const color)** 颜色。



```
//@version=6
indicator("color.b", overlay=true)
plot(color.b(color.blue))
```

返回值

颜色的蓝色调的值（0到255）。

###### color.from_gradient()



根据值在bottom_value到top_value范围内的相对位置，该函数返回由bottom_color到top_color定义的渐变的颜色。



```
color.from_gradient(value, bottom_value, top_value, bottom_color, top_color) → series color
```

参数

**value (series int/float)** 计算位置相关颜色的值。

**bottom_value (series int/float)** bottom_color对应的底部位置值。

**top_value (series int/float)** top_color对应的顶部位置值。

**bottom_color (series color)** 底部位置颜色。

**top_color (series color)** 顶部位置颜色。



```
//@version=6
indicator("color.from_gradient", overlay=true)
color1 = color.from_gradient(close, low, high, color.yellow, color.lime)
color2 = color.from_gradient(ta.rsi(close, 7), 0, 100, color.rgb(255, 0, 0), color.rgb(0, 255, 0, 50))
plot(close, color=color1)
plot(ta.rsi(close,7), color=color2)
```

返回值

根据bottom_color到top_color之间的线性渐变计算的颜色。

备注

使用此函数将对脚本“设置/样式”标签页中显示的颜色产生影响。请参阅[用户手册]了解更多信息。

###### color.g()

4过载



检索颜色的绿色调的值。

语法和重载

[`color.g(color) → const float`][`color.g(color) → input float`][`color.g(color) → simple float`][`color.g(color) → series float`]

参数

**color (const color)** 颜色。



```
//@version=6
indicator("color.g", overlay=true)
plot(color.g(color.green))
```

返回值

颜色的绿色调的值（0到255）。

###### color.new()

4过载



功能颜色将指定透明度应用于给定的颜色。

语法和重载

[`color.new(color, transp) → const color`][`color.new(color, transp) → input color`][`color.new(color, transp) → simple color`][`color.new(color, transp) → series color`]

参数

**color (const color)** 应用透明度的颜色。

**transp (const int/float)** 可用的值是从0(不透明)到100(不可见)



```
//@version=6
indicator("color.new", overlay=true)
plot(close, color=color.new(color.red, 50))
```

返回值

有特定透明度的颜色。

备注

使用非常数的参数（例如，“simple”、“input”或“series”）将对脚本“设置/样式”标签页中显示的颜色产生影响。请参阅[用户手册]了解更多信息。

###### color.r()

4过载



检索颜色的红色调的值。

语法和重载

[`color.r(color) → const float`][`color.r(color) → input float`][`color.r(color) → simple float`][`color.r(color) → series float`]

参数

**color (const color)** 颜色。



```
//@version=6
indicator("color.r", overlay=true)
plot(color.r(color.red))
```

返回值

颜色的红色调的值（0到255）。

###### color.rgb()

4过载



使用RGB颜色模型创建带有透明度的新颜色。

语法和重载

[`color.rgb(red, green, blue, transp) → const color`][`color.rgb(red, green, blue, transp) → input color`][`color.rgb(red, green, blue, transp) → simple color`][`color.rgb(red, green, blue, transp) → series color`]

参数

**red (const int/float)** 红色调。可能的值是从0到255。

**green (const int/float)** 绿色调。可能的值是从0到255。

**blue (const int/float)** 蓝色调。可能的值是从0到255。

**transp (const int/float)** 可选。颜色透明。可能的值从0（不透明）到100（透明）。默认值为0。



```
//@version=6
indicator("color.rgb", overlay=true)
plot(close, color=color.rgb(255, 0, 0, 50))
```

返回值

有特定透明度的颜色。

备注

使用非常数的参数（例如，“simple”、“input”或“series”）将对脚本“设置/样式”标签页中显示的颜色产生影响。请参阅[用户手册]了解更多信息。

###### color.t()

4过载



检索颜色的透明度。

语法和重载

[`color.t(color) → const float`][`color.t(color) → input float`][`color.t(color) → simple float`][`color.t(color) → series float`]

参数

**color (const color)** 颜色。



```
//@version=6
indicator("color.t", overlay=true)
plot(color.t(color.new(color.red, 50)))
```

返回值

颜色透明度的值(0-100)。

###### dayofmonth()



根据UNIX时间戳计算指定时区内月份的天数。



```
dayofmonth(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的UNIX时间戳。

**timezone (series string)** 可选。指定返回日期数值的时区。该值可以是采用UTC/GMT时差表示法（例如“UTC-5”）或IANA时区数据库表示法（例如“America/New_York”）的时区字符串。默认值为[syminfo.timezone]。

返回值

计算出的月份日期，以指定的时区表示。

备注

[UNIX时间戳] 表示自1970-01-01 00:00 UTC以来经过的毫秒数。UNIX时间戳的含义不会相对于任何时区变化。UNIX时间戳的含义不会相对于任何时区变化。

另见

[dayofmonth][dayofweek()][weekofyear()][time()][year()][month()][hour()][minute()][second()]

###### dayofweek()



根据UNIX时间戳计算指定时区内一周中的天数。



```
dayofweek(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的UNIX时间戳。

**timezone (series string)** 可选。指定返回日期数值的时区。该值可以是采用UTC/GMT时差表示法（例如“UTC-5”）或IANA时区数据库表示法（例如“America/New_York”）的时区字符串。默认值为[syminfo.timezone]。

返回值

计算出的天数，以指定的时区表示。

备注

[UNIX时间戳] 表示自1970-01-01 00:00 UTC以来经过的毫秒数。UNIX时间戳的含义不会相对于任何时区变化。UNIX时间戳的含义不会相对于任何时区变化。

另见

[dayofweek][dayofmonth()][weekofyear()][time()][year()][month()][hour()][minute()][second()]

###### fill()

3过载



使用提供的颜色填充两个绘图或hline之间的背景。

语法和重载

[`fill(hline1, hline2, color, title, editable, fillgaps, display) → void`][`fill(plot1, plot2, color, title, editable, show_last, fillgaps, display) → void`][`fill(plot1, plot2, top_value, bottom_value, top_color, bottom_color, title, display, fillgaps, editable) → void`]

参数

**hline1 (hline)** 首个hline对象。 必要参数。

**hline2 (hline)** 第二个hline对象。 必要参数。

**color (series color)** 背景填充的颜色。您可以使用像'color=color.red'或'color=#ff001a'这样的常量以及像'color = close >= open ? color.green : color.red'的复杂表达式。可选参数。

**title (const string)** 已创建填充对象的标题。 可选参数。

**editable (input bool)** 如果为true，则填充样式可在格式对话框中编辑。 默认值为true。

**fillgaps (const bool)** 控制空隙的连续填充，即，当plot()调用之一返回na值时。设置为true时，最后的填充将继续填补空隙。默认为false。

**display (input plot_simple_display)** 控制填充的显示位置。可能的值为：[display.none]、[display.all]。默认为[display.all]。

在两条水平线之间填充



```
//@version=6
indicator("Fill between hlines", overlay = false)
h1 = hline(20)
h2 = hline(10)
fill(h1, h2, color = color.new(color.blue, 90))
```

在两个绘图之间填充



```
//@version=6
indicator("Fill between plots", overlay = true)
p1 = plot(open)
p2 = plot(close)
fill(p1, p2, color = color.new(color.green, 90))
```

在两条水平线之间渐变填充



```
//@version=6
indicator("Gradient Fill between hlines", overlay = false)
topVal = input.int(100)
botVal = input.int(0)
topCol = input.color(color.red)
botCol = input.color(color.blue)
topLine = hline(100, color = topCol, linestyle = hline.style_solid)
botLine = hline(0,   color = botCol, linestyle = hline.style_solid)
fill(topLine, botLine, topVal, botVal, topCol, botCol)
```

另见

[plot()][barcolor()][bgcolor()][hline()][color.new()]

###### fixnan()

3过载



对于给定的系列，将NaN值替换为先前的非NaN值。

语法和重载

[`fixnan(source) → series color`][`fixnan(source) → series int`][`fixnan(source) → series float`]

参数

**source (series color)** 用于计算的源。

返回值

无na间隙的系列。

另见

[na()]`na`[nz()]

###### float()

4过载



将na设置为浮动

语法和重载

[`float(x) → const float`][`float(x) → input float`][`float(x) → simple float`][`float(x) → series float`]

参数

**x (const int/float)** 要转换为指定类型的值，通常为`na`。

返回值

转换为float后的参数值。

另见

[int()][bool()][color()][string()][line()][label()]

###### footprint.buy_volume()



Calculates the total "buy" volume for the volume footprint represented by a [footprint] object.



```
footprint.buy_volume(id) → series float
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The total "buy" volume measured by the footprint.

###### footprint.delta()



计算由[footprint]对象表示的成交量轨迹的整体交易量差值。该值表示该轨迹内的总买入量与总卖出量之间的差值。正值表示该轨迹内的总买入量大于总卖出量，负值则表示相反的情况。



```
footprint.delta(id) → series float
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The overall volume delta for the footprint.

###### footprint.get_row_by_price()



分析由[footprint]对象表示的成交量轨迹，查找价格范围包含指定价格水平的行。如果该价格属于其中一行，则函数返回包含该行数据的[volume_row]对象的ID。否则，返回`na`。



```
footprint.get_row_by_price(id, price) → volume_row
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

**price (series int/float)** The price value for which to find the corresponding footprint row.

返回值

表示包含指定价格的轨迹行的[volume_row]对象的 ID，如果价格超出轨迹的价格范围，则为`na`。

###### footprint.poc()



查找由[footprint]对象表示的成交量轨迹的控制点(POC)行，然后返回包含该行数据的[volume_row]对象的ID。



```
footprint.poc(id) → volume_row
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The ID of a [volume_row] object representing the footprint's POC row.

###### footprint.rows()



创建一个数组，其中包含来自[footprint]对象的所有[volume_row] ID。数组中引用的每个[volume_row]对象都包含计算出的成交量轨迹中一行的数据，其中第一个对象代表最低行，最后一个对象代表最高行。



```
footprint.rows(id) → array<volume_row>
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The ID of an array containing a [volume_row] ID for each row in the footprint.

###### footprint.sell_volume()



Calculates the total "sell" volume for the volume footprint represented by a [footprint] object.



```
footprint.sell_volume(id) → series float
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The total "sell" volume measured by the footprint.

###### footprint.total_volume()



Calculates the sum of the total "buy" volume and "sell" volume for the volume footprint represented by a [footprint] object.



```
footprint.total_volume(id) → series float
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The total volume measured by the footprint.

###### footprint.vah()



查找由[footprint]对象表示的成交量轨迹的值区域高(VAH)行，然后返回包含该行数据的[volume_row]对象的ID。



```
footprint.vah(id) → volume_row
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The ID of a [volume_row] object representing the footprint's VAH row.

###### footprint.val()



查找由[footprint]对象表示的成交量轨迹的低值区域(VAL)行，然后返回包含该行数据的[volume_row]对象的ID。



```
footprint.val(id) → volume_row
```

参数

**id (footprint)** The reference (ID) of the [footprint] object to analyze.

返回值

The ID of a [volume_row] object representing the footprint's VAL row.

###### hline()



在给定的固定价格水平上呈现水平线。



```
hline(price, title, color, linestyle, linewidth, editable, display) → hline
```

参数

**price (input int/float)** 对象将呈现的价格值。必要参数。

**title (const string)** 对象的标题

**color (input color)** 渲染线的颜色。 必须是常量(非表达式)。 可选参数。

**linestyle (input hline_style)** 渲染线的样式。 可能的值有：[hline.style_solid]，[hline.style_dotted]，[hline.style_dashed]。 可选参数。

**linewidth (input int)** 渲染线的宽度。默认值为1。

**editable (input bool)** 如果为true，则hline样式可在格式对话框中编辑。 默认值为true。

**display (input plot_simple_display)** 控制水平线的显示位置。可能的值为：[display.none]、[display.all]。默认为[display.all]。



```
//@version=6
indicator("input.hline", overlay=true)
hline(3.14, title='Pi', color=color.blue, linestyle=hline.style_dotted, linewidth=2)

// You may fill the background between any two hlines with a fill() function:
h1 = hline(20)
h2 = hline(10)
fill(h1, h2, color=color.new(color.green, 90))
```

返回值

可用于[fill()]的hline对象。

另见

[fill()]

###### hour()





```
hour(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的unix时间。

**timezone (series string)** 允许将返回值调整为以UTC/GMT表示法（例如，“UTC-5”、“GMT+0530”）或IANA时区数据库名称（例如，“America/New_York”）指定的时区。可选。默认值为[syminfo.timezone]。

返回值

提供UNIX时间的小时(交换时区)。

备注

UNIX时间是自1970年1月1日UTC 00:00:00起已经过去的毫秒数。

另见

[hour][time()][year()][month()][dayofmonth()][dayofweek()][minute()][second()]

###### indicator()



用于将脚本标识为指标并设置特定脚本范围属性的声明语句。



```
indicator(title, shorttitle, overlay, format, precision, scale, max_bars_back, timeframe, timeframe_gaps, explicit_plot_zorder, max_lines_count, max_labels_count, max_boxes_count, calc_bars_count, max_polylines_count, dynamic_requests, behind_chart) → void
```

参数

**title (const string)** 表示脚本标题的字符串。如果声明语句不包含`shorttitle`参数，则脚本会在所有可能的位置显示该字符串的文本。此外，[“发布脚本”]窗口会将该文本用作脚本发布的默认标题。

**shorttitle (const string)** 可选。此字符串表示脚本在图表上的显示名称。如果指定且不为空，则该值将替换图表中大多数位置，包括“设置”窗口、脚本状态栏、“数据”窗口和“创建警报”对话框的`title`字符串。否则，`title`字符串将显示为脚本在所有位置的标题。默认值为空字符串。

**overlay (const bool)** 可选。如果为`true`，则当用户直接将脚本添加到图表时，脚本的可视化效果将显示在主图表窗格中；如果用户将其应用到另一个脚本，则脚本的可视化效果将显示在另一个脚本的窗格中。如果为`false`，则脚本的可视化效果将显示在单独的窗格中。但是，如果创建[视觉]的函数调用包含`force_overlay = true`，则其输出始终显示在主图表窗格中，即使脚本位于单独的窗格中。对此参数的更改仅在用户再次将脚本添加到图表后生效。此外，如果用户通过在脚本的“更多”菜单中选择“移动到”选项将脚本移动到另一个窗格，则在对源代码进行任何更新后，脚本不会移回其原始窗格。默认值为`false`。

**format (const string)** 可选。指定脚本绘制值的格式。可选值为[format.inherit]、[format.price]、[format.volume]和[format.percent]。默认值为[format.inherit]。

**precision (const int)** 可选。指定脚本绘制的数字的小数位数。该值必须是0到16之间的整数。如果指定了此参数，且`format`参数为[format.inherit]，则脚本将使用[format.price]作为格式化选项。如果`format`参数为{format.volume}，则脚本将忽略`precision`值，因为[format.volume]指定的小数精度规则会覆盖其他精度设置。默认情况下，脚本会继承图表的精度设置。

**scale (const scale_type)** 可选。用于确定脚本价格坐标的位置以及脚本视觉元素的缩放行为。可选值为[scale.right]、[scale.left]和[scale.none]。如果指定此参数，且脚本叠加在主图表窗格或其他脚本的窗格上，则脚本会独立缩放其视觉元素以适应窗格的视觉空间。如果脚本与主图表或其他脚本位于同一窗格中，则[scale.right]或[scale.left]会在该窗格的左侧或右侧为脚本添加一个单独的价格坐标。如果脚本位于单独的窗格中，则这两个参数都会将该窗格的价格坐标放置在左侧或右侧，而不会添加新的坐标。如果参数为[scale.none]，仅当 `overlay`参数为`true` 时有效，则脚本会将绘制的数字直接显示在现有窗格的坐标上；如果用户将其移动到新窗格，则会在新价格坐标上显示数值。对参数的更改仅在用户再次将脚本添加到图表后生效。如果未指定，则脚本使用其所在窗格的主价格坐标，并且如果其叠加在现有窗格上，则不会单独缩放其视觉效果。

**max_bars_back (const int)** Optional. Sets the minimum length of all the script's historical buffers, which determine the number of bars back that the script can reference for each series using the [[\]] operator or the functions that retrieve history internally. The value must be an integer from 0 to 5000. By default, Pine's runtime system automatically calculates appropriate historical buffer sizes for each series while loading a script. Manually setting buffer sizes is necessary only in rare cases where automatic size detection fails. See the [Historical buffers] section of our User Manual for advanced details.

**timeframe (const string)** 可选。一个有效的[时间周期字符串]，用于确定脚本计算时使用的主要时间周期。如果指定，脚本会自动在“设置/输入”标签页中添加一个“时间周期”输入框。该输入框在标签页显示的默认值与指定的参数时间周期相同。如果值为空字符串或未指定，则脚本使用与图表相同的时间周期。仅当脚本不使用[绘图类型]或[alert()](#fun_alert)函数调用时，才允许为此参数指定参数。

**timeframe_gaps (const bool)** 可选。控制当`timeframe`值代表的时间周期高于图表的时间周期时，脚本如何显示绘制的值。仅当调用包含`timeframe`参数时，才允许为此参数指定参数。如果指定，脚本会在“设置/输入”选项卡中生成的“时间周期”输入框下方添加一个“等待时间周期收盘”输入框，用户可以在此处更改设置。如果为`true`，则指标仅在有新的更高时间周期数据的图表K线显示值，并在所有其他K线显示`na`。如果为`false`，则指标在所有没有新数据的图表K线显示上次检索到的值。默认值为`true`。

**explicit_plot_zorder (const bool)** 可选。指定脚本使用哪些规则来确定图表上`plot*()`调用生成的图形、[hline()]调用生成的水平线以及[fill()]调用生成的填充线的视觉顺序。如果为`true`，则指标会按照代码中函数调用的顺序显示这些视觉元素。如果为`false`，则脚本使用默认的[z-index]规则来确定视觉元素的顺序。默认值为`false`。

**max_lines_count (const int)** 可选。此参数决定脚本可访问的[line]对象的最大数量。当线条数量超过此限制时，系统会自动删除最旧的[line]对象。此参数指定的限制为近似值；脚本实际显示的图形数量可能超过指定值。默认值约为50行。

**max_labels_count (const int)** 可选。确定脚本可用的[label]对象的最大数量。当标签数量超过此限制时，系统会自动删除最旧的[label]对象。此参数指定的限制为近似值；脚本可能会显示比指定数量更多的图形。默认值约为50个标签。

**max_boxes_count (const int)** 可选。此参数决定脚本可访问的[box]对象的最大数量。当方框数量超过此限制时，系统会自动删除最旧的[box]对象。此参数指定的限制为近似值；脚本实际显示的图形数量可能超过指定数量。默认值约为50个方框。

**calc_bars_count (const int)** 可选。决定脚本可以使用多少根最近的历史K线。如果指定，脚本会自动在“设置/输入”标签页中添加一个“计算K线”输入项。如果该值为正数且小于数据集中的历史K线数量，则脚本会从最新K线之前相应数量的K线开始计算。如果该值为0，则脚本会从数据集的第一根K线开始计算。默认值为0。

**max_polylines_count (const int)** 可选。确定脚本可用的[polyline]对象的最大数量。当多段线数量超过此限制时，系统会自动删除最旧的[polyline]对象。此参数指定的限制为近似值；脚本可能会显示比指定数量更多的绘图。默认值约为50条折线。

**dynamic_requests (const bool)** 可选。指定脚本是否可以使用动态`request.*()`函数调用。动态`request.*()`调用允许在条件结构（例如[if]）、循环（例如[for]）和导出函数的局部作用域内使用。此外，此类调用允许为多个参数使用“series”参数，而这些参数通常需要使用“simple”或更弱的限定符。有关更多信息，请参阅用户手册中的[动态请求]部分。默认值为`true`。

**behind_chart (const bool)** 可选。控制所有绘图和图形是显示在图表显示下方（如果为`true`）还是上方（如果为`false`）。此参数仅在`overlay`参数为`true`时生效。对该参数的更改仅在用户再次将脚本添加到图表后才会生效。默认值为`true`。



```
//@version=6
indicator("My script", shorttitle="Script")
plot(close)
```

备注

每个指标脚本的代码中必须包含一个[indicator()]语句。

另见

[strategy()][library()]

###### input()

6过载



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数自动检测用于“defval”的参数类型并使用相应的输入插件。

语法和重载

[`input(defval, title, tooltip, inline, group, display, active) → input color`][`input(defval, title, tooltip, inline, group, display, active) → input string`][`input(defval, title, tooltip, inline, group, display, active) → input int`][`input(defval, title, tooltip, inline, group, display, active) → input float`][`input(defval, title, inline, group, tooltip, display, active) → series float`][`input(defval, title, tooltip, inline, group, display, active) → input bool`]

参数

**defval (const int/float/bool/string/color or source-type built-ins)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，脚本用户可以从中更改它。源类型内置函数是指定计算源的内置系列浮点变量：`close`、`hlc3` 等。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值取决于传递给`defval`的值的类型：[display.none]表示[bool]和[color]值，[display.all]表示其它所有值。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input", overlay=true)
i_switch = input(true, "On/Off")
plot(i_switch ? open : na)

i_len = input(7, "Length")
i_src = input(close, "Source")
plot(ta.sma(i_src, i_len))

i_border = input(142.50, "Price Border")
hline(i_border)
bgcolor(close > i_border ? color.green : color.red)

i_col = input(color.red, "Plot Color")
plot(close, color=i_col)

i_text = input("Hello!", "Message")
l = label.new(bar_index, high, text=i_text)
label.delete(l[1`
```

返回值

输入变量值

备注

[input()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.color()][input.int()][input.float()][input.string()][input.symbol()][input.timeframe()][input.text_area()][input.session()][input.source()][input.time()]

###### input.bool()



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数为脚本的输入添加复选标记。



```
input.bool(defval, title, tooltip, inline, group, confirm, display, active) → input bool
```

参数

**defval (const bool)** 确定脚本的“设置/输入”标签页中建议的输入变量默认值，用户可以从中更改它。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.none]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.bool", overlay=true)
i_switch = input.bool(true, "On/Off")
plot(i_switch ? open : na)
```

返回值

输入变量值

备注

[input.bool()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.color()



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数添加了一个颜色选择器，允许用户从调色板或十六进制值中选择颜色和透明度。



```
input.color(defval, title, tooltip, inline, group, confirm, display, active) → input color
```

参数

**defval (const color)** 确定脚本的“设置/输入”标签页中建议的输入变量默认值，用户可以从中更改它。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.none]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.color", overlay=true)
i_col = input.color(color.red, "Plot Color")
plot(close, color=i_col)
```

返回值

输入变量值

备注

[input.color()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.session()][input.source()][input.time()][input()]

###### input.enum()



向脚本设置的“输入”标签页添加输入，以便您为脚本用户提供配置选项。此函数会根据传递给其`defval` 和 `options`参数的[enum]字段添加一个下拉列表，其中包含选项。

结果下拉列表中每个选项的文本对应于所包含字段的标题。如果枚举声明中未指定字段的标题，则其标题是其名称的字符串表示形式。



```
input.enum(defval, title, options, tooltip, inline, group, confirm, display, active) → input enum
```

参数

**defval (const enum)** 确定输入的默认值，用户可以在脚本的“设置/输入”标签页中更改该值。当`options`参数具有指定的枚举字段元组时，该元组必须包含`defval`。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**options (tuple of enum fields: [enumName.field1, enumName.field2, ...`** 可供选择的选项列表。可选。默认情况下，所有枚举字段的标题都在下拉列表中可用。将元组作为`options`参数传递会将列表限制为仅包含的字段。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果`true`，则在将指标添加到图表之前，将要求用户确认输入值。默认值为`false`。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("Session highlight", overlay = true)

//@enum        Contains fields with popular timezones as titles.
//@field exch  Has an empty string as the title to represent the chart timezone.
enum tz
    utc  = "UTC"
    exch = ""
    ny   = "America/New_York"
    chi  = "America/Chicago"
    lon  = "Europe/London"
    tok  = "Asia/Tokyo"

//@variable The session string.
selectedSession = input.session("1200-1500", "Session")
//@variable The selected timezone. The input's dropdown contains the fields in the `tz` enum.
selectedTimezone = input.enum(tz.utc, "Session Timezone")

//@variable Is `true` if the current bar's time is in the specified session.
bool inSession = false
if not na(time("", selectedSession, str.tostring(selectedTimezone)))
    inSession := true

// Highlight the background when `inSession` is `true`.
bgcolor(inSession ? color.new(color.green, 90) : na, title = "Active session highlight")
```

返回值

输入变量值

备注

`defval`和`options`参数中包含的所有字段必须属于同一枚举。

另见

[input.text_area()][input.bool()][input.int()][input.float()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.float()

2过载



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数将浮点输入字段添加到脚本的输入中。

语法和重载

[`input.float(defval, title, options, tooltip, inline, group, confirm, display, active) → input float`][`input.float(defval, title, minval, maxval, step, tooltip, inline, group, confirm, display, active) → input float`]

参数

**defval (const int/float)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，脚本用户可以从中更改它。当值列表与 `options` 参数一起使用时，该值必须是其中之一。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**options (tuple of const int/float values: [val1, val2, ...`** 从下拉菜单中选择的选项列表，以逗号分隔并用方括号括起来：[val1, val2, ...]。使用该参数时，不能使用`minval`、`maxval`和`step`参数。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.float", overlay=true)
i_angle1 = input.float(0.5, "Sin Angle", minval=-3.14, maxval=3.14, step=0.02)
plot(math.sin(i_angle1) > 0 ? close : open, "sin", color=color.green)

i_angle2 = input.float(0, "Cos Angle", options=[-3.14, -1.57, 0, 1.57, 3.14`
plot(math.cos(i_angle2) > 0 ? close : open, "cos", color=color.red)
```

返回值

输入变量值

备注

[input.float()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.int()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.int()

2过载



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数将整数输入字段添加到脚本的输入中。

语法和重载

[`input.int(defval, title, options, tooltip, inline, group, confirm, display, active) → input int`][`input.int(defval, title, minval, maxval, step, tooltip, inline, group, confirm, display, active) → input int`]

参数

**defval (const int)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，脚本用户可以从中更改它。当值列表与 `options` 参数一起使用时，该值必须是其中之一。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**options (tuple of const int values: [val1, val2, ...`** 从下拉菜单中选择的选项列表，以逗号分隔并用方括号括起来：[val1, val2, ...]。使用该参数时，不能使用`minval`、`maxval`和`step`参数。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.int", overlay=true)
i_len1 = input.int(10, "Length 1", minval=5, maxval=21, step=1)
plot(ta.sma(close, i_len1))

i_len2 = input.int(10, "Length 2", options=[5, 10, 21`
plot(ta.sma(close, i_len2))
```

返回值

输入变量值

备注

[input.int()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.float()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.price()



在脚本的“设置/输入”标签页中添加价格输入。用户可以在设置中更改价格，也可以通过选择指标并拖动价格线来更改价格。



```
input.price(defval, title, tooltip, inline, group, confirm, display, active) → input float
```

参数

**defval (const int/float)** 确定脚本的“设置/输入”标签页中建议的输入变量默认值，用户可以从中更改它。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 可选。如果`true`，则脚本通过单击图表上的点来提示用户设置输入的初始值。如果其他类型的输入需要确认，则“确认输入”对话框还显示该输入的字段，可以在脚本开始运行之前对值的最终调整。默认值为`false`。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.price", overlay=true)
price1 = input.price(title="Date", defval=42)
plot(price1)

price2 = input.price(54, title="Date")
plot(price2)
```

返回值

输入变量值

备注

用户可以通过在“设置/输入”标签页中指定新值，或者通过在图表上移动输入标记来更改输入的值。另外，他们可以从脚本的“更多”菜单中选择“重置点”，并通过单击图表上的点来设置新的输入值。

如果[input.time()]和[input.price()]函数在脚本中呼叫共享唯一`inline`参数，并具有匹配的`group`参数，则这些调用在图表上创建一个单个交互式点标记。用户可以移动该标记以同时调整输入时间和价格值。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.resolution()][input.session()][input.source()][input.color()][input()]

###### input.session()



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数添加两个下拉菜单，允许用户使用交易时段选择器指定交易时段的开始和结束，并将结果作为字符串返回。



```
input.session(defval, title, options, tooltip, inline, group, confirm, display, active) → input string
```

参数

**defval (const string)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，用户可以从中更改它。当值列表与`options`参数一起使用时，该值必须是其中之一。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**options (tuple of const string values: [val1, val2, ...`** 可供选择的选项列表。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.session", overlay=true)
i_sess = input.session("1300-1700", "Session", options=["0930-1600", "1300-1700", "1700-2100"`
t = time(timeframe.period, i_sess)
bgcolor(time == t ? color.green : na)
```

返回值

输入变量值

备注

[input.session()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.source()][input.color()][input.time()][input()]

###### input.source()



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此功能添加了一个下拉菜单，允许用户选择计算源，例如[close]、[hl2]等。如果脚本只包含一个input.source()调用，用户还可以选择图表上另一个指标的输出作为源。



```
input.source(defval, title, tooltip, inline, group, display, active, confirm) → series float
```

参数

**defval (open/high/low/close/hl2/hlc3/ohlc4/hlcc4)** 确定脚本的“设置/输入”标签页中建议的输入变量默认值，用户可以从中更改它。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。



```
//@version=6
indicator("input.source", overlay=true)
i_src = input.source(close, "Source")
plot(i_src)
```

返回值

输入变量值

备注

[input.source()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.session()][input.color()][input.time()][input()]

###### input.string()



将input添加到脚本设置的输入选项卡，它允许您向脚本用户提供配置选项。此函数将字符串输入字段添加到脚本的输入中。



```
input.string(defval, title, options, tooltip, inline, group, confirm, display, active) → input string
```

参数

**defval (const string)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，用户可以从中更改它。当值列表与`options`参数一起使用时，该值必须是其中之一。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**options (tuple of const string values: [val1, val2, ...`** 可供选择的选项列表。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.string", overlay=true)
i_text = input.string("Hello!", "Message")
l = label.new(bar_index, high, i_text)
label.delete(l[1`
```

返回值

输入变量值

备注

[input.string()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.text_area()][input.bool()][input.int()][input.float()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.symbol()



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数添加一个字段，允许用户使用商品并返回搜索选择特定商品，并将该商品与其交易所前缀配对，作为字符串。



```
input.symbol(defval, title, tooltip, inline, group, confirm, display, active) → input string
```

参数

**defval (const string)** 确定脚本的“设置/输入”标签页中建议的输入变量默认值，用户可以从中更改它。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.symbol", overlay=true)
i_sym = input.symbol("DELL", "Symbol")
s = request.security(i_sym, 'D', close)
plot(s)
```

返回值

输入变量值

备注

[input.symbol()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.text_area()



将输入添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数为多行文本输入添加一个字段。



```
input.text_area(defval, title, tooltip, group, confirm, display, active) → input string
```

参数

**defval (const string)** 确定脚本的“设置/输入”标签页中建议的输入变量默认值，用户可以从中更改它。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.none]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.text_area")
i_text = input.text_area(defval = "Hello \nWorld!", title = "Message")
plot(close)
```

返回值

输入变量值

备注

[input.text_area()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.string()][input.bool()][input.int()][input.float()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input.time()][input()]

###### input.time()



在同一行上的脚本的“设置/输入”标签页中添加两个输入：一个日期，一个时间为时间。用户可以在设置中更改价格或选择指标并拖动价格线。该功能以UNIX格式返回日期/时间值。



```
input.time(defval, title, tooltip, inline, group, confirm, display, active) → input int
```

参数

**defval (const int)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，用户可以从中更改它。该值可以是[timestamp()]函数，但前提是它使用const字符串格式的日期参数。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 可选。如果`true`，则脚本通过单击图表上的点来提示用户设置输入的初始值。如果其他类型的输入需要确认，则“确认输入”对话框还显示该输入的字段，可以在脚本开始运行之前对值的最终调整。默认值为`false`。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.none]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.time", overlay=true)
i_date = input.time(timestamp("20 Jul 2021 00:00 +0300"), "Date")
l = label.new(i_date, high, "Date", xloc=xloc.bar_time)
label.delete(l[1`
```

返回值

输入变量值

备注

用户可以通过在“设置/输入”标签页中指定新值，或者通过在图表上移动输入标记来更改输入的值。另外，他们可以从脚本的“更多”菜单中选择“重置点”，并通过单击图表上的点来设置新的输入值。

如果[input.time()]和[input.price()]函数在脚本中呼叫共享唯一`inline`参数，并具有匹配的`group`参数，则这些调用在图表上创建一个单个交互式点标记。用户可以移动该标记以同时调整输入时间和价格值。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.timeframe()][input.session()][input.source()][input.color()][input()]

###### input.timeframe()



将input添加到脚本设置的输入标签页，它允许您向脚本用户提供配置选项。此函数添加一个下拉列表，允许用户通过时间周期选择器选择特定时间周期并将其作为字符串返回。选择器包括用户可能使用图表的时间周期下拉菜单添加的自定义时间周期。



```
input.timeframe(defval, title, options, tooltip, inline, group, confirm, display, active) → input string
```

参数

**defval (const string)** 确定脚本的“设置/输入”标签页中建议的输入变量的默认值，用户可以从中更改它。当值列表与`options`参数一起使用时，该值必须是其中之一。

**title (const string)** 输入的标题。如果未指定，则将变量名用作输入的标题。如果指定了标题，但标题为空，则名称将为空字符串。

**options (tuple of const string values: [val1, val2, ...`** 可供选择的选项列表。

**tooltip (const string)** 此字符串将在鼠标悬停在工具提示图标上时显示给用户。

**inline (const string)** 在一行中使用相同的参数合并所有输入调用。不显示用作参数的字符串。它仅用于辨识属于同一行的输入。

**group (const string)** 使用相同的组参数字符串在所有输入上方创建标头。该字符串也用作标头的文本。

**confirm (const bool)** 如果为true，则在将指标添加到图表之前，将要求用户确认输入值。默认值为false。

**display (const plot_display)** 控制脚本在脚本设置之外的位置显示输入信息。此选项允许用户从脚本的状态行或数据窗口中删除特定输入，以确保仅显示最必要的输入。可能的值：[display.none]、[display.data_window]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**active (input bool)** 可选。指定用户是否可以在脚本的“设置/输入”标签页中更改输入的值。脚本可以使用此参数根据其他输入的值设置输入的状态。如果为`true`，则用户可以更改输入的值。如果为`false`，则输入将灰显，用户无法更改其值。默认值为`true`。



```
//@version=6
indicator("input.timeframe", overlay=true)
i_res = input.timeframe('D', "Resolution", options=['D', 'W', 'M'`
s = request.security("AAPL", i_res, close)
plot(s)
```

返回值

输入变量值

备注

[input.timeframe()]函数的结果总是应该分配给一个变量，见上面的。

另见

[input.bool()][input.int()][input.float()][input.string()][input.text_area()][input.symbol()][input.session()][input.source()][input.color()][input.time()][input()]

###### int()

4过载



转换na或将float值截断为int

语法和重载

[`int(x) → const int`][`int(x) → input int`][`int(x) → simple int`][`int(x) → series int`]

参数

**x (const int/float)** 要转换为指定类型的值，通常为`na`。

返回值

转换为int后的参数值。

另见

[float()][bool()][color()][string()][line()][label()]

###### label()



转换na称label



```
label(x) → series label
```

参数

**x (series label)** 要转换为指定类型的值，通常为`na`。

返回值

转换为标签后参数的值。

另见

[float()][int()][bool()][color()][string()][line()]

###### label.copy()



克隆标签对象。



```
label.copy(id) → series label
```

参数

**id (series label)** 标记对象。



```
//@version=6
indicator('Last 100 bars highest/lowest', overlay = true)
LOOKBACK = 100
highest = ta.highest(LOOKBACK)
highestBars = ta.highestbars(LOOKBACK)
lowest = ta.lowest(LOOKBACK)
lowestBars = ta.lowestbars(LOOKBACK)
if barstate.islastconfirmedhistory
    var labelHigh = label.new(bar_index + highestBars, highest, str.tostring(highest), color = color.green)
    var labelLow = label.copy(labelHigh)
    label.set_xy(labelLow, bar_index + lowestBars, lowest)
    label.set_text(labelLow, str.tostring(lowest))
    label.set_color(labelLow, color.red)
    label.set_style(labelLow, label.style_label_up)
```

返回值

可以传递给label.setXXX和label.getXXX函数的新标签ID对象。

另见

[label.new()][label.delete()]

###### label.delete()



删除指定的标签对象。 如果它已被删除，则不执行任何操作。



```
label.delete(id) → void
```

参数

**id (series label)** 要删除的标签对象。

另见

[label.new()]

###### label.get_text()



返回此标签对象的文本。



```
label.get_text(id) → series string
```

参数

**id (series label)** 标记对象。



```
//@version=6
indicator("label.get_text")
my_label = label.new(time, open, text="Open bar text", xloc=xloc.bar_time)
a = label.get_text(my_label)
label.new(time, close, text = a + " new", xloc=xloc.bar_time)
```

返回值

包含此标签文本的String对象。

另见

[label.new()]

###### label.get_x()



返回此标签位置的UNIX时间或K线索引（取决于最后的xloc值集）



```
label.get_x(id) → series int
```

参数

**id (series label)** 标记对象。



```
//@version=6
indicator("label.get_x")
my_label = label.new(time, open, text="Open bar text", xloc=xloc.bar_time)
a = label.get_x(my_label)
plot(time - label.get_x(my_label)) //draws zero plot
```

返回值

UNIX时间戳（以毫秒为单位）或K线索引

另见

[label.new()]

###### label.get_y()



返回此标签位置的价格。



```
label.get_y(id) → series float
```

参数

**id (series label)** 标记对象。

返回值

表示价格的浮点值

另见

[label.new()]

###### label.new()

2过载



创建新标签对象。

语法和重载

[`label.new(point, text, xloc, yloc, color, style, textcolor, size, textalign, tooltip, text_font_family, force_overlay, text_formatting) → series label`][`label.new(x, y, text, xloc, yloc, color, style, textcolor, size, textalign, tooltip, text_font_family, force_overlay, text_formatting) → series label`]

参数

**point (chart.point)** 指定标签位置的[chart.point]对象。

**text (series string)** 标签文字。默认为空字符串。

**xloc (series string)** 请参阅**x**参数的说明。可能的值：[xloc.bar_index]和[xloc.bar_time]。默认为[xloc.bar_index]。

**yloc (series string)** 可能的值为[yloc.price]、[yloc.abovebar]、[yloc.belowbar]。如果yloc=[yloc.price]，则**y**参数指定标签位置的价格。如果yloc=[yloc.abovebar]，则标签位于K线上方。如果yloc=[yloc.belowbar]，则标签位于K线下方。默认为[yloc.price]。

**color (series color)** 标签边框和箭头的颜色

**style (series string)** 标签样式。可能的值：[label.style_none]、[label.style_xcross]、[label.style_cross]、[label.style_triangleup]、[label.style_triangledown]、[label.style_flag]、[label.style_circle]、[label.style_arrowup]、[label.style_arrowdown]、[label.style_label_up]、[label.style_label_down]、[label.style_label_left]、[label.style_label_right]、[label.style_label_lower_left]、[label.style_label_lower_right]、[label.style_label_upper_left]、[label.style_label_upper_right]、[label.style_label_center]、[label.style_square]、[label.style_diamond]、[label.style_text_outline]。 默认为[label.style_label_down]。

**textcolor (series color)** 文字颜色。

**size (series int/string)** 可选。标签的大小。接受正的[int]值或内置的`size.*`常量之一。常量及其等效数字大小为：[size.auto] (0)、[size.tiny] (~7)、[size.small] (~10)、[size.normal] (12)、[size.large] (18)、[size.huge] (24)。默认值为[size.normal]，表示数字大小为12。

**textalign (series string)** 标签文本对齐。可能的值：[text.align_left]、[text.align_center]、[text.align_right]。默认值为[text.align_center]。

**tooltip (series string)** 将鼠标悬停以查看工具提示标签。

**text_font_family (series string)** 文本的字体系列。可选。默认值为[font.family_default]。可能的值：[font.family_default]、[font.family_monospace]。

**force_overlay (const bool)** 如果是`true`，则绘图将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。

**text_formatting (const text_format)** 显示文本的格式。格式选项支持添加。例如，`text.format_bold + text.format_italic`将使文本同时变为粗体和斜体。可能的值：[text.format_none]、[text.format_bold]、[text.format_italic]。可选。默认值为[text.format_none]。



```
//@version=6
indicator("label.new")
var label1 = label.new(bar_index, low, text="Hello, world!", style=label.style_circle)
label.set_x(label1, 0)
label.set_xloc(label1, time, xloc.bar_time)
label.set_color(label1, color.red)
label.set_size(label1, size.large)
```

返回值

标签ID对象，可以传递给label.setXXX和label.getXXX函数。

另见

[label.delete()][label.set_x()][label.set_y()][label.set_xy()][label.set_xloc()][label.set_yloc()][label.set_color()][label.set_textcolor()][label.set_style()][label.set_size()][label.set_textalign()][label.set_tooltip()][label.set_text()][label.set_text_formatting()]

###### label.set_color()



设置标签边框和箭头颜色。



```
label.set_color(id, color) → void
```

参数

**id (series label)** 标记对象。

**color (series color)** 新标签边框和箭头颜色。

另见

[label.new()]

###### label.set_point()



设置`id`标签的位置为`point`。



```
label.set_point(id, point) → void
```

参数

**id (series label)** 一个[label]对象。

**point (chart.point)** 一个[chart.point]对象。

###### label.set_size()



设置指定标签对象的箭头和文本大小。



```
label.set_size(id, size) → void
```

参数

**id (series label)** 标记对象。

**size (series int/string)** 标签大小。接受正的[int]值或内置的`size.*`常量之一。常量及其等效数字大小为：[size.auto] (0)、[size.tiny] (~7)、[size.small] (~10)、[size.normal] (12)、[size.large] (18)、[size.huge] (24)。默认值为[size.normal]，表示数字大小为12。

另见

[size.auto][size.tiny][size.small][size.normal][size.large][size.huge][label.new()]

###### label.set_style()



设置标签样式。



```
label.set_style(id, style) → void
```

参数

**id (series label)** 标记对象。

**style (series string)** 新的标签样式。可能的值：[label.style_none], [label.style_xcross], [label.style_cross], [label.style_triangleup], [label.style_triangledown], [label.style_flag], [label.style_circle], [label.style_arrowup], [label.style_arrowdown], [label.style_label_up], [label.style_label_down], [label.style_label_left], [label.style_label_right], [label.style_label_lower_left], [label.style_label_lower_right], [label.style_label_upper_left], [label.style_label_upper_right], [label.style_label_center], [label.style_square], [label.style_diamond], [label.style_text_outline]。

另见

[label.new()]

###### label.set_text()



设置标签文本



```
label.set_text(id, text) → void
```

参数

**id (series label)** 标记对象。

**text (series string)** 新标签文字。

另见

[label.new()][label.set_text_formatting()]

###### label.set_text_font_family()



该函数设置标签内文本的字体系列。



```
label.set_text_font_family(id, text_font_family) → void
```

参数

**id (series label)** 一个标签对象。

**text_font_family (series string)** 文本的字体系列。可能的值：[font.family_default]、[font.family_monospace]。



```
//@version=6
indicator("Example of setting the label font")
if barstate.islastconfirmedhistory
    l = label.new(bar_index, 0, "monospace", yloc=yloc.abovebar)
    label.set_text_font_family(l, font.family_monospace)
```

另见

[label.new()][font.family_default][font.family_monospace]

###### label.set_text_formatting()



设置绘图应用于显示文本的格式属性。



```
label.set_text_formatting(id, text_formatting) → void
```

参数

**id (series label)** 标记对象。

**text_formatting (const text_format)** 显示文本的格式。格式选项支持添加。例如，`text.format_bold + text.format_italic`将使文本同时变为粗体和斜体。可能的值：[text.format_none]、[text.format_bold]、[text.format_italic]。可选。默认值为[text.format_none]。

另见

[label.new()][label.set_text()]

###### label.set_textalign()



设定标签文本的对齐方式。



```
label.set_textalign(id, textalign) → void
```

参数

**id (series label)** 标记对象。

**textalign (series string)** 标签文本对齐。可能的值：[text.align_left]、[text.align_center]、[text.align_right]

另见

[text.align_left][text.align_center][text.align_right][label.new()]

###### label.set_textcolor()



设置标签文本的颜色。



```
label.set_textcolor(id, textcolor) → void
```

参数

**id (series label)** 标记对象。

**textcolor (series color)** 新文字颜色。

另见

[label.new()]

###### label.set_tooltip()



设置工具提示文字。



```
label.set_tooltip(id, tooltip) → void
```

参数

**id (series label)** 标记对象。

**tooltip (series string)** 工具提示文字。

另见

[label.new()]

###### label.set_x()



设置标签位置的K线索引或K线时间（取决于xloc）



```
label.set_x(id, x) → void
```

参数

**id (series label)** 标记对象。

**x (series int)** 标签位置的新K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象未来不能绘制超过500根K线。

另见

[label.new()]

###### label.set_xloc()



设置x-location和新K线索引/时间值



```
label.set_xloc(id, x, xloc) → void
```

参数

**id (series label)** 标记对象。

**x (series int)** 标签位置的新K线索引或K线时间。

**xloc (series string)** 新的x位置值。

另见

[xloc.bar_index][xloc.bar_time][label.new()]

###### label.set_xy()



设置标签位置的K线索引/时间和价格



```
label.set_xy(id, x, y) → void
```

参数

**id (series label)** 标记对象。

**x (series int)** 标签位置的新K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象未来不能绘制超过500根K线。

**y (series int/float)** 标签位置的新价格。

另见

[label.new()]

###### label.set_y()



设置标签位置的价格



```
label.set_y(id, y) → void
```

参数

**id (series label)** 标记对象。

**y (series int/float)** 标签位置的新价格。

另见

[label.new()]

###### label.set_yloc()



设置新的y位置计算算法。



```
label.set_yloc(id, yloc) → void
```

参数

**id (series label)** 标记对象。

**yloc (series string)** 新的y位置值。

另见

[yloc.price][yloc.abovebar][yloc.belowbar][label.new()]

###### library()



将脚本标识为[库]的声明语句。



```
library(title, overlay, dynamic_requests) → void
```

参数

**title (const string)** 脚本库的标题及其标识符。它不能包含空格、特殊字符或以数字开头。它用作出版物的默认标题，并在另一个脚本使用它时唯一标识[import]语句中的脚本库。它也用作图表上的脚本名称。

**overlay (const bool)** 如果为`true`，则当用户将脚本直接添加到图表时，脚本的视觉效果会显示在主图表窗格中；如果用户将脚本应用于其他脚本，则脚本的视觉效果会显示在该脚本的窗格中。如果为`false`，则脚本的视觉效果会显示在单独的窗格中。对`overlay`值的更改仅在用户再次将脚本添加到图表后生效。此外，如果用户通过选择脚本“更多”菜单中的“移动到”选项将脚本移动到另一个窗格，则在源代码更新后，脚本不会移回其原始窗格。默认值为`false`。无论此设置如何，用于显示入场和出场的策略特定标签都将显示在主图表上方。

**dynamic_requests (const bool)** 指定脚本是否可以动态调用来自`request.*()`命名空间的函数。动态`request.*()`调用允许在条件结构（例如，[if]）、循环（例如，[for]）和导出函数的本地范围内进行。此外，此类调用允许为其许多参数使用“系列”参数。可选。默认值为`true`。有关更多信息，请参阅用户手册的[动态请求]部分。



```
//@version=6
// @description Math library
library("num_methods", overlay = true)
// Calculate "sinh()" from the float parameter `x`
export sinh(float x) =>
    (math.exp(x) - math.exp(-x)) / 2.0
plot(sinh(0))
```

另见

[indicator()][strategy()]

###### line()



转换na成line



```
line(x) → series line
```

参数

**x (series line)** 要转换为指定类型的值，通常为`na`。

返回值

转换为行后参数的值。

另见

[float()][int()][bool()][color()][string()][label()]

###### line.copy()



克隆线条对象。



```
line.copy(id) → series line
```

参数

**id (series line)** 线条对象。



```
//@version=6
indicator('Last 100 bars price range', overlay = true)
LOOKBACK = 100
highest = ta.highest(LOOKBACK)
lowest = ta.lowest(LOOKBACK)
if barstate.islastconfirmedhistory
    var lineTop = line.new(bar_index[LOOKBACK], highest, bar_index, highest, color = color.green)
    var lineBottom = line.copy(lineTop)
    line.set_y1(lineBottom, lowest)
    line.set_y2(lineBottom, lowest)
    line.set_color(lineBottom, color.red)
```

返回值

可以传递给line.setXXX和line.getXXX函数的新线条ID对象。

另见

[line.new()][line.delete()]

###### line.delete()



删除指定的线对象。 如果它已被删除，则不执行任何操作。



```
line.delete(id) → void
```

参数

**id (series line)** 要删除的线条对象。

另见

[line.new()]

###### line.get_price()



返回给定bar index的线的价格水平。



```
line.get_price(id, x) → series float
```

参数

**id (series line)** 线条对象。

**x (series int)** 需要价格的K线索引



```
//@version=6
indicator("GetPrice", overlay=true)
var line l = na
if bar_index == 10
    l := line.new(0, high[5], bar_index, high)
plot(line.get_price(l, bar_index), color=color.green)
```

返回值

bar index 'x' 处 'id' 线的价格值。

备注

该线被认为是使用'extend=extend.both'建立的。

仅可对使用'xloc.bar_index'建立的线调用此函数。如果尝试在使用'xloc.bar_time'建立的线中调用它，则会产生错误。

另见

[line.new()]

###### line.get_x1()



返回线条的第一个点的UNIX时间或K線索引（取决于最后的xloc值集）



```
line.get_x1(id) → series int
```

参数

**id (series line)** 线条对象。



```
//@version=6
indicator("line.get_x1")
my_line = line.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time)
a = line.get_x1(my_line)
plot(time - line.get_x1(my_line)) //draws zero plot
```

返回值

UNIX时间戳（以毫秒为单位）或K线索引

另见

[line.new()]

###### line.get_x2()



返回行的第二个点的UNIX时间或K线索引（取决于最后的xloc值集）



```
line.get_x2(id) → series int
```

参数

**id (series line)** 线条对象。

返回值

UNIX时间戳（以毫秒为单位）或K线索引

另见

[line.new()]

###### line.get_y1()



返回该行第一个点的价格。



```
line.get_y1(id) → series float
```

参数

**id (series line)** 线条对象。

返回值

价格值。

另见

[line.new()]

###### line.get_y2()



返回该行第二个点的价格。



```
line.get_y2(id) → series float
```

参数

**id (series line)** 线条对象。

返回值

价格值。

另见

[line.new()]

###### line.new()

2过载



创建新的线条对象。

语法和重载

[`line.new(first_point, second_point, xloc, extend, color, style, width, force_overlay) → series line`][`line.new(x1, y1, x2, y2, xloc, extend, color, style, width, force_overlay) → series line`]

参数

**first_point (chart.point)** 一个[chart.point]对象，指定线的起始坐标。

**second_point (chart.point)** 指定线条结束坐标的[chart.point]对象。

**xloc (series string)** 请参阅**x1**参数的说明。可能的值：[xloc.bar_index]和[xloc.bar_time]。默认为[xloc.bar_index]。

**extend (series string)** 如果extend=[extend.none]，则绘制从点(x1, y1)开始并在点(x2,y2)结束的线段。如果extend等于[extend.right]或[extend.left]，则分别从点(x1,y1)或(x2,y2)开始绘制一条射线。如果extend=[extend.both]，则绘制一条穿过这些点的直线。默认值为[extend.none]。

**color (series color)** 线条颜色。

**style (series string)** 线条样式。可能的值：[line.style_solid]、[line.style_dotted]、[line.style_dashed]、[line.style_arrow_left]、[line.style_arrow_right]、[line.style_arrow_both]。

**width (series int)** 以像素为单位的线宽。

**force_overlay (const bool)** 如果是`true`，则绘图将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("line.new")
var line1 = line.new(0, low, bar_index, high, extend=extend.right)
var line2 = line.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time, style=line.style_dashed)
line.set_x2(line1, 0)
line.set_xloc(line1, time, time + 60 * 60 * 24, xloc.bar_time)
line.set_color(line2, color.green)
line.set_width(line2, 5)
```

返回值

线条ID对象，可以传递给line.setXXX和line.getXXX函数。

另见

[line.delete()][line.set_x1()][line.set_y1()][line.set_xy1()][line.set_x2()][line.set_y2()][line.set_xy2()][line.set_xloc()][line.set_color()][line.set_extend()][line.set_style()][line.set_width()]

###### line.set_color()



设置线条颜色



```
line.set_color(id, color) → void
```

参数

**id (series line)** 线条对象。

**color (series color)** 新线条颜色

另见

[line.new()]

###### line.set_extend()



设置此线对象的扩展类型。如果extend=[extend.none]，则从点(x1,y1)开始绘制线段并在点(x2,y2)结束。如果extend等于[extend.right]或[extend.left]，则分别从点(x1,y1)或(x2,y2)开始绘制一条射线。如果extend=[extend.both]，则绘制一条贯穿这些点的直线。



```
line.set_extend(id, extend) → void
```

参数

**id (series line)** 线条对象。

**extend (series string)** 新的扩展类型。

另见

[extend.none][extend.right][extend.left][extend.both][line.new()]

###### line.set_first_point()



设置`id`线的第一个点为`point`。



```
line.set_first_point(id, point) → void
```

参数

**id (series line)** 一个[line]对象。

**point (chart.point)** 一个[chart.point]对象。

###### line.set_second_point()



设置`id`线的第二个点为`point`。



```
line.set_second_point(id, point) → void
```

参数

**id (series line)** 一个[line]对象。

**point (chart.point)** 一个[chart.point]对象。

###### line.set_style()



设置线条样式



```
line.set_style(id, style) → void
```

参数

**id (series line)** 线条对象。

**style (series string)** 新的线条样式。

另见

[line.style_solid][line.style_dotted][line.style_dashed][line.style_arrow_left][line.style_arrow_right][line.style_arrow_both][line.new()]

###### line.set_width()



设置线宽。



```
line.set_width(id, width) → void
```

参数

**id (series line)** 线条对象。

**width (series int)** 新的线宽，以像素为单位。

另见

[line.new()]

###### line.set_x1()



设置第一个点的K线索引或K线时间（取决于xloc）



```
line.set_x1(id, x) → void
```

参数

**id (series line)** 线条对象。

**x (series int)** K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象未来不能绘制超过500根K线。

另见

[line.new()]

###### line.set_x2()



设定第二个点的K线索引或K线时间（取决于xloc）。



```
line.set_x2(id, x) → void
```

参数

**id (series line)** 线条对象。

**x (series int)** K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象未来不能绘制超过500根K线。

另见

[line.new()]

###### line.set_xloc()



设定x位置和新K线索引/时间值



```
line.set_xloc(id, x1, x2, xloc) → void
```

参数

**id (series line)** 线条对象。

**x1 (series int)** 第一个点的K线索引或K线时间

**x2 (series int)** 第二个点的K线索引或K线时间

**xloc (series string)** 新的x位置值。

另见

[xloc.bar_index][xloc.bar_time][line.new()]

###### line.set_xy1()



设定第一个点的K线索引/时间和价格



```
line.set_xy1(id, x, y) → void
```

参数

**id (series line)** 线条对象。

**x (series int)** K线索引或K线时间。请注意，使用[xloc.bar_index]定位的对象未来不能绘制超过500根K线。

**y (series int/float)** 价格。

另见

[line.new()]

###### line.set_xy2()



设置第二个点的条形索引/时间和价格



```
line.set_xy2(id, x, y) → void
```

参数

**id (series line)** 线条对象。

**x (series int)** K线索引或K线时间

**y (series int/float)** 价格。

另见

[line.new()]

###### line.set_y1()



设定第一点的价格



```
line.set_y1(id, y) → void
```

参数

**id (series line)** 线条对象。

**y (series int/float)** 价格。

另见

[line.new()]

###### line.set_y2()



设定第二点的价格。



```
line.set_y2(id, y) → void
```

参数

**id (series line)** 线条对象。

**y (series int/float)** 价格。

另见

[line.new()]

###### linefill()



将na转换为linefill。



```
linefill(x) → series linefill
```

参数

**x (series linefill)** 要转换为指定类型的值，通常为`na`。

返回值

转换为linefill后参数的值。

另见

[float()][int()][bool()][color()][string()][line()][label()]

###### linefill.delete()



删除指定的linefill对象。如果它已经被删除，则什么都不做。



```
linefill.delete(id) → void
```

参数

**id (series linefill)** 一个linefill对象。

###### linefill.get_line1()



返回在`id` linefill中使用的第一条线的ID。



```
linefill.get_line1(id) → series line
```

参数

**id (series linefill)** 一个linefill对象。

###### linefill.get_line2()



返回在`id` linefill中使用的第二条线的ID。



```
linefill.get_line2(id) → series line
```

参数

**id (series linefill)** 一个linefill对象。

###### linefill.new()



创建一个新的linefill对象并将其显示在图表上，使用`line1`中指定的颜色填充`line2`和`color`之间的空间。



```
linefill.new(line1, line2, color) → series linefill
```

参数

**line1 (series line)** 第一条线对象。

**line2 (series line)** 第二条线对象。

**color (series color)** 用于填充线条之间空间的颜色。

返回值

可以传递给其他linefill.*()函数的linefill对象的ID。

备注

如果两者中的任何一条线被删除，则linefill对象也将被删除。如果线条被移动（例如通过[line.set_xy()]函数），linefill对象也会被移动。

如果两条线相对于线本身沿相同的方向延伸（例如，它们的`extend=`参数的值为[extend.right]），则线延伸之间的空间也将被填充。

###### linefill.set_color()



该函数设置传递给它的linefill对象的颜色。



```
linefill.set_color(id, color) → void
```

参数

**id (series linefill)** 一个linefill对象。

**color (series color)** linefill对象的颜色。

###### log.error()

2过载



将格式字符串和值转换为格式化的字符串，并将结果发送到标有“error”调试级别的“Pine日志”菜单。

对于要格式化的每个值，格式化字符串可以包含文字文本和大括号{}中的一个占位符。每个占位符都包含将替换它的所需参数的索引（从0开始）和一个可选的格式说明符。索引表示该参数在函数参数列表中的位置。

语法和重载

[`log.error(message) → void`][`log.error(formatString, arg0, arg1, ...) → void`]

参数

**message (series string)** 日志消息。



```
//@version=6
strategy("My strategy", overlay = true, process_orders_on_close = true)
bracketTickSizeInput = input.int(1000, "Stoploss/Take-Profit distance (in ticks)")

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    limitLevel = close * 1.01
    log.info("Long limit order has been placed at {0}", limitLevel)
    strategy.order("My Long Entry Id", strategy.long, limit = limitLevel)

    log.info("Exit orders have been placed: Take-profit at {0}, Stop-loss at {1}", close, limitLevel)
    strategy.exit("Exit", "My Long Entry Id", profit = bracketTickSizeInput, loss = bracketTickSizeInput)

if strategy.opentrades > 10
    log.warning("{0} positions opened in the same direction in a row. Try adjusting `bracketTickSizeInput`", strategy.opentrades)

last10Perc = strategy.initial_capital / 10 > strategy.equity
if (last10Perc and not last10Perc[1`
    log.error("The strategy has lost 90% of the initial capital!")
```

返回值

格式化的字符串。

备注

未引用模式中的任何花括号都必须平衡。例如，“ab {0} de”和“ab '}' de”是有效模式，但“ab {0'}' de”、“ab } de”和“''{''”不是。

该函数可以对`{}`内的某些值应用附加格式。其他格式选项的列表可以在[str.format()]文章的示例部分中找到。

用作`formatString`参数的字符串可以包含单引号字符 (')。但是，必须将该字符串中的所有单引号配对，以避免意外的格式化结果。

可以从Pine编辑器中的“更多”下拉菜单，和在使用`log.*()`函数的任何脚本的状态行中的“更多”下拉菜单中访问“Pine 日志...”按钮。

###### log.info()

2过载



将格式字符串和值转换为格式化的字符串，并将结果发送到标有“info”调试级别的“Pine日志”菜单。

对于要格式化的每个值，格式化字符串可以包含文字文本和大括号{}中的一个占位符。每个占位符都包含将替换它的所需参数的索引（从0开始）和一个可选的格式说明符。索引表示该参数在函数参数列表中的位置。

语法和重载

[`log.info(message) → void`][`log.info(formatString, arg0, arg1, ...) → void`]

参数

**message (series string)** 日志消息。



```
//@version=6
strategy("My strategy", overlay = true, process_orders_on_close = true)
bracketTickSizeInput = input.int(1000, "Stoploss/Take-Profit distance (in ticks)")

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    limitLevel = close * 1.01
    log.info("Long limit order has been placed at {0}", limitLevel)
    strategy.order("My Long Entry Id", strategy.long, limit = limitLevel)

    log.info("Exit orders have been placed: Take-profit at {0}, Stop-loss at {1}", close, limitLevel)
    strategy.exit("Exit", "My Long Entry Id", profit = bracketTickSizeInput, loss = bracketTickSizeInput)

if strategy.opentrades > 10
    log.warning("{0} positions opened in the same direction in a row. Try adjusting `bracketTickSizeInput`", strategy.opentrades)

last10Perc = strategy.initial_capital / 10 > strategy.equity
if (last10Perc and not last10Perc[1`
    log.error("The strategy has lost 90% of the initial capital!")
```

返回值

格式化的字符串。

备注

未引用模式中的任何花括号都必须平衡。例如，“ab {0} de”和“ab '}' de”是有效模式，但“ab {0'}' de”、“ab } de”和“''{''”不是。

该函数可以对`{}`内的某些值应用附加格式。其他格式选项的列表可以在[str.format()]文章的示例部分中找到。

用作`formatString`参数的字符串可以包含单引号字符 (')。但是，必须将该字符串中的所有单引号配对，以避免意外的格式化结果。

可以从Pine编辑器中的“更多”下拉菜单，和在使用`log.*()`函数的任何脚本的状态行中的“更多”下拉菜单中访问“Pine 日志...”按钮。

###### log.warning()

2过载



将格式字符串和值转换为格式化的字符串，并将结果发送到标有“warning”调试级别的“Pine日志”菜单。

对于要格式化的每个值，格式化字符串可以包含文字文本和大括号{}中的一个占位符。每个占位符都包含将替换它的所需参数的索引（从0开始）和一个可选的格式说明符。索引表示该参数在函数参数列表中的位置。

语法和重载

[`log.warning(message) → void`][`log.warning(formatString, arg0, arg1, ...) → void`]

参数

**message (series string)** 日志消息。



```
//@version=6
strategy("My strategy", overlay = true, process_orders_on_close = true)
bracketTickSizeInput = input.int(1000, "Stoploss/Take-Profit distance (in ticks)")

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    limitLevel = close * 1.01
    log.info("Long limit order has been placed at {0}", limitLevel)
    strategy.order("My Long Entry Id", strategy.long, limit = limitLevel)

    log.info("Exit orders have been placed: Take-profit at {0}, Stop-loss at {1}", close, limitLevel)
    strategy.exit("Exit", "My Long Entry Id", profit = bracketTickSizeInput, loss = bracketTickSizeInput)

if strategy.opentrades > 10
    log.warning("{0} positions opened in the same direction in a row. Try adjusting `bracketTickSizeInput`", strategy.opentrades)

last10Perc = strategy.initial_capital / 10 > strategy.equity
if (last10Perc and not last10Perc[1`
    log.error("The strategy has lost 90% of the initial capital!")
```

返回值

格式化的字符串。

备注

未引用模式中的任何花括号都必须平衡。例如，“ab {0} de”和“ab '}' de”是有效模式，但“ab {0'}' de”、“ab } de”和“''{''”不是。

该函数可以对`{}`内的某些值应用附加格式。其他格式选项的列表可以在[str.format()]文章的示例部分中找到。

用作`formatString`参数的字符串可以包含单引号字符 (')。但是，必须将该字符串中的所有单引号配对，以避免意外的格式化结果。

可以从Pine编辑器中的“更多”下拉菜单，和在使用`log.*()`函数的任何脚本的状态行中的“更多”下拉菜单中访问“Pine 日志...”按钮。

###### map.clear()



清除map，从中删除所有键值对。



```
map.clear(id) → void
```

参数

**id (any map type)** 一个map对象



```
//@version=6
indicator("map.clear example")
oddMap = map.new<int, bool>()
oddMap.put(1, true)
oddMap.put(2, false)
oddMap.put(3, true)
map.clear(oddMap)
plot(oddMap.size())
```

另见

[map.new()][map.put_all()][map.keys()][map.values()][map.remove()]

###### map.contains()



如果在`id`map中找到`key`，则返回`true`，否则返回`false`。



```
map.contains(id, key) → series bool
```

参数

**id (any map type)** 一个map对象

**key (series <type of the map's elements>)** 在map中搜索的键。



```
//@version=6
indicator("map.includes example")
a = map.new<string, float>()
a.put("open", open)
p = close
if map.contains(a, "open")
    p := a.get("open")
plot(p)
```

另见

[map.new()][map.put()][map.keys()][map.values()][map.size()]

###### map.copy()



创建现有map的副本。



```
map.copy(id) → map<keyType, valueType>
```

参数

**id (any map type)** 要复制的map对象。



```
//@version=6
indicator("map.copy example")
a = map.new<string, int>()
a.put("example", 1)
b = map.copy(a)
a := map.new<string, int>()
a.put("example", 2)
plot(a.get("example"))
plot(b.get("example"))
```

返回值

`id`map副本。

另见

[map.new()][map.put()][map.keys()][map.values()][map.get()][map.size()]

###### map.get()



返回与`id`map中指定的`key`关联的值。



```
map.get(id, key) → <value_type>
```

参数

**id (any map type)** 一个map对象

**key (series <type of the map's elements>)** 要检索值的键。



```
//@version=6
indicator("map.get example")
a = map.new<int, int>()
size = 10
for i = 0 to size
    a.put(i, size-i)
plot(map.get(a, 1))
```

另见

[map.new()][map.put()][map.keys()][map.values()][map.contains()]

###### map.keys()



返回`id`映射中所有键的数组。生成的数组是副本，对其进行的任何更改都不会反映在原始映射中。



```
map.keys(id) → array<type>
```

参数

**id (any map type)** 一个map对象



```
//@version=6
indicator("map.keys example")
a = map.new<string, float>()
a.put("open", open)
a.put("high", high)
a.put("low", low)
a.put("close", close)
keys = map.keys(a)
ohlc = 0.0
for key in keys
    ohlc += a.get(key)
plot(ohlc/4)
```

备注

Map保持插入顺序。此函数返回的数组中的元素也将按插入顺序排列。

另见

[map.new()][map.put()][map.get()][map.values()][map.size()]

###### map.new<type,type>()



创建一个新的map对象：一个由键值对组成的集合，其中所有键都属于`keyType`，所有值都属于`valueType`。

`keyType`只能是原始类型，即以下之一：[int]、[float]、[bool]、[string]、[color]。

`valueType`可以是除`array<>`、`matrix<>`和`map<>`之外的任何类型。允许用户定义的类型，即使它们的字段之一为`array<>`、`matrix<>`或`map<>`。



```
map.new<keyType, valueType>() → map<keyType, valueType>
```



```
//@version=6
indicator("map.new<string, int> example")
a = map.new<string, int>()
a.put("example", 1)
label.new(bar_index, close, str.tostring(a.get("example")))
```

返回值

可以在其他map.*()函数中使用的map对象的ID。

备注

每个密钥都是唯一的并且只能出现一次。当使用map已包含的键添加新值时，该值将替换与该键关联的旧值。

Map保持插入顺序。请注意，插入带有map中已存在的`key`的对时，顺序不会改变。在这种情况下，新对将用`key`替换现有对。

另见

[map.put()][map.keys()][map.values()][map.get()][array.new()]

###### map.put()



将新的键值对放入`id`map中。



```
map.put(id, key, value) → <value_type>
```

参数

**id (any map type)** 一个map对象

**key (series <type of the map's elements>)** 要放入map中的键。

**value (series <type of the map's elements>)** 要放入map中的键值。



```
//@version=6
indicator("map.put example")
a = map.new<string, float>()
map.put(a, "first", 10)
map.put(a, "second", 15)
prevFirst = map.put(a, "first", 20)
currFirst = a.get("first")
plot(prevFirst)
plot(currFirst)
```

返回值

如果键已存在于map中，则与`key`关联的先前值；如果键是新的，则与`na`关联。

备注

Map保持插入顺序。请注意，插入带有map中已存在的`key`的对时，顺序不会改变。在这种情况下，新对将用`key`替换现有对。

另见

[map.new()][map.put_all()][map.keys()][map.values()][map.remove()]

###### map.put_all()



将`id2`map中的所有键值对放入`id`map中。



```
map.put_all(id, id2) → void
```

参数

**id (any map type)** 要附加到的map对象。

**id2 (any map type)** 要附加的map对象。



```
//@version=6
indicator("map.put_all example")
a = map.new<string, float>()
b = map.new<string, float>()
a.put("first", 10)
a.put("second", 15)
b.put("third", 20)
map.put_all(a, b)
plot(a.get("third"))
```

另见

[map.new()][map.put()][map.keys()][map.values()][map.remove()]

###### map.remove()



从`id`map中删除键值对。



```
map.remove(id, key) → <value_type>
```

参数

**id (any map type)** 一个map对象

**key (series <type of the map's elements>)** 要从map中删除的键对。



```
//@version=6
indicator("map.remove example")
a = map.new<string, color>()
a.put("firstColor", color.green)
oldColorValue = map.remove(a, "firstColor")
plot(close, color = oldColorValue)
```

返回值

如果map中存在该键，则与`key`关联的先前值；如果不存在此类键，则与`na`关联。

另见

[map.new()][map.put()][map.keys()][map.values()][map.clear()]

###### map.size()



返回`id`map中键值对的数量。



```
map.size(id) → series int
```

参数

**id (any map type)** 一个map对象



```
//@version=6
indicator("map.size example")
a = map.new<int, int>()
size = 10
for i = 0 to size
    a.put(i, size-i)
plot(map.size(a))
```

另见

[map.new()][map.put()][map.keys()][map.values()][map.get()]

###### map.values()



返回`id`映射中所有值的数组。生成的数组是副本，对其进行的任何更改都不会反映在原始映射中。



```
map.values(id) → array<type>
```

参数

**id (any map type)** 一个map对象



```
//@version=6
indicator("map.values example")
a = map.new<string, float>()
a.put("open", open)
a.put("high", high)
a.put("low", low)
a.put("close", close)
values = map.values(a)
ohlc = 0.0
for value in values
    ohlc += value
plot(ohlc/4)
```

备注

Map保持插入顺序。此函数返回的数组中的元素也将按插入顺序排列。

另见

[map.new()][map.put()][map.get()][map.keys()][map.size()]

###### math.abs()

8过载



如果`number` >= 0，则`number`的绝对值为`number`，否则为-`number`。

语法和重载

[`math.abs(number) → const int`][`math.abs(number) → input int`][`math.abs(number) → const float`][`math.abs(number) → simple int`][`math.abs(number) → input float`][`math.abs(number) → series int`][`math.abs(number) → simple float`][`math.abs(number) → series float`]

参数

**number (const int)** 计算中使用的数字。

返回值

`number`的绝对值。

###### math.acos()

4过载



acos函数返回数字的反余弦(以弧度表示)，如cos(acos(y)) = y 在 y 范围内 [-1, 1]。

语法和重载

[`math.acos(angle) → const float`][`math.acos(angle) → input float`][`math.acos(angle) → simple float`][`math.acos(angle) → series float`]

参数

**angle (const int/float)** 用于计算的值，以弧度为单位。

返回值

反余弦值。如果y超出范围[-1,1]，返回角度在[0，Pi]或`na`的范围内。

###### math.asin()

4过载



asin函数返回数字的反正弦(以弧度表示)，正弦(asin(y)) = y 在 y 范围内[-1, 1]。

语法和重载

[`math.asin(angle) → const float`][`math.asin(angle) → input float`][`math.asin(angle) → simple float`][`math.asin(angle) → series float`]

参数

**angle (const int/float)** 用于计算的值，以弧度为单位。

返回值

反正弦值。如果y超出范围[-1,1]，返回角度在[-Pi / 2，Pi / 2]或`na`的范围内。

###### math.atan()

4过载



atan函数返回数字的反正切(以弧度表示)，tan(atan(y)) = 任何 y 中的 y。

语法和重载

[`math.atan(angle) → const float`][`math.atan(angle) → input float`][`math.atan(angle) → simple float`][`math.atan(angle) → series float`]

参数

**angle (const int/float)** 用于计算的值，以弧度为单位。

返回值

反正切值; 返回角度在[-Pi / 2，Pi / 2]的范围内。

###### math.avg()

2过载



计算所有系列的平均值(对应元素)。

语法和重载

[`math.avg(number0, number1, ...) → simple float`][`math.avg(number0, number1, ...) → series float`]

参数

**number0, number1, ... (simple int/float)** 计算中使用的数字序列。

返回值

平均

另见

[math.sum()][ta.cum()][ta.sma()]

###### math.ceil()

4过载



向上舍入指定的`number`为大于或等于它的最小整数（“int”值）。

语法和重载

[`math.ceil(number) → const int`][`math.ceil(number) → input int`][`math.ceil(number) → simple int`][`math.ceil(number) → series int`]

参数

**number (const int/float)** 要舍入的数字。

返回值

大于或等于`number`的最小“int”值。

另见

[math.floor()][math.round()]

###### math.cos()

4过载



cos函数返回角度的三角余弦。

语法和重载

[`math.cos(angle) → const float`][`math.cos(angle) → input float`][`math.cos(angle) → simple float`][`math.cos(angle) → series float`]

参数

**angle (const int/float)** 角度，以弧度

返回值

角的三角余弦。

###### math.exp()

4过载



`number`的exp函数是e的`number`次方，其中e是欧拉数。

语法和重载

[`math.exp(number) → const float`][`math.exp(number) → input float`][`math.exp(number) → simple float`][`math.exp(number) → series float`]

参数

**number (const int/float)** 计算中使用的数字。

返回值

一个表示 e 的值，它是 `number` 的幂。

另见

[math.pow()]

###### math.floor()

4过载



向下舍入指定的`number`为小于或等于它的最大整数（“int”值）。

语法和重载

[`math.floor(number) → const int`][`math.floor(number) → input int`][`math.floor(number) → simple int`][`math.floor(number) → series int`]

参数

**number (const int/float)** 要舍入的数字。

返回值

小于或等于`number`的最大“int”值。

另见

[math.ceil()][math.round()]

###### math.log()

4过载



任何`number` > 0的自然对数是唯一y，使得e^y = `number`。

语法和重载

[`math.log(number) → const float`][`math.log(number) → input float`][`math.log(number) → simple float`][`math.log(number) → series float`]

参数

**number (const int/float)** 计算中使用的数字。

返回值

`number`的自然对数。

另见

[math.log10()]

###### math.log10()

4过载



`number`的常用（或以10为底）对数是必须乘以10才能获得`number`的幂。10^y = `number`。

语法和重载

[`math.log10(number) → const float`][`math.log10(number) → input float`][`math.log10(number) → simple float`][`math.log10(number) → series float`]

参数

**number (const int/float)** 计算中使用的数字。

返回值

`number`的以10为底的对数。

另见

[math.log()]

###### math.max()

8过载



返回多个值中最大的一个。

语法和重载

[`math.max(number0, number1, ...) → const int`][`math.max(number0, number1, ...) → const float`][`math.max(number0, number1, ...) → input int`][`math.max(number0, number1, ...) → simple int`][`math.max(number0, number1, ...) → input float`][`math.max(number0, number1, ...) → series int`][`math.max(number0, number1, ...) → simple float`][`math.max(number0, number1, ...) → series float`]

参数

**number0, number1, ... (const int)** 计算中使用的数字序列。



```
//@version=6
indicator("math.max", overlay=true)
plot(math.max(close, open))
plot(math.max(close, math.max(open, 42)))
```

返回值

多个给定值中最大的。

另见

[math.min()]

###### math.min()

8过载



返回多个值中最小的一个。

语法和重载

[`math.min(number0, number1, ...) → const int`][`math.min(number0, number1, ...) → const float`][`math.min(number0, number1, ...) → input int`][`math.min(number0, number1, ...) → simple int`][`math.min(number0, number1, ...) → input float`][`math.min(number0, number1, ...) → series int`][`math.min(number0, number1, ...) → simple float`][`math.min(number0, number1, ...) → series float`]

参数

**number0, number1, ... (const int)** 计算中使用的数字序列。



```
//@version=6
indicator("math.min", overlay=true)
plot(math.min(close, open))
plot(math.min(close, math.min(open, 42)))
```

返回值

多个给定值中的最小值。

另见

[math.max()]

###### math.pow()

4过载



数学幂函数

语法和重载

[`math.pow(base, exponent) → const float`][`math.pow(base, exponent) → input float`][`math.pow(base, exponent) → simple float`][`math.pow(base, exponent) → series float`]

参数

**base (const int/float)** 指定要使用的基础。

**exponent (const int/float)** 指定指数。



```
//@version=6
indicator("math.pow", overlay=true)
plot(math.pow(close, 2))
```

返回值

`base`的`exponent`次方。如果`base`是一个系列，则按元素计算。

另见

[math.sqrt()][math.exp()]

###### math.random()



返回伪随机值。该函数将为每个脚本执行生成不同的值序列。对可选的seed参数使用相同的值将产生可重复的序列。



```
math.random(min, max, seed) → series float
```

参数

**min (series int/float)** 随机值范围的下限。该值不包括在范围内。默认值为0。

**max (series int/float)** 随机值范围的上限。该值不包括在范围内。默认值为1。

**seed (series int)** 可选参数。当使用相同的seed时，允许连续调用该函数以产生一组可重复的值。

返回值

一个随机值。

###### math.round()

8过载



返回 `number` 的值，四舍五入到最接近的整数，并向上取整。如果使用了 `precision` 参数，则返回一个四舍五入到小数位数的浮点值。

语法和重载

[`math.round(number) → const int`][`math.round(number) → input int`][`math.round(number) → simple int`][`math.round(number) → series int`][`math.round(number, precision) → const float`][`math.round(number, precision) → input float`][`math.round(number, precision) → simple float`][`math.round(number, precision) → series float`]

参数

**number (const int/float)** 要四舍五入的值。

返回值

`number`的值四舍五入到最接近的整数，或根据精度。

备注

请注意，对于'na'值，函数返回'na'。

另见

[math.ceil()][math.floor()]

###### math.round_to_mintick()

2过载



返回四舍五入到商品的mintick的值，即可以除以[syminfo.mintick]的最接近的值，没有余数，并向上舍入。

语法和重载

[`math.round_to_mintick(number) → simple float`][`math.round_to_mintick(number) → series float`]

参数

**number (simple int/float)** 要四舍五入的值。

返回值

`number`四舍五入以精确到tick。

备注

请注意，对于'na'值，函数返回'na'。

另见

[math.ceil()][math.floor()]

###### math.sign()

4过载



如果`number`为零，则`number`的符号(signum)为零；如果`number`大于零，则为1.0；如果`number`小于零，则为-1.0。

语法和重载

[`math.sign(number) → const float`][`math.sign(number) → input float`][`math.sign(number) → simple float`][`math.sign(number) → series float`]

参数

**number (const int/float)** 计算中使用的数字。

返回值

参数的标志。

###### math.sin()

4过载



正弦函数返回一个角度的三角正弦。

语法和重载

[`math.sin(angle) → const float`][`math.sin(angle) → input float`][`math.sin(angle) → simple float`][`math.sin(angle) → series float`]

参数

**angle (const int/float)** 角度，以弧度

返回值

角的三角正弦。

###### math.sqrt()

4过载



任何`number` >= 0的平方根是唯一y >= 0，使得y^2 = `number`。

语法和重载

[`math.sqrt(number) → const float`][`math.sqrt(number) → input float`][`math.sqrt(number) → simple float`][`math.sqrt(number) → series float`]

参数

**number (const int/float)** 计算中使用的数字。

返回值

`number`的平方根。

另见

[math.pow()]

###### math.sum()



sum函数返回x的最后y值的滑动综合。



```
math.sum(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

`source`K线返回的`length`总和。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.cum()][for]

###### math.tan()

4过载



tan函数返回角度的三角正切。

语法和重载

[`math.tan(angle) → const float`][`math.tan(angle) → input float`][`math.tan(angle) → simple float`][`math.tan(angle) → series float`]

参数

**angle (const int/float)** 角度，以弧度

返回值

角的三角正切。

###### math.todegrees()



从以弧度为单位的角度，返回以度为单位的近似等效角度。



```
math.todegrees(radians) → series float
```

参数

**radians (series int/float)** 以弧度为单位的角度。

返回值

以度为单位的角度值。

###### math.toradians()



从以度为单位的角度，返回以弧度为单位的近似等效角度。



```
math.toradians(degrees) → series float
```

参数

**degrees (series int/float)** 以度为单位的角度。

返回值

以弧度为单位的角度值。

###### matrix.add_col()



在`id`矩阵的`column`索引处插入一个新列。



```
matrix.add_col(id, column, array_id) → void
```

参数

**id (any matrix type)** 矩阵对象的ID（引用）。

**column (series int)** 可选。新列的索引。必须为0到`matrix.columns(id)`之间的值。所有索引大于或等于此值的现有列都会将其索引加一。默认值为`matrix.columns(id)`。

**array_id (any array type)** 可选。用作新列的数组的 ID。如果矩阵为空，则数组可以是任意大小。否则，其大小必须等于`matrix.rows(id)`。默认情况下，该函数会插入一列`na`值。

添加一列到矩阵



```
//@version=6
indicator("`matrix.add_col()` Example 1")

// Create a 2x3 "int" matrix containing values `0`.
m = matrix.new<int>(2, 3, 0)

// Add a column with `na` values to the matrix.
matrix.add_col(m)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))
```

将阵列作为列添加到矩阵



```
//@version=6
indicator("`matrix.add_col()` Example 2")

if barstate.islastconfirmedhistory
    // Create an empty matrix object.
    var m = matrix.new<int>()

    // Create an array with values `1` and `3`.
    var a = array.from(1, 3)

    // Add the `a` array as the first column of the empty matrix.
    matrix.add_col(m, 0, a)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))
```

备注

与添加列到空矩阵相比，声明具有显式维度的矩阵并用值填充它的效率要高得多。 添加一列也比使用[matrix.add_row()]函数添加一行要慢得多。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()][matrix.add_row()]

###### matrix.add_row()



在`id`矩阵的`row`索引处插入一个新行。



```
matrix.add_row(id, row, array_id) → void
```

参数

**id (any matrix type)** 矩阵对象的ID（引用）。

**row (series int)** 可选。新行的索引。必须为0到`matrix.rows(id)`之间的值。所有索引大于或等于此值的现有行都会将其索引加一。默认值为`matrix.rows(id)`。

**array_id (any array type)** 可选。用作新行的数组的ID。如果矩阵为空，则数组可以是任意大小。否则，其大小必须等于`matrix.columns(id)`。默认情况下，该函数会插入一行`na`值。

添加一行到矩阵



```
//@version=6
indicator("`matrix.add_row()` Example 1")

// Create a 2x3 "int" matrix containing values `0`.
m = matrix.new<int>(2, 3, 0)

// Add a row with `na` values to the matrix.
matrix.add_row(m)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))
```

将阵列作为行添加到矩阵



```
//@version=6
indicator("`matrix.add_row()` Example 2")

if barstate.islastconfirmedhistory
    // Create an empty matrix object.
    var m = matrix.new<int>()

    // Create an array with values `1` and `2`.
    var a = array.from(1, 2)

    // Add the `a` array as the first row of the empty matrix.
    matrix.add_row(m, 0, a)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))
```

备注

行和列的索引从零开始。与添加行到空矩阵相比，声明具有显式维度的矩阵并用值填充它的效率要高得多。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()][matrix.add_col()]

###### matrix.avg()

2过载



该函数计算矩阵中所有元素的平均值。

语法和重载

[`matrix.avg(id) → series float`][`matrix.avg(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.avg()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the average value of the matrix.
var x = matrix.avg(m)

plot(x, 'Matrix average value')
```

返回值

`id` 矩阵的平均值。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.col()



该函数从矩阵列的元素创建一维阵列。



```
matrix.col(id, column) → array<type>
```

参数

**id (any matrix type)** 一个矩阵对象。

**column (series int)** 所需列的索引。



```
//@version=6
indicator("`matrix.col()` Example", "", true)

// Create a 2x3 "float" matrix from `hlc3` values.
m = matrix.new<float>(2, 3, hlc3)

// Return an array with the values of the first column of matrix `m`.
a = matrix.col(m, 0)

// Plot the first value from the array `a`.
plot(array.get(a, 0))
```

返回值

包含`column`矩阵的`id`值的阵列ID。

备注

行的索引从0开始。

另见

[matrix.new()][matrix.get()][array.get()][matrix.col()][matrix.columns()]

###### matrix.columns()



该函数返回矩阵中的列数。



```
matrix.columns(id) → series int
```

参数

**id (any matrix type)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.columns()` Example")

// Create a 2x6 matrix with values `0`.
var m = matrix.new<int>(2, 6, 0)

// Get the quantity of columns in matrix `m`.
var x = matrix.columns(m)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, "Columns: " + str.tostring(x) + "\n" + str.tostring(m))
```

返回值

矩阵`id`中的列数。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.col()][matrix.row()][matrix.rows()]

###### matrix.concat()



该函数将`m2`矩阵附加到`m1`矩阵。



```
matrix.concat(id1, id2) → matrix<type>
```

参数

**id1 (any matrix type)** 要连接到的矩阵对象。

**id2 (any matrix type)** 其元素将附加到 `id1` 的矩阵对象。



```
//@version=6
indicator("`matrix.concat()` Example")

// Create a 2x4 "int" matrix containing values `0`.
m1 = matrix.new<int>(2, 4, 0)
// Create a 2x4 "int" matrix containing values `1`.
m2 = matrix.new<int>(2, 4, 1)

// Append matrix `m2` to `m1`.
matrix.concat(m1, m2)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix Elements:")
    table.cell(t, 0, 1, str.tostring(m1))
```

返回值

返回与 `id1` 矩阵连接的 `id2` 矩阵。

备注

两个矩阵中的列数必须相同。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.copy()



该函数创建一个新矩阵，它是原始矩阵的副本。



```
matrix.copy(id) → matrix<type>
```

参数

**id (any matrix type)** 要复制的矩阵对象。



```
//@version=6
indicator("`matrix.copy()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 "float" matrix with `1` values.
    var m1 = matrix.new<float>(2, 3, 1)

    // Copy the matrix to a new one.
    // Note that unlike what `matrix.copy()` does,
    // the simple assignment operation `m2 = m1`
    // would NOT create a new copy of the `m1` matrix.
    // It would merely create a copy of its ID referencing the same matrix.
    var m2 = matrix.copy(m1)

    // Display using a table.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Matrix Copy:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

复制的`id`矩阵的新矩阵对象。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.det()

2过载



该函数返回方阵的[行列式]。

语法和重载

[`matrix.det(id) → series float`][`matrix.det(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.det` Example")

// Create a 2x2 matrix.
var m = matrix.new<float>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0,  3)
matrix.set(m, 0, 1,  7)
matrix.set(m, 1, 0,  1)
matrix.set(m, 1, 1, -4)

// Get the determinant of the matrix.
var x = matrix.det(m)

plot(x, 'Matrix determinant')
```

返回值

`id` 矩阵的行列式值。

备注

基于[LU分解]算法的函数计算。

另见

[matrix.new()][matrix.set()][matrix.is_square()]

###### matrix.diff()

2过载



该函数返回矩阵`id1`和`id2`之间或矩阵`id1`和`id2`标量（数值）相减所得的新矩阵。

语法和重载

[`matrix.diff(id1, id2) → matrix`][`matrix.diff(id1, id2) → matrix`]

参数

**id1 (matrix<int>)** 要从中减去的矩阵。

**id2 (series int/float/matrix<int>)** 要减去的矩阵对象或标量值。

两个矩阵之间的差异



```
//@version=6
indicator("`matrix.diff()` Example 1")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `5`.
    var m1 = matrix.new<float>(2, 3, 5)
    // Create a 2x3 matrix containing values `4`.
    var m2 = matrix.new<float>(2, 3, 4)
    // Create a new matrix containing the difference between matrices `m1` and `m2`.
    var m3 = matrix.diff(m1, m2)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "Difference between two matrices:")
    table.cell(t, 0, 1, str.tostring(m3))
```

矩阵和标量值之间的差异



```
//@version=6
indicator("`matrix.diff()` Example 2")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix with values `4`.
    var m1 = matrix.new<float>(2, 3, 4)

    // Create a new matrix containing the difference between the `m1` matrix and the "int" value `1`.
    var m2 = matrix.diff(m1, 1)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "Difference between a matrix and a scalar:")
    table.cell(t, 0, 1, str.tostring(m2))
```

返回值

一个新的矩阵对象，包含 `id2` 和 `id1` 之间的差异。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.eigenvalues()

2过载



该函数返回一个包含方阵的[特征值]的数组。

语法和重载

[`matrix.eigenvalues(id) → array`][`matrix.eigenvalues(id) → array`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.eigenvalues()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 2)
    matrix.set(m1, 0, 1, 4)
    matrix.set(m1, 1, 0, 6)
    matrix.set(m1, 1, 1, 8)

    // Get the eigenvalues of the matrix.
    tr = matrix.eigenvalues(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Array of Eigenvalues:")
    table.cell(t, 1, 1, str.tostring(tr))
```

返回值

包含`id`矩阵特征值的阵列。

备注

该函数是使用“隐式 QL 算法”计算的。

另见

[matrix.new()][matrix.set()][matrix.eigenvectors()]

###### matrix.eigenvectors()

2过载



返回一个由[特征向量]组成的矩阵，其中每一列都是 `id` 矩阵的特征向量。

语法和重载

[`matrix.eigenvectors(id) → matrix`][`matrix.eigenvectors(id) → matrix`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.eigenvectors()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix
    var m1 = matrix.new<int>(2, 2, 1)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 2)
    matrix.set(m1, 0, 1, 4)
    matrix.set(m1, 1, 0, 6)
    matrix.set(m1, 1, 1, 8)

    // Get the eigenvectors of the matrix.
    m2 = matrix.eigenvectors(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix Elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Matrix Eigenvectors:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

包含`id`矩阵的特征向量的新矩阵。

备注

该函数是使用“隐式 QL 算法”计算的。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.eigenvalues()]

###### matrix.elements_count()



该函数返回所有矩阵元素的总数。



```
matrix.elements_count(id) → series int
```

参数

**id (any matrix type)** 一个矩阵对象。

另见

[matrix.new()][matrix.columns()][matrix.rows()]

###### matrix.fill()



该函数用`id`填充由索引`from_column`到`to_column`（不包括它）和`from_row`到`to_row`（不包括它）定义的`value`矩阵的矩形区域。



```
matrix.fill(id, value, from_row, to_row, from_column, to_column) → void
```

参数

**id (any matrix type)** 一个矩阵对象。

**value (series <type of the matrix's elements>)** 要填入的值。

**from_row (series int)** 将开始填充的行索引（包括）。可选。默认值为 0。

**to_row (series int)** 填充将结束的行索引（不包括在内）。可选。默认值为[matrix.rows()]。

**from_column (series int)** 将开始填充的列索引（包括）。可选。默认值为 0。

**to_column (series int)** 填充将结束的列索引（不包括在内）。可选。默认值为[matrix.columns()]。



```
//@version=6
indicator("`matrix.fill()` Example")

// Create a 4x5 "int" matrix containing values `0`.
m = matrix.new<float>(4, 5, 0)

// Fill the intersection of rows 1 to 2 and columns 2 to 3 of the matrix with `hl2` values.
matrix.fill(m, hl2, 0, 2, 1, 3)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
```

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.get()



该函数返回具有指定矩阵索引的元素。



```
matrix.get(id, row, column) → <matrix_type>
```

参数

**id (any matrix type)** 一个矩阵对象。

**row (series int)** 所需行的索引。

**column (series int)** 所需列的索引。



```
//@version=6
indicator("`matrix.get()` Example", "", true)

// Create a 2x3 "float" matrix from the `hl2` values.
m = matrix.new<float>(2, 3, hl2)

// Return the value of the element at index [0, 0] of matrix `m`.
x = matrix.get(m, 0, 0)

plot(x)
```

返回值

`row` 矩阵的`column` 和 `id` 索引处的元素的值。

备注

行和列的索引从零开始。

另见

[matrix.new()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.inv()

2过载



该函数返回方阵的[逆矩阵]。

语法和重载

[`matrix.inv(id) → matrix`][`matrix.inv(id) → matrix`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.inv()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Inverse of the matrix.
    var m2 = matrix.inv(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Inverse matrix:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

一个新矩阵，它是`id`矩阵的逆矩阵。

备注

该函数使用[LU 分解]算法计算。

另见

[matrix.new()][matrix.set()][matrix.pinv()][matrix.copy()][str.tostring()]

###### matrix.is_antidiagonal()



该函数确定矩阵是否为[反对角线矩阵]（次对角线之外的所有元素均为零）。



```
matrix.is_antidiagonal(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是反对角矩阵，则返回 true，否则返回 false。

备注

使用非方阵返回 false。

另见

[matrix.new()][matrix.set()][matrix.is_square()][matrix.is_identity()][matrix.is_diagonal()]

###### matrix.is_antisymmetric()



该函数确定矩阵是否为 [反对称矩阵]（其[颠倒]等于其负数）。



```
matrix.is_antisymmetric(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是反对称矩阵，则返回 true，否则返回 false。

备注

使用非方阵返回 false。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.is_square()]

###### matrix.is_binary()



该函数确定矩阵是否为[逻辑矩阵]（当矩阵的所有元素为 0 或 1 时）。



```
matrix.is_binary(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是逻辑矩阵，则返回 true，否则返回 false。

另见

[matrix.new()][matrix.get()][matrix.set()]

###### matrix.is_diagonal()



该函数确定矩阵是否为[对角线矩阵]（主对角线之外的所有元素都为零）。



```
matrix.is_diagonal(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是对角线矩阵，则返回 true，否则返回 false。

备注

使用非方阵返回 false。

另见

[matrix.new()][matrix.set()][matrix.is_square()][matrix.is_identity()][matrix.is_antidiagonal()]

###### matrix.is_identity()



该函数确定矩阵是否为[单位矩阵]（元素在[主对角线]上为1，其他位置为0）。



```
matrix.is_identity(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 是一个单位矩阵，则返回 true，否则返回 false。

备注

使用非方阵返回 false。

另见

[matrix.new()][matrix.is_square()][matrix.is_diagonal()]

###### matrix.is_square()



该函数确定矩阵是否为[正方矩阵]（它具有相同的行数和列数）。



```
matrix.is_square(id) → series bool
```

参数

**id (any matrix type)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是正方矩阵，则返回 true，否则返回 false。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.is_stochastic()



该函数确定矩阵是否为[随机矩阵]。



```
matrix.is_stochastic(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是随机矩阵，则返回 true，否则返回 false。

另见

[matrix.new()][matrix.set()]

###### matrix.is_symmetric()



该函数确定[正方矩阵]是否为[对称矩阵]（元素相对于[主对角线]对称）。



```
matrix.is_symmetric(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是对称矩阵，则返回 true，否则返回 false。

备注

使用非方阵返回 false。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.is_square()]

###### matrix.is_triangular()



该函数确定矩阵是否为[三角矩阵]（如果[主对角线]上方或下方的所有元素均为零）。



```
matrix.is_triangular(id) → series bool
```

参数

**id (matrix<int/float>)** 要测试的矩阵对象。

返回值

如果 `id` 矩阵是三角矩阵，则返回 true，否则返回 false。

备注

使用非方阵返回 false。

另见

[matrix.new()][matrix.set()][matrix.is_square()]

###### matrix.is_zero()



该函数确定矩阵的所有元素是否为零。



```
matrix.is_zero(id) → series bool
```

参数

**id (matrix<int/float>)** 要检查的矩阵对象。

返回值

如果 `id` 矩阵的所有元素都为零，则返回 true，否则返回 false。

另见

[matrix.new()][matrix.get()][matrix.set()]

###### matrix.kron()

2过载



该函数返回 `id1` 和 `id2` 矩阵的[Kronecker 积]。

语法和重载

[`matrix.kron(id1, id2) → matrix`][`matrix.kron(id1, id2) → matrix`]

参数

**id1 (matrix<int/float>)** 第一个矩阵对象。

**id2 (matrix<int/float>)** 第二个矩阵对象。



```
//@version=6
indicator("`matrix.kron()` Example")

// Display using a table.
if barstate.islastconfirmedhistory
    // Create two matrices with default values `1` and `2`.
    var m1 = matrix.new<float>(2, 2, 1)
    var m2 = matrix.new<float>(2, 2, 2)

    // Calculate the Kronecker product of the matrices.
    var m3 = matrix.kron(m1, m2)

    // Display matrix elements.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Matrix 1:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 1, "⊗")
    table.cell(t, 2, 0, "Matrix 2:")
    table.cell(t, 2, 1, str.tostring(m2))
    table.cell(t, 3, 1, "=")
    table.cell(t, 4, 0, "Kronecker product:")
    table.cell(t, 4, 1, str.tostring(m3))
```

返回值

包含 `id1` 和 `id2` 的[Kronecker 积]的新矩阵。

另见

[matrix.new()][matrix.mult()][str.tostring()][table.new()]

###### matrix.max()

2过载



该函数返回矩阵元素中的最大值。

语法和重载

[`matrix.max(id) → series float`][`matrix.max(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.max()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the maximum value in the matrix.
var x = matrix.max(m)

plot(x, 'Matrix maximum value')
```

返回值

`id` 矩阵的最大值。

另见

[matrix.new()][matrix.min()][matrix.avg()][matrix.sort()]

###### matrix.median()

2过载



该函数计算矩阵元素的 [中位数]（“中间”值）。

语法和重载

[`matrix.median(id) → series float`][`matrix.median(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.median()` Example")

// Create a 2x2 matrix.
m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the median of the matrix.
x = matrix.median(m)

plot(x, 'Median of the matrix')
```

备注

请注意，计算中位数时不考虑矩阵的`na`元素。

另见

[matrix.new()][matrix.mode()][matrix.sort()][matrix.avg()]

###### matrix.min()

2过载



`id` 矩阵中的最小值。

语法和重载

[`matrix.min(id) → series float`][`matrix.min(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.min()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the minimum value from the matrix.
var x = matrix.min(m)

plot(x, 'Matrix minimum value')
```

返回值

`id` 矩阵中的最小值。

另见

[matrix.new()][matrix.max()][matrix.avg()][matrix.sort()]

###### matrix.mode()

2过载



该函数计算矩阵的[众数`，这是矩阵元素中出现频率最高的值。 当有多个值同样频繁地出现时，该函数返回这些值中的最小值。

语法和重载

[`matrix.mode(id) → series float`][`matrix.mode(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.mode()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 0)
matrix.set(m, 0, 1, 0)
matrix.set(m, 1, 0, 1)
matrix.set(m, 1, 1, 1)

// Get the mode of the matrix.
var x = matrix.mode(m)

plot(x, 'Mode of the matrix')
```

返回值

`id` 矩阵中出现频率最高的值。如果不存在，则返回最小值。

备注

请注意，在计算众数时不考虑矩阵的`na`元素。

另见

[matrix.new()][matrix.set()][matrix.median()][matrix.sort()][matrix.avg()]

###### matrix.mult()

4过载



该函数返回由矩阵`id1`和`id2`之间，或在`id1`矩阵和`id2`标量（数值）之间，或在`id1`矩阵和`id2`向量（值数组）之间[产品]生成的新矩阵

语法和重载

[`matrix.mult(id1, id2) → array`][`matrix.mult(id1, id2) → array`][`matrix.mult(id1, id2) → matrix`][`matrix.mult(id1, id2) → matrix`]

参数

**id1 (matrix<int>)** 第一个矩阵对象。

**id2 (array<int>)** 第二个矩阵对象、值或阵列。

两个矩阵的乘积



```
//@version=6
indicator("`matrix.mult()` Example 1")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 6x2 matrix containing values `5`.
    var m1 = matrix.new<float>(6, 2, 5)
    // Create a 2x3 matrix containing values `4`.
    // Note that it must have the same quantity of rows as there are columns in the first matrix.
    var m2 = matrix.new<float>(2, 3, 4)
    // Create a new matrix from the multiplication of the two matrices.
    var m3 = matrix.mult(m1, m2)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "Product of two matrices:")
    table.cell(t, 0, 1, str.tostring(m3))
```

矩阵和标量的乘积



```
//@version=6
indicator("`matrix.mult()` Example 2")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `4`.
    var m1 = matrix.new<float>(2, 3, 4)

    // Create a new matrix from the product of the two matrices.
    scalar = 5
    var m2 = matrix.mult(m1, scalar)

    // Display using a table.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Matrix 1:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 1, "x")
    table.cell(t, 2, 0, "Scalar:")
    table.cell(t, 2, 1, str.tostring(scalar))
    table.cell(t, 3, 1, "=")
    table.cell(t, 4, 0, "Matrix 2:")
    table.cell(t, 4, 1, str.tostring(m2))
```

矩阵和阵列向量的乘积



```
//@version=6
indicator("`matrix.mult()` Example 3")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `4`.
    var m1 = matrix.new<int>(2, 3, 4)

    // Create an array of three elements.
    var array<int> a = array.from(1, 1, 1)

    // Create a new matrix containing the product of the `m1` matrix and the `a` array.
    var m3 = matrix.mult(m1, a)

    // Display using a table.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Matrix 1:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 1, "x")
    table.cell(t, 2, 0, "Value:")
    table.cell(t, 2, 1, str.tostring(a, " "))
    table.cell(t, 3, 1, "=")
    table.cell(t, 4, 0, "Matrix 3:")
    table.cell(t, 4, 1, str.tostring(m3))
```

返回值

包含`id2`和`id1`乘积的新矩阵对象。

另见

[matrix.new()][matrix.sum()][matrix.diff()]

###### matrix.new<type>()



该函数创建一个新的矩阵对象。矩阵是包含行和列的二维数据结构。矩阵中的所有元素都必须是类型模板（“<type>”）中指定的类型。



```
matrix.new<type>(rows, columns, initial_value) → matrix<type>
```

参数

**rows (series int)** 矩阵的初始行数。可选。默认值为0。

**columns (series int)** 矩阵的初始列数。可选。默认值为0。

**initial_value (<matrix_type>)** 所有矩阵元素的初始值。可选。默认值为'na'。

创建具有相同初始值的元素矩阵



```
//@version=6
indicator("`matrix.new<type>()` Example 1")

// Create a 2x3 (2 rows x 3 columns) "int" matrix with values zero.
var m = matrix.new<int>(2, 3, 0)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
```

从阵列值创建矩阵



```
//@version=6
indicator("`matrix.new<type>()` Example 2")

// Function to create a matrix whose rows are filled with array values.
matrixFromArray(int rows, int columns, array<float> data) =>
    m = matrix.new<float>(rows, columns)
    for i = 0 to rows <= 0 ? na : rows - 1
        for j = 0 to columns <= 0 ? na : columns - 1
            matrix.set(m, i, j, array.get(data, i * columns + j))
    m

// Create a 3x3 matrix from an array of values.
var m1 = matrixFromArray(3, 3, array.from(1, 2, 3, 4, 5, 6, 7, 8, 9))
// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m1))
```

从 `input.text_area()` 字段创建矩阵



```
//@version=6
indicator("`matrix.new<type>()` Example 3")

// Function to create a matrix from a text string.
// Values in a row must be separated by a space. Each line is one row.
matrixFromInputArea(stringOfValues) =>
    var rowsArray = str.split(stringOfValues, "\n")
    var rows = array.size(rowsArray)
    var cols = array.size(str.split(array.get(rowsArray, 0), " "))
    var matrix = matrix.new<float>(rows, cols, na)
    row = 0
    for rowString in rowsArray
        col = 0
        values = str.split(rowString, " ")
        for val in values
            matrix.set(matrix, row, col, str.tonumber(val))
            col += 1
        row += 1
    matrix


stringInput = input.text_area("1 2 3\n4 5 6\n7 8 9")
var m = matrixFromInputArea(stringInput)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
```

从随机值创建矩阵



```
//@version=6
indicator("`matrix.new<type>()` Example 4")

// Function to create a matrix with random values (0.0 to 1.0).
matrixRandom(int rows, int columns)=>
    result = matrix.new<float>(rows, columns)
    for i = 0 to rows - 1
        for j = 0 to columns - 1
            matrix.set(result, i, j, math.random())
    result

// Create a 2x3 matrix with random values.
var m = matrixRandom(2, 3)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
```

返回值

新矩阵对象的ID。

另见

[matrix.set()][matrix.fill()][matrix.columns()][matrix.rows()][array.new()]

###### matrix.pinv()

2过载



该函数返回矩阵的[伪逆矩阵]。

语法和重载

[`matrix.pinv(id) → matrix`][`matrix.pinv(id) → matrix`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.pinv()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Pseudoinverse of the matrix.
    var m2 = matrix.pinv(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Pseudoinverse matrix:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

包含`id`矩阵的伪逆矩阵的新矩阵。

备注

该函数是使用基于矩阵奇异值分解的[Moore–Penrose]逆公式计算的。对于非奇异方阵，此函数返回[matrix.inv()]的结果。

另见

[matrix.new()][matrix.set()][matrix.inv()]

###### matrix.pow()

2过载



该函数通过自身的`power`次计算矩阵的乘积。

语法和重载

[`matrix.pow(id, power) → matrix`][`matrix.pow(id, power) → matrix`]

参数

**id (matrix<int/float>)** 一个矩阵对象。

**power (series int)** 矩阵将被自身相乘的次数。



```
//@version=6
indicator("`matrix.pow()` Example")

// Display using a table.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, 2)
    // Calculate the power of three of the matrix.
    var m2 = matrix.pow(m1, 3)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Matrix³:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

`id`矩阵与其本身`power`次的乘积。

另见

[matrix.new()][matrix.set()][matrix.mult()]

###### matrix.rank()



该函数计算矩阵的[秩`。



```
matrix.rank(id) → series int
```

参数

**id (any matrix type)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.rank()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Get the rank of the matrix.
    r = matrix.rank(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Rank of the matrix:")
    table.cell(t, 1, 1, str.tostring(r))
```

返回值

`id` 矩阵的秩。

另见

[matrix.new()][matrix.set()][str.tostring()]

###### matrix.remove_col()



该函数删除`id`矩阵的`column`索引处的列，并返回包含删除列值的阵列。



```
matrix.remove_col(id, column) → array<type>
```

参数

**id (any matrix type)** 一个矩阵对象。

**column (series int)** 要删除的列的索引。可选。默认值为[matrix.columns()]。



```
//@version=6
indicator("matrix_remove_col", overlay = true)

// Create a 2x2 matrix with ones.
var matrixOrig = matrix.new<int>(2, 2, 1)

// Set values to the 'matrixOrig' matrix.
matrix.set(matrixOrig, 0, 1, 2)
matrix.set(matrixOrig, 1, 0, 3)
matrix.set(matrixOrig, 1, 1, 4)


// Create a copy of the 'matrixOrig' matrix.
matrixCopy = matrix.copy(matrixOrig)

// Remove the first column from the `matrixCopy` matrix.
arr = matrix.remove_col(matrixCopy, 0)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 3, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(matrixOrig))
    table.cell(t, 1, 0, "Removed Elements:")
    table.cell(t, 1, 1, str.tostring(arr))
    table.cell(t, 2, 0, "Result Matrix:")
    table.cell(t, 2, 1, str.tostring(matrixCopy))
```

返回值

一个阵列，包含从 `id` 矩阵中删除的列元素。

备注

行和列的索引从零开始。声明具有显式维度的矩阵比通过添加或删除列来构建矩阵要高效得多。删除一列也比使用[matrix.remove_row()]函数删除一行要慢得多。

另见

[matrix.new()][matrix.set()][matrix.copy()][matrix.remove_row()]

###### matrix.remove_row()



该函数删除 `row` 矩阵的 `id` 索引处的行，并返回一个包含删除行的值的阵列。



```
matrix.remove_row(id, row) → array<type>
```

参数

**id (any matrix type)** 一个矩阵对象。

**row (series int)** 要删除的行的索引。可选。默认值为[matrix.rows()]。



```
//@version=6
indicator("matrix_remove_row", overlay = true)

// Create a 2x2 "int" matrix containing values `1`.
var matrixOrig = matrix.new<int>(2, 2, 1)

// Set values to the 'matrixOrig' matrix.
matrix.set(matrixOrig, 0, 1, 2)
matrix.set(matrixOrig, 1, 0, 3)
matrix.set(matrixOrig, 1, 1, 4)

// Create a copy of the 'matrixOrig' matrix.
matrixCopy = matrix.copy(matrixOrig)

// Remove the first row from the matrix `matrixCopy`.
arr = matrix.remove_row(matrixCopy, 0)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 3, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(matrixOrig))
    table.cell(t, 1, 0, "Removed Elements:")
    table.cell(t, 1, 1, str.tostring(arr))
    table.cell(t, 2, 0, "Result Matrix:")
    table.cell(t, 2, 1, str.tostring(matrixCopy))
```

返回值

一个阵列，包含从 `id` 矩阵中删除的行的元素。

备注

行和列的索引从零开始。声明具有显式维度的矩阵比通过添加或删除行来构建矩阵要高效得多。

另见

[matrix.new()][matrix.set()][matrix.copy()][matrix.remove_col()]

###### matrix.reshape()



该函数将 `id` 矩阵重建为 `rows` x `cols` 维度。



```
matrix.reshape(id, rows, columns) → void
```

参数

**id (any matrix type)** 一个矩阵对象。

**rows (series int)** 重构矩阵的行数。

**columns (series int)** 重构矩阵的列数。



```
//@version=6
indicator("`matrix.reshape()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix.
    var m1 = matrix.new<float>(2, 3)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 0, 2, 3)
    matrix.set(m1, 1, 0, 4)
    matrix.set(m1, 1, 1, 5)
    matrix.set(m1, 1, 2, 6)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)

    // Reshape the copy to a 3x2.
    matrix.reshape(m2, 3, 2)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Reshaped matrix:")
    table.cell(t, 1, 1, str.tostring(m2))
```

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.add_row()][matrix.add_col()]

###### matrix.reverse()



该函数反转矩阵`id`中的行和列的顺序。第一行和第一列成为最后一个，最后一个成为第一个。



```
matrix.reverse(id) → void
```

参数

**id (any matrix type)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.reverse()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Copy the matrix to a new one.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Copy matrix elements to a new matrix.
    var m2 = matrix.copy(m1)

    // Reverse the `m2` copy of the original matrix.
    matrix.reverse(m2)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Reversed matrix:")
    table.cell(t, 1, 1, str.tostring(m2))
```

另见

[matrix.new()][matrix.set()][matrix.columns()][matrix.rows()][matrix.reshape()]

###### matrix.row()



该函数从矩阵行的元素创建一个一维阵列。



```
matrix.row(id, row) → array<type>
```

参数

**id (any matrix type)** 一个矩阵对象。

**row (series int)** 所需行的索引。



```
//@version=6
indicator("`matrix.row()` Example", "", true)

// Create a 2x3 "float" matrix from `hlc3` values.
m = matrix.new<float>(2, 3, hlc3)

// Return an array with the values of the first row of the matrix.
a = matrix.row(m, 0)

// Plot the first value from the array `a`.
plot(array.get(a, 0))
```

返回值

包含`row`矩阵的`id`值的阵列ID。

备注

行的索引从0开始。

另见

[matrix.new()][matrix.get()][array.get()][matrix.col()][matrix.rows()]

###### matrix.rows()



该函数返回矩阵中的行数。



```
matrix.rows(id) → series int
```

参数

**id (any matrix type)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.rows()` Example")

// Create a 2x6 matrix with values `0`.
var m = matrix.new<int>(2, 6, 0)

// Get the quantity of rows in the matrix.
var x = matrix.rows(m)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, "Rows: " + str.tostring(x) + "\n" + str.tostring(m))
```

返回值

矩阵`id`中的行数。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.row()]

###### matrix.set()



该函数将`value`分配给`row`矩阵的`column`和`id`处的元素。



```
matrix.set(id, row, column, value) → void
```

参数

**id (any matrix type)** 一个矩阵对象。

**row (series int)** 要修改的元素的行索引。

**column (series int)** 要修改的元素的列索引。

**value (series <type of the matrix's elements>)** 要设置的新值。



```
//@version=6
indicator("`matrix.set()` Example")

// Create a 2x3 "int" matrix containing values `4`.
m = matrix.new<int>(2, 3, 4)

// Replace the value of element at row 1 and column 2 with value `3`.
matrix.set(m, 0, 1, 3)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
```

另见

[matrix.new()][matrix.get()][matrix.columns()][matrix.rows()]

###### matrix.sort()



该函数按照`id`中值的排序顺序重新排列`column`矩阵中的行。



```
matrix.sort(id, column, order) → void
```

参数

**id (matrix<int/float/string>)** 要排序的矩阵对象。

**column (series int)** 其排序值确定行的新顺序的列的索引。可选的。默认值为 0。

**order (series sort_order)** 排序顺序。可能的值：[order.ascending]（默认）、[order.descending]。



```
//@version=6
indicator("`matrix.sort()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<float>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 3)
    matrix.set(m1, 0, 1, 4)
    matrix.set(m1, 1, 0, 1)
    matrix.set(m1, 1, 1, 2)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)
    // Sort the rows of `m2` using the default arguments (first column and ascending order).
    matrix.sort(m2)

    // Display using a table.
    if barstate.islastconfirmedhistory
        var t = table.new(position.top_right, 2, 2, color.green)
        table.cell(t, 0, 0, "Original matrix:")
        table.cell(t, 0, 1, str.tostring(m1))
        table.cell(t, 1, 0, "Sorted matrix:")
        table.cell(t, 1, 1, str.tostring(m2))
```

另见

[matrix.new()][matrix.max()][matrix.min()][matrix.avg()]

###### matrix.submatrix()



该函数提取指定索引内的`id`矩阵的子矩阵。



```
matrix.submatrix(id, from_row, to_row, from_column, to_column) → matrix<type>
```

参数

**id (any matrix type)** 一个矩阵对象。

**from_row (series int)** 将开始提取的行的索引（包括）。可选。默认值为 0。

**to_row (series int)** 提取将结束的行的索引（不包括在内）。可选。默认值为[matrix.rows()]。

**from_column (series int)** 将开始提取的列索引（包括）。可选。默认值为 0。

**to_column (series int)** 提取将结束的列的索引（不包括在内）。可选。默认值为[matrix.columns()]。



```
//@version=6
indicator("`matrix.submatrix()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix matrix with values `0`.
    var m1 = matrix.new<int>(2, 3, 0)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 0, 2, 3)
    matrix.set(m1, 1, 0, 4)
    matrix.set(m1, 1, 1, 5)
    matrix.set(m1, 1, 2, 6)

    // Create a 2x2 submatrix of the `m1` matrix.
    var m2 = matrix.submatrix(m1, 0, 2, 1, 3)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Submatrix:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

一个新的矩阵对象，包含由`from_row`、`to_row`、`from_column`和`to_column`索引定义的`id`矩阵的子矩阵。

备注

行和列的索引从零开始。

另见

[matrix.new()][matrix.set()][matrix.row()][matrix.col()][matrix.reshape()]

###### matrix.sum()

2过载



该函数返回一个新矩阵，该新矩阵由两个矩阵`id1`和`id2`，或`id1`矩阵和`id2`标量（数值）的[和]相加而成。

语法和重载

[`matrix.sum(id1, id2) → matrix`][`matrix.sum(id1, id2) → matrix`]

参数

**id1 (matrix<int>)** 第一个矩阵对象。

**id2 (series int/float/matrix<int>)** 第二个矩阵对象，或标量值。

两个矩阵之和



```
//@version=6
indicator("`matrix.sum()` Example 1")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `5`.
    var m1 = matrix.new<float>(2, 3, 5)
    // Create a 2x3 matrix containing values `4`.
    var m2 = matrix.new<float>(2, 3, 4)
    // Create a new matrix that sums matrices `m1` and `m2`.
    var m3 = matrix.sum(m1, m2)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "Sum of two matrices:")
    table.cell(t, 0, 1, str.tostring(m3))
```

矩阵和标量之和



```
//@version=6
indicator("`matrix.sum()` Example 2")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix with values `4`.
    var m1 = matrix.new<float>(2, 3, 4)

    // Create a new matrix containing the sum of the `m1` matrix with the "int" value `1`.
    var m2 = matrix.sum(m1, 1)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "Sum of a matrix and a scalar:")
    table.cell(t, 0, 1, str.tostring(m2))
```

返回值

包含`id2`和`id1`之和的新矩阵对象。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.swap_columns()



该函数交换 `column1` 矩阵中索引 `column2` 和 `id` 的列。



```
matrix.swap_columns(id, column1, column2) → void
```

参数

**id (any matrix type)** 一个矩阵对象。

**column1 (series int)** 要交换的第一列的索引。

**column2 (series int)** 要交换的第二列的索引。



```
//@version=6
indicator("`matrix.swap_columns()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix with ‘na’ values.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)

    // Swap the first and second columns of the matrix copy.
    matrix.swap_columns(m2, 0, 1)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Swapped columns in copy:")
    table.cell(t, 1, 1, str.tostring(m2))
```

备注

行和列的索引从零开始。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.swap_rows()



该函数交换 `row1` 矩阵中索引 `row2` 和 `id` 的行。



```
matrix.swap_rows(id, row1, row2) → void
```

参数

**id (any matrix type)** 一个矩阵对象。

**row1 (series int)** 要交换的第一行的索引。

**row2 (series int)** 要交换的第二行的索引。



```
//@version=6
indicator("`matrix.swap_rows()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 3x2 matrix with ‘na’ values.
    var m1 = matrix.new<int>(3, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)
    matrix.set(m1, 2, 0, 5)
    matrix.set(m1, 2, 1, 6)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)

    // Swap the first and second rows of the matrix copy.
    matrix.swap_rows(m2, 0, 1)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Swapped rows in copy:")
    table.cell(t, 1, 1, str.tostring(m2))
```

备注

行和列的索引从零开始。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.swap_columns()]

###### matrix.trace()

2过载



该函数计算矩阵的 [迹`（主对角线元素的总和）。

语法和重载

[`matrix.trace(id) → series float`][`matrix.trace(id) → series int`]

参数

**id (matrix<int/float>)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.trace()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Get the trace of the matrix.
    tr = matrix.trace(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Trace of the matrix:")
    table.cell(t, 1, 1, str.tostring(tr))
```

返回值

`id` 矩阵的迹。

另见

[matrix.new()][matrix.get()][matrix.set()][matrix.columns()][matrix.rows()]

###### matrix.transpose()



该函数会创建一个新的[转置]版本的 `id`。这将交换每个元素的行和列索引。



```
matrix.transpose(id) → matrix<type>
```

参数

**id (any matrix type)** 一个矩阵对象。



```
//@version=6
indicator("`matrix.transpose()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<float>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Create a transpose of the matrix.
    var m2 = matrix.transpose(m1)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Transposed matrix:")
    table.cell(t, 1, 1, str.tostring(m2))
```

返回值

包含`id`矩阵的转置版本的新矩阵。

另见

[matrix.new()][matrix.set()][matrix.columns()][matrix.rows()][matrix.reshape()][matrix.reverse()]

###### max_bars_back()



函数设置可用于给定内置或用户变量的历史引用的最大柱数。 当运算符'[]'应用于变量时 - 它是对该变量的历史值的引用。

如果运算符“[]”的参数是编译时常量值（例如“v[10]”、“close[500]”），则无需对该变量使用“max_bars_back”函数。Pine Script®编译器将使用该常量值作为历史缓冲区大小。

如果运算符“[]”的参数是在运行时计算的值（例如“v[i]”，其中“i”是系列变量），则Pine Script®会尝试在运行时自动检测历史缓冲区大小。有时它会失败并且脚本在运行时崩溃，因为它最终引用了缓冲区之外的历史值。在这种情况下，您应该使用“max_bars_back”手动解决该问题。



```
max_bars_back(var, num) → void
```

参数

**var (series int/float/bool/color/label/line)** 应为其调整历史记录缓冲区的系列变量标识符。 可能的值包括：'open'，'high'，'low'，'close'，'volume'，'time'或任何用户定义的变量id。

**num (const int)** 历史缓冲区大小，即变量 'var' 可以引用的K线数。



```
//@version=6
indicator("max_bars_back")
close_() => close
depth() => 400
d = depth()
v = close_()
max_bars_back(v, 500)
out = if bar_index > 0
    v[d]
else
    v
plot(out)
```

返回值

void

备注

目前 'max_bars_back' 不能应用于像 'hl2'、'hlc3'、'ohlc4' 这样的内置函数。请在此处使用多个“max_bars_back”调用作为解决方法（例如，您应该调用该函数两次，而不是单个“max_bars_back(hl2, 100)”：“max_bars_back(high, 100), max_bars_back(low, 100)”）。

如果使用[indicator()]或[strategy()]'max_bars_back'参数，指标中的所有变量都会受到影响。这可能会导致内存使用过多并导致运行时问题。如果可能（即当原因是变量而不是函数时），请改用[max_bars_back()]函数。

另见

[indicator()]

###### minute()





```
minute(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的unix时间。

**timezone (series string)** 允许将返回值调整为以UTC/GMT表示法（例如，“UTC-5”、“GMT+0530”）或IANA时区数据库名称（例如，“America/New_York”）指定的时区。可选。默认值为[syminfo.timezone]。

返回值

提供UNIX时间的分钟(交换时区)。

备注

UNIX时间是自1970年1月1日UTC 00:00:00起已经过去的毫秒数。

另见

[minute][time()][year()][month()][dayofmonth()][dayofweek()][hour()][second()]

###### month()





```
month(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的unix时间。

**timezone (series string)** 允许将返回值调整为以UTC/GMT表示法（例如，“UTC-5”、“GMT+0530”）或IANA时区数据库名称（例如，“America/New_York”）指定的时区。可选。默认值为[syminfo.timezone]。

返回值

提供UNIX时间的月份(交换时区)。

备注

UNIX时间是自1970年1月1日UTC 00:00:00起已经过去的毫秒数。

请注意，此函数根据K线的打开时间返回月份。对于隔夜交易时段（例如，EURUSD周一交易时段从周日17:00 UTC-4开始），该值可以比交易日的月份低1。

另见

[month][time()][year()][dayofmonth()][dayofweek()][hour()][minute()][second()]

###### na()

2过载



测试 `x` 是否为`na`。

语法和重载

[`na(x) → simple bool`][`na(x) → series bool`]

参数

**x (simple int/float)** 要测试的值。



```
//@version=6
indicator("na")
// Use the `na()` function to test for `na`.
plot(na(close[1` ? close : close[1`
// ALTERNATIVE
// `nz()` also tests `close[1]` for `na`. It returns `close[1]` if it is not `na`, and `close` if it is.
plot(nz(close[1], close))
```

返回值

如果`x`是`na`，则返回`true`，否则返回`false`。

另见

`na`[fixnan()][nz()]

###### nz()

6过载



用特定类型的默认值或指定的替换值替换`na`（未定义）值。

语法和重载

[`nz(source, replacement) → simple color`][`nz(source, replacement) → simple int`][`nz(source, replacement) → series color`][`nz(source, replacement) → series int`][`nz(source, replacement) → simple float`][`nz(source, replacement) → series float`]

参数

**source (simple color)** 要处理的源系列。

**replacement (simple color)** 可选。函数用于替换`source`系列中的`na`值的值。默认值取决于`source`的类型：`0`表示“int”，`0.0`表示“float”，`#00000000` 表示“color”。



```
//@version=6
indicator("nz", overlay=true)
plot(nz(ta.sma(close, 100)))
```

返回值

如果不是 `na`，`source`的值。如果`source`的值为`na`，则返回零；如果使用1，则返回`replacement`参数。

另见

`na`[na()][fixnan()]

###### plot()



在图表上绘制一系列数据。



```
plot(series, title, color, linewidth, style, trackprice, histbase, offset, join, editable, show_last, display, format, precision, force_overlay, linestyle) → plot
```

参数

**series (series int/float)** 要绘制的数据系列。 必要参数。

**title (const string)** 绘图标题。

**color (series color)** 绘图的颜色。您可以使用如'color = red'或'color =＃ff001a'的常量以及如 'color = close >= open ? green : red'的复杂表达式。 可选参数。

**linewidth (input int)** 绘制线的宽度。默认值为1。不适用于每种样式。

**style (input plot_style)** 绘图类型。可能的值为：[plot.style_line]、[plot.style_stepline]、[plot.style_stepline_diamond]、[plot.style_histogram]、[plot.style_cross]、[plot.style_area]、[plot.style_columns]、[plot.style_circles]、[plot.style_linebr]、[plot.style_areabr]、[plot.style_steplinebr]。 默认值为[plot.style_line]。

**trackprice (input bool)** 如果为true，则水平价格线将显示在最后一个指标值的水平。默认为false。

**histbase (input int/float)** 以[plot.style_histogram]，[plot.style_columns]或[plot.style_area]样式绘制图时，用作参考水平的价格值。默认值为0.0。

**offset (simple int)** 在k线特定数量上向左或向右移动绘图。 默认值为0。

**join (input bool)** 如果为true，则绘图点将与线条相加，仅适用于[plot.style_cross]和[plot.style_circles]样式。 默认值为false。

**editable (input bool)** 如果为true，则绘图样式可在格式对话框中编辑。 默认值为true。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**display (input plot_display)** 控制绘图信息的显示位置。显示选项支持加法和减法，这意味着使用`display.all - display.status_line`将在除脚本状态行之外的所有位置显示绘图信息。 `display.price_scale + display.status_line`将仅在价格坐标和状态行中显示绘图。当`display`参数，例如`display.price_scale`，具有用户控制的图表设置等效项时，仅当所有设置允许时才会显示相关绘图信息。 可能的值：[display.none]、[display.pane]、[display.data_window]、[display.price_scale]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**format (input string)** 确定脚本是否将绘图值的格式设置为价格、百分比或数量值。传递给此参数的参数取代[indicator()]和[strategy()]函数的`format`参数。可选。默认值是[indicator()]/[strategy()]函数使用的`format`值。可能的值：[format.price]、[format.percent]、[format.volume]。

**precision (input int)** 绘图值在图表窗格的y轴、脚本的状态行和数据窗口上显示的小数点后的位数。接受小于或等于16的非负整数。传递给此参数的实参取代[indicator()]和[strategy()]函数的`precision`参数。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选；默认值是[indicator()]/[strategy()]函数使用的`precision`值。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。

**linestyle (input plot_line_style)** 可选。用于显示线条的绘图样式的修饰符。它指定绘制的线条是实线 `plot.linestyle_solid`、虚线 `plot.linestyle_dashed` 还是点线 `plot.linestyle_dotted`。仅当函数使用以下`style`参数之一时，此修饰符才适用：[plot.style_line]、[plot.style_linebr]、[plot.style_stepline]、[plot.style_stepline_diamond]和[plot.style_area]。默认值为[plot.linestyle_solid]。



```
//@version=6
indicator("plot")
plot(high+low, title='Title', color=color.new(#00ffaa, 70), linewidth=2, style=plot.style_area, offset=15, trackprice=true)

// You may fill the background between any two plots with a fill() function:
p1 = plot(open)
p2 = plot(close)
fill(p1, p2, color=color.new(color.green, 90))
```

返回值

可用于[fill()]的绘图对象。

另见

[plotshape()][plotchar()][plotarrow()][barcolor()][bgcolor()][fill()]

###### plotarrow()



在图表上绘制向上和向下箭头：向上箭头绘制在每个正值指示器上，而向下箭头绘制在每个负值上。 如果指标返回`na`，则不会绘制箭头。 箭头具有不同的高度，指标值越肯定，绘制箭头越长。



```
plotarrow(series, title, colorup, colordown, offset, minheight, maxheight, editable, show_last, display, format, precision, force_overlay) → void
```

参数

**series (series int/float)** 要绘制成箭头的数据系列。 必要参数。

**title (const string)** 绘图标题。

**colorup (series color)** 向上箭头的颜色。可选参数。

**colordown (series color)** 向下箭头的颜色。可选参数。

**offset (simple int)** 在K线特定数量上向左或向右移动箭头。 默认值为0。

**minheight (input int)** 以像素为单位最小可能的箭头高度。默认值为5。

**maxheight (input int)** 以像素为单位的最大可能的箭头高度。默认值为100

**editable (input bool)** 如果为true，则plotarrow样式可在格式对话框中编辑。 默认值为true。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**display (input plot_display)** 控制绘图信息的显示位置。显示选项支持加法和减法，这意味着使用`display.all - display.status_line`将在除脚本状态行之外的所有位置显示绘图信息。 `display.price_scale + display.status_line`将仅在价格坐标和状态行中显示绘图。当`display`参数，例如`display.price_scale`，具有用户控制的图表设置等效项时，仅当所有设置允许时才会显示相关绘图信息。 可能的值：[display.none]、[display.pane]、[display.data_window]、[display.price_scale]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**format (input string)** 确定脚本是否将绘图值的格式设置为价格、百分比或数量值。传递给此参数的参数取代[indicator()]和[strategy()]函数的`format`参数。可选。默认值是[indicator()]/[strategy()]函数使用的`format`值。可能的值：[format.price]、[format.percent]、[format.volume]。

**precision (input int)** 绘图值在图表窗格的y轴、脚本的状态行和数据窗口上显示的小数点后的位数。接受小于或等于16的非负整数。传递给此参数的实参取代[indicator()]和[strategy()]函数的`precision`参数。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选；默认值是[indicator()]/[strategy()]函数使用的`precision`值。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("plotarrow example", overlay=true)
codiff = close - open
plotarrow(codiff, colorup=color.new(color.teal,40), colordown=color.new(color.orange, 40))
```

备注

使用 [plotarrow()] 功能与 'overlay=true' [indicator()] 参数结合!

另见

[plot()][plotshape()][plotchar()][barcolor()][bgcolor()]

###### plotbar()



在图表上绘制ohlc蜡烛图。



```
plotbar(open, high, low, close, title, color, editable, show_last, display, format, precision, force_overlay) → void
```

参数

**open (series int/float)** 数据开放系列用作k线开放值。必要参数。

**high (series int/float)** 高系列数据用作k线的高值。必要参数。

**low (series int/float)** 低系列数据作为k线低值。必要参数。

**close (series int/float)** 关闭系列数据作为关闭k线的值。必要参数。

**title (const string)** 划分栏的标题。 可选参数。

**color (series color)** ohlc线的颜色。 您可以使用'color = color.red'或'color =＃ff001a'等常量以及'color = close> = open等复杂表达式？ color.green：color.red'。 可选参数。

**editable (input bool)** 如果为true，则plotbar样式可在格式对话框中编辑。默认值true。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**display (input plot_display)** 控制绘图信息的显示位置。显示选项支持加法和减法，这意味着使用`display.all - display.status_line`将在除脚本状态行之外的所有位置显示绘图信息。 `display.price_scale + display.status_line`将仅在价格坐标和状态行中显示绘图。当`display`参数，例如`display.price_scale`，具有用户控制的图表设置等效项时，仅当所有设置允许时才会显示相关绘图信息。 可能的值：[display.none]、[display.pane]、[display.data_window]、[display.price_scale]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**format (input string)** 确定脚本是否将绘图值的格式设置为价格、百分比或数量值。传递给此参数的参数取代[indicator()]和[strategy()]函数的`format`参数。可选。默认值是[indicator()]/[strategy()]函数使用的`format`值。可能的值：[format.price]、[format.percent]、[format.volume]。

**precision (input int)** 绘图值在图表窗格的y轴、脚本的状态行和数据窗口上显示的小数点后的位数。接受小于或等于16的非负整数。传递给此参数的实参取代[indicator()]和[strategy()]函数的`precision`参数。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选；默认值是[indicator()]/[strategy()]函数使用的`precision`值。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("plotbar example", overlay=true)
plotbar(open, high, low, close, title='Title', color = open < close ? color.green : color.red)
```

备注

如果开高低收都是NaN，那么K线不需要显示出来。

开、高、低、收的最大值将被设置为“高”，最小值被设置为“低”。

另见

[plotcandle()]

###### plotcandle()



在图表上绘制蜡烛。



```
plotcandle(open, high, low, close, title, color, wickcolor, editable, show_last, bordercolor, display, format, precision, force_overlay) → void
```

参数

**open (series int/float)** 数据开放系列用作蜡烛开放值。必要参数。

**high (series int/float)** 高系列数据用作蜡烛的高值。必要参数。

**low (series int/float)** 低系列数据被用作蜡烛的低值。 必要参数。

**close (series int/float)** 关闭系列数据作为关闭k线的值。 必要参数。

**title (const string)** plotcandle的标题。 可选参数。

**color (series color)** 蜡烛的颜色。您可以使用如'color = red'或'color =＃ff001a'的常量以及像'color = close >= open ? green : red'的复杂表达式。可选参数。

**wickcolor (series color)** 蜡烛灯芯的颜色。一个可选参数。

**editable (input bool)** 如果为true，则plotcandle样式可在格式对话框中编辑。 默认值为true。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**bordercolor (series color)** 蜡烛的边框颜色。一个可选参数。

**display (input plot_display)** 控制绘图信息的显示位置。显示选项支持加法和减法，这意味着使用`display.all - display.status_line`将在除脚本状态行之外的所有位置显示绘图信息。 `display.price_scale + display.status_line`将仅在价格坐标和状态行中显示绘图。当`display`参数，例如`display.price_scale`，具有用户控制的图表设置等效项时，仅当所有设置允许时才会显示相关绘图信息。 可能的值：[display.none]、[display.pane]、[display.data_window]、[display.price_scale]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**format (input string)** 确定脚本是否将绘图值的格式设置为价格、百分比或数量值。传递给此参数的参数取代[indicator()]和[strategy()]函数的`format`参数。可选。默认值是[indicator()]/[strategy()]函数使用的`format`值。可能的值：[format.price]、[format.percent]、[format.volume]。

**precision (input int)** 绘图值在图表窗格的y轴、脚本的状态行和数据窗口上显示的小数点后的位数。接受小于或等于16的非负整数。传递给此参数的实参取代[indicator()]和[strategy()]函数的`precision`参数。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选；默认值是[indicator()]/[strategy()]函数使用的`precision`值。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("plotcandle example", overlay=true)
plotcandle(open, high, low, close, title='Title', color = open < close ? color.green : color.red, wickcolor=color.black)
```

备注

如果开高低收都是NaN，那么K线不需要显示出来。

开、高、低、收的最大值将被设置为“高”，最小值被设置为“低”。

另见

[plotbar()]

###### plotchar()



在图表上使用任何给定的Unicode字符绘制可视形状。



```
plotchar(series, title, char, location, color, offset, text, textcolor, editable, size, show_last, display, format, precision, force_overlay) → void
```

参数

**series (series int/float/bool)** 作为形状绘制的一系列数据 。 除了[location.absolute]之外，系列被视为所有位置值的一系列布尔值。 必要参数。

**title (const string)** 绘图标题。

**char (input string)** 作为视觉形状使用的字符

**location (input string)** 图表上的形状位置。可能的值为：[location.abovebar]、[location.belowbar]、[location.top]、[location.bottom]、[location.absolute]。默认值为[location.abovebar]。

**color (series color)** 形状的颜色。 您可以使用如'color = red'或'color =＃ff001a'的常量以及如 'color = close >= open ? green : red'的复杂表达式。 可选参数。

**offset (simple int)** 在k线特定数量上向左或向右移动形状。 默认值为0。

**text (const string)** Text to display with the shape. You can use multiline text, to separate lines use '\n' escape sequence. Example: 'line one\nline two'.

**textcolor (series color)** 文字的颜色。 您可以使用如 'textcolor=red' 或'textcolor=#ff001a' 的常量，以及如'textcolor = close >= open ? green : red'的复杂表达式。 可选参数。

**editable (input bool)** 如果为true，则plotchar样式可在格式对话框中编辑。 默认值为true。

**size (const string)** 图表上的字符大小。可能的值为：[size.auto]、[size.tiny]、[size.small]、[size.normal]、[size.large]、[size.huge]。默认为[size.auto]。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**display (input plot_display)** 控制绘图信息的显示位置。显示选项支持加法和减法，这意味着使用`display.all - display.status_line`将在除脚本状态行之外的所有位置显示绘图信息。 `display.price_scale + display.status_line`将仅在价格坐标和状态行中显示绘图。当`display`参数，例如`display.price_scale`，具有用户控制的图表设置等效项时，仅当所有设置允许时才会显示相关绘图信息。 可能的值：[display.none]、[display.pane]、[display.data_window]、[display.price_scale]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**format (input string)** 确定脚本是否将绘图值的格式设置为价格、百分比或数量值。传递给此参数的参数取代[indicator()]和[strategy()]函数的`format`参数。可选。默认值是[indicator()]/[strategy()]函数使用的`format`值。可能的值：[format.price]、[format.percent]、[format.volume]。

**precision (input int)** 绘图值在图表窗格的y轴、脚本的状态行和数据窗口上显示的小数点后的位数。接受小于或等于16的非负整数。传递给此参数的实参取代[indicator()]和[strategy()]函数的`precision`参数。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选；默认值是[indicator()]/[strategy()]函数使用的`precision`值。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("plotchar example", overlay=true)
data = close >= open
plotchar(data, char='❄')
```

备注

使用 [plotchar()] 功能与 'overlay=true' [indicator()] 参数结合!

另见

[plot()][plotshape()][plotarrow()][barcolor()][bgcolor()]

###### plotshape()



在图表上绘制可视形状。



```
plotshape(series, title, style, location, color, offset, text, textcolor, editable, size, show_last, display, format, precision, force_overlay) → void
```

参数

**series (series int/float/bool)** 作为形状绘制的一系列数据 。 除了[location.absolute]之外，系列被视为所有位置值的一系列布尔值。 必要参数。

**title (const string)** 绘图标题。

**style (input string)** 绘图类型。可能的值为：[shape.xcross]、[shape.cross]、[shape.triangleup]、[shape.triangledown]、[shape.flag]、[shape.circle]、[shape.arrowup]、[shape.arrowdown]、[shape.labelup]、[shape.labeldown]、[shape.square]、[shape.diamond]。 默认值为[shape.xcross]。

**location (input string)** 图表上的形状位置。可能的值为：[location.abovebar]、[location.belowbar]、[location.top]、[location.bottom]、[location.absolute]。默认值为[location.abovebar]。

**color (series color)** 形状的颜色。 您可以使用如'color = red'或'color =＃ff001a'的常量以及如 'color = close >= open ? green : red'的复杂表达式。 可选参数。

**offset (simple int)** 在k线特定数量上向左或向右移动形状。 默认值为0。

**text (const string)** Text to display with the shape. You can use multiline text, to separate lines use '\n' escape sequence. Example: 'line one\nline two'.

**textcolor (series color)** 文字的颜色。 您可以使用如 'textcolor=red' 或'textcolor=#ff001a' 的常量，以及如'textcolor = close >= open ? green : red'的复杂表达式。 可选参数。

**editable (input bool)** 如果为true，则plotshape样式可在格式对话框中编辑。 默认值为true。

**size (const string)** 图表上的形状大小。可能的值为：[size.auto]、[size.tiny]、[size.small]、[size.normal]、[size.large]、[size.huge]。默认为[size.auto]。

**show_last (input int)** 可选。从最近的K线开始向后计数，函数可以绘制的K线数量。

**display (input plot_display)** 控制绘图信息的显示位置。显示选项支持加法和减法，这意味着使用`display.all - display.status_line`将在除脚本状态行之外的所有位置显示绘图信息。 `display.price_scale + display.status_line`将仅在价格坐标和状态行中显示绘图。当`display`参数，例如`display.price_scale`，具有用户控制的图表设置等效项时，仅当所有设置允许时才会显示相关绘图信息。 可能的值：[display.none]、[display.pane]、[display.data_window]、[display.price_scale]、[display.status_line]、[display.all]。可选。默认值为[display.all]。

**format (input string)** 确定脚本是否将绘图值的格式设置为价格、百分比或数量值。传递给此参数的参数取代[indicator()]和[strategy()]函数的`format`参数。可选。默认值是[indicator()]/[strategy()]函数使用的`format`值。可能的值：[format.price]、[format.percent]、[format.volume]。

**precision (input int)** 绘图值在图表窗格的y轴、脚本的状态行和数据窗口上显示的小数点后的位数。接受小于或等于16的非负整数。传递给此参数的实参取代[indicator()]和[strategy()]函数的`precision`参数。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选；默认值是[indicator()]/[strategy()]函数使用的`precision`值。

**force_overlay (const bool)** 如果是`true`，则绘制的结果将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("plotshape example 1", overlay=true)
data = close >= open
plotshape(data, style=shape.xcross)
```

备注

使用 [plotshape()] 功能与 'overlay=true' [indicator()] 参数结合!

另见

[plot()][plotchar()][plotarrow()][barcolor()][bgcolor()]

###### polyline.delete()



删除指定的[polyline]对象。如果`id`不存在，则无效。



```
polyline.delete(id) → void
```

参数

**id (series polyline)** 要删除的折线ID。

###### polyline.new()



创建一个新的[polyline]实例并将其显示在图表上，用线段顺序连接`points`数组中的所有点。绘图中的线段可以是直线或曲线，具体取决于`curved`参数。



```
polyline.new(points, curved, closed, xloc, line_color, fill_color, line_style, line_width, force_overlay) → series polyline
```

参数

**points (array<chart.point>)** 用于按顺序连接绘图的[chart.point]对象数组。

**curved (series bool)** 如果是`true`，绘图将使用曲线段连接`points`数组中的所有点。可选。默认值为`false`。

**closed (series bool)** 如果是`true`，则绘图还会将`points`数组中的第一个点连接到最后一个点，从而形成闭合的折线。可选。默认值为`false`。

**xloc (series string)** 确定折线将用于其x坐标的`points`数组中的[chart.point]对象的字段。如果是[xloc.bar_index]，折线将使用每个点的`index`字段。如果是[xloc.bar_time]，它将使用`time`字段。可选。默认值为[xloc.bar_index]。

**line_color (series color)** 线段的颜色。可选。默认值为[color.blue]。

**fill_color (series color)** 折线的填充颜色。可选。默认值为`na`。

**line_style (series string)** 折线的样式。可能的值：[line.style_solid]、[line.style_dotted]、[line.style_dashed]、[line.style_arrow_left]、[line.style_arrow_right]、[line.style_arrow_both]。可选。默认值为[line.style_solid]。

**line_width (series int)** 线段的宽度，以像素表示。可选。默认值为1。

**force_overlay (const bool)** 如果是`true`，则绘图将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("Polylines example", overlay = true)

//@variable If `true`, connects all points in the polyline with curved line segments.
bool curvedInput = input.bool(false, "Curve Polyline")
//@variable If `true`, connects the first point in the polyline to the last point.
bool closedInput = input.bool(true, "Close Polyline")
//@variable The color of the space filled by the polyline.
color fillcolor = input.color(color.new(color.blue, 90), "Fill Color")

// Time and price inputs for the polyline's points.
p1x = input.time(0,  "p1", confirm = true, inline = "p1")
p1y = input.price(0, "  ", confirm = true, inline = "p1")
p2x = input.time(0,  "p2", confirm = true, inline = "p2")
p2y = input.price(0, "  ", confirm = true, inline = "p2")
p3x = input.time(0,  "p3", confirm = true, inline = "p3")
p3y = input.price(0, "  ", confirm = true, inline = "p3")
p4x = input.time(0,  "p4", confirm = true, inline = "p4")
p4y = input.price(0, "  ", confirm = true, inline = "p4")
p5x = input.time(0,  "p5", confirm = true, inline = "p5")
p5y = input.price(0, "  ", confirm = true, inline = "p5")

if barstate.islastconfirmedhistory
    //@variable An array of `chart.point` objects for the new polyline.
    var points = array.new<chart.point>()
    // Push new `chart.point` instances into the `points` array.
    points.push(chart.point.from_time(p1x, p1y))
    points.push(chart.point.from_time(p2x, p2y))
    points.push(chart.point.from_time(p3x, p3y))
    points.push(chart.point.from_time(p4x, p4y))
    points.push(chart.point.from_time(p5x, p5y))
    // Add labels for each `chart.point` in `points`.
    l1p1 = label.new(points.get(0), text = "p1", xloc = xloc.bar_time, color = na)
    l1p2 = label.new(points.get(1), text = "p2", xloc = xloc.bar_time, color = na)
    l2p1 = label.new(points.get(2), text = "p3", xloc = xloc.bar_time, color = na)
    l2p2 = label.new(points.get(3), text = "p4", xloc = xloc.bar_time, color = na)
    // Create a new polyline that connects each `chart.point` in the `points` array, starting from the first.
    polyline.new(points, curved = curvedInput, closed = closedInput, fill_color = fillcolor, xloc = xloc.bar_time)
```

返回值

脚本可在其它`polyline.*()`函数中使用的新折线对象的ID。

另见

[chart.point.new()]

###### request.currency_rate()



提供每日汇率，可用于将以`from`货币表示的值，转换为另一个以`to`货币表示的值。



```
request.currency_rate(from, to, ignore_invalid_currency) → series float
```

参数

**from (series string)** 表示要转换值的货币。可能的值：包含[ISO 4217 格式]货币代码的三字母字符串（例如“USD”），或返回货币代码的内置变量之一，如[syminfo.currency]或[currency.USD]。

**to (series string)** 要转换值的货币。可能的值：包含[ISO 4217 格式]货币代码的三字母字符串（例如“USD”），或返回货币代码的内置变量之一，如[syminfo.currency]或[currency.USD]。

**ignore_invalid_currency (series bool)** 确定在无法计算两种货币之间的汇率时函数的行为：如果为`false`，脚本将停止并返回运行时错误；如果为`true`，该函数将返回`na`并继续执行。可选。默认值为`false`。



```
//@version=6
indicator("Close in British Pounds")
rate = request.currency_rate(syminfo.currency, "GBP")
plot(close * rate)
```

备注

如果`from`和`to`参数相等，则函数返回1。请注意，使用此变量/函数可能会导致[指标重绘]。

###### request.dividends()



请求指定商品的股息数据。



```
request.dividends(ticker, field, gaps, lookahead, ignore_invalid_symbol, currency) → series float
```

参数

**ticker (series string)** 商品代码。请注意，该商品代码应带有前缀。例如：“NASDAQ:AAPL”而不是“ AAPL”。使用[syminfo.ticker]将导致错误。请改用[syminfo.tickerid]。

**field (series string)** 输入字符串。可能的值包括：[dividends.net]、[dividends.gross]。默认值为[dividends.gross]。

**gaps (simple barmerge_gaps)** 请求数据的合并策略（请求数据自动与主系列OHLC数据合并）。可能的值：[barmerge.gaps_on]、[barmerge.gaps_off]。 [barmerge.gaps_on] — 请求的数据与可能的跳空（`na` 值）合并。 [barmerge.gaps_off] — 请求的数据连续无跳空地合并，所有跳空都用之前最接近的现有值填充。默认值为[barmerge.gaps_off]。

**lookahead (simple barmerge_lookahead)** 请求的数据位置的合并策略。可能的值：[barmerge.lookahead_on]、[barmerge.lookahead_off]。从版本3开始，默认值为[barmerge.lookahead_off]。请注意，实时行为是相同的，仅历史行为不同。

**ignore_invalid_symbol (input bool)** 一个可选参数。如果未找到指定的商品，则确定函数的行为：如果为 false，脚本将停止并返回运行时错误； 如果为true，函数将返回na并继续执行。默认值为false。

**currency (series string)** 商品的货币相关股息值（例如[dividends.gross]）要转换成的货币。转换率取决于最受欢迎交易所对应货币对的先前每日价值。如果没有交易所直接提供汇率，则使用价差商品。可能的值：表示有效货币代码的“字符串”（例如“USD”或“USDT”）或来自`currency.*`命名空间的常量（例如[currency.USD]或[currency.USDT]）。默认值为[syminfo.currency]。



```
//@version=6
indicator("request.dividends")
s1 = request.dividends("NASDAQ:BELFA")
plot(s1)
s2 = request.dividends("NASDAQ:BELFA", dividends.net, gaps=barmerge.gaps_on, lookahead=barmerge.lookahead_on)
plot(s2)
```

返回值

请求序列，如果指定商品没有股息数据，则为n/a。

另见

[request.earnings()][request.splits()][request.security()][syminfo.tickerid]

###### request.earnings()



请求指定商品的收益数据。



```
request.earnings(ticker, field, gaps, lookahead, ignore_invalid_symbol, currency) → series float
```

参数

**ticker (series string)** 商品代码。请注意，该商品代码应带有前缀。例如：“NASDAQ:AAPL”而不是“ AAPL”。使用[syminfo.ticker]将导致错误。请改用[syminfo.tickerid]。

**field (series string)** 输入字符串。可能的值包括：[earnings.actual]、[earnings.estimate]、[earnings.standardized]。默认值为[earnings.actual]。

**gaps (simple barmerge_gaps)** 请求数据的合并策略（请求数据自动与主系列OHLC数据合并）。可能的值：[barmerge.gaps_on]、[barmerge.gaps_off]。 [barmerge.gaps_on] — 请求的数据与可能的跳空（`na` 值）合并。 [barmerge.gaps_off] — 请求的数据连续无跳空地合并，所有跳空都用之前最接近的现有值填充。默认值为[barmerge.gaps_off]。

**lookahead (simple barmerge_lookahead)** 请求的数据位置的合并策略。可能的值：[barmerge.lookahead_on]、[barmerge.lookahead_off]。从版本3开始，默认值为[barmerge.lookahead_off]。请注意，实时行为是相同的，仅历史行为不同。

**ignore_invalid_symbol (input bool)** 一个可选参数。如果未找到指定的商品，则确定函数的行为：如果为 false，脚本将停止并返回运行时错误； 如果为true，函数将返回na并继续执行。默认值为false。

**currency (series string)** 商品的货币相关收益值（例如[earnings.actual]）要转换成的货币。转换率取决于最受欢迎交易所对应货币对的上一每日价值。如果没有交易所直接提供汇率，则使用价差商品。可能的值：表示有效货币代码的“字符串”（例如“USD”或“USDT”）或来自`currency.*`命名空间的常量（例如[currency.USD]或[currency.USDT]）。默认值为[syminfo.currency]。



```
//@version=6
indicator("request.earnings")
s1 = request.earnings("NASDAQ:BELFA")
plot(s1)
s2 = request.earnings("NASDAQ:BELFA", earnings.actual, gaps=barmerge.gaps_on, lookahead=barmerge.lookahead_on)
plot(s2)
```

返回值

请求序列，如果指定商品没有收益数据，则为n/a。

另见

[request.dividends()][request.splits()][request.security()][syminfo.tickerid]

###### request.economic()



请求商品的经济数据。经济数据包括国家经济状况（GDP、通货膨胀率等）或特定行业（钢铁生产、ICU病床等）的信息。



```
request.economic(country_code, field, gaps, ignore_invalid_symbol) → series float
```

参数

**country_code (series string)** 请求经济数据的国家（例如“美国”）或地区（例如“欧盟”）的代码。 [帮助中心文章]列出了国家及其代码。可获得信息的国家/地区因指标而异。[每个指标的帮助中心文章]列出了该指标适用的国家/地区。

**field (series string)** 请求的经济指标的代码（例如，“GDP”）。 [帮助中心文章]列出了指标及其代码。

**gaps (simple barmerge_gaps)** 指定如何在图表K线上合并返回值。可能的值：[barmerge.gaps_off]、[barmerge.gaps_on]。对于[barmerge.gaps_on]，值仅在首次从函数上下文中可用时出现在当前图表K线上，否则返回`na`（因此会出现“跳空”）。使用[barmerge.gaps_off]，原本存在的跳空将被返回的最新已知值填充，从而避免使用`na`值。可选。默认值为[barmerge.gaps_off]。

**ignore_invalid_symbol (input bool)** 确定在未找到指定商品时函数的行为：如果为`false`，则脚本将停止并返回运行时错误； 如果`true`，该函数将返回`na`并继续执行。可选。默认值为`false`。



```
//@version=6
indicator("US GDP")
e = request.economic("US", "GDP")
plot(e)
```

返回值

要求系列

备注

经济数据也可以从图表中访问，就像常规商品一样。使用“ECONOMIC”作为交易所名称，使用`{country_code}{field}`作为股票代码。因此，美国GDP数据的名称为“ECONOMIC:USGDP”。

另见

[request.financial()]

###### request.financial()



请求商品的财务系列。



```
request.financial(symbol, financial_id, period, gaps, ignore_invalid_symbol, currency) → series float
```

参数

**symbol (series string)** 商品代码。请注意，该商品代码应带有前缀。例如：是 “NASDAQ:AAPL” 而不是 “AAPL”。

**financial_id (series string)** 财务标识符。您可以在我们的[帮助中心]找到可用的 ids 列表。

**period (series string)** 报告时期。可能的值为“TTM”、“FY”、“FQ”、“FH”、“D”。

**gaps (simple barmerge_gaps)** 请求数据的合并策略（请求数据自动与主系列合并：OHLC数据）。可能的值包括：[barmerge.gaps_on]、[barmerge.gaps_off]。 [barmerge.gaps_on] — 请求的数据与可能的跳空（`na`值）合并。[barmerge.gaps_off] — 请求的数据连续无跳空地合并，所有跳空都用之前最接近的现有值填充。默认值为[barmerge.gaps_off]。

**ignore_invalid_symbol (input bool)** 一个可选参数。如果未找到指定的商品，则确定函数的行为：如果为 false，脚本将停止并返回运行时错误； 如果为true，函数将返回na并继续执行。默认值为false。

**currency (series string)** 可选。商品的财务指标（例如净收入）要转换成的货币。转换率取决于最受欢迎交易所对应货币对的上一每日价值。如果没有交易所直接提供汇率，则使用价差商品。可能的值：表示有效货币代码的“字符串”（例如“USD”或“USDT”）或来自`currency.*`命名空间的常量（例如[currency.USD]或[currency.USDT]）。默认值为[syminfo.currency]。



```
//@version=6
indicator("request.financial")
f = request.financial("NASDAQ:MSFT", "ACCOUNTS_PAYABLE", "FY")
plot(f)
```

返回值

要求系列

另见

[request.security()][syminfo.tickerid]

###### request.footprint()



请求包含用于计算当前图表K线[成交量轨迹]信息的[footprint]对象的ID。脚本可以使用返回的ID调用`footprint.*()`函数来检索成交量分布数据，包括成交量分布行、成交量总和以及成交量变化。



```
request.footprint(ticks_per_row, va_percent, imbalance_percent) → footprint
```

参数

**ticks_per_row (simple int)** The price range of each footprint row, expressed in ticks.

**va_percent (simple int/float)** Optional. The percentage of each footprint's total volume to use for calculating the value area (VA). The default is 70.

**imbalance_percent (simple int/float)** 可选。用于检测行成交量不平衡的成交量百分比差异。脚本可以使用从返回的[footprint]对象中检索到的[volume_row]ID，通过调用[volume_row.has_buy_imbalance()]和[volume_row.has_sell_imbalance()]来识别不平衡的行。如果某一行的“买入”成交量超过其下方行的“卖出”成交量指定百分比，或者如果某一行的“卖出”成交量超过其上方行的“买入”成交量指定百分比，则该行被视为不平衡。默认值为300。

返回值

包含当前K线成交量轨迹数据的[footprint]对象的ID，如果没有数据，则为`na`。

备注

Only accounts with Premium or Ultimate [plans] can use scripts that call this function.

A single script cannot include more than one `request.footprint()` call.

###### request.quandl()



**Note:**由于NASDAQ数据链接API变更，此函数已被弃用。“QUANDL”商品的请求不再有效，并且会返回运行时错误。

此函数先前提供的部分数据可通过其他源在TradingView上获取，例如“BCHAIN”或“FRED”。使用商品代码搜索根据其描述查找此类数据。可以使用官方[LibraryCOT]库请求交易者承诺(COT)数据。

请求商品的[纳斯达克数据连接]（以前称为Quandl）数据。



```
request.quandl(ticker, gaps, index, ignore_invalid_symbol) → series float
```

参数

**ticker (series string)** Symbol。请注意，时间序列和Quandl数据源的名称应以下划线分隔。例如：“CFTC / SB_FO_ALL”。

**gaps (simple barmerge_gaps)** 请求数据的合并策略（请求数据自动与主系列合并：OHLC数据）。可能的值包括：[barmerge.gaps_on]、[barmerge.gaps_off]。 [barmerge.gaps_on] — 请求的数据与可能的跳空（`na`值）合并。[barmerge.gaps_off] — 请求的数据连续无跳空地合并，所有跳空都用之前最接近的现有值填充。默认值为[barmerge.gaps_off]。

**index (series int)** Quandl时间序列列索引。

**ignore_invalid_symbol (input bool)** 一个可选参数。如果未找到指定的商品，则确定函数的行为：如果为 false，脚本将停止并返回运行时错误； 如果为true，函数将返回na并继续执行。默认值为false。



```
//@version=6
indicator("request.quandl")
f = request.quandl("CFTC/SB_FO_ALL", barmerge.gaps_off, 0)
plot(f)
```

返回值

要求系列

另见

[request.security()][syminfo.tickerid]

###### request.security()



请求指定上下文（商品和时间周期）的表达式结果。



```
request.security(symbol, timeframe, expression, gaps, lookahead, ignore_invalid_symbol, currency, calc_bars_count) → series <type>
```

参数

**symbol (series string)** 请求数据的s商品或股票代码标识符。使用空字符串或[syminfo.tickerid]来使用图表商品请求数据。要使用附加修饰符（延长时段、股息调整、非标准图表类型，如Heikin Ashi和Renko等）检索数据，请使用`ticker.*`命名空间中的函数为请求创建自定义股票代码ID。

**timeframe (series string)** 所请求数据的时间周期。使用空字符串或[timeframe.period]来请求图表时间周期或[indicator()]函数中指定的`timeframe`的数据。要请求不同时间周期的数据，请提供有效的时间周期字符串。请参阅[此处]，了解如何指定时间周期字符串。

**expression (variable, function, object, array, matrix, or map of series int/float/bool/string/color/enum, or a tuple of these)** 从请求的上下文计算并返回的表达式。它可以接受内置变量，如 [close]、用户定义变量、表达式，如`ta.change(close) / (high - low)`、不使用Pine Script®绘图的函数调用、[对象]、[集合]或表达式元组。

**gaps (simple barmerge_gaps)** 指定如何在图表K线上合并返回值。可能的值：[barmerge.gaps_on]、[barmerge.gaps_off]。对于[barmerge.gaps_on]，值仅在首次从函数上下文中可用时出现在当前图表K线上，否则返回`na`（因此会出现“跳空”）。使用[barmerge.gaps_off]时，原本存在的跳空将被返回的最新已知值填充，从而避免使用`na`值。可选。默认值为[barmerge.gaps_off]。

**lookahead (simple barmerge_lookahead)** 仅在历史K线上，返回时间周期内过去之前的数据。可能的值：[barmerge.lookahead_on]、[barmerge.lookahead_off]。对实时值没有影响。可选。从Pine Script® v3开始，默认值为[barmerge.lookahead_off]。 v1和v2中的默认值为[barmerge.lookahead_on]。 警告：在高于图表的时间周期内使用[barmerge.lookahead_on] 而不像`close[1]`中那样抵消`expression`参数，将会在脚本中引入未来的泄漏，因为该函数将在当前上下文中实际已知之前返回`close`价格。正如用户手册的[重新绘制]页面中所解释的那样，这会产生误导性的结果。

**ignore_invalid_symbol (input bool)** 确定在未找到指定商品时函数的行为：如果为`false`，则脚本将停止并抛出运行时错误；如果`true`，该函数将返回`na`并继续执行。可选。默认值为`false`。

**currency (series string)** 可选。指定用于转换以货币单位表示的值（例如，[open]、[high]、[low]、[close]）或涉及此类值的表达式的目标货币。文字值（例如，`200`）不会被转换。货币值的转换率取决于来自最流行交易所的相应货币对的先前每日值。如果没有交易所直接提供汇率，则使用价差商品。可能的值：表示有效货币代码的“字符串”（例如，"USD" 或 "USDT"）或来自 `currency.*` 命名空间的常量（例如，[currency.USD]或[currency.USDT]）。默认值为[syminfo.currency]。

**calc_bars_count (simple int)** 可选。确定函数可以请求的最近历史K线的最大数量。如果指定，函数将从请求数据集中最后一个历史K线之前指定数量的K线开始计算`expression`参数，并将这些K线视为唯一可用的数据。在某些情况下，限制请求中的历史K线数量有助于提高计算效率。默认值与该交易品种和时间周期可用的[图表K线]数量相同。函数可以尝试检索的最大K线数量取决于用户方案的[日内K线限制]。但是，请求检索的K线数量不能超过数据集中可用的K线数量。



```
//@version=6
indicator("Simple `request.security()` calls")
// Returns 1D close of the current symbol.
dailyClose = request.security(syminfo.tickerid, "1D", close)
plot(dailyClose)

// Returns the close of "AAPL" from the same timeframe as currently open on the chart.
aaplClose = request.security("AAPL", timeframe.period, close)
plot(aaplClose)
```



```
//@version=6
indicator("Advanced `request.security()` calls")
// This calculates a 10-period moving average on the active chart.
sma = ta.sma(close, 10)
// This sends the `sma` calculation for execution in the context of the "AAPL" symbol at a "240" (4 hours) timeframe.
aaplSma = request.security("AAPL", "240", sma)
plot(aaplSma)

// To avoid differences on historical and realtime bars, you can use this technique, which only returns a value from the higher timeframe on the bar after it completes:
indexHighTF = barstate.isrealtime ? 1 : 0
indexCurrTF = barstate.isrealtime ? 0 : 1
nonRepaintingClose = request.security(syminfo.tickerid, "1D", close[indexHighTF`[indexCurrTF]
plot(nonRepaintingClose, "Non-repainting close")

// Returns the 1H close of "AAPL", extended session included. The value is dividend-adjusted.
extendedTicker = ticker.modify("NASDAQ:AAPL", session = session.extended, adjustment = adjustment.dividends)
aaplExtAdj = request.security(extendedTicker, "60", close)
plot(aaplExtAdj)

// Returns the result of a user-defined function.
// The `max` variable is mutable, but we can pass it to `request.security()` because it is wrapped in a function.
allTimeHigh(source) =>
    var max = source
    max := math.max(max, source)
allTimeHigh1D = request.security(syminfo.tickerid, "1D", allTimeHigh(high))

// By using a tuple `expression`, we obtain several values with only one `request.security()` call.
[open1D, high1D, low1D, close1D, ema1D] = request.security(syminfo.tickerid, "1D", [open, high, low, close, ta.ema(close, 10)`
plotcandle(open1D, high1D, low1D, close1D)
plot(ema1D)

// Returns an array containing the OHLC values of the chart's symbol from the 1D timeframe.
ohlcArray = request.security(syminfo.tickerid, "1D", array.from(open, high, low, close))
plotcandle(array.get(ohlcArray, 0), array.get(ohlcArray, 1), array.get(ohlcArray, 2), array.get(ohlcArray, 3))
```

返回值

由`expression`确定的结果。

备注

使用此函数的脚本可能会在历史K线和实时K线上进行不同的计算，从而导致[重新绘制]。

单个脚本最多可以包含40个唯一的`request.*()`函数调用。只有当调用不调用具有相同参数的相同函数时，该调用才是唯一的。

当使用两次对`request.*()`函数的调用来评估来自相同上下文的具有不同`calc_bars_count`值的相同表达式时，第二次调用请求的历史条数与第一次相同。例如，如果脚本调用`request.security("AAPL", "", close, calc_bars_count = 3)` after it calls `request.security("AAPL", "", close, calc_bars_count = 5)`，第二次调用也会使用五条历史数据，而不是三条。

如果没有精确指定，即如果`symbol`参数为空字符串或[syminfo.tickerid]，则可以*继承*`request.()`调用的符号。同样，如果`timeframe`参数为空字符串或[timeframe.period]，则可以继承`request.()`调用的时间周期。这些值通常取自运行脚本的图表。但是，如果从`request.*()`函数B的表达式中调用`request.*()`函数A，则函数A可以从函数B继承值。有关更多信息，请参阅[此处]。

另见

[syminfo.ticker][syminfo.tickerid][timeframe.period][ticker.new()][ticker.modify()][request.security_lower_tf()][request.dividends()][request.earnings()][request.splits()][request.financial()]

###### request.security_lower_tf()



请求指定符号的表达式结果，该表达式的时间周期小于或等于图表的时间周期。它返回一个[array]，其中包含图表K线内每个较低时间周期K线的一个元素。在5分钟图表上，使用`timeframe`参数“1”请求数据通常会返回一个包含五个元素的数组，这些元素表示每个1分钟栏上的`expression`值，按时间排序，最早的值排在最前面。



```
request.security_lower_tf(symbol, timeframe, expression, ignore_invalid_symbol, currency, ignore_invalid_timeframe, calc_bars_count) → array<type>
```

参数

**symbol (series string)** 请求数据的s商品或股票代码标识符。使用空字符串或[syminfo.tickerid]来使用图表商品请求数据。要使用附加修饰符（延长时段、股息调整、非标准图表类型，如Heikin Ashi和Renko等）检索数据，请使用`ticker.*`命名空间中的函数为请求创建自定义股票代码ID。

**timeframe (series string)** 所请求数据的时间周期。使用空字符串或[timeframe.period]来请求图表时间周期或[indicator()]函数中指定的`timeframe`的数据。要请求不同时间周期的数据，请提供有效的时间周期字符串。请参阅[此处]，了解如何指定时间周期字符串。

**expression (variable, object or function of series int/float/bool/string/color/enum, or a tuple of these)** 从请求的上下文计算并返回的表达式。它可以接受内置变量，如 [close]、用户定义变量、表达式，如 `ta.change(close) / (high - low)`、不使用 Pine Script® 绘图的函数调用、[对象] 或表达式元组。除非位于对象的字段内，否则不允许使用[集合]

**ignore_invalid_symbol (series bool)** 确定在未找到指定商品时函数的行为：如果为`false`，则脚本将停止并抛出运行时错误；如果`true`，该函数将返回`na`并继续执行。可选。默认值为`false`。

**currency (series string)** 可选。指定用于转换以货币单位表示的值（例如，[open]、[high]、[low]、[close]）或涉及此类值的表达式的目标货币。文字值（例如，`200`）不会被转换。货币值的转换率取决于来自最流行交易所的相应货币对的先前每日值。如果没有交易所直接提供汇率，则使用价差商品。可能的值：表示有效货币代码的“字符串”（例如，"USD" 或 "USDT"）或来自 `currency.*` 命名空间的常量（例如，[currency.USD]或[currency.USDT]）。默认值为[syminfo.currency]。

**ignore_invalid_timeframe (series bool)** 确定当图表的时间周期小于函数调用中使用的`timeframe`时函数的行为。 如果是`false`，脚本将停止并抛出运行时错误。如果是`true`，则该函数将返回`na`并继续执行。可选。默认值为`false`。

**calc_bars_count (simple int)** 可选。确定函数可以请求的最近历史K线的最大数量。如果指定，函数将从请求数据集中最后一个历史K线之前指定数量的K线开始计算`expression`参数，并将这些K线视为唯一可用的数据。在某些情况下，限制请求中的历史K线数量有助于提高计算效率。默认值与该交易品种和时间周期可用的[图表K线]数量相同。函数可以尝试检索的最大K线数量取决于用户方案的[日内K线限制]。但是，请求检索的K线数量不能超过数据集中可用的K线数量。



```
//@version=6
indicator("`request.security_lower_tf()` Example", overlay = true)

// If the current chart timeframe is set to 120 minutes, then the `arrayClose` array will contain two 'close' values from the 60 minute timeframe for each bar.
arrClose = request.security_lower_tf(syminfo.tickerid, "60", close)

if bar_index == last_bar_index - 1
    label.new(bar_index, high, str.tostring(arrClose))
```

返回值

由 `expression` 确定的类型数组，或它们的元组。

备注

使用此函数的脚本可能会在历史K线和实时K线上进行不同的计算，从而导致[重新绘制]。

请注意，价差（例如“AAPL+MSFT*TSLA”）并不总是使用此函数返回可靠数据。

单个脚本最多可以包含40个唯一的`request.*()`函数调用。只有当调用不调用具有相同参数的相同函数时，该调用才是唯一的。

当使用两次对`request.*()`函数的调用来评估来自相同上下文的具有不同`calc_bars_count`值的相同表达式时，第二次调用请求的历史条数与第一次相同。例如，如果脚本调用`request.security("AAPL", "", close, calc_bars_count = 3)` after it calls `request.security("AAPL", "", close, calc_bars_count = 5)`，第二次调用也会使用五条历史数据，而不是三条。

如果没有精确指定，即如果`symbol`参数为空字符串或[syminfo.tickerid]，则可以*继承*`request.()`调用的商品。同样，如果`timeframe`参数为空字符串或[timeframe.period]，则可以继承`request.()`调用的时间周期。这些值通常取自脚本正在运行的图表。但是，如果从`request.*()`函数B的表达式中调用`request.*()`函数A，则函数A可以从函数B继承这些值。有关更多信息，请参阅[此处]。

另见

[request.security()][syminfo.ticker][syminfo.tickerid][timeframe.period][ticker.new()][request.dividends()][request.earnings()][request.splits()][request.financial()]

###### request.seed()



请求对来自用户维护的GitHub存储库的数据评估的表达式结果。 **Note:**新的Pine Seeds存储库的创建被暂停；目前仅支持现有的存储库。请参阅Github上的[Pine Seeds documentation]以了解更多信息。



```
request.seed(source, symbol, expression, ignore_invalid_symbol, calc_bars_count) → series <type>
```

参数

**source (series string)** GitHub存储库的名称。

**symbol (series string)** GitHub存储库中包含数据的文件的名称。不得包含“.csv”文件扩展名。

**expression (<arg_expr_type>)** 要从所请求商品的上下文中计算和返回的表达式。它可以是内置变量如[close]，表达式如`ta.sma(close, 100)`，先前在脚本中计算的非可变变量，不使用Pine Script®绘图的函数调用、数组、矩阵、 或一个元组。不允许可变变量，除非它们包含在表达式中使用的函数体中。

**ignore_invalid_symbol (input bool)** 确定在未找到指定商品时函数的行为：如果为`false`，则脚本将停止并抛出运行时错误；如果`true`，该函数将返回`na`并继续执行。可选。默认值为`false`。

**calc_bars_count (simple int)** 可选。如果指定，该函数仅请求该商品历史记录末尾指定数量的值，并假设这些值是唯一可用数据来计算`expression`，这在某些情况下可以提高计算速度。默认值与该商品和时间周期可用的[图表K线数量]相同。该函数可以尝试检索的最大K线数量取决于用户方案的[日内K线限制]。但是，请求检索的K线数量不能超过数据集中可用的K线数量。



```
//@version=6
indicator("BTC Development Activity")

[devAct, devActSMA] = request.seed("seed_crypto_santiment", "BTC_DEV_ACTIVITY", [close, ta.sma(close, 10)`

plot(devAct, "BTC Development Activity")
plot(devActSMA, "BTC Development Activity SMA10", color = color.yellow)
```

返回值

请求的系列或系列元组，其中可能包括数组/矩阵ID。

###### request.splits()



请求指定商品的拆分数据。



```
request.splits(ticker, field, gaps, lookahead, ignore_invalid_symbol) → series float
```

参数

**ticker (series string)** 商品代码。请注意，该商品代码应带有前缀。例如：“NASDAQ:AAPL”而不是“ AAPL”。使用[syminfo.ticker]将导致错误。请改用[syminfo.tickerid]。

**field (series string)** 输入字符串。可能的值包括：[splits.denominator]，[splits.numerator]。

**gaps (simple barmerge_gaps)** 请求数据的合并策略（请求数据自动与主系列OHLC数据合并）。可能的值：[barmerge.gaps_on]、[barmerge.gaps_off]。 [barmerge.gaps_on] — 请求的数据与可能的跳空（`na` 值）合并。 [barmerge.gaps_off] — 请求的数据连续无跳空地合并，所有跳空都用之前最接近的现有值填充。默认值为[barmerge.gaps_off]。

**lookahead (simple barmerge_lookahead)** 请求的数据位置的合并策略。可能的值：[barmerge.lookahead_on]、[barmerge.lookahead_off]。从版本3开始，默认值为[barmerge.lookahead_off]。请注意，实时行为是相同的，仅历史行为不同。

**ignore_invalid_symbol (input bool)** 一个可选参数。如果未找到指定的商品，则确定函数的行为：如果为 false，脚本将停止并返回运行时错误； 如果为true，函数将返回na并继续执行。默认值为false。



```
//@version=6
indicator("request.splits")
s1 = request.splits("NASDAQ:BELFA", splits.denominator)
plot(s1)
s2 = request.splits("NASDAQ:BELFA", splits.denominator, gaps=barmerge.gaps_on, lookahead=barmerge.lookahead_on)
plot(s2)
```

返回值

请求序列，如果指定商品没有拆分数据，则为n/a。

另见

[request.earnings()][request.dividends()][request.security()][syminfo.tickerid]

###### runtime.error()



调用时，会导致运行时错误，并带有在`message`参数中指定的错误消息。



```
runtime.error(message) → void
```

参数

**message (series string)** 错误消息。

###### second()





```
second(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的unix时间。

**timezone (series string)** 允许将返回值调整为以UTC/GMT表示法（例如，“UTC-5”、“GMT+0530”）或IANA时区数据库名称（例如，“America/New_York”）指定的时区。可选。默认值为[syminfo.timezone]。

返回值

提供UNIX时间的秒数(交换时区)。

备注

UNIX时间是自1970年1月1日UTC 00:00:00起已经过去的毫秒数。

另见

[second][time()][year()][month()][dayofmonth()][dayofweek()][hour()][minute()]

###### str.contains()

3过载



如果`source`字符串包含`str`子字符串，则返回true，否则返回false。

语法和重载

[`str.contains(source, str) → const bool`][`str.contains(source, str) → simple bool`][`str.contains(source, str) → series bool`]

参数

**source (const string)** 来源字符串

**str (const string)** 要搜索的子字符串。



```
//@version=6
indicator("str.contains")
// If the current chart is a continuous futures chart, e.g “BTC1!”, then the function will return true, false otherwise.
var isFutures = str.contains(syminfo.tickerid, "!")
plot(isFutures ? 1 : 0)
```

返回值

如果在`str`字符串中找到 `source`，则为true ，否则为false。

另见

[str.pos()][str.match()]

###### str.endswith()

3过载



如果`source`字符串以`str`中指定的子字符串结尾，则返回true，否则返回false。

语法和重载

[`str.endswith(source, str) → const bool`][`str.endswith(source, str) → simple bool`][`str.endswith(source, str) → series bool`]

参数

**source (const string)** 来源字符串

**str (const string)** 要搜索的子字符串。

返回值

如果`source`字符串以`str`中指定的子字符串结尾，则为true，否则为false。

另见

[str.startswith()]

###### str.format()

2过载



使用指定的格式字符串(`formatString`)和一个或多个附加参数（`arg0`、`arg1`等）创建格式化字符串。格式字符串定义返回字符串的结构，其中大括号 (`{}`) 中的所有占位符均指向附加参数。每个占位符都需要一个表示参数位置的数字，从0开始。例如，占位符`{0}`指向`formatString`之后的第一个参数(`arg0`)，`{1}`指向第二个参数(`arg1`)，依此类推。该函数将每个占位符替换为相应参数的字符串表示形式。

语法和重载

[`str.format(formatString, arg0, arg1, ...) → simple string`][`str.format(formatString, arg0, arg1, ...) → series string`]

参数

**formatString (simple string)** 格式字符串。

**arg0, arg1, ... (simple int/float/bool/string)** 要格式化的值。



```
//@version=6
indicator("Simple `str.format()` demo")

//@variable A formatted string that includes representations of the current `bar_index` and `close` values.
//          The placeholder `{0}` refers to the first argument after the formatting string (`bar_index`), and 
//          `{1}` refers to the second (`close`).
string labelText = str.format("Current bar index: {0}\nCurrent bar close: {1}", bar_index, close)

// Draw a label to display the `labelText` string at the current bar's `high` price. 
label.new(bar_index, high, labelText)
```



```
//@version=6
indicator("Extensive `str.format()` demo", overlay=true)
// The format specifier inside the curly braces accepts certain modifiers:
// - Specify the number of decimals to display:
s1 = str.format("{0,number,#.#}", 1.34) // returns: 1.3
label.new(bar_index, close, text=s1)
// - Round a float value to an integer:
s2 = str.format("{0,number,integer}", 1.34) // returns: 1
label.new(bar_index - 1, close, text=s2)
// - Display a number in currency:
s3 = str.format("{0,number,currency}", 1.34) // returns: $1.34
label.new(bar_index - 2, close, text=s3)
// - Display a number as a percentage:
s4 = str.format("{0,number,percent}", 0.5) // returns: 50%
label.new(bar_index - 3, close, text=s4)
// EXAMPLES WITH SEVERAL ARGUMENTS
// returns: Number 1 is not equal to 4
s5 = str.format("Number {0} is not {1} to {2}", 1, "equal", 4)
label.new(bar_index - 4, close, text=s5)
// returns: 1.34 != 1.3
s6 = str.format("{0} != {0, number, #.#}", 1.34)
label.new(bar_index - 5, close, text=s6)
// returns: 1 is equal to 1, but 2 is equal to 2
s7 = str.format("{0, number, integer} is equal to 1, but {1, number, integer} is equal to 2", 1.34, 1.52)
label.new(bar_index - 6, close, text=s7)
// returns: The cash turnover amounted to $1,340,000.00
s8 = str.format("The cash turnover amounted to {0, number, currency}", 1340000)
label.new(bar_index - 7, close, text=s8)
// returns: Expected return is 10% - 20%
s9 = str.format("Expected return is {0, number, percent} - {1, number, percent}", 0.1, 0.2)
label.new(bar_index - 8, close, text=s9)
```

返回值

格式化的字符串。

备注

用作`formatString`参数的字符串可以包含单引号字符 (')。但是，程序员必须将该字符串中的所有单引号配对，以避免出现意外的格式结果。

所有未引用的左大括号必须在格式字符串中具有相应的右大括号。如果字符串包含不平衡的左大括号，则会导致运行时错误。例如，“ ab {0} de”和“ ab} {0} de”是有效的格式字符串，但“ ab {0'}'de”，“ ab} {0} {de” {de“”和“'''''{0}”不是。

“int”或“float”值或数组的占位符可以包含修饰符和格式化标记，以自定义结果字符串如何表示它们。

例如，占位符 `{0,number,#.#)` specifies that the result inserts characters representing the `arg0` 数字四舍五入到一个小数位。

有关占位符和支持格式的详细信息，请参阅用户手册的[字符串]页面的[格式化字符串]部分。

在格式化字符串中，撇号(`'`)充当引号字符，而不是字面字符。如果格式化字符串中两个撇号之间有一串字符，则函数的结果会按字面意思包含这些字符。例如，子字符串`'{'`会将字面字符`{` 添加到结果中，而不是将其视为占位符的开头。请注意，如果格式化字符串使用撇号而不是引号作为括起来的字符，则必须使用反斜杠对字符序列中的任何撇号进行转义。

###### str.format_time()



将 `time` 时间戳转换为根据 `format` 和 `timezone` 格式化的字符串。



```
str.format_time(time, format, timezone) → series string
```

参数

**time (series int)** UNIX时间，以毫秒为单位。

**format (series string)** 格式字符串，指定返回字符串中`time`的日期/时间表示形式。除了那些用单引号`'`转义的字母，字符串中使用的所有字母都被视为格式化标记，并将用作格式化指令。请参阅“备注”部分，获取最有用的标记列表。可选。默认为“yyyy-MM-dd'T'HH:mm:ssZ”，代表ISO 8601标准。

**timezone (series string)** 允许将返回值调整为以 UTC/GMT 表示法（例如，“UTC-5”、“GMT+0530”）或[IANA时区数据库名称]（例如，“America /New_York”）。可选。默认值为[syminfo.timezone]。



```
//@version=6
indicator("str.format_time")
if timeframe.change("1D")
    formattedTime = str.format_time(time, "yyyy-MM-dd HH:mm", syminfo.timezone)
    label.new(bar_index, high, formattedTime)
```

返回值

格式化的字符串。

备注

`M`、`d`、`h`、`H`、`m` 和 `s`标记都可以加倍以生成前导零。例如，一月份将显示为`1`和`M`，或`01`和`MM`。

最常用的格式化标记是：

y - 年。 使用`yy`输出年份的最后两位数字，或使用`yyyy`输出全部四位数字。2000年将是`00`和`yy`或`2000`和`yyyy`。

M — 月。不要与小写的`m`混淆，后者代表分钟。

d - 一个月中的某一天。

a - AM/PM后缀。

h — 12小时格式的小时。采用这种格式，一天的最后一个小时将是`11`。

H — 24小时格式的小时。采用这种格式，一天的最后一个小时将是`23`。

m - 分钟。

s - 秒。

S - 秒的分数。

Z - 时区，与UTC的HHmm偏移量，前面有 `+` 或 `-`。

###### str.length()

3过载



返回与该字符串中的字符数相对应的整数。

语法和重载

[`str.length(string) → const int`][`str.length(string) → simple int`][`str.length(string) → series int`]

参数

**string (const string)** 来源字符串

返回值

源字符串中的字符数。

###### str.lower()

3过载



返回一个所有字母都转换为小写的新字符串。

语法和重载

[`str.lower(source) → const string`][`str.lower(source) → simple string`][`str.lower(source) → series string`]

参数

**source (const string)** 要转换的字符串。

返回值

所有字母都转换为小写的新字符串。

另见

[str.upper()]

###### str.match()

2过载



如果与`regex`正则表达式匹配，则返回`source`字符串的新子字符串，否则返回空字符串。

语法和重载

[`str.match(source, regex) → simple string`][`str.match(source, regex) → series string`]

参数

**source (simple string)** 来源字符串

**regex (simple string)** 与此字符串匹配的正则表达式。



```
//@version=6
indicator("str.match")

s = input.string("It's time to sell some NASDAQ:AAPL!")

// finding first substring that matches regular expression "[\w]+:[\w]+"
var string tickerid = str.match(s, "[\\w]+:[\\w]+")

if barstate.islastconfirmedhistory
    label.new(bar_index, high, text = tickerid) // "NASDAQ:AAPL"
```

返回值

如果与`regex`正则表达式匹配，则为`source`字符串的新子字符串，否则为空字符串。

备注

函数返回`source`字符串中第一次出现的[正则表达式]。

`regex`字符串中的反斜杠“\”符号需要使用额外的反斜杠进行转义，例如“\\d”代表正则表达式“\d”。

另见

[str.contains()][str.substring()]

###### str.pos()

3过载



返回`str`字符串中第一次出现`source`字符串的位置，否则返回'na'。

语法和重载

[`str.pos(source, str) → const int`][`str.pos(source, str) → simple int`][`str.pos(source, str) → series int`]

参数

**source (const string)** 来源字符串

**str (const string)** 要搜索的子字符串。

返回值

`str`字符串在`source`字符串中的位置。

备注

字符串索引从0开始。

另见

[str.contains()][str.match()][str.substring()]

###### str.repeat()

4过载



构造一个新字符串，其中包含重复`repeat`次的`source`字符串，并在每个重复实例之间注入`separator`。

语法和重载

[`str.repeat(source, repeat, separator) → const string`][`str.repeat(source, repeat, separator) → input string`][`str.repeat(source, repeat, separator) → simple string`][`str.repeat(source, repeat, separator) → series string`]

参数

**source (const string)** 要重复的字符串。

**repeat (const int)** 重复`source`字符串的次数。必须大于或等于0。

**separator (const string)** 要在重复值之间注入的字符串。可选。默认为空字符串。



```
//@version=6
indicator("str.repeat")
repeat = str.repeat("?", 3, ",") // Returns "?,?,?"
label.new(bar_index,close,repeat)
```

备注

如果`source`为`na`，则返回`na`。

###### str.replace()

3过载



返回一个新字符串，其中第N次出现的`target`字符串替换为`replacement`字符串，其中N在`occurrence`中指定。

语法和重载

[`str.replace(source, target, replacement, occurrence) → const string`][`str.replace(source, target, replacement, occurrence) → simple string`][`str.replace(source, target, replacement, occurrence) → series string`]

参数

**source (const string)** 来源字符串

**target (const string)** 被替换字符串

**replacement (const string)** 要插入的字符串而不是目标字符串。

**occurrence (const int)** 要替换的目标字符串的第N次出现。第一个匹配的索引从0开始。可选。默认值为0。



```
//@version=6
indicator("str.replace")
var source = "FTX:BTCUSD / FTX:BTCEUR"

// Replace first occurrence of "FTX" with "BINANCE" replacement string
var newSource = str.replace(source, "FTX", "BINANCE", 0)

if barstate.islastconfirmedhistory
    // Display "BINANCE:BTCUSD / FTX:BTCEUR"
    label.new(bar_index, high, text = newSource)
```

返回值

已处理字符串

另见

[str.replace_all()][str.match()]

###### str.replace_all()

2过载



用替换字符串，替换源字符串中每次出现的目标字符串。

语法和重载

[`str.replace_all(source, target, replacement) → simple string`][`str.replace_all(source, target, replacement) → series string`]

参数

**source (simple string)** 来源字符串

**target (simple string)** 被替换字符串

**replacement (simple string)** 每次出现的目标字串都将替换的字串

返回值

已处理字符串

###### str.split()



将字符串划分为子字符串阵列，并返回其阵列ID。



```
str.split(string, separator) → array<string>
```

参数

**string (series string)** 来源字符串

**separator (series string)** 分隔每个子字符串的字符串。

返回值

字符串阵列的ID。

###### str.startswith()

3过载



如果`source`字符串以`str`中指定的子字符串开头，则返回true，否则返回false。

语法和重载

[`str.startswith(source, str) → const bool`][`str.startswith(source, str) → simple bool`][`str.startswith(source, str) → series bool`]

参数

**source (const string)** 来源字符串

**str (const string)** 要搜索的子字符串。

返回值

如果`source`字符串以`str`中指定的子字符串开头，则为true，否则为false。

另见

[str.endswith()]

###### str.substring()

3过载



返回一个新字符串，该字符串是`source`字符串的子字符串。子字符串以`begin_pos`指定的索引处的字符开始，并延伸到`source`字符串的“end_pos - 1”。

语法和重载

[`str.substring(source, begin_pos, end_pos) → const string`][`str.substring(source, begin_pos, end_pos) → simple string`][`str.substring(source, begin_pos, end_pos) → series string`]

参数

**source (const string)** 从中提取子字符串的源字符串。

**begin_pos (const int)** 提取的子串的起始位置。它是独占的（提取的子字符串包括该位置的字符）。

**end_pos (const int)** 结束位置。它是独占的（提取的字符串不包括该位置的字符）。可选。默认值为`source`字符串的长度。



```
//@version=6
indicator("str.substring", overlay = true)
sym= input.symbol("NASDAQ:AAPL")
pos = str.pos(sym, ":") // Get position of ":" character
tkr= str.substring(sym, pos+1) // "AAPL"
if barstate.islastconfirmedhistory
    label.new(bar_index, high, text = tkr)
```

返回值

从源字符串中提取的子字符串。

备注

字符串索引从0开始。如果`begin_pos`等于`end_pos`，函数返回一个空字符串。

另见

[str.contains()][str.pos()][str.match()]

###### str.tonumber()

4过载



将 `string` 中表示的值转换为其等效的“float”。

语法和重载

[`str.tonumber(string) → const float`][`str.tonumber(string) → input float`][`str.tonumber(string) → simple float`][`str.tonumber(string) → series float`]

参数

**string (const string)** 包含整数或浮点值表示形式的字符串。

返回值

`string` 中的值的“浮点”等价物。如果该值不是格式正确的整数或浮点值，则函数返回 `na`。

###### str.tostring()

5过载



语法和重载

[`str.tostring(value) → const string`][`str.tostring(value, format) → simple string`][`str.tostring(value, format) → series string`][`str.tostring(value) → simple string`][`str.tostring(value) → series string`]

参数

**value (const enum)** 其元素转换为字符串的值或数组ID。

返回值

`value`参数的字符串表示形式。

如果`value`参数是字符串，则按原样返回。

当`value`为na时，函数返回字符串“NaN”。

备注

浮点值的格式也会在必要时四舍五入这些值，例如str.tostring(3.99, '#') 将返回“4”。

要显示尾随零，请使用'0'而不是'#'。例如，'#.000'。

当使用[format.mintick]时，该值将四舍五入到可以除以[syminfo.mintick]，且没有余数的最接近的数字。返回的字符串带有尾随零。

如果x参数是字符串，则将返回相同的字符串值。

Bool类型参数返回“true”或“false”。

当x为na时，函数返回“NaN”。

###### str.trim()

4过载



构造一个包含所有连续空格和其他控制字符的新字符串（例如“\n”、“\t”等）从`source`的左侧和右侧删除。

语法和重载

[`str.trim(source) → const string`][`str.trim(source) → input string`][`str.trim(source) → simple string`][`str.trim(source) → series string`]

参数

**source (const string)** 要修剪的字符串。



```
//@version=6
indicator("str.trim")
trim = str.trim("    abc    ") // Returns "abc"
label.new(bar_index,close,trim)
```

备注

如果修剪后结果为空或`source`为`na`，则返回空字符串("")。

###### str.upper()

3过载



返回一个所有字母都转换为大写的新字符串。

语法和重载

[`str.upper(source) → const string`][`str.upper(source) → simple string`][`str.upper(source) → series string`]

参数

**source (const string)** 要转换的字符串。

返回值

所有字母都转换为大写的新字符串。

另见

[str.lower()]

###### strategy()



此声明语句将脚本指定为策略并设置许多与策略相关的属性。



```
strategy(title, shorttitle, overlay, format, precision, scale, pyramiding, calc_on_order_fills, calc_on_every_tick, max_bars_back, backtest_fill_limits_assumption, default_qty_type, default_qty_value, initial_capital, currency, slippage, commission_type, commission_value, process_orders_on_close, close_entries_rule, margin_long, margin_short, explicit_plot_zorder, max_lines_count, max_labels_count, max_boxes_count, calc_bars_count, risk_free_rate, use_bar_magnifier, fill_orders_on_standard_ohlc, max_polylines_count, dynamic_requests, behind_chart) → void
```

参数

**title (const string)** 脚本标题。当没有使用`shorttitle`参数时，它会显示在图表上，并在发布脚本时成为出版物的默认标题。

**shorttitle (const string)** 图表上脚本的显示名称。如果指定，它将替换大多数图表相关窗口中的`title`参数。可选。默认值是用于`title`的参数。

**overlay (const bool)** 如果为`true`，则当用户将脚本直接添加到图表时，脚本的视觉效果会显示在主图表窗格中；如果用户将脚本应用于其他脚本，则脚本的视觉效果会显示在该脚本的窗格中。如果为`false`，则脚本的视觉效果会显示在单独的窗格中。对`overlay`值的更改仅在用户再次将脚本添加到图表后生效。此外，如果用户通过选择脚本“更多”菜单中的“移动到”选项将脚本移动到另一个窗格，则在源代码更新后，脚本不会移回其原始窗格。默认值为`false`。无论此设置如何，用于显示入场和出场的策略特定标签都将显示在主图表上方。

**format (const string)** 指定脚本显示值的格式。可能的值：[format.inherit]、[format.price]、[format.volume]、[format.percent]。可选。默认值为[format.inherit]。

**precision (const int)** 指定脚本显示值的浮点后的位数。必须是不大于16的非负整数。如果`format`设置为[format.inherit]并指定了`precision`，则格式将设置为[format.price]。当函数的`format`参数使用[format.volume]时，`precision`参数不会影响结果，因为[format.volume]定义的小数精度规则会取代其他精度设置。可选选修的。默认值继承自图表商品的精度。

**scale (const scale_type)** 可选。用于确定脚本价格坐标的位置以及脚本视觉元素的缩放行为。可选值为[scale.right]、[scale.left]和[scale.none]。如果指定此参数，且脚本叠加在主图表窗格或其他脚本的窗格上，则脚本会独立缩放其视觉元素以适应窗格的视觉空间。如果脚本与主图表或其他脚本位于同一窗格中，则[scale.right]或[scale.left]会在该窗格的左侧或右侧为脚本添加一个单独的价格坐标。如果脚本位于单独的窗格中，则这两个参数都会将该窗格的价格坐标放置在左侧或右侧，而不会添加新的坐标。如果参数为[scale.none]，仅当 `overlay`参数为`true` 时有效，则脚本会将绘制的数字直接显示在现有窗格的坐标上；如果用户将其移动到新窗格，则会在新价格坐标上显示数值。对参数的更改仅在用户再次将脚本添加到图表后生效。如果未指定，则脚本使用其所在窗格的主价格坐标，并且如果其叠加在现有窗格上，则不会单独缩放其视觉效果。

**pyramiding (const int)** 同一方向允许的最大条目数。如果值为0，则只能开同一个方向的挂单，拒绝追加挂单。此设置也可以在策略的“设置/属性”标签页中更改。可选。默认值为0。

**calc_on_order_fills (const bool)** 指定是否应在订单成交后重新计算策略。如果`true`，策略会在订单成交后重新计算，而不是仅在K线关闭时重新计算。此设置也可以在策略的“设置/属性”标签页中更改。可选。默认值为`false`。

**calc_on_every_tick (const bool)** 指定是否应在每个实时tick时重新计算策略。如果是`true`，当策略在实时K线上运行时，它将在每次图表更新时重新计算。如果是`false`，则策略仅在实时K线收盘时进行计算。使用的参数不影响历史数据的策略计算。也可以在策略的“设置/属性”标签页中更改此设置。可选。默认值为`false`。

**max_bars_back (const int)** 脚本为每个变量和函数保留的历史缓冲区的长度，它确定可以使用`[]`历史引用运算符引用多少个过去的值。Pine Script®运行时会自动检测所需的缓冲区大小。仅当由于自动检测失败而发生运行时错误时才需要使用此参数。有关历史缓冲区底层机制的更多信息，请访问[我们的帮助中心]。可选。默认值为0。

**backtest_fill_limits_assumption (const int)** 以tick为单位的限价单执行阈值。使用时，限价单仅在市场价格超过订单的限价水平指定的tick数时才会执行。可选。默认值为0。

**default_qty_type (const string)** 指定用于`default_qty_value`的单位。可能的值有：[strategy.fixed]表示合约/股票/手数，[strategy.cash]表示货币金额，或[strategy.percent_of_equity]表示可用权益的百分比。也可以在策略的“设置/属性”标签页中更改此设置。可选。默认值为[strategy.fixed]。

**default_qty_value (const int/float)** 默认交易数量，单位由与`default_qty_type`参数一起使用的参数确定。此设置也可以在策略的“设置/属性”标签页中更改。可选。默认值为1。

**initial_capital (const int/float)** 最初可用于策略交易的资金量，以`currency`为单位。可选。默认值为1000000。

**currency (const string)** 策略在货币相关计算中使用的货币。市场仓位仍通过将`currency`转换为图表商品的货币来开仓。转换率取决于最受欢迎交易所对应货币对的先前每日价值。如果没有交易所直接提供汇率，则使用价差商品。可能的值：表示有效货币代码的“字符串”（例如“USD”或“USDT”）或来自`currency.*` 命名空间的常量（例如[currency.USD]或[currency.USDT]）。默认值为[syminfo.currency]。

**slippage (const int)** 滑点以tick表示。这个值被添加到市场单/止损单的执行价格中或从中减去，以使执行价格对策略不太有利。例如，如果[syminfo.mintick]为0.01 并且`slippage`设置为5，则多头市价单将在实际价格上方5 * 0.01=0.05点处进入。此设置也可以在策略的“设置/属性”标签页中更改。可选。默认值为0。

**commission_type (const string)** 确定传递给`commission_value`的数字所表示的内容：[strategy.commission.percent]表示订单现金量的百分比，[strategy.commission.cash_per_contract]表示每个合约的货币，[strategy.commission.cash_per_order]表示每个订单的货币。也可以在策略的“设置/属性”标签页中更改此设置。可选。默认值为[strategy.commission.percent]。

**commission_value (const int/float)** 应用于策略订单的佣金，其单位由传递给`commission_type`参数的参数决定。也可以在策略的“设置/属性”标签页中更改此设置。可选。默认值为0。

**process_orders_on_close (const bool)** 当设置为 `true` 时，在K线收盘和策略计算完成后生成额外的执行订单尝试。如果订单是市价订单，经纪商模拟器会在下一个K线开盘前执行它们。如果订单是价格相关的，则只有在满足价格条件时才会执行。如果您希望在当前K线上平仓，此选项很有用。此设置也可以在策略的“设置/属性”标签页中更改。可选。默认值为 `false`。

**close_entries_rule (const string)** 确定关闭交易的顺序。可能的值是：“FIFO”（先进先出）如果最早的退出订单必须关闭最早的进入订单。如果订单基于[strategy.exit()]函数的`from_entry`参数关闭，则为 "ANY"。“FIFO”只能用于股票、期货和美国外汇（NFA合规规则2-43b），而“ANY”允许用于非美国外汇。可选。默认值为“FIFO”。

**margin_long (const int/float)** 多头保证金是多头仓位必须用现金或抵押品支付的证券购买价格的百分比。必须是非负数。模拟追加保证金的逻辑在[帮助中心]中有说明。此设置也可以在策略的“设置/属性”选项卡中更改。可选。如果值为0，则策略不对仓位规模实施任何限制。默认值为100，在这种情况下，策略仅使用其自有资金，并且多头仓位不能被追加保证金。

**margin_short (const int/float)** 空头保证金是指证券购买价格的百分比，必须用现金或抵押品来支付空头仓位。必须为非负数。模拟保证金追缴的逻辑在[帮助中心]中有说明。此设置也可以在策略的“设置/属性”选项卡中更改。可选。如果值为0，则策略不对仓位大小实施任何限制。默认值为100，在这种情况下，策略仅使用其自有资金。请注意，即使没有使用保证金，如果损失超过可用资金，空头仓位也可以被追缴保证金。

**explicit_plot_zorder (const bool)** 指定脚本的绘图、填充和水平线的渲染顺序。如果`true`，绘图将按照它们在脚本代码中出现的顺序绘制，每个较新的绘图都绘制在之前的绘图之上。这仅适用于`plot*()`函数、[fill()]和[hline()]。可选。默认值为`false`。

**max_lines_count (const int)** 最后显示的[line]绘图数量。可能的值：1-500。可选。默认值为50。

**max_labels_count (const int)** 最后显示的[label]绘图数量。可能的值：1-500。可选。默认值为50。

**max_boxes_count (const int)** 最后显示的[box]绘图数量。可能的值：1-500。可选。默认值为50。

**calc_bars_count (const int)** 将脚本的初始计算限制为最后指定的K线数。指定后，“计算K线”字段将包含在脚本“设置/输入”标签页的“计算”部分中。可选。默认值为0，在这种情况下脚本将在所有可用K线上执行。

**risk_free_rate (const int/float)** 无风险回报率是风险最小或零的投资价值的年度百分比变化。它用于计算[Sharpe]和[Sortino]比率。可选。默认值为2。

**use_bar_magnifier (const bool)** 可选。当为`true`时，[经纪商模拟器]会在历史K线上回测时使用较低的时间周期数据，以获得更真实的结果。默认值为`false`。只有[Premium]及更高级别的方案可以使用此功能。

**fill_orders_on_standard_ohlc (const bool)** 当`true`时，强制在Heikin Ashi图表上运行的策略使用实际OHLC价格填写订单，以获得更真实的结果。可选。默认值为`false`。

**max_polylines_count (const int)** 最后显示的[polyline]绘图的数量。可能的值：1-100。计数为近似值；可能会显示多于指定数量的绘图。可选。默认值为50。

**dynamic_requests (const bool)** 指定脚本是否可以动态调用来自`request.*()`命名空间的函数。动态`request.*()`调用允许在条件结构（例如，[if]）、循环（例如，[for]）和导出函数的本地范围内进行。此外，此类调用允许为其许多参数使用“系列”参数。可选。默认值为`true`。有关更多信息，请参阅用户手册的[动态请求]部分。

**behind_chart (const bool)** 可选。控制所有绘图和绘图是否显示在图表显示之后出现（如果`true`）或在之前（如果`false`）。此参数仅在`overlay`参数为`true`时才生效。默认值为`true`。



```
//@version=6
strategy("My strategy", overlay = true)

// Enter long by market if current open is greater than previous high.
if open > high[1]
    strategy.entry("Long", strategy.long, 1)
// Generate a full exit bracket (profit 10 points, loss 5 points per contract) from the entry named "Long".
strategy.exit("Exit", "Long", profit = 10, loss = 5)
```

备注

您可以在我们的[用户手册]中了解有关策略的更多信息。

每个策略脚本必须有一个 [strategy()] 调用。

使用`calc_on_every_tick = true`参数的策略可能在历史和实时K线上计算不同，这会导致[重新绘制]。

策略总是使用图表的价格进入和退出仓位。在非标准图表类型（Heikin Ashi、Renko 等）使用它们会产生误导性结果，因为它们的价格是合成的。因此不建议在非标准图表上进行回测。

除非使用深度回测模式，否则策略可以打开的最大订单数量为9000。如果策略超出此限制，则当“交易列表”标签页中出现新条目时，它会删除最旧的订单信息。`strategy.closedtrades.*()`函数返回已删除订单打开或关闭的交易的`na`。要检索最早可用的已关闭交易的索引，请使用[strategy.closedtrades.first_index]变量。

另见

[indicator()][library()]

###### strategy.cancel()



取消具有特定标识符的待处理或未执行订单。如果多个未执行订单共享同一个 ID，则使用该ID作为`id`参数调用此命令将取消所有订单。如果脚本使用表示已执行订单ID的`id`调用此命令，则不起作用。

此命令在处理基于价格的订单（例如，[限价订单]）非常有用。调用此命令还可以取消[市价订单]，但前提是它们在与下单命令相同的报价上执行。



```
strategy.cancel(id) → void
```

参数

**id (series string)** 要取消的未成交订单标识符。



```
//@version=6
strategy(title = "Order cancellation demo")

conditionForBuy = open > high[1]
if conditionForBuy
    strategy.entry("Long", strategy.long, 1, limit = low) // Enter long using limit order at low price of current bar if `conditionForBuy` is `true`.
if not conditionForBuy
    strategy.cancel("Long") // Cancel the entry order with name "Long" if `conditionForBuy` is `false`.
```

###### strategy.cancel_all()



取消所有待处理或未完成的订单，无论其标识符是什么。

此命令在处理基于价格的订单（例如，[限价订单]）非常有用。调用此命令还可以取消[市价订单]，但前提是它们在与下单命令相同的报价上执行。



```
strategy.cancel_all() → void
```



```
//@version=6
strategy(title = "Cancel all orders demo")
conditionForBuy1 = open > high[1]
if conditionForBuy1
    strategy.entry("Long entry 1", strategy.long, 1, limit = low) // Enter long using a limit order if `conditionForBuy1` is `true`.
conditionForBuy2 = conditionForBuy1 and open[1] > high[2]
float lowest2 = ta.lowest(low, 2)
if conditionForBuy2
    strategy.entry("Long entry 2", strategy.long, 1, limit = lowest2) // Enter long using a limit order if `conditionForBuy2` is `true`.
conditionForStopTrading = open < lowest2
if conditionForStopTrading
    strategy.cancel_all() // Cancel both limit orders if `conditionForStopTrading` is `true`.
```

###### strategy.close()



创建订单以退出由具有特定标识符的入场订单所开仓的部分。如果仓位中的多个条目共享相同的 ID，则当该命令的调用使用该 ID 作为 `id` 参数时，该命令的订单将适用于所有这些条目，从第一个开仓交易开始。

此命令始终生成 [市价单]。要使用基于价格的订单（例如，[止损]订单）退出仓位，请使用[strategy.exit()]命令。



```
strategy.close(id, comment, qty, qty_percent, alert_message, immediately, disable_alert) → void
```

参数

**id (series string)** 要关闭的开仓交易的入场标识符。

**comment (series string)** 可选。已成交订单的附加说明。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是自动生成的退出标识符。默认值为空字符串。

**qty (series int/float)** 可选。退出订单成交时要关闭的合约/手数/股票/单位数。如果指定，命令将使用此值而不是`qty_percent`来确定订单大小。默认值为`na`，这意味着订单大小取决于`qty_percent`值。

**qty_percent (series int/float)** 可选。0到100之间的值，表示当退出订单成交时要关闭的未平仓交易数量的百分比。百分比计算取决于具有`id`入场标识符的未平仓交易的总规模。如果`qty`值不是`na`，则命令将忽略此参数。默认值为100。

**alert_message (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。默认值为空字符串。

**immediately (series bool)** 可选。如果为`true`，则平仓订单将在策略下单的同一tick执行，忽略限制执行至下一根K线的开盘tick的策略属性。默认值为`false`。

**disable_alert (series bool)** 可选。如果命令创建订单时为`true`，则该订单成交时策略不会触发警报。此参数接受“系列”值，这意味着用户可以控制哪些订单在执行时触发警报。默认值为`false`。



```
//@version=6
strategy("Partial close strategy")

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

// Place a market order to enter a long position when `sma14` crosses over `sma28`.
if ta.crossover(sma14, sma28)
    strategy.entry("My Long Entry ID", strategy.long)

// Place a market order to close the long trade when `sma14` crosses under `sma28`.
if ta.crossunder(sma14, sma28)
    strategy.close("My Long Entry ID", "50% market close", qty_percent = 50)

// Plot the position size.
plot(strategy.position_size)
```

备注

当一个仓位由多笔未平仓交易组成，并且[strategy()]声明语句中的`close_entries_rule`为“FIFO”（默认）时，[strategy.close()]调用将从第一笔未平仓交易开始退出仓位。即使`id`值是不同未平仓交易的入场ID，此行为也适用。但是，在这种情况下，最大退出订单规模仍然取决于具有`id`标识符的订单开立的交易。有关更多信息，请参阅我们的用户手册的[这个]部分。

###### strategy.close_all()



创建订单来完全关闭一个未平仓位，无论打开或添加的订单的标识符是什么。

此命令始终生成 [市价单]。要使用基于价格的订单（例如，[止损]订单）退出仓位，请使用[strategy.exit()]命令。



```
strategy.close_all(comment, alert_message, immediately, disable_alert) → void
```

参数

**comment (series string)** 可选。已成交订单的附加说明。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是自动生成的退出标识符。默认值为空字符串。

**alert_message (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。默认值为空字符串。

**immediately (series bool)** 可选。如果为`true`，则平仓订单将在策略下单的同一tick执行，忽略限制执行至下一根K线的开盘tick的策略属性。默认值为`false`。

**disable_alert (series bool)** 可选。如果命令创建订单时为`true`，则该订单成交时策略不会触发警报。此参数接受“系列”值，这意味着用户可以控制哪些订单在执行时触发警报。默认值为`false`。



```
//@version=6
strategy("Multi-entry close strategy")

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

// Place a market order to enter a long trade every time `sma14` crosses over `sma28`.
if ta.crossover(sma14, sma28)
    strategy.order("My Long Entry ID " + str.tostring(strategy.opentrades), strategy.long)

// Place a market order to close the entire position every 500 bars.
if bar_index % 500 == 0
    strategy.close_all()

// Plot the position size.
plot(strategy.position_size)
```

###### strategy.closedtrades.commission()



返回已平仓交易中支付的入场费和出场费总和，以[strategy.account_currency]表示。



```
strategy.closedtrades.commission(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.commission` Example", commission_type = strategy.commission.percent, commission_value = 0.1)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Plot total fees for the latest closed trade.
plot(strategy.closedtrades.commission(strategy.closedtrades - 1))
```

另见

[strategy()][strategy.opentrades.commission()]

###### strategy.closedtrades.entry_bar_index()



返回已平仓交易入场的bar_index。



```
strategy.closedtrades.entry_bar_index(trade_num) → series int
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.entry_bar_index Example")
// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")
// Function that calculates the average amount of bars in a trade.
avgBarsPerTrade() =>
    sumBarsPerTrade = 0
    for tradeNo = 0 to strategy.closedtrades - 1
        // Loop through all closed trades, starting with the oldest.
        sumBarsPerTrade += strategy.closedtrades.exit_bar_index(tradeNo) - strategy.closedtrades.entry_bar_index(tradeNo) + 1
    result = nz(sumBarsPerTrade / strategy.closedtrades)
plot(avgBarsPerTrade())
```

另见

[strategy.closedtrades.exit_bar_index()][strategy.opentrades.entry_bar_index()]

###### strategy.closedtrades.entry_comment()



返回已关闭交易条目的注释消息，如果没有带有此`trade_num`的条目，则返回`na`。



```
strategy.closedtrades.entry_comment(trade_num) → series string
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.entry_comment()` Example", overlay = true)

stopPrice = open * 1.01

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))

if (longCondition)
    strategy.entry("Long", strategy.long, stop = stopPrice, comment = str.tostring(stopPrice, "#.####"))
    strategy.exit("EXIT", trail_points = 1000, trail_offset = 0)

var testTable = table.new(position.top_right, 1, 3, color.orange, border_width = 1)

if barstate.islastconfirmedhistory or barstate.isrealtime
    table.cell(testTable, 0, 0, 'Last closed trade:')
    table.cell(testTable, 0, 1, "Order stop price value: " + strategy.closedtrades.entry_comment(strategy.closedtrades - 1))
    table.cell(testTable, 0, 2, "Actual Entry Price: " + str.tostring(strategy.closedtrades.entry_price(strategy.closedtrades - 1)))
```

另见

[strategy()][strategy.entry()][strategy.closedtrades]

###### strategy.closedtrades.entry_id()



返回已平仓交易的入场的id。



```
strategy.closedtrades.entry_id(trade_num) → series string
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.entry_id Example", overlay = true)

// Enter a short position and close at the previous to last bar.
if bar_index == 1
    strategy.entry("Short at bar #" + str.tostring(bar_index), strategy.short)
if bar_index == last_bar_index - 2
    strategy.close_all()

// Display ID of the last entry position.
if barstate.islastconfirmedhistory
    label.new(last_bar_index, high, "Last Entry ID is: " + strategy.closedtrades.entry_id(strategy.closedtrades - 1))
```

返回值

返回已平仓交易的入场的id。

备注

如果 trade_num 不在范围内，则该函数返回 na：0 到 strategy.closedtrades-1。

另见

[strategy.closedtrades.entry_bar_index()][strategy.closedtrades.entry_price()][strategy.closedtrades.entry_time()]

###### strategy.closedtrades.entry_price()



返回已平仓交易的入场价格。



```
strategy.closedtrades.entry_price(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.entry_price Example 1")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Return the entry price for the latest entry.
entryPrice = strategy.closedtrades.entry_price(strategy.closedtrades - 1)

plot(entryPrice, "Long entry price")
```



```
// Calculates the average profit percentage for all closed trades.
//@version=6
strategy("strategy.closedtrades.entry_price Example 2")

// Strategy calls to create single short and long trades
if bar_index == last_bar_index - 15
    strategy.entry("Long Entry", strategy.long)
else if bar_index == last_bar_index - 10
    strategy.close("Long Entry")
    strategy.entry("Short", strategy.short)
else if bar_index == last_bar_index - 5
    strategy.close("Short")

// Calculate profit for both closed trades.
profitPct = 0.0
for tradeNo = 0 to strategy.closedtrades - 1
    entryP = strategy.closedtrades.entry_price(tradeNo)
    exitP = strategy.closedtrades.exit_price(tradeNo)
    profitPct += (exitP - entryP) / entryP * strategy.closedtrades.size(tradeNo) * 100

// Calculate average profit percent for both closed trades.
avgProfitPct = nz(profitPct / strategy.closedtrades)

plot(avgProfitPct)
```

另见

[strategy.closedtrades.entry_price()][strategy.closedtrades.exit_price()][strategy.closedtrades.size()][strategy.closedtrades]

###### strategy.closedtrades.entry_time()



返回已平仓交易入场的UNIX时间，以毫秒表示。



```
strategy.closedtrades.entry_time(trade_num) → series int
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.entry_time Example", overlay = true)

// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")

// Calculate the average trade duration
avgTradeDuration() =>
    sumTradeDuration = 0
    for i = 0 to strategy.closedtrades - 1
        sumTradeDuration += strategy.closedtrades.exit_time(i) - strategy.closedtrades.entry_time(i)
    result = nz(sumTradeDuration / strategy.closedtrades)

// Display average duration converted to seconds and formatted using 2 decimal points
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(avgTradeDuration() / 1000, "#.##") + " seconds")
```

另见

[strategy.opentrades.entry_time()][strategy.closedtrades.exit_time()][time]

###### strategy.closedtrades.exit_bar_index()



返回已平仓交易退出的bar_index。



```
strategy.closedtrades.exit_bar_index(trade_num) → series int
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.exit_bar_index Example 1")

// Strategy calls to place a single short trade. We enter the trade at the first bar and exit the trade at 10 bars before the last chart bar.
if bar_index == 0
    strategy.entry("Short", strategy.short)
if bar_index == last_bar_index - 10
    strategy.close("Short")

// Calculate the amount of bars since the last closed trade.
barsSinceClosed = strategy.closedtrades > 0 ? bar_index - strategy.closedtrades.exit_bar_index(strategy.closedtrades - 1) : na

plot(barsSinceClosed, "Bars since last closed trade")
```



```
// Calculates the average amount of bars per trade.
//@version=6
strategy("strategy.closedtrades.exit_bar_index Example 2")

// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")

// Function that calculates the average amount of bars per trade.
avgBarsPerTrade() =>
    sumBarsPerTrade = 0
    for tradeNo = 0 to strategy.closedtrades - 1
        // Loop through all closed trades, starting with the oldest.
        sumBarsPerTrade += strategy.closedtrades.exit_bar_index(tradeNo) - strategy.closedtrades.entry_bar_index(tradeNo) + 1
    result = nz(sumBarsPerTrade / strategy.closedtrades)

plot(avgBarsPerTrade())
```

另见

[bar_index][last_bar_index]

###### strategy.closedtrades.exit_comment()



返回已关闭交易退出的评论消息，如果没有此`trade_num`的条目，则返回`na`。



```
strategy.closedtrades.exit_comment(trade_num) → series string
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.exit_comment()` Example", overlay = true)

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit", stop = open * 0.95, limit = close * 1.05, trail_points = 100, trail_offset = 0, comment_profit = "TP", comment_loss = "SL", comment_trailing = "TRAIL")

exitStats() =>
    int slCount = 0
    int tpCount = 0
    int trailCount = 0

    if strategy.closedtrades > 0
        for i = 0 to strategy.closedtrades - 1
            switch strategy.closedtrades.exit_comment(i)
                "TP"    => tpCount    += 1
                "SL"    => slCount    += 1
                "TRAIL" => trailCount += 1
    [slCount, tpCount, trailCount]

var testTable = table.new(position.top_right, 1, 4, color.orange, border_width = 1)

if barstate.islastconfirmedhistory
    [slCount, tpCount, trailCount] = exitStats()
    table.cell(testTable, 0, 0, "Closed trades (" + str.tostring(strategy.closedtrades) +") stats:")
    table.cell(testTable, 0, 1, "Stop Loss: " + str.tostring(slCount))
    table.cell(testTable, 0, 2, "Take Profit: " + str.tostring(tpCount))
    table.cell(testTable, 0, 3, "Trailing Stop: " + str.tostring(trailCount))
```

另见

[strategy()][strategy.exit()][strategy.close()][strategy.closedtrades()]

###### strategy.closedtrades.exit_id()



返回已平仓交易的出场的id。



```
strategy.closedtrades.exit_id(trade_num) → series string
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.exit_id Example", overlay = true)

// Strategy calls to create single short and long trades
if bar_index == last_bar_index - 15
    strategy.entry("Long Entry", strategy.long)
else if bar_index == last_bar_index - 10
    strategy.entry("Short Entry", strategy.short)

// When a new open trade is detected then we create the exit strategy corresponding with the matching entry id
// We detect the correct entry id by determining if a position is long or short based on the position quantity
if ta.change(strategy.opentrades) != 0
    posSign = strategy.opentrades.size(strategy.opentrades - 1)
    strategy.exit(posSign > 0 ? "SL Long Exit" : "SL Short Exit", strategy.opentrades.entry_id(strategy.opentrades - 1), stop = posSign > 0 ? high - ta.tr : low + ta.tr)

// When a new closed trade is detected then we place a label above the bar with the exit info
if ta.change(strategy.closedtrades) != 0
    msg = "Trade closed by: " + strategy.closedtrades.exit_id(strategy.closedtrades - 1)
    label.new(bar_index, high + (3 * ta.tr), msg)
```

返回值

返回已平仓交易的出场的id。

备注

如果 trade_num 不在范围内，则该函数返回 na：0 到 strategy.closedtrades-1。

另见

[strategy.closedtrades.exit_bar_index()][strategy.closedtrades.exit_price()][strategy.closedtrades.exit_time()]

###### strategy.closedtrades.exit_price()



返回已平仓交易的出场价格。



```
strategy.closedtrades.exit_price(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.exit_price Example 1")

// We are creating a long trade every 5 bars
if bar_index % 5 == 0
    strategy.entry("Long", strategy.long)
strategy.close("Long")

// Return the exit price from the latest closed trade.
exitPrice = strategy.closedtrades.exit_price(strategy.closedtrades - 1)

plot(exitPrice, "Long exit price")
```



```
// Calculates the average profit percentage for all closed trades.
//@version=6
strategy("strategy.closedtrades.exit_price Example 2")

// Strategy calls to create single short and long trades.
if bar_index == last_bar_index - 15
    strategy.entry("Long Entry", strategy.long)
else if bar_index == last_bar_index - 10
    strategy.close("Long Entry")
    strategy.entry("Short", strategy.short)
else if bar_index == last_bar_index - 5
    strategy.close("Short")

// Calculate profit for both closed trades.
profitPct = 0.0
for tradeNo = 0 to strategy.closedtrades - 1
    entryP = strategy.closedtrades.entry_price(tradeNo)
    exitP = strategy.closedtrades.exit_price(tradeNo)
    profitPct += (exitP - entryP) / entryP * strategy.closedtrades.size(tradeNo) * 100

// Calculate average profit percent for both closed trades.
avgProfitPct = nz(profitPct / strategy.closedtrades)

plot(avgProfitPct)
```

另见

[strategy.closedtrades.entry_price()]

###### strategy.closedtrades.exit_time()



返回已平仓交易退出的UNIX时间，以毫秒表示。



```
strategy.closedtrades.exit_time(trade_num) → series int
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.closedtrades.exit_time Example 1")

// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")

// Calculate the average trade duration.
avgTradeDuration() =>
    sumTradeDuration = 0
    for i = 0 to strategy.closedtrades - 1
        sumTradeDuration += strategy.closedtrades.exit_time(i) - strategy.closedtrades.entry_time(i)
    result = nz(sumTradeDuration / strategy.closedtrades)

// Display average duration converted to seconds and formatted using 2 decimal points.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(avgTradeDuration() / 1000, "#.##") + " seconds")
```



```
// Reopens a closed trade after X seconds.
//@version=6
strategy("strategy.closedtrades.exit_time Example 2")

// Strategy calls to emulate a single long trade at the first bar.
if bar_index == 0
    strategy.entry("Long", strategy.long)

reopenPositionAfter(timeSec) =>
    if strategy.closedtrades > 0
        if time - strategy.closedtrades.exit_time(strategy.closedtrades - 1) >= timeSec * 1000
            strategy.entry("Long", strategy.long)

// Reopen last closed position after 120 sec.
reopenPositionAfter(120)

if ta.change(strategy.opentrades) != 0
    strategy.exit("Long", stop = low * 0.9, profit = high * 2.5)
```

另见

[strategy.closedtrades.entry_time()]

###### strategy.closedtrades.max_drawdown()



返回已平仓交易的最大回撤，即交易期间可能的最大损失，以[strategy.account_currency]表示。



```
strategy.closedtrades.max_drawdown(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.max_drawdown` Example")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Get the biggest max trade drawdown value from all of the closed trades.
maxTradeDrawDown() =>
    maxDrawdown = 0.0
    for tradeNo = 0 to strategy.closedtrades - 1
        maxDrawdown := math.max(maxDrawdown, strategy.closedtrades.max_drawdown(tradeNo))
    result = maxDrawdown

plot(maxTradeDrawDown(), "Biggest max drawdown")
```

备注

如果 trade_num 不在范围内，则该函数返回 na：0 到 strategy.closedtrades - 1。

另见

[strategy.opentrades.max_drawdown()][strategy.max_drawdown]

###### strategy.closedtrades.max_drawdown_percent()



返回已平仓交易的最大回撤，即交易期间可能的最大损失，以百分比表示并按公式计算：`Lowest Value During Trade / (Entry Price x Quantity) * 100`。



```
strategy.closedtrades.max_drawdown_percent(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。

另见

[strategy.closedtrades.max_drawdown()][strategy.max_drawdown]

###### strategy.closedtrades.max_runup()



返回已平仓交易的最大涨幅，即交易期间的最大可能利润，以[strategy.account_currency]表示。



```
strategy.closedtrades.max_runup(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.max_runup` Example")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Get the biggest max trade runup value from all of the closed trades.
maxTradeRunUp() =>
    maxRunup = 0.0
    for tradeNo = 0 to strategy.closedtrades - 1
        maxRunup := math.max(maxRunup, strategy.closedtrades.max_runup(tradeNo))
    result = maxRunup

plot(maxTradeRunUp(), "Max trade runup")
```

另见

[strategy.opentrades.max_runup()][strategy.max_runup]

###### strategy.closedtrades.max_runup_percent()



返回已平仓交易的最大涨幅，即交易期间的最大可能利润，以百分比表示并按公式计算：`Highest Value During Trade / (Entry Price x Quantity) * 100`。



```
strategy.closedtrades.max_runup_percent(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。

另见

[strategy.closedtrades.max_runup()][strategy.max_runup]

###### strategy.closedtrades.profit()



返回已平仓交易的盈亏，以策略账户货币计算，扣除交易佣金。返回正值表示盈利，负值表示亏损。



```
strategy.closedtrades.profit(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.profit()` example")

// Enter a long trade every 15 bars, and close a long trade every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

//@function Calculates the average gross profit from all available closed trades. 
avgGrossProfit() =>
    var float result = 0.0
    if result == 0.0 or strategy.closedtrades > strategy.closedtrades[1]
        float sumGrossProfit = 0.0
        for tradeNo = 0 to strategy.closedtrades - 1
            sumGrossProfit += strategy.closedtrades.profit(tradeNo)
        result := nz(sumGrossProfit / strategy.closedtrades)
    result

plot(avgGrossProfit(), "Average gross profit")
```

另见

[strategy.account_currency][strategy.opentrades.profit()][strategy.closedtrades.commission()]

###### strategy.closedtrades.profit_percent()



返回已平仓交易的损益值，以百分比表示。损失以负值表示。



```
strategy.closedtrades.profit_percent(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。

另见

[strategy.closedtrades.profit()]

###### strategy.closedtrades.size()



返回已平仓交易中的交易方向和合约数量。如果该值>0，则市场仓位为多头。 如果该值<0，则市场仓位为空头。



```
strategy.closedtrades.size(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.closedtrades.size` Example 1")

// We calculate the max amt of shares we can buy.
amtShares = math.floor(strategy.equity / close)
// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long, qty = amtShares)
if bar_index % 20 == 0
    strategy.close("Long")

// Plot the number of contracts traded in the last closed trade.
plot(strategy.closedtrades.size(strategy.closedtrades - 1), "Number of contracts traded")
```



```
// Calculates the average profit percentage for all closed trades.
//@version=6
strategy("`strategy.closedtrades.size` Example 2")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")


// Calculate profit for both closed trades.
profitPct = 0.0
for tradeNo = 0 to strategy.closedtrades - 1
    entryP = strategy.closedtrades.entry_price(tradeNo)
    exitP = strategy.closedtrades.exit_price(tradeNo)
    profitPct += (exitP - entryP) / entryP * strategy.closedtrades.size(tradeNo) * 100

// Calculate average profit percent for both closed trades.
avgProfitPct = nz(profitPct / strategy.closedtrades)

plot(avgProfitPct)
```

另见

[strategy.opentrades.size()][strategy.position_size][strategy.closedtrades][strategy.opentrades]

###### strategy.convert_to_account()



将图表上商品的货币值 `syminfo.currency` 转换为策略使用的货币 `strategy.account_currency`。



```
strategy.convert_to_account(value) → series float
```

参数

**value (series int/float)** 要转换的值。



```
//@version=6
strategy("`strategy.convert_to_account` Example 1", currency = currency.EUR)

plot(close, "Close price using default currency")
plot(strategy.convert_to_account(close), "Close price converted to strategy currency")
```



```
// Calculates the "Buy and hold return" using your account's currency.
//@version=6
strategy("`strategy.convert_to_account` Example 2", currency = currency.EUR)

dateInput = input.time(timestamp("20 Jul 2021 00:00 +0300"), "From Date", confirm = true)

buyAndHoldReturnPct(fromDate) =>
    if time >= fromDate
        money = close * syminfo.pointvalue
        var initialBal = strategy.convert_to_account(money)
        (strategy.convert_to_account(money) - initialBal) / initialBal * 100

plot(buyAndHoldReturnPct(dateInput))
```

另见

[strategy()][strategy.convert_to_symbol()]

###### strategy.convert_to_symbol()



将值从策略使用的货币 `strategy.account_currency` 转换为图表上商品的货币 `syminfo.currency`。



```
strategy.convert_to_symbol(value) → series float
```

参数

**value (series int/float)** 要转换的值。



```
//@version=6
strategy("`strategy.convert_to_symbol` Example", currency = currency.EUR)

// Calculate the max qty we can buy using current chart's currency.
calcContracts(accountMoney) =>
    math.floor(strategy.convert_to_symbol(accountMoney) / syminfo.pointvalue / close)

// Return max qty we can buy using 300 euros
qt = calcContracts(300)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars using our custom qty.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long, qty = qt)
if bar_index % 20 == 0
    strategy.close("Long")
```

另见

[strategy()][strategy.convert_to_account()]

###### strategy.default_entry_qty()



如果要按指定的`fill_price`值成交，则从[strategy.entry()]或[strategy.order()]计算挂单的默认数量，以单位为单位。计算取决于多个策略属性，包括`default_qty_type`、`default_qty_value`、`currency`以及[strategy()]函数中的其他参数，及其在策略设置的“属性”标签页中的表示形式。



```
strategy.default_entry_qty(fill_price) → series float
```

参数

**fill_price (series int/float)** 用于计算默认订单数量的成交价格。



```
//@version=6
strategy("Supertrend Strategy", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 15)

//@variable The length of the ATR calculation.
atrPeriod = input(10, "ATR Length")
//@variable The ATR multiplier.
factor = input.float(3.0, "Factor", step = 0.01)
//@variable The tick offset of the stop order.
stopOffsetInput = input.int(100, "Tick offset for entry stop")

// Get the direction of the SuperTrend.
[_, direction] = ta.supertrend(factor, atrPeriod)

if ta.change(direction) < 0
    //@variable The stop price of the entry order.
    stopPrice = close + syminfo.mintick * stopOffsetInput
    //@variable The expected default fill quantity at the `stopPrice`. This value may not reflect actual qty of the filled order, because fill price may be different.
    calculatedQty = strategy.default_entry_qty(stopPrice)
    strategy.entry("My Long Entry Id", strategy.long, stop = stopPrice)
    label.new(bar_index, stopPrice, str.format("Stop set at {0}\nExpected qty at {0}: {1}", math.round_to_mintick(stopPrice), calculatedQty))

if ta.change(direction) > 0
    strategy.close_all()
```

备注

该函数不考虑策略模拟的未平仓位。例如，如果策略脚本具有`qty`为10个单位的多头订单的未平仓位，使用[strategy.entry()]函数模拟`qty`为5的空单，将提示脚本卖出15个单位以反转仓位。在这种情况下，该函数仍将返回5，因为它不考虑未平仓交易。

该值代表订单的默认计算数量。

下单命令可以通过在函数调用中显式传递新的`qty`值来覆盖默认值。

###### strategy.entry()



创建新订单以开仓或加仓。如果存在具有相同`id`的未成交订单，则调用此命令会修改该订单。

生成的订单类型取决于`limit`和`stop`参数。如果调用不包含`limit`或`stop`参数，它会创建一个在下一个报价执行的[市价单]。如果调用指定了`limit`值但没有指定`stop` 值，它会下达一个[限价单]，在市场价格达到`limit`值或更优价格（买单更低，卖单更高）后执行。如果调用指定了`stop`值但没有指定`limit`值，则会下达[止损订单]，该订单在市场价格达到`stop`值或更差价格（买单为更高价格，卖单为更低价格）后执行。如果调用包含`limit`和`stop`参数，则会创建[止损限价]订单，该订单仅在市场价格达到`stop`值或更差价格后才会以`limit`价格生成限价订单。

与来自[strategy.order()]的订单不同，来自此命令的订单受[strategy()]声明语句的`pyramiding`参数的影响。金字塔式交易指定每个仓位允许的并发开仓数量。例如，使用`pyramiding = 3`，该策略最多可以有三笔开仓交易，并且该命令无法创建订单来开仓其他交易，直到至少有一笔现有交易结束。

默认情况下，当策略按照与当前市场仓位相反的方向执行此命令中的订单时，它会反转仓位。例如，如果有5股的未平多头仓位，则此命令中的`qty`为5且`direction`为[strategy.short]的订单将触发卖出10股以平仓多头仓位并开设新的5股空头仓位。用户可以通过使用[strategy.risk_allow_entry_in()]函数指定允许的方向来更改此行为。



```
strategy.entry(id, direction, qty, limit, stop, oca_name, oca_type, comment, alert_message, disable_alert) → void
```

参数

**id (series string)** 订单标识符，对应于订单成交后策略交易中的入场ID。如果策略在成交订单后开立新仓位，订单ID将成为[strategy.position_entry_name]值。策略命令可以引用订单ID来取消或修改挂单，并为特定未平仓交易生成退出订单。除非命令指定`comment`值，否则策略测试器和图表将显示订单ID。

**direction (series strategy_direction)** 交易的方向。可能的值：[strategy.long]表示多头交易，[strategy.short]表示空头交易。

**qty (series int/float)** 可选。订单成交时产生的未平仓交易的合约/股数/手数/单位数。默认值为`na`，这意味着该命令使用[strategy()]声明语句的`default_qty_type`和`default_qty_value`参数来确定数量。

**limit (series int/float)** 可选。订单的限价。如果指定，命令将创建限价或止损限价订单，具体取决于是否还指定了`stop`值。默认值为`na`，这意味着生成的订单不是限价或止损限价类型。

**stop (series int/float)** 可选。订单的止损价。如果指定，命令将创建止损或止损限价订单，具体取决于是否还指定了`limit`值。默认值为`na`，这意味着生成的订单不是止损或止损限价类型。

**oca_name (series string)** 可选。订单的“一取消全”(OCA)组的名称。当具有相同`oca_name`和`oca_type`参数的挂单执行时，该订单会影响该组内所有未成交的订单。默认值为空字符串，表示该订单不属于OCA组。

**oca_type (input string)** 可选。指定当另一个具有相同`oca_name`和`oca_type`值的挂单执行时未成交订单的行为。可能的值：[strategy.oca.cancel]、[strategy.oca.reduce]、[strategy.oca.none]。默认值为[strategy.oca.none]。

**comment (series string)** 可选。已成交订单的附加说明。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是指定的`id`。默认值为空字符串。

**alert_message (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。默认值为空字符串。

**disable_alert (series bool)** 可选。如果命令创建订单时为`true`，则该订单成交时策略不会触发警报。此参数接受“系列”值，这意味着用户可以控制哪些订单在执行时触发警报。默认值为`false`。



```
//@version=6
strategy("Market order strategy", overlay = true)

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

// Place a market order to close the short trade and enter a long position when `sma14` crosses over `sma28`.
if ta.crossover(sma14, sma28)
    strategy.entry("My Long Entry ID", strategy.long)

// Place a market order to close the long trade and enter a short position when `sma14` crosses under `sma28`.
if ta.crossunder(sma14, sma28)
    strategy.entry("My Short Entry ID", strategy.short)
```



```
//@version=6
strategy("Limit order strategy", overlay=true, margin_long=100, margin_short=100)

//@variable The distance from the `close` price for each limit order.
float limitOffsetInput = input.int(100, "Limit offset, in ticks", 1) * syminfo.mintick

//@function Draws a label and line at the specified `price` to visualize a limit order's level.
drawLimit(float price, bool isLong) =>
    color col = isLong ? color.blue : color.red
    label.new(
         bar_index, price, (isLong ? "Long" : "Short") + " limit order created",
         style = label.style_label_right, color = col, textcolor = color.white
     )
    line.new(bar_index, price, bar_index + 1, price, extend = extend.right, style = line.style_dashed, color = col)

//@function Stops the `l` line from extending further.
method stopExtend(line l) =>
    l.set_x2(bar_index)
    l.set_extend(extend.none)

// Initialize two `line` variables to reference limit line IDs.
var line longLimit  = na
var line shortLimit = na

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

if ta.crossover(sma14, sma28)
    // Cancel any unfilled sell orders with the specified ID.
    strategy.cancel("My Short Entry ID")
    //@variable The limit price level. Its value is `limitOffsetInput` ticks below the current `close`.
    float limitLevel = close - limitOffsetInput
    // Place a long limit order to close the short trade and enter a long position at the `limitLevel`.
    strategy.entry("My Long Entry ID", strategy.long, limit = limitLevel)
    // Make new drawings for the long limit and stop extending the `shortLimit` line.
    longLimit := drawLimit(limitLevel, isLong = true)
    shortLimit.stopExtend()

if ta.crossunder(sma14, sma28)
    // Cancel any unfilled buy orders with the specified ID.
    strategy.cancel("My Long Entry ID")
    //@variable The limit price level. Its value is `limitOffsetInput` ticks above the current `close`.
    float limitLevel = close + limitOffsetInput
    // Place a short limit order to close the long trade and enter a short position at the `limitLevel`.
    strategy.entry("My Short Entry ID", strategy.short, limit = limitLevel)
    // Make new drawings for the short limit and stop extending the `shortLimit` line.
    shortLimit := drawLimit(limitLevel, isLong = false)
    longLimit.stopExtend()
```

###### strategy.exit()



创建基于价格的订单以退出未平仓位。如果存在具有相同`id`的未完成退出订单，则调用此命令会修改这些订单。此命令可以生成多种类型的退出订单，具体取决于指定的参数。但是，它不会创建[市价单]。要使用市价单退出仓位，请使用[strategy.close()]或[strategy.close_all()]。

如果对此命令的调用包含`profit`或`limit`参数，它会创建[止盈]订单，以在确定的价格水平或更优值（多头交易更高，空头交易更低）退出适用交易。如果调用包含`loss`或`stop`参数，它会创建[止损] 订单，以在确定的水平或更差值（多头交易更低，空头交易更高）退出适用交易。使用`profit`或`limit`，和`loss`或 `stop`参数调用此命令会创建包含两种订单类型的订单括号。

此命令的调用指定了`trail_price`或`trail_points`参数和`trail_offset`参数时，可以创建[追踪止损]订单。当价格移动`trail_points`tick超过入场价或触及`trail_price`水平时，追踪止损订单将激活。一旦激活，每次交易利润达到新高时，止损都会跟随市场价格`trail_offset`tick。当交易未达到新的最佳值时，止损不会移动。

每次调用此命令都会保留一部分仓位以进行平仓，直到策略完成或取消其订单。例如，如果有50份合约的未平仓位，并且[strategy.exit()]调用指定`qty`为20，则该调用的订单会保留20份合约。第二个调用最多可以平仓30份合约，即使其`qty`为50且其中一个订单先执行。此行为不会影响其他命令的订单，例如[strategy.close()]或[strategy.order()]。

如果在创建的入场订单执行之前调用此命令，则该策略将等待并且在入场订单执行之后才创建退出订单。



```
strategy.exit(id, from_entry, qty, qty_percent, profit, limit, loss, stop, trail_price, trail_points, trail_offset, oca_name, comment, comment_profit, comment_loss, comment_trailing, alert_message, alert_profit, alert_loss, alert_trailing, disable_alert) → void
```

参数

**id (series string)** 订单标识符，对应于订单成交后策略交易中的退出ID。策略命令可以引用订单ID来取消或修改待定退出订单。策略测试程序和图表会显示订单ID，除非命令包含适用于已成交订单的`comment*`参数。

**from_entry (series string)** 可选。要退出的交易的入场订单ID。如果有多个具有指定入场ID的未平仓交易，则该命令将为调用之前或调用时的所有入场生成退出订单。默认值为空字符串，这意味着该命令将为所有未平仓交易生成退出订单，直到平仓。

**qty (series int/float)** 可选。退出订单成交时要关闭的合约/手数/股票/单位数。如果指定，命令将使用此值而不是`qty_percent`来确定订单大小。退出订单会从仓位中保留此数量，这意味着对该命令的其他调用无法关闭此部分，直到策略完成或取消这些订单。默认值为`na`，这意味着订单大小取决于`qty_percent`值。

**qty_percent (series int/float)** 可选。0到100之间的值，表示退出订单成交时要关闭的未平仓交易数量的百分比。退出订单从适用的未平仓交易中保留此百分比，这意味着对该命令的其他调用在策略成交或取消这些订单之前无法关闭此部分。百分比计算取决于适用的未平仓交易的总规模，而不考虑其他[strategy.exit()]调用的保留金额。如果`qty`值不是`na`，则命令将忽略此参数。默认值为100。

**profit (series int/float)** 可选。止盈距离，以刻度表示。如果指定，该命令将创建一个限价订单，以在距离入场价`profit`tick处以有利方向退出交易。订单以计算的价格或更优值执行。如果此参数和`limit`不是`na`，该命令仅在预期首先触发退出的价格水平下达止盈订单。默认值为`na`。

**limit (series int/float)** 可选。止盈价格。如果此参数和`profit`不是`na`，则命令仅在预期首先触发退出的价格水平下达止盈订单。默认值为`na`。

**loss (series int/float)** 可选。止损距离，以tick表示。如果指定，该命令将创建一个止损订单，以在不利方向上以距入场价格`loss`tick退出交易。订单以计算的价格或更差的值执行。如果此参数和`stop`不是`na`，则该命令仅在预期首先触发退出的价格水平下达止损订单。默认值为`na`。

**stop (series int/float)** 可选。止损价。如果此参数和`loss`不是`na`，则命令仅在预期首先触发退出的价格水平下止损订单。默认值为`na`。

**trail_price (series int/float)** 可选。追踪止损激活水平的价格。如果该值比入场价更有利，则命令会在市场价格达到该值时创建追踪止损。如果该值比入场价更不利，则命令会在当前市场价格等于或优于该值时立即创建追踪止损。如果此参数和`trail_points`不是`na`，则命令使用预期首先激活止损的值来设置激活水平。默认值为`na`。

**trail_points (series int/float)** 可选。追踪止损激活距离，以刻度表示。如果该值为正，则当市场价格向有利方向偏离交易入场价`trail_points`个tick时，命令会创建追踪止损订单。如果该值为负，则当市场价格等于或大于向不利方向偏离入场价`trail_points`个tick时，命令会立即创建追踪止损。默认值为`na`。

**trail_offset (series int/float)** 可选。追踪止损偏移量。当市场价格达到由`trail_price`或`trail_points`参数确定的激活水平，或超出有利方向的水平时，该命令会创建一个追踪止损，其初始值为`trail_offset`，从不利方向偏离该水平。激活后，每次交易利润达到更优值时，追踪止损都会向市场价格移动，与最佳价格保持指定的距离。默认值为`na`。

**oca_name (series string)** 可选。命令的止盈、止损和追踪止损订单所属的“一取消全”(OCA)组的名称。来自此命令的所有订单均为[strategy.oca.reduce]OCA类型。当具有相`oca_name`的此OCA类型的订单执行时，该策略会将OCA组中其他未成交订单的大小减少成交数量。默认值为空字符串，这意味着策略会自动分配OCA名称，并且生成的订单不能减少或被来自其他命令的订单减少。

**comment (series string)** 可选。已成交订单的附加说明。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是指定的`id`。如果调用包含适用于订单的`comment_*`参数的参数，则命令将忽略此值。默认值为空字符串。

**comment_profit (series string)** 可选。已成交订单的附加注释。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是指定的`id`或`comment`。此注释仅适用于使用`profit`或`limit`参数创建的命令的止盈订单。默认值为空字符串。

**comment_loss (series string)** 可选。已成交订单的附加注释。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是指定的`id`或`comment`。此注释仅适用于使用`loss`或`stop`参数创建的命令止损订单。默认值为空字符串。

**comment_trailing (series string)** 可选。已成交订单的附加注释。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是指定的`id`或`comment`。此注释仅适用于使用`trail_price`，或`trail_points`和`trail_offset`参数创建的命令的追踪止损订单。默认值为空字符串。

**alert_message (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。如果调用包含适用于订单的其他`alert_*`参数的参数，则命令将忽略此值。默认值为空字符串。

**alert_profit (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。此消息仅适用于使用`profit`或`limit`参数创建的命令的获利订单。默认值为空字符串。

**alert_loss (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包括`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。此消息仅适用于使用`loss`或`stop`参数创建的命令的止损订单。默认值为空字符串。

**alert_trailing (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。此消息仅适用于使用`trail_price`，或`trail_points`和`trail_offset`参数创建的命令的追踪止损订单。默认值为空字符串。

**disable_alert (series bool)** 可选。如果命令创建订单时为`true`，则该订单成交时策略不会触发警报。此参数接受“系列”值，这意味着用户可以控制哪些订单在执行时触发警报。默认值为`false`。



```
//@version=6
strategy("Exit bracket strategy", overlay = true)

// Inputs that define the profit and loss amount of each trade as a tick distance from the entry price.
int profitDistanceInput = input.int(100, "Profit distance, in ticks", 1)
int lossDistanceInput   = input.int(100, "Loss distance, in ticks", 1)

// Variables to track the take-profit and stop-loss price.
var float takeProfit = na
var float stopLoss   = na

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

if ta.crossover(sma14, sma28) and strategy.opentrades == 0
    // Place a market order to enter a long position.
    strategy.entry("My Long Entry ID", strategy.long)
    // Place a take-profit and stop-loss order when the entry order fills.
    strategy.exit("My Long Exit ID", "My Long Entry ID", profit = profitDistanceInput, loss = lossDistanceInput)

if ta.change(strategy.opentrades) == 1
    //@variable The long entry price.
    float entryPrice = strategy.opentrades.entry_price(0)
    // Update the `takeProfit` and `stopLoss` values.
    takeProfit := entryPrice + profitDistanceInput * syminfo.mintick
    stopLoss   := entryPrice - lossDistanceInput * syminfo.mintick

if ta.change(strategy.closedtrades) == 1
    // Reset the `takeProfit` and `stopLoss`.
    takeProfit := na
    stopLoss   := na

// Plot the `takeProfit` and `stopLoss`.
plot(takeProfit, "Take-profit level", color.green, 2, plot.style_linebr)
plot(stopLoss, "Stop-loss level", color.red, 2, plot.style_linebr)
```



```
//@version=6
strategy("Trailing stop strategy", overlay = true)

//@variable The distance required to activate the trailing stop.
float activationDistanceInput = input.int(100, "Trail activation distance, in ticks") * syminfo.mintick
//@variable The number of ticks the trailing stop follows behind the price as it reaches new peaks.
int trailDistanceInput = input.int(100, "Trail distance, in ticks")

//@function Draws a label and line at the specified `price` to visualize a trailing stop order's activation level.
drawActivation(float price) =>
    label.new(
         bar_index, price, "Activation level", style = label.style_label_right,
         color = color.gray, textcolor = color.white
     )
    line.new(
         bar_index, price, bar_index + 1, price, extend = extend.right, style = line.style_dashed, color = color.gray
     )

//@function Stops the `l` line from extending further.
method stopExtend(line l) =>
    l.set_x2(bar_index)
    l.set_extend(extend.none)

// The activation line, active trailing stop price, and active trailing stop flag.
var line activationLine     = na
var float trailingStopPrice = na
var bool isActive           = false

if bar_index % 100 == 0 and strategy.opentrades == 0
    trailingStopPrice := na
    isActive          := false
    // Place a market order to enter a long position.
    strategy.entry("My Long Entry ID", strategy.long)
    //@variable The activation level's price.
    float activationPrice = close + activationDistanceInput
    // Create a trailing stop order that activates the defined number of ticks above the entry price.
    strategy.exit(
         "My Long Exit ID", "My Long Entry ID", trail_price = activationPrice, trail_offset = trailDistanceInput,
         oca_name = "Exit"
     )
    // Create new drawings at the `activationPrice`.
    activationLine := drawActivation(activationPrice)

// Logic for trailing stop visualization.
if strategy.opentrades == 1
    // Stop extending the `activationLine` when the stop activates.
    if not isActive and high > activationLine.get_price(bar_index)
        isActive := true
        activationLine.stopExtend()
    // Update the `trailingStopPrice` while the trailing stop is active.
    if isActive
        float offsetPrice = high - trailDistanceInput * syminfo.mintick
        trailingStopPrice := math.max(nz(trailingStopPrice, offsetPrice), offsetPrice)

// Close the trade with a market order if the trailing stop does not activate before the next 300th bar.
if not isActive and bar_index % 300 == 0
    strategy.close_all("Market close")

// Reset the `trailingStopPrice` and `isActive` flags when the trade closes, and stop extending the `activationLine`.
if ta.change(strategy.closedtrades) > 0
    if not isActive
        activationLine.stopExtend()
    trailingStopPrice := na
    isActive          := false

// Plot the `trailingStopPrice`.
plot(trailingStopPrice, "Trailing stop", color.red, 3, plot.style_linebr)
```

备注

一次调用[strategy.exit()]命令即可为未平仓位的多个入场点生成退出订单，具体取决于调用的`from_entry`值。如果调用不包含 `from_entry` 参数，它会为所有未平仓交易创建退出订单，即使是调用后开仓的交易，直到仓位关闭。请参阅我们的用户手册中的[这个]部分，了解更多信息。

当一个仓位由多笔未平仓交易组成，并且[strategy()]声明语句中的`close_entries_rule`为“FIFO”（默认）时，来自[strategy.exit()]调用的订单将从第一笔未平仓交易开始退出仓位。即使`from_entry`值是不同未平仓交易的入场ID，此行为也适用。但是，在这种情况下，退出订单的最大规模仍然取决于ID为`from_entry`的订单开仓的交易。有关更多信息，请参阅我们的用户手册的[这个]部分。

如果[strategy.exit()]调用包含创建止损和追踪止损订单的参数，则该命令仅下达应该首先填写的订单，因为两个订单都是“止损”类型。

###### strategy.opentrades.commission()



返回未平仓交易中支付的入场费和出场费总和，以[strategy.account_currency]表示。



```
strategy.opentrades.commission(trade_num) → series float
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
// Calculates the gross profit or loss for the current open position.
//@version=6
strategy("`strategy.opentrades.commission` Example", commission_type = strategy.commission.percent, commission_value = 0.1)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculate gross profit or loss for open positions only.
tradeOpenGrossPL() =>
    sumOpenGrossPL = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        sumOpenGrossPL += strategy.opentrades.profit(tradeNo) - strategy.opentrades.commission(tradeNo)
    result = sumOpenGrossPL

plot(tradeOpenGrossPL())
```

另见

[strategy()][strategy.closedtrades.commission()]

###### strategy.opentrades.entry_bar_index()



返回未平仓交易入场的bar_index。



```
strategy.opentrades.entry_bar_index(trade_num) → series int
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
// Wait 10 bars and then close the position.
//@version=6
strategy("`strategy.opentrades.entry_bar_index` Example")

barsSinceLastEntry() =>
    strategy.opentrades > 0 ? bar_index - strategy.opentrades.entry_bar_index(strategy.opentrades - 1) : na

// Enter a long position if there are no open positions.
if strategy.opentrades == 0
    strategy.entry("Long", strategy.long)

// Close the long position after 10 bars.
if barsSinceLastEntry() >= 10
    strategy.close("Long")
```

另见

[strategy.closedtrades.entry_bar_index()][strategy.closedtrades.exit_bar_index()]

###### strategy.opentrades.entry_comment()



返回未平仓交易条目的注释消息，如果没有带有此`trade_num`的条目，则返回`na`。



```
strategy.opentrades.entry_comment(trade_num) → series string
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.opentrades.entry_comment()` Example", overlay = true)

stopPrice = open * 1.01

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))

if (longCondition)
    strategy.entry("Long", strategy.long, stop = stopPrice, comment = str.tostring(stopPrice, "#.####"))

var testTable = table.new(position.top_right, 1, 3, color.orange, border_width = 1)

if barstate.islastconfirmedhistory or barstate.isrealtime
    table.cell(testTable, 0, 0, 'Last entry stats')
    table.cell(testTable, 0, 1, "Order stop price value: " + strategy.opentrades.entry_comment(strategy.opentrades - 1))
    table.cell(testTable, 0, 2, "Actual Entry Price: " + str.tostring(strategy.opentrades.entry_price(strategy.opentrades - 1)))
```

另见

[strategy()][strategy.entry()][strategy.opentrades]

###### strategy.opentrades.entry_id()



返回未平仓交易的入场的ID。



```
strategy.opentrades.entry_id(trade_num) → series string
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.opentrades.entry_id` Example", overlay = true)

// We enter a long position when 14 period sma crosses over 28 period sma.
// We enter a short position when 14 period sma crosses under 28 period sma.
longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
shortCondition = ta.crossunder(ta.sma(close, 14), ta.sma(close, 28))

// Strategy calls to enter a long or short position when the corresponding condition is met.
if longCondition
    strategy.entry("Long entry at bar #" + str.tostring(bar_index), strategy.long)
if shortCondition
    strategy.entry("Short entry at bar #" + str.tostring(bar_index), strategy.short)

// Display ID of the latest open position.
if barstate.islastconfirmedhistory
    label.new(bar_index, high + (2 * ta.tr), "Last opened position is \n " + strategy.opentrades.entry_id(strategy.opentrades - 1))
```

返回值

返回未平仓交易的入场的ID。

备注

如果 trade_num 不在范围内，则该函数返回 na：0 到 strategy.opentrades-1。

另见

[strategy.opentrades.entry_bar_index()][strategy.opentrades.entry_price()][strategy.opentrades.entry_time()]

###### strategy.opentrades.entry_price()



返回未平仓交易的入场价格。



```
strategy.opentrades.entry_price(trade_num) → series float
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.opentrades.entry_price Example 1", overlay = true)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if ta.crossover(close, ta.sma(close, 14))
    strategy.entry("Long", strategy.long)

// Return the entry price for the latest closed trade.
currEntryPrice = strategy.opentrades.entry_price(strategy.opentrades - 1)
currExitPrice = currEntryPrice * 1.05

if high >= currExitPrice
    strategy.close("Long")

plot(currEntryPrice, "Long entry price", style = plot.style_linebr)
plot(currExitPrice, "Long exit price", color.green, style = plot.style_linebr)
```



```
// Calculates the average price for the open position.
//@version=6
strategy("strategy.opentrades.entry_price Example 2", pyramiding = 2)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculates the average price for the open position.
avgOpenPositionPrice() =>
    sumOpenPositionPrice = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        sumOpenPositionPrice += strategy.opentrades.entry_price(tradeNo) * strategy.opentrades.size(tradeNo) / strategy.position_size
    result = nz(sumOpenPositionPrice / strategy.opentrades)

plot(avgOpenPositionPrice())
```

另见

[strategy.closedtrades.exit_price()]

###### strategy.opentrades.entry_time()



返回未平仓交易入场的UNIX时间，以毫秒表示。



```
strategy.opentrades.entry_time(trade_num) → series int
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.opentrades.entry_time Example")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculates duration in milliseconds since the last position was opened.
timeSinceLastEntry()=>
    strategy.opentrades > 0 ? (time - strategy.opentrades.entry_time(strategy.opentrades - 1)) : na

plot(timeSinceLastEntry() / 1000 * 60 * 60 * 24, "Days since last entry")
```

另见

[strategy.closedtrades.entry_time()][strategy.closedtrades.exit_time()]

###### strategy.opentrades.max_drawdown()



返回未平仓交易的最大回撤，即交易期间可能的最大损失，以[strategy.account_currency]表示。



```
strategy.opentrades.max_drawdown(trade_num) → series float
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.opentrades.max_drawdown Example 1")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Plot the max drawdown of the latest open trade.
plot(strategy.opentrades.max_drawdown(strategy.opentrades - 1), "Max drawdown of the latest open trade")
```



```
// Calculates the max trade drawdown value for all open trades.
//@version=6
strategy("`strategy.opentrades.max_drawdown` Example 2", pyramiding = 100)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Get the biggest max trade drawdown value from all of the open trades.
maxTradeDrawDown() =>
    maxDrawdown = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        maxDrawdown := math.max(maxDrawdown, strategy.opentrades.max_drawdown(tradeNo))
    result = maxDrawdown

plot(maxTradeDrawDown(), "Biggest max drawdown")
```

备注

如果 trade_num 不在范围内，则该函数返回 na：0 到 strategy.closedtrades - 1。

另见

[strategy.closedtrades.max_drawdown()][strategy.max_drawdown]

###### strategy.opentrades.max_drawdown_percent()



返回未平仓交易的最大回撤，即交易期间可能的最大损失，以百分比表示并按公式计算：`Lowest Value During Trade / (Entry Price x Quantity) * 100`。



```
strategy.opentrades.max_drawdown_percent(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。

另见

[strategy.opentrades.max_drawdown()][strategy.max_drawdown]

###### strategy.opentrades.max_runup()



返回未平仓交易的最大涨幅，即交易期间的最大可能利润，以[strategy.account_currency]表示。



```
strategy.opentrades.max_runup(trade_num) → series float
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("strategy.opentrades.max_runup Example 1")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Plot the max runup of the latest open trade.
plot(strategy.opentrades.max_runup(strategy.opentrades - 1), "Max runup of the latest open trade")
```



```
// Calculates the max trade runup value for all open trades.
//@version=6
strategy("strategy.opentrades.max_runup Example 2", pyramiding = 100)

// Enter a long position every 30 bars.
if bar_index % 30 == 0
    strategy.entry("Long", strategy.long)

// Calculate biggest max trade runup value from all of the open trades.
maxOpenTradeRunUp() =>
    maxRunup = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        maxRunup := math.max(maxRunup, strategy.opentrades.max_runup(tradeNo))
    result = maxRunup

plot(maxOpenTradeRunUp(), "Biggest max runup of all open trades")
```

另见

[strategy.closedtrades.max_runup()][strategy.max_drawdown]

###### strategy.opentrades.max_runup_percent()



返回未平仓交易的最大涨幅，即交易期间的最大可能利润，以百分比表示并按公式计算：`Highest Value During Trade / (Entry Price x Quantity) * 100`。



```
strategy.opentrades.max_runup_percent(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。

另见

[strategy.opentrades.max_runup()][strategy.max_runup]

###### strategy.opentrades.profit()



返回未平仓交易的利润/损失，以[strategy.account_currency]表示。损失以负值表示。



```
strategy.opentrades.profit(trade_num) → series float
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
// Returns the profit of the last open trade.
//@version=6
strategy("`strategy.opentrades.profit` Example 1", commission_type = strategy.commission.percent, commission_value = 0.1)

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

plot(strategy.opentrades.profit(strategy.opentrades - 1), "Profit of the latest open trade")
```



```
// Calculates the profit for all open trades.
//@version=6
strategy("`strategy.opentrades.profit` Example 2", pyramiding = 5)

// Strategy calls to enter 5 long positions every 2 bars.
if bar_index % 2 == 0
    strategy.entry("Long", strategy.long, qty = 5)

// Calculate open profit or loss for the open positions.
tradeOpenPL() =>
    sumProfit = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        sumProfit += strategy.opentrades.profit(tradeNo)
    result = sumProfit

plot(tradeOpenPL(), "Profit of all open trades")
```

另见

[strategy.closedtrades.profit()][strategy.openprofit][strategy.netprofit][strategy.grossprofit]

###### strategy.opentrades.profit_percent()



返回未平仓交易的利润/损失，以百分比表示。损失以负值表示。



```
strategy.opentrades.profit_percent(trade_num) → series float
```

参数

**trade_num (series int)** 已平仓交易的交易编号。第一笔交易的编号为零。

另见

[strategy.opentrades.profit()]

###### strategy.opentrades.size()



返回未平仓交易中的交易方向和合约数量。如果该值>0，则市场仓位为多头。如果该值<0，则市场仓位为空头。



```
strategy.opentrades.size(trade_num) → series float
```

参数

**trade_num (series int)** 未平仓交易的交易编号。第一笔交易的编号为零。



```
//@version=6
strategy("`strategy.opentrades.size` Example 1")

// We calculate the max amt of shares we can buy.
amtShares = math.floor(strategy.equity / close)
// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long, qty = amtShares)
if bar_index % 20 == 0
    strategy.close("Long")

// Plot the number of contracts in the latest open trade.
plot(strategy.opentrades.size(strategy.opentrades - 1), "Amount of contracts in latest open trade")
```



```
// Calculates the average profit percentage for all open trades.
//@version=6
strategy("`strategy.opentrades.size` Example 2")

// Strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculate profit for all open trades.
profitPct = 0.0
for tradeNo = 0 to strategy.opentrades - 1
    entryP = strategy.opentrades.entry_price(tradeNo)
    exitP = close
    profitPct += (exitP - entryP) / entryP * strategy.opentrades.size(tradeNo) * 100

// Calculate average profit percent for all open trades.
avgProfitPct = nz(profitPct / strategy.opentrades)
plot(avgProfitPct)
```

另见

[strategy.closedtrades.size()][strategy.position_size][strategy.opentrades][strategy.closedtrades]

###### strategy.order()



创建新订单以开仓、增仓或平仓。如果存在具有相同`id`的未成交订单，则调用此命令会修改该订单。

生成的订单类型取决于`limit`和`stop`参数。如果调用不包含`limit`或`stop`参数，它会创建一个在下一个报价执行的[市价单]。如果调用指定了`limit`值但没有指定`stop` 值，它会下达一个[限价单]，在市场价格达到`limit`值或更优价格（买单更低，卖单更高）后执行。如果调用指定了`stop`值但没有指定`limit`值，则会下达[止损订单]，该订单在市场价格达到`stop`值或更差价格（买单为更高价格，卖单为更低价格）后执行。如果调用包含`limit`和`stop`参数，则会创建[止损限价]订单，该订单仅在市场价格达到`stop`值或更差价格后才会以`limit`价格生成限价订单。

与来自[strategy.entry()]的订单不同，来自此命令的订单不受[strategy()]声明语句的`pyramiding`参数的影响。策略可以通过调用此函数在同一方向开立任意数量的交易。

此命令不会自动反转未平仓位，因为它不像[strategy.entry()]那样专门创建入场订单。例如，如果有5股未平仓多头仓位，则此命令中的`qty`为5且`direction`为[strategy.short]的订单将触发卖出5股，从而平仓。



```
strategy.order(id, direction, qty, limit, stop, oca_name, oca_type, comment, alert_message, disable_alert) → void
```

参数

**id (series string)** 订单的标识符，对应于订单成交后策略交易中的入场或退出ID。如果策略在成交订单后开立新仓位，订单的ID将成为[strategy.position_entry_name]值。策略命令可以引用订单ID来取消或修改挂单，并为特定的未平仓交易生成退出订单。除非命令指定`comment`值，否则策略测试器和图表将显示订单 ID。

**direction (series strategy_direction)** 交易的方向。可能的值：[strategy.long]表示多头交易，[strategy.short]表示空头交易。

**qty (series int/float)** 可选。订单成交时交易的合约/股数/手数/单位数。默认值为`na`，这意味着该命令使用[strategy()]声明语句的`default_qty_type`和`default_qty_value`参数来确定数量。

**limit (series int/float)** 可选。订单的限价。如果指定，命令将创建限价或止损限价订单，具体取决于是否还指定了`stop`值。默认值为`na`，这意味着生成的订单不是限价或止损限价类型。

**stop (series int/float)** 可选。订单的止损价。如果指定，命令将创建止损或止损限价订单，具体取决于是否还指定了`limit`值。默认值为`na`，这意味着生成的订单不是止损或止损限价类型。

**oca_name (series string)** 可选。订单的“一取消全”(OCA)组的名称。当具有相同`oca_name`和`oca_type`参数的挂单执行时，该订单会影响该组内所有未成交的订单。默认值为空字符串，表示该订单不属于OCA组。

**oca_type (input string)** 可选。指定当另一个具有相同`oca_name`和`oca_type`值的挂单执行时未成交订单的行为。可能的值：[strategy.oca.cancel]、[strategy.oca.reduce]、[strategy.oca.none]。默认值为[strategy.oca.none]。

**comment (series string)** 可选。已成交订单的附加说明。如果值不是空字符串，策略测试程序和图表将显示订单的此文本，而不是指定的`id`。默认值为空字符串。

**alert_message (series string)** 可选。订单成交时触发的警报的自定义文本。如果“创建警报”对话框的“消息”字段包含`{{strategy.order.alert_message}}`占位符，则警报消息将用此文本替换占位符。默认值为空字符串。

**disable_alert (series bool)** 可选。如果命令创建订单时为`true`，则该订单成交时策略不会触发警报。此参数接受“系列”值，这意味着用户可以控制哪些订单在执行时触发警报。默认值为`false`。



```
//@version=6
strategy("Market order strategy", overlay = true)

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

// Place a market order to enter a long position when `sma14` crosses over `sma28`.
if ta.crossover(sma14, sma28) and strategy.position_size == 0
    strategy.order("My Long Entry ID", strategy.long)

// Place a market order to sell the same quantity as the long trade when `sma14` crosses under `sma28`,
// effectively closing the long position.
if ta.crossunder(sma14, sma28) and strategy.position_size > 0
    strategy.order("My Long Exit ID", strategy.short)
```



```
//@version=6
strategy("Limit and stop exit strategy", overlay = true)

//@variable The distance from the long entry price for each short limit order.
float shortOffsetInput = input.int(200, "Sell limit/stop offset, in ticks", 1) * syminfo.mintick

//@function Draws a label and line at the specified `price` to visualize a limit order's level.
drawLimit(float price, bool isLong, bool isStop = false) =>
    color col = isLong ? color.blue : color.red
    label.new(
         bar_index, price, (isLong ? "Long " : "Short ") + (isStop ? "stop" : "limit") + " order created",
         style = label.style_label_right, color = col, textcolor = color.white
     )
    line.new(bar_index, price, bar_index + 1, price, extend = extend.right, style = line.style_dashed, color = col)

//@function Stops the `l` line from extending further.
method stopExtend(line l) =>
    l.set_x2(bar_index)
    l.set_extend(extend.none)

// Initialize two `line` variables to reference limit and stop line IDs.
var line profitLimit = na
var line lossStop    = na

// Calculate a 14-bar and 28-bar moving average of `close` prices.
float sma14 = ta.sma(close, 14)
float sma28 = ta.sma(close, 28)

if ta.crossover(sma14, sma28) and strategy.position_size == 0
    // Place a market order to enter a long position.
    strategy.order("My Long Entry ID", strategy.long)

if strategy.position_size > 0 and strategy.position_size[1] == 0
    //@variable The entry price of the long trade.
    float entryPrice = strategy.opentrades.entry_price(0)
    // Calculate short limit and stop levels above and below the `entryPrice`.
    float profitLevel = entryPrice + shortOffsetInput
    float lossLevel   = entryPrice - shortOffsetInput
    // Place short limit and stop orders at the `profitLevel` and `lossLevel`.
    strategy.order("Profit", strategy.short, limit = profitLevel, oca_name = "Bracket", oca_type = strategy.oca.cancel)
    strategy.order("Loss", strategy.short, stop = lossLevel, oca_name = "Bracket", oca_type = strategy.oca.cancel)
    // Make new drawings for the `profitLimit` and `lossStop` lines.
    profitLimit := drawLimit(profitLevel, isLong = false)
    lossStop    := drawLimit(lossLevel, isLong = false, isStop = true)

if ta.change(strategy.closedtrades) > 0
    // Stop extending the `profitLimit` and `lossStop` lines.
    profitLimit.stopExtend()
    lossStop.stopExtend()
```

###### strategy.risk.allow_entry_in()



此函数可用于指定[strategy.entry()]函数允许在哪个市场方向开仓。



```
strategy.risk.allow_entry_in(value) → void
```

参数

**value (simple string)** 允许的方向。可能的值：[strategy.direction.all]、[strategy.direction.long]、[strategy.direction.short]



```
//@version=6
strategy("strategy.risk.allow_entry_in")

strategy.risk.allow_entry_in(strategy.direction.long)
if open > close
    strategy.entry("Long", strategy.long)
// Instead of opening a short position with 10 contracts, this command will close long entries.
if open < close
    strategy.entry("Short", strategy.short, qty = 10)
```

###### strategy.risk.max_cons_loss_days()



此规则的目的是取消所有挂单，了结所有未平仓位，并在指定数量的连续止损之后停止下单。 此规则影响所有策略。



```
strategy.risk.max_cons_loss_days(count, alert_message) → void
```

参数

**count (simple int)** 必要参数。允许连续亏损的天数。

**alert_message (simple string)** 一个可选参数，用于在“创建警报”对话框的"消息"字段中使用时替换{{strategy.order.alert_message}}占位符。



```
//@version=6
strategy("risk.max_cons_loss_days Demo 1")
strategy.risk.max_cons_loss_days(3) // No orders will be placed after 3 days, if each day is with loss.
plot(strategy.position_size)
```

###### strategy.risk.max_drawdown()



此规则的目的是确定最大跌幅。 规则影响整个策略。 一旦达到最大下降值，所有待处理订单都将被取消，所有未平仓位都将被关闭，并且不会放置新订单。



```
strategy.risk.max_drawdown(value, type, alert_message) → void
```

参数

**value (simple int/float)** 必要参数。最大回撤值。可被指定为金额(基准货币)，或最大权本的百分比。若是权本的百分比，数值为 0 至 100 之间。

**type (simple string)** 必要参数。 值的类型。 请指定下列值之一：[strategy.percent_of_equity]或[strategy.cash]。 注意：如果股本下降到零或负值，并且指定“strategy.percent_of_equity”，则所有未完成订单都将被取消，所有未平仓位都将被关闭，并且不会下新的订单。

**alert_message (simple string)** 一个可选参数，用于在“创建警报”对话框的"消息"字段中使用时替换{{strategy.order.alert_message}}占位符。



```
//@version=6
strategy("risk.max_drawdown Demo 1")
strategy.risk.max_drawdown(50, strategy.percent_of_equity) // set maximum drawdown to 50% of maximum equity
plot(strategy.position_size)
```



```
//@version=6
strategy("risk.max_drawdown Demo 2", currency = "EUR")
strategy.risk.max_drawdown(2000, strategy.cash) // set maximum drawdown to 2000 EUR from maximum equity
plot(strategy.position_size)
```

###### strategy.risk.max_intraday_filled_orders()



此规则的目的是确定每1天成交订单的最大数量(如果图表周期高于1天，则取每1条)。 规则影响整个策略。 一旦达到已下单的最大数量，所有待处理订单都将被取消，所有未平仓位将被关闭，直到当前交易时段结束为止，不会成交新订单。



```
strategy.risk.max_intraday_filled_orders(count, alert_message) → void
```

参数

**count (simple int)** 必选参数。每1天完成订单的最大数量。

**alert_message (simple string)** 一个可选参数，用于在“创建警报”对话框的"消息"字段中使用时替换{{strategy.order.alert_message}}占位符。



```
//@version=6
strategy("risk.max_intraday_filled_orders Demo")
strategy.risk.max_intraday_filled_orders(10) // After 10 orders are filled, no more strategy orders will be placed (except for a market order to exit current open market position, if there is any).
if open > close
    strategy.entry("buy", strategy.long)
if open < close
    strategy.entry("sell", strategy.short)
```

###### strategy.risk.max_intraday_loss()



一天内允许的最大损失值。它以货币（基础货币）或最大盘中股权价值的百分比（0 -100）指定。



```
strategy.risk.max_intraday_loss(value, type, alert_message) → void
```

参数

**value (simple int/float)** 一个必需的参数。最大损失值。它以货币（基础货币）或最大盘中股权价值的百分比指定。对于股权百分比，允许值的范围是从0到100。

**type (simple string)** 必要参数。值的类型。请指定以下值之一：[strategy.percent_of_equity]或[strategy.cash]。注意：如果净值降至零或负数，并且指定了[strategy.percent_of_equity]，则所有挂单将被取消，所有未平仓位将被平仓，并且无法永久下达新订单。

**alert_message (simple string)** 一个可选参数，用于在“创建警报”对话框的"消息"字段中使用时替换{{strategy.order.alert_message}}占位符。



```
// Sets the maximum intraday loss using the strategy's equity value.
//@version=6
strategy("strategy.risk.max_intraday_loss Example 1", overlay = false, default_qty_type = strategy.percent_of_equity, default_qty_value = 100)

// Input for maximum intraday loss %.
lossPct = input.float(10)

// Set maximum intraday loss to our lossPct input
strategy.risk.max_intraday_loss(lossPct, strategy.percent_of_equity)

// Enter Short at bar_index zero.
if bar_index == 0
    strategy.entry("Short", strategy.short)

// Store equity value from the beginning of the day
eqFromDayStart = ta.valuewhen(ta.change(dayofweek) > 0, strategy.equity, 0)

// Calculate change of the current equity from the beginning of the current day.
eqChgPct = 100 * ((strategy.equity - eqFromDayStart) / strategy.equity)

// Plot it
plot(eqChgPct)
hline(-lossPct)
```



```
// Sets the maximum intraday loss using the strategy's cash value.
//@version=6
strategy("strategy.risk.max_intraday_loss Example 2", overlay = false)

// Input for maximum intraday loss in absolute cash value of the symbol.
absCashLoss = input.float(5)

// Set maximum intraday loss to `absCashLoss` in account currency.
strategy.risk.max_intraday_loss(absCashLoss, strategy.cash)

// Enter Short at bar_index zero.
if bar_index == 0
    strategy.entry("Short", strategy.short)

// Store the open price value from the beginning of the day.
beginPrice = ta.valuewhen(ta.change(dayofweek) > 0, open, 0)

// Calculate the absolute price change for the current period.
priceChg = (close - beginPrice)

hline(absCashLoss)
plot(priceChg)
```

另见

[strategy()][strategy.percent_of_equity][strategy.cash]

###### strategy.risk.max_position_size()



此规则的目的是确定市场仓位的最大值。 该规则影响以下功能：[strategy.entry()]。 “entry”数量可以减少(如果需要)到合同/股/手/单位数，所以仓位总值不超过'strategy.risk.max_position_size'中指定的值。 如果最低数量仍然违反规则，则不会放置订单。



```
strategy.risk.max_position_size(contracts) → void
```

参数

**contracts (simple int/float)** 必要参数。仓位的合同/股/手/单位的最大数。



```
//@version=6
strategy("risk.max_position_size Demo", default_qty_value = 100)
strategy.risk.max_position_size(10)
if open > close
    strategy.entry("buy", strategy.long)
plot(strategy.position_size) // max plot value will be 10
```

###### string()

4过载



转换na成string

语法和重载

[`string(x) → const string`][`string(x) → input string`][`string(x) → simple string`][`string(x) → series string`]

参数

**x (const string)** 要转换为指定类型的值，通常为`na`。

返回值

转换为字符串后参数的值。

另见

[float()][int()][bool()][color()][line()][label()]

###### syminfo.prefix()

2过载



返回 `symbol` 的交易所前缀，例如“NASDAQ”。

语法和重载

[`syminfo.prefix(symbol) → simple string`][`syminfo.prefix(symbol) → series string`]

参数

**symbol (simple string)** 商品代码。请注意，该商品代码应带有前缀。例如：是 “NASDAQ:AAPL” 而不是 “AAPL”。



```
//@version=6
indicator("syminfo.prefix fun", overlay=true)
i_sym = input.symbol("NASDAQ:AAPL")
pref = syminfo.prefix(i_sym)
tick = syminfo.ticker(i_sym)
t = ticker.new(pref, tick, session.extended)
s = request.security(t, "1D", close)
plot(s)
```

返回值

返回 `symbol` 的交易所前缀，例如“NASDAQ”。

备注

该函数的结果用于[ticker.new()]/[ticker.modify()]和[request.security()]。

另见

[syminfo.tickerid][syminfo.ticker][syminfo.prefix][syminfo.ticker()][ticker.new()]

###### syminfo.ticker()

2过载



返回不带交易所前缀的 `symbol` 名称，例如“AAPL”。

语法和重载

[`syminfo.ticker(symbol) → simple string`][`syminfo.ticker(symbol) → series string`]

参数

**symbol (simple string)** 商品代码。请注意，该商品代码应带有前缀。例如：是 “NASDAQ:AAPL” 而不是 “AAPL”。



```
//@version=6
indicator("syminfo.ticker fun", overlay=true)
i_sym = input.symbol("NASDAQ:AAPL")
pref = syminfo.prefix(i_sym)
tick = syminfo.ticker(i_sym)
t = ticker.new(pref, tick, session.extended)
s = request.security(t, "1D", close)
plot(s)
```

返回值

返回不带交易所前缀的 `symbol` 名称，例如“AAPL”。

备注

该函数的结果用于[ticker.new()]/[ticker.modify()]和[request.security()]。

另见

[syminfo.tickerid][syminfo.ticker][syminfo.prefix][syminfo.prefix()][ticker.new()]

###### ta.alma()



Arnaud Legoux移动平均线。 它使用高斯分布作为移动平均值的权重。



```
ta.alma(series, length, offset, sigma, floor) → series float
```

参数

**series (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

**offset (simple int/float)** 控制平滑度(更接近1)和响应性(更接近0)之间的权衡。

**sigma (simple int/float)** 改变ALMA的平滑度。Sigma越大，ALMA越平滑。

**floor (simple bool)** 可选参数。在计算ALMA之前，指定偏移量计算是否为下限。默认值为false。



```
//@version=6
indicator("ta.alma", overlay=true)
plot(ta.alma(close, 9, 0.85, 6))

// same on pine, but much less efficient
pine_alma(series, windowsize, offset, sigma) =>
    m = offset * (windowsize - 1)
    //m = math.floor(offset * (windowsize - 1)) // Used as m when math.floor=true
    s = windowsize / sigma
    norm = 0.0
    sum = 0.0
    for i = 0 to windowsize - 1
        weight = math.exp(-1 * math.pow(i - m, 2) / (2 * math.pow(s, 2)))
        norm := norm + weight
        sum := sum + series[windowsize - i - 1] * weight
    sum / norm
plot(pine_alma(close, 9, 0.85, 6))
```

返回值

Arnaud Legoux移动平均线

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

另见

[ta.sma()][ta.ema()][ta.rma()][ta.wma()][ta.vwma()][ta.swma()]

###### ta.atr()



函数ATR（真实波动幅度均值）返回真实范围的RMA。真实波动幅度是max(high - low, abs(high - close[1`, abs(low - close[1`)。



```
ta.atr(length) → series float
```

参数

**length (simple int)** 长度(K线数量)



```
//@version=6
indicator("ta.atr")
plot(ta.atr(14))

//the same on pine
pine_atr(length) =>
    trueRange = na(high[1`? high-low : math.max(math.max(high - low, math.abs(high - close[1`), math.abs(low - close[1`)
    //true range can be also calculated with ta.tr(true)
    ta.rma(trueRange, length)

plot(pine_atr(14))
```

返回值

真实波动幅度均值(ATR)

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.tr()][ta.rma()]

###### ta.barssince()



从上次条件为true起，计算K线数量。



```
ta.barssince(condition) → series int
```

参数

**condition (series bool)** 要检查的条件。



```
//@version=6
indicator("ta.barssince")
// get number of bars since last color.green bar
plot(ta.barssince(close >= open))
```

返回值

如状况为true的k线数目。

备注

如果在当前K线之前从未满足该条件，则该函数返回na。

请注意，使用此变量/函数可能会导致[指标重新绘制]。

另见

[ta.lowestbars()][ta.highestbars()][ta.valuewhen()][ta.highest()][ta.lowest()]

###### ta.bb()



布林带。布林带是一种技术分析工具，由一组线定义，这些线与证券价格的简单移动平均线（SMA）相距两个标准偏差（正向和负向），但可以根据用户偏好进行调整。



```
ta.bb(series, length, mult) → [series float, series float, series float]
```

参数

**series (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

**mult (simple int/float)** 标准差因子。



```
//@version=6
indicator("ta.bb")

[middle, upper, lower] = ta.bb(close, 5, 4)
plot(middle, color=color.yellow)
plot(upper, color=color.yellow)
plot(lower, color=color.yellow)

// the same on pine
f_bb(src, length, mult) =>
    float basis = ta.sma(src, length)
    float dev = mult * ta.stdev(src, length)
    [basis, basis + dev, basis - dev]

[pineMiddle, pineUpper, pineLower] = f_bb(close, 5, 4)

plot(pineMiddle)
plot(pineUpper)
plot(pineLower)
```

返回值

布林带。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.sma()][ta.stdev()][ta.kc()]

###### ta.bbw()



布林带的宽度。布林带宽度是上轨和下轨到中线的距离。



```
ta.bbw(series, length, mult) → series float
```

参数

**series (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

**mult (simple int/float)** 标准差因子。



```
//@version=6
indicator("ta.bbw")

plot(ta.bbw(close, 5, 4), color=color.yellow)

// the same on pine
f_bbw(src, length, mult) =>
    float basis = ta.sma(src, length)
    float dev = mult * ta.stdev(src, length)
    (((basis + dev) - (basis - dev)) / basis) * 100

plot(f_bbw(close, 5, 4))
```

返回值

布林带宽度。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.bb()][ta.sma()][ta.stdev()]

###### ta.cci()



CCI（商品路径指数）的计算方法是商品的典型价格与其简单移动平均线之间的差值除以典型价格的平均绝对偏差。该指数按0.015的倒数进行缩放，以提供更多可读的数字。



```
ta.cci(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

lengthK线返回的source的商品渠道指数。

备注

`source`系列中的`na`值将被忽略。

###### ta.change()

3过载



比较当前 `source` 值与它的值 `length` K线之前的值并返回差值。

语法和重载

[`ta.change(source, length) → series int`][`ta.change(source, length) → series float`][`ta.change(source, length) → series bool`]

参数

**source (series int)** 源系列。

**length (series int)** 过去的 `source` 值与当前值的偏移量，以K线为单位。可选。默认值为1。



```
//@version=6
indicator('Day and Direction Change', overlay = true)
dailyBarTime = time('1D')
isNewDay = ta.change(dailyBarTime) != 0
bgcolor(isNewDay ? color.new(color.green, 80) : na)

isGreenBar = close >= open
colorChange = ta.change(isGreenBar)
plotshape(colorChange, 'Direction Change')
```

返回值

数值为数值时的值之间的差异。当使用 'bool' 源时，如果当前源与前一个源不同，则返回 `true`。

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

另见

[ta.mom()][ta.cross()]

###### ta.cmo()



钱德动量摆动指标。计算最近的上涨点数之和与最近的下跌点数之和，然后将两者相减，然后将结果除以同一时期内所有价格变动的总和



```
ta.cmo(series, length) → series float
```

参数

**series (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("ta.cmo")
plot(ta.cmo(close, 5), color=color.yellow)

// the same on pine
f_cmo(src, length) =>
    float mom = ta.change(src)
    float sm1 = math.sum((mom >= 0) ? mom : 0.0, length)
    float sm2 = math.sum((mom >= 0) ? 0.0 : -mom, length)
    100 * (sm1 - sm2) / (sm1 + sm2)

plot(f_cmo(close, 5))
```

返回值

钱德动量摆动指标

备注

`source`系列中的`na`值将被忽略。

另见

[ta.rsi()][ta.stoch()][math.sum()]

###### ta.cog()



cog(重心点)是基于统计学和斐波那契黄金比例的指标。



```
ta.cog(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("ta.cog", overlay=true)
plot(ta.cog(close, 10))

// the same on pine
pine_cog(source, length) =>
    sum = math.sum(source, length)
    num = 0.0
    for i = 0 to length - 1
        price = source[i]
        num := num + price * (i + 1)
    -num / sum

plot(pine_cog(close, 10))
```

返回值

重心

备注

`source`系列中的`na`值将被忽略。

另见

[ta.stoch()]

###### ta.correlation()



相关系数。描述两个系列倾向于偏离其[ta.sma()]值的程度。



```
ta.correlation(source1, source2, length) → series float
```

参数

**source1 (series int/float)** 源系列。

**source2 (series int/float)** 目标系列。

**length (series int)** 长度(K线数量)

返回值

相关系数。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[request.security()]

###### ta.cross()





```
ta.cross(source1, source2) → series bool
```

参数

**source1 (series int/float)** 第一数据系列。

**source2 (series int/float)** 第二数据系列。

返回值

如果两个系列相互交叉则为true，否则为false。

另见

[ta.change()]

###### ta.crossover()



如果在当前K线上，`source1`的值大于`source2`的值，并且在前一根K线上，`source1`的值小于或等于`source2`的值，则`source1`系列被定义为已穿过`source2`系列。



```
ta.crossover(source1, source2) → series bool
```

参数

**source1 (series int/float)** 第一数据系列。

**source2 (series int/float)** 第二数据系列。

返回值

如果`source1`穿过`source2`则为true，否则为false。

###### ta.crossunder()



如果在当前K线上，`source1`的值小于`source2`的值，并且在前一根K线上，`source1`的值大于或等于`source2`的值，则`source1`系列被定义为在`source2`系列下交叉。



```
ta.crossunder(source1, source2) → series bool
```

参数

**source1 (series int/float)** 第一数据系列。

**source2 (series int/float)** 第二数据系列。

返回值

如果`source1`在`source2`下交叉，则为true，否则为false。

###### ta.cum()



`source`的累积（总）和。换句话说，它是`source`所有元素的总和。



```
ta.cum(source) → series float
```

参数

**source (series int/float)** 用于计算的源。

返回值

系列总和。

另见

[math.sum()]

###### ta.dev()



系列与[ta.sma()]之间的差量数



```
ta.dev(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("ta.dev")
plot(ta.dev(close, 10))

// the same on pine
pine_dev(source, length) =>
    mean = ta.sma(source, length)
    sum = 0.0
    for i = 0 to length - 1
        val = source[i]
        sum := sum + math.abs(val - mean)
    dev = sum/length
plot(pine_dev(close, 10))
```

返回值

`source`K线返回的`length`偏差。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.variance()][ta.stdev()]

###### ta.dmi()



dmi函数返回动向指数DMI。



```
ta.dmi(diLength, adxSmoothing) → [series float, series float, series float]
```

参数

**diLength (simple int)** DI Period。

**adxSmoothing (simple int)** ADX平滑周期



```
//@version=6
indicator(title="Directional Movement Index", shorttitle="DMI", format=format.price, precision=4)
len = input.int(17, minval=1, title="DI Length")
lensig = input.int(14, title="ADX Smoothing", minval=1)
[diplus, diminus, adx] = ta.dmi(len, lensig)
plot(adx, color=color.red, title="ADX")
plot(diplus, color=color.blue, title="+DI")
plot(diminus, color=color.orange, title="-DI")
```

返回值

三个DMI系列的[元组]：正方向运动(+DI)、负方向运动(-DI) 和平均方向运动指数(ADX)。

另见

[ta.rsi()][ta.tsi()][ta.mfi()]

###### ta.ema()



ema函数返回指数加权移动平均值。在ema中，权重因子呈指数下降。它使用以下公式进行计算：`EMA = alpha * source + (1 - alpha) * EMA[1]`，其中`alpha = 2 / (length + 1)`。



```
ta.ema(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (simple int)** K线数量(长度).



```
//@version=6
indicator("ta.ema")
plot(ta.ema(close, 15))

//the same on pine
pine_ema(src, length) =>
    alpha = 2 / (length + 1)
    sum = 0.0
    sum := na(sum[1` ? src : alpha * src + (1 - alpha) * nz(sum[1`
plot(pine_ema(close,15))
```

返回值

`source` 的指数移动平均线，alpha = 2 / (长度 + 1)。

备注

请注意，使用此变量/函数可能会导致[指标重新绘制]。

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.sma()][ta.rma()][ta.wma()][ta.vwma()][ta.swma()][ta.alma()]

###### ta.falling()



测试 `source` 系列对于 `length` K线long是否正在下跌。



```
ta.falling(source, length) → series bool
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

如果当前`source`值小于`length` K线返回的任何先前`source`值，则为true，否则为false。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.rising()]

###### ta.highest()



过去k线的给定数目的最高值。



```
ta.highest(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

系列中的最高值。

备注

两个 args 版本：`source` 是一个系列，`length` 是返回的K线数。

一个 arg 版本：`length` 是返回的K线数。算法使用high作为 `source` 系列。

`source`系列中的`na`值将被忽略。

另见

[ta.lowest()][ta.lowestbars()][ta.highestbars()][ta.valuewhen()][ta.barssince()]

###### ta.highestbars()



过去k线的给定数目的最高值偏移。



```
ta.highestbars(source, length) → series int
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

偏移到最高k线。

备注

两个 args 版本：`source` 是一个系列，`length` 是返回的K线数。

一个 arg 版本：`length` 是返回的K线数。算法使用high作为 `source` 系列。

`source`系列中的`na`值将被忽略。

另见

[ta.lowest()][ta.highest()][ta.lowestbars()][ta.barssince()][ta.valuewhen()]

###### ta.hma()



hma函数返回船体移动平均线HMA。



```
ta.hma(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (simple int)** K线数量



```
//@version=6
indicator("Hull Moving Average")
src = input(defval=close, title="Source")
length = input(defval=9, title="Length")
hmaBuildIn = ta.hma(src, length)
plot(hmaBuildIn, title="Hull MA", color=#674EA7)
```

返回值

返回 'length' 柱的 'source' 的船体移动平均线Hull Moving Average。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.ema()][ta.rma()][ta.wma()][ta.vwma()][ta.sma()]

###### ta.kc()



肯特纳通道。肯特那通道是一个技术指标，包含了中间的移动平均线以及上下轨的通道。



```
ta.kc(series, length, mult, useTrueRange) → [series float, series float, series float]
```

参数

**series (series int/float)** 待执行的系列值。

**length (simple int)** K线数量(长度).

**mult (simple int/float)** 标准差因子。

**useTrueRange (simple bool)** 可选参数。指定是否使用真实范围； 默认为true。 如果值为false，则将使用表达式（high-low）来计算范围。



```
//@version=6
indicator("ta.kc")

[middle, upper, lower] = ta.kc(close, 5, 4)
plot(middle, color=color.yellow)
plot(upper, color=color.yellow)
plot(lower, color=color.yellow)


// the same on pine
f_kc(src, length, mult, useTrueRange) =>
    float basis = ta.ema(src, length)
    float span = (useTrueRange) ? ta.tr : (high - low)
    float rangeEma = ta.ema(span, length)
    [basis, basis + rangeEma * mult, basis - rangeEma * mult]

[pineMiddle, pineUpper, pineLower] = f_kc(close, 5, 4, true)

plot(pineMiddle)
plot(pineUpper)
plot(pineLower)
```

返回值

肯特纳通道

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.ema()][ta.atr()][ta.bb()]

###### ta.kcw()



肯特纳通道宽度。肯特那通道宽度是上，下通道之间的差除以中间通道的值。



```
ta.kcw(series, length, mult, useTrueRange) → series float
```

参数

**series (series int/float)** 待执行的系列值。

**length (simple int)** K线数量(长度).

**mult (simple int/float)** 标准差因子。

**useTrueRange (simple bool)** 可选参数。指定是否使用真实范围； 默认为true。 如果值为false，则将使用表达式（high-low）来计算范围。



```
//@version=6
indicator("ta.kcw")

plot(ta.kcw(close, 5, 4), color=color.yellow)

// the same on pine
f_kcw(src, length, mult, useTrueRange) =>
    float basis = ta.ema(src, length)
    float span = (useTrueRange) ? ta.tr : (high - low)
    float rangeEma = ta.ema(span, length)

    ((basis + rangeEma * mult) - (basis - rangeEma * mult)) / basis

plot(f_kcw(close, 5, 4, true))
```

返回值

肯特纳通道宽度。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.kc()][ta.ema()][ta.atr()][ta.bb()]

###### ta.linreg()



线性回归曲线。一条最符合用户定义时间段内指定价格的线。它是使用最小二乘法计算的。此函数的结果使用以下公式计算：linreg = intercept + slope * (length - 1 - offset)，其中 intercept 和 slope 是使用 `source` 系列的最小二乘法计算的值。



```
ta.linreg(source, length, offset) → series float
```

参数

**source (series int/float)** 源系列。

**length (series int)** K线数量(长度).

**offset (simple int)** 偏移

返回值

线性回归曲线

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

###### ta.lowest()



过去k线的给定数目的最低值。



```
ta.lowest(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

系列中的最低值。

备注

两个 args 版本：`source` 是一个系列，`length` 是返回的K线数。

一个 arg 版本：`length` 是返回的K线数。算法使用low作为`source`系列。

`source`系列中的`na`值将被忽略。

另见

[ta.highest()][ta.lowestbars()][ta.highestbars()][ta.valuewhen()][ta.barssince()]

###### ta.lowestbars()



过去k线的给定数目的最低值偏移。



```
ta.lowestbars(source, length) → series int
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** 返回K线数。

返回值

偏移到最低k线。

备注

两个 args 版本：`source` 是一个系列，`length` 是返回的K线数。

一个 arg 版本：`length` 是返回的K线数。算法使用low作为`source`系列。

`source`系列中的`na`值将被忽略。

另见

[ta.lowest()][ta.highest()][ta.highestbars()][ta.barssince()][ta.valuewhen()]

###### ta.macd()



MACD(平滑异同平均线)。 它应该揭示股票价格趋势的实力、方向、动量和持续时间的变化。



```
ta.macd(source, fastlen, slowlen, siglen) → [series float, series float, series float]
```

参数

**source (series int/float)** 待执行的系列值。

**fastlen (simple int)** 快线参数

**slowlen (simple int)** 慢长度参数。

**siglen (simple int)** 信号长度参数。



```
//@version=6
indicator("MACD")
[macdLine, signalLine, histLine] = ta.macd(close, 12, 26, 9)
plot(macdLine, color=color.blue)
plot(signalLine, color=color.orange)
plot(histLine, color=color.red, style=plot.style_histogram)
```

如果您只需要一个值，请使用像这样的占位符'_'：



```
//@version=6
indicator("MACD")
[_, signalLine, _] = ta.macd(close, 12, 26, 9)
plot(signalLine, color=color.orange)
```

返回值

三个MACD系列的[元组]：MACD线、信号线和直方图线。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.sma()][ta.ema()]

###### ta.max()



返回从图表开始到当前K线的 `source` 的历史最高值。



```
ta.max(source) → series float
```

参数

**source (series int/float)** 用于计算的源。

备注

`na`

###### ta.median()

2过载



返回序列的中位数。

语法和重载

[`ta.median(source, length) → series int`][`ta.median(source, length) → series float`]

参数

**source (series int)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

序列的中位数。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

###### ta.mfi()



资金流量指标。资金流量指标是一种技术指标，它使用价格和成交量来确定资产中的超买或超卖状况。



```
ta.mfi(series, length) → series float
```

参数

**series (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("Money Flow Index")

plot(ta.mfi(hlc3, 14), color=color.yellow)

// the same on pine
pine_mfi(src, length) =>
    float upper = math.sum(volume * (ta.change(src) <= 0.0 ? 0.0 : src), length)
    float lower = math.sum(volume * (ta.change(src) >= 0.0 ? 0.0 : src), length)
    mfi = 100.0 - (100.0 / (1.0 + upper / lower))
    mfi

plot(pine_mfi(hlc3, 14))
```

返回值

资金流量指标

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.rsi()][math.sum()]

###### ta.min()



返回从图表开始到当前K线的 `source` 的历史最低值。



```
ta.min(source) → series float
```

参数

**source (series int/float)** 用于计算的源。

备注

`na`

###### ta.mode()

2过载



返回序列的[模式`。如果有多个具有相同频率的值，则返回最小值。

语法和重载

[`ta.mode(source, length) → series int`][`ta.mode(source, length) → series float`]

参数

**source (series int)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

来自`source`的最常出现的值。如果不存在，则返回最小值。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

###### ta.mom()



`source`价格和`source`价格`length`K线之前的动量。这只是一个区别：源 - 源[长度]。



```
ta.mom(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** 从当前k线偏移到上一个k线。

返回值

`source`价格和`source`价格`length`K线之前的动量。

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

另见

[ta.change()]

###### ta.percentile_linear_interpolation()



使用最近的两个排名之间的线性插值方法计算百分比。



```
ta.percentile_linear_interpolation(source, length, percentage) → series float
```

参数

**source (series int/float)** 待执行的系列值(来源)。

**length (series int)** 过去的K线数量(长度)

**percentage (simple int/float)** 百分比，从0到100的范围内的数字

返回值

`source`K线返回的`length`系列的第P个百分位数。

备注

请注意，使用此方法计算的百分比并非都是输入数据集一员。

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

另见

[ta.percentile_nearest_rank()]

###### ta.percentile_nearest_rank()



根据最近的排名方法计算百分比。



```
ta.percentile_nearest_rank(source, length, percentage) → series float
```

参数

**source (series int/float)** 待执行的系列值(来源)。

**length (series int)** 过去的K线数量(长度)

**percentage (simple int/float)** 百分比，从0到100的范围内的数字

返回值

`source`K线返回的`length`系列的第P个百分位数。

备注

使用少于过去100 k线长度的最近排名法可导致相同的数字用于多个百分位数。

最近排名法计算的百分比都是输入数据集一员。

第100个百分点被定义为输入数据集中的最大值。

`source`系列中的`na`值将被忽略。

另见

[ta.percentile_linear_interpolation()]

###### ta.percentrank()



百分比等级是以前的值小于或等于给定系列当前值的百分比。



```
ta.percentrank(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

`source`K线返回的`length`百分比排名。

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

###### ta.pivot_point_levels()



使用指定的`type`和`anchor`计算枢轴点水平。



```
ta.pivot_point_levels(type, anchor, developing) → array<float>
```

参数

**type (series string)** 枢轴点级别的类型。可能的值：“Traditional”、“Fibonacci”、“Woodie”、“Classic”、“DM”、“Camarilla”。

**anchor (series bool)** 触发枢轴点计算重置的条件。当`true`时，计算重置；当`false`时，上次重置时计算的结果仍然存在。

**developing (series bool)** 如果是`false`，则这些值是上次锚定条件为`true`时计算的值。它们保持不变，直到锚定条件再次变为`true`。如果是`true`，则枢轴正在发展，即，它们不断地重新计算最后一个锚点（如果锚条件从来不是`true`，则为零K线）和当前K线之间发展的数据。可选。默认值为`false`。



```
//@version=6
indicator("Weekly Pivots", max_lines_count=500, overlay=true)
timeframe = "1W"
typeInput = input.string("Traditional", "Type", options=["Traditional", "Fibonacci", "Woodie", "Classic", "DM", "Camarilla"`
weekChange = timeframe.change(timeframe)
pivotPointsArray = ta.pivot_point_levels(typeInput, weekChange)
if weekChange
    for pivotLevel in pivotPointsArray
        line.new(time, pivotLevel, time + timeframe.in_seconds(timeframe) * 1000, pivotLevel, xloc=xloc.bar_time)
```

返回值

`array<float>`，其数值代表11个枢轴点水平：[P、R1、S1、R2、S2、R3、S3、R4、S4、R5、S5]。 指定的`type`中缺少的水平返回 `na`值（例如，“DM”仅计算P、R1和S1）。

备注

当 `developing` 设置为 "Woodie" 时，`true` 参数不能为 `type`，因为某个时期的 Woodie 计算取决于该时期的开盘，这意味着枢轴值可用或不可用，但永远不会发展。如果一起使用，指标将返回运行时错误。

###### ta.pivothigh()

2过载



此函数返回枢轴高点的价格。 如果没有枢轴高点，则返回“NaN”。

语法和重载

[`ta.pivothigh(leftbars, rightbars) → series float`][`ta.pivothigh(source, leftbars, rightbars) → series float`]

参数

**leftbars (series int/float)** 左力量。

**rightbars (series int/float)** 右长度。



```
//@version=6
indicator("PivotHigh", overlay=true)
leftBars = input(2)
rightBars=input(2)
ph = ta.pivothigh(leftBars, rightBars)
plot(ph, style=plot.style_cross, linewidth=3, color= color.red, offset=-rightBars)
```

返回值

此点的价格或者 'NaN'.

备注

如果参数'leftbars'或'rightbars'是系列，你应该使用[max_bars_back()]函数作为'source'变量。

###### ta.pivotlow()

2过载



此函数返回枢轴低点的价格。 如果没有枢轴低点，它返回“NaN”。

语法和重载

[`ta.pivotlow(leftbars, rightbars) → series float`][`ta.pivotlow(source, leftbars, rightbars) → series float`]

参数

**leftbars (series int/float)** 左力量。

**rightbars (series int/float)** 右长度。



```
//@version=6
indicator("PivotLow", overlay=true)
leftBars = input(2)
rightBars=input(2)
pl = ta.pivotlow(close, leftBars, rightBars)
plot(pl, style=plot.style_cross, linewidth=3, color= color.blue, offset=-rightBars)
```

返回值

此点的价格或者 'NaN'.

备注

如果参数'leftbars'或'rightbars'是系列，你应该使用[max_bars_back()]函数作为'source'变量。

###### ta.range()

2过载



返回序列中最小值和最大值之间的差。

语法和重载

[`ta.range(source, length) → series int`][`ta.range(source, length) → series float`]

参数

**source (series int)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

序列中最小值和最大值之间的差。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

###### ta.rci()



计算等级相关指数(RCI)，该指数用于衡量价格变动的方向一致性。它使用Spearman等级相关系数评估`source`系列与`length`根K线上的K线索引之间的单调关系。结果值被缩放到-100到100的范围，其中100表示`source`在这段时间内持续增加，-100表示持续减少。-100到100之间的值反映不同程度的向上或向下一致性。



```
ta.rci(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (simple int)** K线数量(长度).

返回值

排名相关指数，值介于-100 至100之间。

另见

###### ta.rising()



测试 `source` 系列对于 `length` K线long是否正在上涨。



```
ta.rising(source, length) → series bool
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

如果当前`source`大于`length`K线返回任何先前的`source`，则为true，否则为false。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.falling()]

###### ta.rma()



RSI中使用的移动平均线。 它是指数加权移动平均线，alpha加权值 = 1 /长度。



```
ta.rma(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (simple int)** K线数量(长度).



```
//@version=6
indicator("ta.rma")
plot(ta.rma(close, 15))

//the same on pine
pine_rma(src, length) =>
    alpha = 1/length
    sum = 0.0
    sum := na(sum[1` ? ta.sma(src, length) : alpha * src + (1 - alpha) * nz(sum[1`
plot(pine_rma(close, 15))
```

返回值

`source`的指数移动平均线，alpha = 1 / `length`。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.sma()][ta.ema()][ta.wma()][ta.vwma()][ta.swma()][ta.alma()][ta.rsi()]

###### ta.roc()



计算 `source` 的当前值与其值 `length` K线之前的涨跌百分比（涨跌幅）。

由以下公式计算：100 * change(src, length) / src[length]。



```
ta.roc(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

返回值

`source`K线返回的`length`的变化率。

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

###### ta.rsi()



相对强度指数。它是使用在最后一个 `ta.rma()` K线上`source` 的向上和向下变化的`length` 计算的。



```
ta.rsi(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (simple int)** K线数量(长度).



```
//@version=6
indicator("ta.rsi")
plot(ta.rsi(close, 7))

// same on pine, but less efficient
pine_rsi(x, y) =>
    u = math.max(x - x[1], 0) // upward ta.change
    d = math.max(x[1] - x, 0) // downward ta.change
    rs = ta.rma(u, y) / ta.rma(d, y)
    res = 100 - 100 / (1 + rs)
    res

plot(pine_rsi(close, 7))
```

返回值

相对强弱指标(RSI)

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.rma()]

###### ta.sar()



抛物线转向(抛物线停止和反向)是J. Welles Wilder, Jr.设计的方法，以找出交易市场价格方向的潜在逆转。



```
ta.sar(start, inc, max) → series float
```

参数

**start (simple int/float)** 开始。

**inc (simple int/float)** 增加

**max (simple int/float)** 最大.



```
//@version=6
indicator("ta.sar")
plot(ta.sar(0.02, 0.02, 0.2), style=plot.style_cross, linewidth=3)

// The same on Pine Script®
pine_sar(start, inc, max) =>
    var float result = na
    var float maxMin = na
    var float acceleration = na
    var bool isBelow = false
    bool isFirstTrendBar = false

    if bar_index == 1
        if close > close[1]
            isBelow := true
            maxMin := high
            result := low[1]
        else
            isBelow := false
            maxMin := low
            result := high[1]
        isFirstTrendBar := true
        acceleration := start

    result := result + acceleration * (maxMin - result)

    if isBelow
        if result > low
            isFirstTrendBar := true
            isBelow := false
            result := math.max(high, maxMin)
            maxMin := low
            acceleration := start
    else
        if result < high
            isFirstTrendBar := true
            isBelow := true
            result := math.min(low, maxMin)
            maxMin := high
            acceleration := start
            
    if not isFirstTrendBar
        if isBelow
            if high > maxMin
                maxMin := high
                acceleration := math.min(acceleration + inc, max)
        else
            if low < maxMin
                maxMin := low
                acceleration := math.min(acceleration + inc, max)

    if isBelow
        result := math.min(result, low[1`
        if bar_index > 1
            result := math.min(result, low[2`
        
    else
        result := math.max(result, high[1`
        if bar_index > 1
            result := math.max(result, high[2`

    result

plot(pine_sar(0.02, 0.02, 0.2), style=plot.style_cross, linewidth=3)
```

返回值

抛物线转向指标。

###### ta.sma()



sma函数返回移动平均值，即x的最后y值，除以y。



```
ta.sma(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("ta.sma")
plot(ta.sma(close, 15))

// same on pine, but much less efficient
pine_sma(x, y) =>
    sum = 0.0
    for i = 0 to y - 1
        sum := sum + x[i] / y
    sum
plot(pine_sma(close, 15))
```

返回值

`source`K线返回的`length`的简单移动平均线。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.ema()][ta.rma()][ta.wma()][ta.vwma()][ta.swma()][ta.alma()]

###### ta.stdev()





```
ta.stdev(source, length, biased) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

**biased (series bool)** 确定应该使用哪个估计。可选。默认值为true。



```
//@version=6
indicator("ta.stdev")
plot(ta.stdev(close, 5))

//the same on pine
isZero(val, eps) => math.abs(val) <= eps

SUM(fst, snd) =>
    EPS = 1e-10
    res = fst + snd
    if isZero(res, EPS)
        res := 0
    else
        if not isZero(res, 1e-4)
            res := res
        else
            15

pine_stdev(src, length) =>
    avg = ta.sma(src, length)
    sumOfSquareDeviations = 0.0
    for i = 0 to length - 1
        sum = SUM(src[i], -avg)
        sumOfSquareDeviations := sumOfSquareDeviations + sum * sum

    stdev = math.sqrt(sumOfSquareDeviations / length)
plot(pine_stdev(close, 5))
```

返回值

标准差

备注

如果`biased`为true，函数将使用对整个总体的有偏估计进行计算，如果为false - 对样本的无偏估计。

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.dev()][ta.variance()]

###### ta.stoch()



随机指标。计算方程：100 * (close - lowest(low, length)) / (highest(high, length) - lowest(low, length))。



```
ta.stoch(source, high, low, length) → series float
```

参数

**source (series int/float)** 源系列。

**high (series int/float)** 高系列

**low (series int/float)** 低系列

**length (series int)** 长度(K线数量)

返回值

随机

备注

`source`系列中的`na`值将被忽略。

另见

[ta.cog()]

###### ta.supertrend()



超级趋势指标。超级趋势指标是一个跟随趋势的指标。



```
ta.supertrend(factor, atrPeriod) → [series float, series float]
```

参数

**factor (series int/float)** ATR将乘以的乘数。

**atrPeriod (simple int)** 平均真实波幅长度



```
//@version=6
indicator("Pine Script® Supertrend")

[supertrend, direction] = ta.supertrend(3, 10)
plot(direction < 0 ? supertrend : na, "Up direction", color = color.green, style=plot.style_linebr)
plot(direction > 0 ? supertrend : na, "Down direction", color = color.red, style=plot.style_linebr)

// The same on Pine Script®
pine_supertrend(factor, atrPeriod) =>
    src = hl2
    atr = ta.atr(atrPeriod)
    upperBand = src + factor * atr
    lowerBand = src - factor * atr
    prevLowerBand = nz(lowerBand[1`
    prevUpperBand = nz(upperBand[1`

    lowerBand := lowerBand > prevLowerBand or close[1] < prevLowerBand ? lowerBand : prevLowerBand
    upperBand := upperBand < prevUpperBand or close[1] > prevUpperBand ? upperBand : prevUpperBand
    int _direction = na
    float superTrend = na
    prevSuperTrend = superTrend[1]
    if na(atr[1`
        _direction := 1
    else if prevSuperTrend == prevUpperBand
        _direction := close > upperBand ? -1 : 1
    else
        _direction := close < lowerBand ? 1 : -1
    superTrend := _direction == -1 ? lowerBand : upperBand
    [superTrend, _direction]

[Pine_Supertrend, pineDirection] = pine_supertrend(3, 10)
plot(pineDirection < 0 ? Pine_Supertrend : na, "Up direction", color = color.green, style=plot.style_linebr)
plot(pineDirection > 0 ? Pine_Supertrend : na, "Down direction", color = color.red, style=plot.style_linebr)
```

返回值

两个超趋势系列的[元组]：超趋势线和趋势方向。可能的值为 1（向下方向）和 -1（向上方向）。

另见

[ta.macd()]

###### ta.swma()



具有固定长度的对称加权移动平均线：4.权重：[1/6,2 / 6,2 / 6,1 / 6]。



```
ta.swma(source) → series float
```

参数

**source (series int/float)** 源系列。



```
//@version=6
indicator("ta.swma")
plot(ta.swma(close))

// same on pine, but less efficient
pine_swma(x) =>
    x[3] * 1 / 6 + x[2] * 2 / 6 + x[1] * 2 / 6 + x[0] * 1 / 6
plot(pine_swma(close))
```

返回值

对称加权移动平均线。

备注

`source`系列中的`na`值包含在计算中，并将产生`na`结果。

另见

[ta.sma()][ta.ema()][ta.rma()][ta.wma()][ta.vwma()][ta.alma()]

###### ta.tr()



计算当前K线的真实范围。与K线的实际范围（`high - low`）不同，真实范围通过最大程度地利用了当前条的实际范围以及从上一根K线的[close]到当前K线的[high]和[low]的绝对距离来解释潜在差距。公式为：`math.max(high - low, math.abs(high - close[1`, math.abs(low - close[1`)`。



```
ta.tr(handle_na) → series float
```

参数

**handle_na (simple bool)** 定义在前一根K线的[close]为`na`时，函数如何计算结果。如果为`true`，则函数返回K线的`high - low`值。如果为`false`，则返回`na`。

返回值

真实范围。它是math.max(high - low, math.abs(high - close[1`, math.abs(low - close[1`)。

备注

ta.tr(false) 与[ta.tr]完全相同。

另见

[ta.tr][ta.atr()]

###### ta.tsi()



真实强弱指数。它使用金融工具潜在动量的移动平均线。



```
ta.tsi(source, short_length, long_length) → series float
```

参数

**source (series int/float)** 源系列。

**short_length (simple int)** 短的长度。

**long_length (simple int)** 长线长度。

返回值

真实强弱指数。范围[-1，1]中的值。

备注

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

###### ta.valuewhen()

4过载



返回K线上`source`系列的值，其中`condition`在最近第n次出现时为为true。

语法和重载

[`ta.valuewhen(condition, source, occurrence) → series color`][`ta.valuewhen(condition, source, occurrence) → series int`][`ta.valuewhen(condition, source, occurrence) → series float`][`ta.valuewhen(condition, source, occurrence) → series bool`]

参数

**condition (series bool)** 要搜索的条件。

**source (series color)** 要从满足条件的K线返回的值。

**occurrence (simple int)** 条件的出现。编号从0开始并按时间倒退，因此“0”是最近出现的`condition`，“1”是第二个最近出现的，依此类推。必须是整数 >= 0。



```
//@version=6
indicator("ta.valuewhen")
slow = ta.sma(close, 7)
fast = ta.sma(close, 14)
// Get value of `close` on second most recent cross
plot(ta.valuewhen(ta.cross(slow, fast), close, 1))
```

备注

此功能需要在每根K线上执行。不建议在[for]或[while]循环结构中使用它，因为它的行为可能出乎意料。请注意，使用此功能可能会导致[指标重绘]。

另见

[ta.lowestbars()][ta.highestbars()][ta.barssince()][ta.highest()][ta.lowest()]

###### ta.variance()



差异是一系列平均偏差`ta.sma()`的预期，并且非正式地衡量 一组数字从其平均分布的程度。



```
ta.variance(source, length, biased) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).

**biased (series bool)** 确定应该使用哪个估计。可选。默认值为true。

返回值

`source` K线返回的`length`的方差。

备注

如果`biased`为true，函数将使用对整个总体的有偏估计进行计算，如果为false - 对样本的无偏估计。

`source`系列中的`na`值将被忽略；该函数计算非`na`值的`length`数量。

另见

[ta.dev()][ta.stdev()]

###### ta.vwap()

2过载



成交量加权平均价格

语法和重载

[`ta.vwap(source, anchor) → series float`][`ta.vwap(source, anchor, stdev_mult) → [series float, series float, series float\]`]

参数

**source (series int/float)** 用于VWAP计算的来源。

**anchor (series bool)** 触发重置 VWAP 计算的条件。当`true`时，计算重置； 当`false`时，使用自上次重置以来累积的值进行计算。可选。默认等效于传递[timeframe.change()]并以“1D”作为其参数。



```
//@version=6
indicator("Simple VWAP")
vwap = ta.vwap(open)
plot(vwap)
```



```
//@version=6
indicator("Advanced VWAP")
vwapAnchorInput = input.string("Daily", "Anchor", options = ["Daily", "Weekly", "Monthly"`
stdevMultiplierInput = input.float(1.0, "Standard Deviation Multiplier")
anchorTimeframe = switch vwapAnchorInput
    "Daily"   => "1D"
    "Weekly"  => "1W"
    "Monthly" => "1M"
anchor = timeframe.change(anchorTimeframe)
[vwap, upper, lower] = ta.vwap(open, anchor, stdevMultiplierInput)
plot(vwap)
plot(upper, color = color.green)
plot(lower, color = color.green)
```

返回值

如果指定了`stdev_mult`，则为VWAP系列或元组[vwap, upper_band, lower_band]。

备注

计算仅在锚点条件第一次变为`true`时开始。在此之前，该函数返回`na`。

另见

[ta.vwap]

###### ta.vwma()



vwma 函数返回 `source` K线的 `length` 的成交量加权移动平均值。等同于：sma(source * volume, length) / sma(volume, length)。



```
ta.vwma(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("ta.vwma")
plot(ta.vwma(close, 15))

// same on pine, but less efficient
pine_vwma(x, y) =>
    ta.sma(x * volume, y) / ta.sma(volume, y)
plot(pine_vwma(close, 15))
```

返回值

`source`K线返回的`length`的成交量加权移动平均线。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.sma()][ta.ema()][ta.rma()][ta.wma()][ta.swma()][ta.alma()]

###### ta.wma()



wma 函数返回 `source` K线的 `length` 的加权移动平均值。在 wma 中，加权因子以算术级数递减。



```
ta.wma(source, length) → series float
```

参数

**source (series int/float)** 待执行的系列值。

**length (series int)** K线数量(长度).



```
//@version=6
indicator("ta.wma")
plot(ta.wma(close, 15))

// same on pine, but much less efficient
pine_wma(x, y) =>
    norm = 0.0
    sum = 0.0
    for i = 0 to y - 1
        weight = (y - i) * y
        norm := norm + weight
        sum := sum + x[i] * weight
    sum / norm
plot(pine_wma(close, 15))
```

返回值

`source`K线返回的`length`加权移动平均线。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.sma()][ta.ema()][ta.rma()][ta.vwma()][ta.swma()][ta.alma()]

###### ta.wpr()



威廉姆斯指标Williams %R。。该振荡指标显示当前收盘价与过去“一段时间内”的高/低价之间的关系。



```
ta.wpr(length) → series float
```

参数

**length (series int)** K线数量



```
//@version=6
indicator("Williams %R", shorttitle="%R", format=format.price, precision=2)
plot(ta.wpr(14), title="%R", color=color.new(#ff6d00, 0))
```

返回值

Williams %R。

备注

`source`系列中的`na`值将被忽略。

另见

[ta.mfi()][ta.cmo()]

###### table()



将na转换为表格



```
table(x) → series table
```

参数

**x (series table)** 要转换为指定类型的值，通常为`na`。

返回值

转换为表格后参数的值。

另见

[float()][int()][bool()][color()][string()][line()][label()]

###### table.cell()



此函数在表格中定义一个单元格并设置其属性。



```
table.cell(table_id, column, row, text, width, height, text_color, text_halign, text_valign, text_size, bgcolor, tooltip, text_font_family, text_formatting) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text (series string)** 在单元格内显示的文本。可选。默认值为空字符串。

**width (series int/float)** 单元格宽度占指标可视空间的百分比。可选。默认情况下，根据单元格内的文本自动调整宽度。0值具有相同的效果。

**height (series int/float)** 单元格的高度，以指标可视空间的%表示。可选。默认情况下，根据单元格内的文本自动调整高度。值0具有相同的效果。

**text_color (series color)** 文字的颜色。可选。默认值为[color.black]。

**text_halign (series string)** 单元格文本的水平对齐方式。可选。默认值为[text.align_center]。可能的值：[text.align_left]、[text.align_center]、[text.align_right]。

**text_valign (series string)** 单元格文本的垂直对齐方式。可选。默认值为 [text.align_center]。可能的值：[text.align_top]、[text.align_center]、[text.align_bottom]。

**text_size (series int/string)** 对象的大小，size可以是任意正整数，也可以是size.*内置常量字符串之一，常量字符串及其等效整数值为：[size.auto] (0)、[size.tiny] (8)、[size.small] (10)、[size.normal] (14)、[size.large] (20)、[size.huge] (36)，默认值为[size.normal]或14。

**bgcolor (series color)** 文本的背景颜色。可选。默认为无颜色。

**tooltip (series string)** 要在单元格内显示的tooltip。可选。

**text_font_family (series string)** 文本的字体系列。可选。默认值为[font.family_default]。可能的值：[font.family_default]、[font.family_monospace]。

**text_formatting (const text_format)** 显示文本的格式。格式选项支持添加。例如，`text.format_bold + text.format_italic`将使文本同时变为粗体和斜体。可能的值：[text.format_none]、[text.format_bold]、[text.format_italic]。可选。默认值为[text.format_none]。

备注

此函数不创建表格本身，而是定义表格的单元格。要使用它，您首先需要使用[table.new()]创建一个表对象。

每个[table.cell()]调用都会覆盖单元格的所有先前定义的属性。如果您连续调用[table.cell()]两次，例如，第一次使用text='Test Text'，第二次使用text_color=[color.red]，但没有新的文本参数，“text”的默认值为空字符串，它将覆盖“Test Text”，并且您的单元格将显示空字符串。如果您想修改单元格的任何属性，请使用table.cell_set_*()函数。

单个脚本只能在每个可能的位置显示一个表格。如果[table.cell()]用于多根K线以更改单元格的相同属性（例如，在第一根K线上将单元格的背景颜色更改为红色，然后在第二根K线上改为黄色），只有最后一次更改会反映在表格中，即单元格的背景将为黄色。尽可能通过将函数调用包含在[if][barstate.islast]块中，以将它们的执行限制为系列的最后一根K线，来避免不必要的单元格属性设置。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text()][table.cell_set_text_formatting()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_bgcolor()



此函数设置单元格的背景颜色。



```
table.cell_set_bgcolor(table_id, column, row, bgcolor) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**bgcolor (series color)** 单元格的背景颜色。

另见

[table.cell_set_height()][table.cell_set_text()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_height()



此函数设置单元格的高度。



```
table.cell_set_height(table_id, column, row, height) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**height (series int/float)** 单元格的高度，以图表窗口的%表示。输入0会根据单元格内的文本自动调整高度。

另见

[table.cell_set_bgcolor()][table.cell_set_text()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_text()



此函数在指定的单元格中设置文本。



```
table.cell_set_text(table_id, column, row, text) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text (series string)** 在单元格内显示的文本。



```
//@version=6
indicator("TABLE example")
var tLog = table.new(position = position.top_left, rows = 1, columns = 2, bgcolor = color.yellow, border_width=1)
table.cell(tLog, row = 0, column = 0, text = "sometext", text_color = color.blue)
table.cell_set_text(tLog, row = 0, column = 0, text = "sometext")
```

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()][table.cell_set_text_formatting()]

###### table.cell_set_text_color()



此功能设置单元格内文字的颜色。



```
table.cell_set_text_color(table_id, column, row, text_color) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text_color (series color)** 文字颜色。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_text_font_family()



该函数设置单元格内文本的字体系列。



```
table.cell_set_text_font_family(table_id, column, row, text_font_family) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text_font_family (series string)** 文本的字体系列。可能的值：[font.family_default]、[font.family_monospace]。



```
//@version=6
indicator("Example of setting the table cell font")
var t = table.new(position.top_left, rows = 1, columns = 1)
table.cell(t, 0, 0, "monospace", text_color = color.blue)
table.cell_set_text_font_family(t, 0, 0, font.family_monospace)
```

另见

[table.new()][font.family_default][font.family_monospace]

###### table.cell_set_text_formatting()



设置绘图应用于显示文本的格式属性。



```
table.cell_set_text_formatting(table_id, column, row, text_formatting) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text_formatting (const text_format)** 显示文本的格式。格式选项支持添加。例如，`text.format_bold + text.format_italic`将使文本同时变为粗体和斜体。可能的值：[text.format_none]、[text.format_bold]、[text.format_italic]。可选。默认值为[text.format_none]。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()][table.cell_set_text()]

###### table.cell_set_text_halign()



此函数设置单元格文本的水平对齐方式。



```
table.cell_set_text_halign(table_id, column, row, text_halign) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text_halign (series string)** 单元格文本的水平对齐方式。可能的值：[text.align_left]，[text.align_center]，[text.align_right]。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text()][table.cell_set_text_color()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_text_size()



此函数设置单元格的文字大小。



```
table.cell_set_text_size(table_id, column, row, text_size) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text_size (series int/string)** 对象的大小，size可以是任意正整数，也可以是size.*内置常量字符串之一，常量字符串及其等效整数值为：[size.auto] (0)、[size.tiny] (8)、[size.small] (10)、[size.normal] (14)、[size.large] (20)、[size.huge] (36)，默认值为[size.normal]或14。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_text_valign()



此函数设置单元格文本的垂直对齐方式。



```
table.cell_set_text_valign(table_id, column, row, text_valign) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**text_valign (series string)** 单元格文本的垂直对齐方式。可能的值：[text.align_top]，[text.align_center]，[text.align_bottom]。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_width()][table.cell_set_tooltip()]

###### table.cell_set_tooltip()



该函数在指定单元格中设置tooltip。



```
table.cell_set_tooltip(table_id, column, row, tooltip) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**tooltip (series string)** 要在单元格内显示的tooltip。



```
//@version=6
indicator("TABLE example")
var tLog = table.new(position = position.top_left, rows = 1, columns = 2, bgcolor = color.yellow, border_width=1)
table.cell(tLog, row = 0, column = 0, text = "sometext", text_color = color.blue)
table.cell_set_tooltip(tLog, row = 0, column = 0, tooltip = "sometext")
```

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_width()][table.cell_set_text()]

###### table.cell_set_width()



此函数设置单元格的宽度。



```
table.cell_set_width(table_id, column, row, width) → void
```

参数

**table_id (series table)** 表格对象。

**column (series int)** 单元格列的索引。编号从0开始。

**row (series int)** 单元格行的索引。编号从0开始。

**width (series int/float)** 单元格的宽度，以图表窗口的%表示。输入0会根据单元格内的文本自动调整宽度。

另见

[table.cell_set_bgcolor()][table.cell_set_height()][table.cell_set_text()][table.cell_set_text_color()][table.cell_set_text_halign()][table.cell_set_text_size()][table.cell_set_text_valign()][table.cell_set_tooltip()]

###### table.clear()



此函数从表格中删除一个单元格或一系列单元格。单元格以矩形形式移除，其中start_column和start_row指定左上角，end_column和end_row指定右下角。



```
table.clear(table_id, start_column, start_row, end_column, end_row) → void
```

参数

**table_id (series table)** 表格对象。

**start_column (series int)** 要删除的第一个单元格列的索引。编号从0开始。

**start_row (series int)** 要删除的第一个单元格行的索引。编号从0开始。

**end_column (series int)** 要删除的最后一个单元格列的索引。可选。默认值是用于start_column的参数。编号从0开始。

**end_row (series int)** 要删除的最后一个单元格行的索引。可选。默认值为用于start_row的参数。编号从0开始。



```
//@version=6
indicator("A donut", overlay=true)
if barstate.islast
    colNum = 8, rowNum = 8
    padding = "◯"
    donutTable = table.new(position.middle_right, colNum, rowNum)
    for c = 0 to colNum - 1
        for r = 0 to rowNum - 1
            table.cell(donutTable, c, r, text=padding, bgcolor=#face6e, text_color=color.new(color.black, 100))
    table.clear(donutTable, 2, 2, 5, 5)
```

另见

[table.delete()][table.new()]

###### table.delete()



此函数删除一个表格。



```
table.delete(table_id) → void
```

参数

**table_id (series table)** 表格对象。



```
//@version=6
indicator("table.delete example")
var testTable = table.new(position = position.top_right, columns = 2, rows = 1, bgcolor = color.yellow, border_width = 1)
if barstate.islast
    table.cell(table_id = testTable, column = 0, row = 0, text = "Open is " + str.tostring(open))
    table.cell(table_id = testTable, column = 1, row = 0, text = "Close is " + str.tostring(close), bgcolor=color.teal)
if barstate.isrealtime
    table.delete(testTable)
```

另见

[table.new()][table.clear()]

###### table.merge_cells()



该函数将表格中的一系列单元格合并为一个单元格。单元格合并为一个矩形，其中 start_column 和 start_row 指定左上角，end_column 和 end_row 指定右下角。



```
table.merge_cells(table_id, start_column, start_row, end_column, end_row) → void
```

参数

**table_id (series table)** 表格对象。

**start_column (series int)** 要合并的第一个单元格的列的索引。编号从 0 开始。

**start_row (series int)** 要合并的第一个单元格的行的索引。编号从 0 开始。

**end_column (series int)** 要合并的最后一个单元格的列的索引。编号从 0 开始。

**end_row (series int)** 要合并的最后一个单元格的行的索引。编号从 0 开始。



```
//@version=6
indicator("table.merge_cells example")
SMA50  = ta.sma(close, 50)
SMA100 = ta.sma(close, 100)
SMA200 = ta.sma(close, 200)
if barstate.islast
    maTable = table.new(position.bottom_right, 3, 3, bgcolor = color.gray, border_width = 1, border_color = color.black)
    // Header
    table.cell(maTable, 0, 0, text = "SMA Table")
    table.merge_cells(maTable, 0, 0, 2, 0)
    // Cell Titles
    table.cell(maTable, 0, 1, text = "SMA 50")
    table.cell(maTable, 1, 1, text = "SMA 100")
    table.cell(maTable, 2, 1, text = "SMA 200")
    // Values
    table.cell(maTable, 0, 2, bgcolor = color.white, text = str.tostring(SMA50))
    table.cell(maTable, 1, 2, bgcolor = color.white, text = str.tostring(SMA100))
    table.cell(maTable, 2, 2, bgcolor = color.white, text = str.tostring(SMA200))
```

备注

此函数将合并单元格，即使它们的属性尚未使用 [table.cell()] 定义。

生成的合并单元格从位于 `start_column`:`start_row` 的单元格继承其所有值，宽度和高度除外。结果合并单元格的宽度和高度基于相邻列/行中其他单元格的宽度/高度，无法手动设置。

要使用任何 `table.cell_set_*` 函数修改合并的单元格，请将单元格定位在 `start_column`:`start_row` 坐标。

尝试合并已合并的单元格将导致错误。

另见

[table.delete()][table.new()]

###### table.new()



此函数创建一个新表格。



```
table.new(position, columns, rows, bgcolor, frame_color, frame_width, border_color, border_width, force_overlay) → series table
```

参数

**position (series string)** 表格的位置。可能的值为： [position.top_left], [position.top_center], [position.top_right], [position.middle_left], [position.middle_center], [position.middle_right], [position.bottom_left], [position.bottom_center], [position.bottom_right]。

**columns (series int)** 表格中的列数。

**rows (series int)** 表格中的行数。

**bgcolor (series color)** 表格的背景色。可选。默认为无颜色。

**frame_color (series color)** 表格外框的颜色。可选。默认为无颜色。

**frame_width (series int)** 表格外框的宽度。可选。默认值为0。

**border_color (series color)** 单元格边框的颜色（不包括外框）。可选。默认为无颜色。

**border_width (series int)** 单元格边框的宽度（不包括外框）。可选。默认值为0。

**force_overlay (const bool)** 如果是`true`，则绘图将显示在主图表窗格上，即使脚本占用单独的窗格也是如此。可选。默认值为`false`。



```
//@version=6
indicator("table.new example")
var testTable = table.new(position = position.top_right, columns = 2, rows = 1, bgcolor = color.yellow, border_width = 1)
if barstate.islast
    table.cell(table_id = testTable, column = 0, row = 0, text = "Open is " + str.tostring(open))
    table.cell(table_id = testTable, column = 1, row = 0, text = "Close is " + str.tostring(close), bgcolor=color.teal)
```

返回值

可以传递给其他table.*()函数的表格对象的ID。

备注

此函数会创建表格对象本身，但表格在填充单元格之前不会显示。要定义单元格并更改其内容或属性，请使用[table.cell()]和其他table.cell_*()函数。

一次[table.new()]调用只能显示一张表格（最后绘制的一张表格），但函数本身将在使用它的每根K线上重新计算。出于表现原因，明智的做法是将[table.new()]与[var]关键字结合使用（因此仅在第一根K线上创建表格对象）或在[if][barstate.islast]块中使用（因此仅在最后一根K线上创建表格对象）。

另见

[table.cell()][table.clear()][table.delete()][table.set_bgcolor()][table.set_border_color()][table.set_border_width()][table.set_frame_color()][table.set_frame_width()][table.set_position()]

###### table.set_bgcolor()



此函数设置表格的背景色。



```
table.set_bgcolor(table_id, bgcolor) → void
```

参数

**table_id (series table)** 表格对象。

**bgcolor (series color)** 表格的背景色。可选。默认为无颜色。

另见

[table.clear()][table.delete()][table.new()][table.set_border_color()][table.set_border_width()][table.set_frame_color()][table.set_frame_width()][table.set_position()]

###### table.set_border_color()



此函数设置表格单元格的边框（不包括外框）的颜色。



```
table.set_border_color(table_id, border_color) → void
```

参数

**table_id (series table)** 表格对象。

**border_color (series color)** 边框的颜色。可选。默认为无颜色。

另见

[table.clear()][table.delete()][table.new()][table.set_frame_color()][table.set_border_width()][table.set_bgcolor()][table.set_frame_width()][table.set_position()]

###### table.set_border_width()



此函数设置表格单元格的边框（不包括外框）的宽度。



```
table.set_border_width(table_id, border_width) → void
```

参数

**table_id (series table)** 表格对象。

**border_width (series int)** 边框的宽度。可选。默认值为0。

另见

[table.clear()][table.delete()][table.new()][table.set_frame_color()][table.set_frame_width()][table.set_bgcolor()][table.set_border_color()][table.set_position()]

###### table.set_frame_color()



此函数设置表格外框的颜色。



```
table.set_frame_color(table_id, frame_color) → void
```

参数

**table_id (series table)** 表格对象。

**frame_color (series color)** 表格边框的颜色。可选。默认为无颜色。

另见

[table.clear()][table.delete()][table.new()][table.set_border_color()][table.set_border_width()][table.set_bgcolor()][table.set_frame_width()][table.set_position()]

###### table.set_frame_width()



此函数设置表格外框的宽度。



```
table.set_frame_width(table_id, frame_width) → void
```

参数

**table_id (series table)** 表格对象。

**frame_width (series int)** 表格外框的宽度。可选。默认值为0。

另见

[table.clear()][table.delete()][table.new()][table.set_frame_color()][table.set_border_width()][table.set_bgcolor()][table.set_border_color()][table.set_position()]

###### table.set_position()



此函数设置表格的位置。



```
table.set_position(table_id, position) → void
```

参数

**table_id (series table)** 表格对象。

**position (series string)** 表格的位置。可能的值为： [position.top_left], [position.top_center], [position.top_right], [position.middle_left], [position.middle_center], [position.middle_right], [position.bottom_left], [position.bottom_center], [position.bottom_right]。

另见

[table.clear()][table.delete()][table.new()][table.set_bgcolor()][table.set_border_color()][table.set_border_width()][table.set_frame_color()][table.set_frame_width()]

###### ticker.heikinashi()

2过载



创建一个代码标识符请求平滑平均K线值。

语法和重载

[`ticker.heikinashi(symbol) → simple string`][`ticker.heikinashi(symbol) → series string`]

参数

**symbol (simple string)** 商品代码标识符。



```
//@version=6
indicator("ticker.heikinashi", overlay=true)
heikinashi_close = request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, close)

heikinashi_aapl_60_close = request.security(ticker.heikinashi("AAPL"), "60", close)
plot(heikinashi_close)
plot(heikinashi_aapl_60_close)
```

返回值

可提供给[request.security()]功能的股票ID串值。

另见

[syminfo.tickerid][syminfo.ticker][request.security()][ticker.renko()][ticker.linebreak()][ticker.kagi()][ticker.pointfigure()]

###### ticker.inherit()

2过载



为指定的`symbol`构造一个股票代码ID，并使用从传递到函数调用的股票代码ID继承的附加参数，允许脚本使用与`from_tickerid`相同的修饰符来请求商品的数据，包括延长交易时段、股息调整、 货币换算、非标准图表类型、回溯调整、收盘结算等

语法和重载

[`ticker.inherit(from_tickerid, symbol) → simple string`][`ticker.inherit(from_tickerid, symbol) → series string`]

参数

**from_tickerid (simple string)** 从中继承修饰符的股票代码ID。

**symbol (simple string)** 用于构建新股票代码ID的商品代码。



```
//@version=6
indicator("ticker.inherit")

//@variable A "NASDAQ:AAPL" ticker ID with Extender Hours enabled.
tickerExtHours = ticker.new("NASDAQ", "AAPL", session.extended)
//@variable A Heikin Ashi ticker ID for "NASDAQ:AAPL" with Extended Hours enabled.
HAtickerExtHours = ticker.heikinashi(tickerExtHours)
//@variable The "NASDAQ:MSFT" symbol with no modifiers.
testSymbol = "NASDAQ:MSFT"
//@variable A ticker ID for "NASDAQ:MSFT" with inherited Heikin Ashi and Extended Hours modifiers.
testSymbolHAtickerExtHours = ticker.inherit(HAtickerExtHours, testSymbol)

//@variable The `close` price requested using "NASDAQ:MSFT" with inherited modifiers.
secData = request.security(testSymbolHAtickerExtHours, "60", close, ignore_invalid_symbol = true)
//@variable The `close` price requested using "NASDAQ:MSFT" without modifiers.
compareData = request.security(testSymbol, "60", close, ignore_invalid_symbol = true)

plot(secData, color = color.green)
plot(compareData)
```

备注

如果构造的股票代码ID继承了不适用于代码的修饰符（例如，如果`from_tickerid`启用了延长时段，但`symbol`没有这样的选项），则脚本将在使用该ID请求数据时忽略该修饰符。

###### ticker.kagi()

4过载



创建一个代码标识符请求卡吉图价值。

语法和重载

[`ticker.kagi(symbol, reversal) → simple string`][`ticker.kagi(symbol, reversal) → series string`][`ticker.kagi(symbol, param, style) → simple string`][`ticker.kagi(symbol, param, style) → series string`]

参数

**symbol (simple string)** 商品代码标识符。

**reversal (simple int/float)** 转向值(绝对价格值)。



```
//@version=6
indicator("ticker.kagi", overlay=true)
kagi_tickerid = ticker.kagi(syminfo.tickerid, 3)
kagi_close = request.security(kagi_tickerid, timeframe.period, close)
plot(kagi_close)
```

返回值

可提供给[request.security()]功能的股票ID串值。

另见

[syminfo.tickerid][syminfo.ticker][request.security()][ticker.heikinashi()][ticker.renko()][ticker.linebreak()][ticker.pointfigure()]

###### ticker.linebreak()

2过载



创建一个代码标识符请求换行符价值。

语法和重载

[`ticker.linebreak(symbol, number_of_lines) → simple string`][`ticker.linebreak(symbol, number_of_lines) → series string`]

参数

**symbol (simple string)** 商品代码标识符。

**number_of_lines (simple int)** 线的数量



```
//@version=6
indicator("ticker.linebreak", overlay=true)
linebreak_tickerid = ticker.linebreak(syminfo.tickerid, 3)
linebreak_close = request.security(linebreak_tickerid, timeframe.period, close)
plot(linebreak_close)
```

返回值

可提供给[request.security()]功能的股票ID串值。

另见

[syminfo.tickerid][syminfo.ticker][request.security()][ticker.heikinashi()][ticker.renko()][ticker.kagi()][ticker.pointfigure()]

###### ticker.modify()

2过载



创建一个代码标识符请求脚本的附加数据。

语法和重载

[`ticker.modify(tickerid, session, adjustment, backadjustment, settlement_as_close) → simple string`][`ticker.modify(tickerid, session, adjustment, backadjustment, settlement_as_close) → series string`]

参数

**tickerid (simple string)** 带有交易所前缀的商品名称，例如'BATS:MSFT'、'NASDAQ:MSFT'或带有交易时段和调整的股票代码[ticker.new()]函数。

**session (simple string)** 时段类型。可选参数。可能的值：[session.regular]、[session.extended]。 当前图表的时段类型是[syminfo.session]。如果未给出时段，则使用[syminfo.session]值。

**adjustment (simple string)** 调整类型。 可选参数。 可能的值：[adjustment.none]，[adjustment.splits]，[adjustment.dividends]。 如果未给出调整，则使用默认调整值（可能因品种而异）。

**backadjustment (simple backadjustment)** 指定连续期货商品的过去合约数据是否进行反向调整。此设置仅影响图表上具有此选项的商品数据。可选。默认值为[backadjustment.inherit]，这意味着修改后的商品ID会从传递给`tickerid`参数的商品ID继承设置，或者如果`tickerid`未指定此设置，则它会继承商品的默认值。可能的值：[backadjustment.inherit]、[backadjustment.on]、[backadjustment.off]。

**settlement_as_close (simple settlement)** 指定期货交易代码的[close]值是否代表“1D”及更高时间周期内的实际收盘价或结算价。此设置仅影响图表上具有此选项的商品代码数据。可选。默认值为[settlement_as_close.inherit]，这意味着修改后的代码ID会继承传入函数的`tickerid`的设置，或者如果`tickerid`未指定此设置，则它会继承图表商品代码的默认值。可能的值：[settlement_as_close.inherit]、[settlement_as_close.on]、[settlement_as_close.off]。



```
//@version=6
indicator("ticker_modify", overlay=true)
t1 = ticker.new(syminfo.prefix, syminfo.ticker, session.regular, adjustment.splits)
c1 = request.security(t1, "D", close)
t2 = ticker.modify(t1, session.extended)
c2 = request.security(t2, "2D", close)
plot(c1)
plot(c2)
```

返回值

可提供给[request.security()]功能的股票ID串值。

另见

[syminfo.tickerid][syminfo.ticker][syminfo.session][session.extended][session.regular][ticker.heikinashi()][adjustment.none][adjustment.splits][adjustment.dividends][backadjustment.inherit][backadjustment.on][backadjustment.off][settlement_as_close.inherit][settlement_as_close.on][settlement_as_close.off]

###### ticker.new()

2过载



创建一个代码标识符请求脚本的附加数据。

语法和重载

[`ticker.new(prefix, ticker, session, adjustment, backadjustment, settlement_as_close) → simple string`][`ticker.new(prefix, ticker, session, adjustment, backadjustment, settlement_as_close) → series string`]

参数

**prefix (simple string)** 交易所简称。例如:'BATS', 'NYSE', 'NASDAQ'.交易所简称主要是[syminfo.prefix].

**ticker (simple string)** 股票名称。例如'AAPL'，'MSFT'，'EURUSD'。 主要系列的股票名称是[syminfo.ticker]。

**session (simple string)** 时段类型。可选参数。可能的值：[session.regular]、[session.extended]。 当前图表的时段类型是[syminfo.session]。如果未给出时段，则使用[syminfo.session]值。

**adjustment (simple string)** 调整类型。 可选参数。 可能的值：[adjustment.none]，[adjustment.splits]，[adjustment.dividends]。 如果未给出调整，则使用默认调整值（可能因品种而异）。

**backadjustment (simple backadjustment)** 指定是否对连续期货代码的过去合约数据进行回溯调整。此设置仅影响图表上具有此选项的商品代码数据。可选。默认值为[backadjustment.inherit]，这意味着新的代码ID继承了代码的默认设置。可能的值：[backadjustment.inherit]、[backadjustment.on]、[backadjustment.off]。

**settlement_as_close (simple settlement)** 指定期货代码的[close]值是否代表“1D”及更高时间周期内的实际收盘价或结算价。此设置仅影响图表上具有此选项的商品代码数据。可选。默认值为[settlement_as_close.inherit]，这意味着新的代码ID继承了图表代码的默认设置。可能的值：[settlement_as_close.inherit]、[settlement_as_close.on]、[settlement_as_close.off]。



```
//@version=6
indicator("ticker.new", overlay=true)
t = ticker.new(syminfo.prefix, syminfo.ticker, session.regular, adjustment.splits)
t2 = ticker.heikinashi(t)
c = request.security(t2, timeframe.period, low, barmerge.gaps_on)
plot(c, style=plot.style_linebr)
```

返回值

可提供给[request.security()]功能的股票ID串值。

备注

您可以使用[ticker.new()]功能的返回值作为[ticker.heikinashi()]，[ticker.renko()]，[ticker.linebreak()]，[ticker.kagi()]，[ticker.pointfigure()]功能的输入参数。

另见

[syminfo.tickerid][syminfo.ticker][syminfo.session][session.extended][session.regular][ticker.heikinashi()][adjustment.none][adjustment.splits][adjustment.dividends][backadjustment.inherit][backadjustment.on][backadjustment.off][settlement_as_close.inherit][settlement_as_close.on][settlement_as_close.off]

###### ticker.pointfigure()

2过载



创建一个代码标识符请求点数图值。

语法和重载

[`ticker.pointfigure(symbol, source, style, param, reversal) → simple string`][`ticker.pointfigure(symbol, source, style, param, reversal) → series string`]

参数

**symbol (simple string)** 商品代码标识符。

**source (simple string)** 计算Point & Figure的来源。可能的值为：'hl'、'close'。

**style (simple string)** 指定股票行情box大小的分配方法。可能的值：“ATR”表示平均真实波动幅度，“Traditional”表示使用固定尺寸，“PercentageLTP”表示使用最新交易价格的百分比。

**param (simple int/float)** 如果`style`值为“ATR”，则表示股票行情的“ATR 长度”值；如果`style`为“Traditional”，则表示“Box size”值；如果`style`为“PercentageLTP”，则表示“Percentage”值。

**reversal (simple int)** 转向值。



```
//@version=6
indicator("ticker.pointfigure", overlay=true)
pnf_tickerid = ticker.pointfigure(syminfo.tickerid, "hl", "Traditional", 1, 3)
pnf_close = request.security(pnf_tickerid, timeframe.period, close)
plot(pnf_close)
```

返回值

可提供给[request.security()]功能的股票ID串值。

另见

[syminfo.tickerid][syminfo.ticker][request.security()][ticker.heikinashi()][ticker.renko()][ticker.linebreak()][ticker.kagi()]

###### ticker.renko()

2过载



创建一个代码标识符请求砖形图价值。

语法和重载

[`ticker.renko(symbol, style, param, request_wicks, source) → simple string`][`ticker.renko(symbol, style, param, request_wicks, source) → series string`]

参数

**symbol (simple string)** 商品代码标识符。

**style (simple string)** 指定股票行情box大小的分配方法。可能的值：“ATR”表示平均真实波动幅度，“Traditional”表示使用固定尺寸，“PercentageLTP”表示使用最新交易价格的百分比。

**param (simple int/float)** 如果`style`值为“ATR”，则表示股票行情的“ATR 长度”值；如果`style`为“Traditional”，则表示“Box size”值；如果`style`为“PercentageLTP”，则表示“Percentage”值。

**request_wicks (simple bool)** 指定是否返回Renko砖的灯芯值。当使用此函数形成的股票代码从商品请求的`true`、[high]和[low]值存在时，将包括烛芯值。当`false`、[high]和[low]始终等于[open]或[close]时。可选。默认值为`false`。有关如何计算Renko烛芯的详细说明，请访问我们的[帮助中心]。

**source (simple string)** 用于计算砖块的来源。可选。可能的值：“Close”、“OHLC”。默认为“Close”。



```
//@version=6
indicator("ticker.renko", overlay=true)
renko_tickerid = ticker.renko(syminfo.tickerid, "ATR", 10)
renko_close = request.security(renko_tickerid, timeframe.period, close)
plot(renko_close)
```



```
//@version=6
indicator("Renko candles", overlay=false)
renko_tickerid = ticker.renko(syminfo.tickerid, "ATR", 10)
[renko_open, renko_high, renko_low, renko_close] = request.security(renko_tickerid, timeframe.period, [open, high, low, close`
plotcandle(renko_open, renko_high, renko_low, renko_close, color = renko_close > renko_open ? color.green : color.red)
```

返回值

可提供给[request.security()]功能的股票ID串值。

另见

[syminfo.tickerid][syminfo.ticker][request.security()][ticker.heikinashi()][ticker.linebreak()][ticker.kagi()][ticker.pointfigure()]

###### ticker.standard()

2过载



创建一个行情代码以从不受延长交易时段、股息调整、货币转换和非标准图表类型的计算影响的标准图表请求数据：Heikin Ashi、Renko等。除其它外，这使得当脚本在非标准图表上运行时检索标准图表值成为可能。

语法和重载

[`ticker.standard(symbol) → simple string`][`ticker.standard(symbol) → series string`]

参数

**symbol (simple string)** 要转换为其标准形式的代码ID。可选。默认值为[syminfo.tickerid]。



```
//@version=6
indicator("ticker.standard", overlay = true)
// This script should be run on a non-standard chart such as HA, Renko...

// Requests data from the chart type the script is running on.
chartTypeValue = request.security(syminfo.tickerid, "1D", close)

// Request data from the standard chart type, regardless of the chart type the script is running on.
standardChartValue = request.security(ticker.standard(syminfo.tickerid), "1D", close)

// This will not use a standard ticker ID because the `symbol` argument contains only the ticker — not the prefix (exchange).
standardChartValue2 = request.security(ticker.standard(syminfo.ticker), "1D", close)

plot(chartTypeValue)
plot(standardChartValue, color = color.green)
```

返回值

代表标准图表代码的字符串，格式为“prefix:ticker”。如果 `symbol` 参数不包含前缀和商品代码信息，该函数将按原样返回提供的参数。

另见

[request.security()]

###### time()

2过载



返回指定时段和会话的UNIX时间戳，如果时间点在时段之外，则返回`na`。

语法和重载

[`time(timeframe, session, bars_back, timeframe_bars_back) → series int`][`time(timeframe, session, timezone, bars_back, timeframe_bars_back) → series int`]

参数

**timeframe (series string)** 时间戳计算的时间周期。如果该值为空字符串，则函数使用脚本的主时间周期。

**session (series string)** 可选。用于筛选时间的[session string]。如果时间在指定的时段中，该函数返回时间戳；如果时间在时段之外，则返回`na`。如果参数为空字符串，则函数使用默认值，即该商品所在的时段。

**bars_back (series int)** 可选。脚本主时间周期的K线偏移量。如果该值为正数，则函数会找到主时间框架上当前K线前N根K线的位置，然后检索由`timeframe`参数指定的时间框架上对应K线的时间戳。如果该值为-1到-500之间的负数，则函数会计算主时间框架上当前K线后N根K线对应的`timeframe`根K线的预期时间戳。默认值为0。

**timeframe_bars_back (series int)** 可选。在由`timeframe`参数指定的时间周期上，额外的K线偏移量。如果该值为正数，则函数会检索与`bars_back`偏移量对应的K线前N`timeframe`个K线的时间戳。如果该值为-1到-500之间的负数，则函数会计算对应`bars_back`偏移量的`timeframe`根K线之后N`timeframe`根K线的预期时间戳。默认值为0。



```
//@version=6
indicator("Time", overlay=true)
// Try this on chart AAPL,1
timeinrange(res, sess) => not na(time(res, sess, "America/New_York")) ? 1 : 0
plot(timeinrange("1", "1300-1400"), color=color.red)

// This plots 1.0 at every start of 10 minute bar on a 1 minute chart:
newbar(res) => ta.change(time(res)) == 0 ? 0 : 1
plot(newbar("10"))
```

当设置某个会话时，您不仅可以指定小时与分钟，也可以指定某一周内的日期。

如果没有指定日期，则认为交易时段设置为从星期日 (1) 到星期六 (7)，即“1100-2000”与“1100-1200:1234567”相同。

您可以通过指定日期来更改它。例如，对于每周7天交易且24小时交易时段的商品，以下脚本不会为周六和周日着色：



```
//@version=6
indicator("Time", overlay=true)
t1 = time(timeframe.period, "0000-0000:23456")
bgcolor(not na(t1) ? color.new(color.blue, 90) : na)
```

一个`session`参数可以包含多个不同的交易时段，以逗号分隔。例如，以下脚本将突出显示从10:00到11:00以及从14:00到15:00（仅限工作日）的K线图：



```
//@version=6
indicator("Time", overlay=true)
t1 = time(timeframe.period, "1000-1100,1400-1500:23456")
bgcolor(not na(t1) ? color.new(color.blue, 90) : na)
```

返回值

开盘UNIX时间戳

备注

UNIX时间是一种标准化的日期和时间表示方法，它衡量的是自1970年1月1日00:00:00UTC以来经过的非闰秒数。Pine脚本以毫秒为单位表示UNIX时间值。请参阅用户手册[Time]页面的[UNIX timestamps]部分以了解更多信息。

另见

[time]

###### time_close()

2过载



返回指定时间周期和交易时段的UNIX收盘时间戳，如果时间点超出交易时段，则返回`na`。对于基于价格的图表，例如砖形图表、线形图、卡吉图、点数图和范围图，由于未来的收盘时间不可预测，该函数会在最新的实时K线处返回`na`。但是，对于任何之前的K线，它都会返回有效的时间戳。

语法和重载

[`time_close(timeframe, session, bars_back, timeframe_bars_back) → series int`][`time_close(timeframe, session, timezone, bars_back, timeframe_bars_back) → series int`]

参数

**timeframe (series string)** 时间戳计算的时间周期。如果该值为空字符串，则函数使用脚本的主时间周期。

**session (series string)** 可选。用于筛选时间的[session string]。如果时间在指定的时段中，该函数返回时间戳；如果时间在时段之外，则返回`na`。如果参数为空字符串，则函数使用默认值，即该商品所在的时段。

**bars_back (series int)** 可选。脚本主时间周期的K线偏移量。如果该值为正数，则函数会找到主时间框架上当前K线前N根K线的位置，然后检索由`timeframe`参数指定的时间框架上对应K线的时间戳。如果该值为-1到-500之间的负数，则函数会计算主时间框架上当前K线后N根K线对应的`timeframe`根K线的预期时间戳。默认值为0。

**timeframe_bars_back (series int)** 可选。在由`timeframe`参数指定的时间周期上，额外的K线偏移量。如果该值为正数，则函数会检索与`bars_back`偏移量对应的K线前N`timeframe`个K线的时间戳。如果该值为-1到-500之间的负数，则函数会计算对应`bars_back`偏移量的`timeframe`根K线之后N`timeframe`根K线的预期时间戳。默认值为0。



```
//@version=6
indicator("Time", overlay=true)
t1 = time_close(timeframe.period, "1200-1300", "America/New_York")
bgcolor(not na(t1) ? color.new(color.blue, 90) : na)
```

返回值

收盘UNIX时间戳。

备注

UNIX时间是一种标准化的日期和时间表示方法，它衡量的是自1970年1月1日00:00:00UTC以来经过的非闰秒数。Pine脚本以毫秒为单位表示UNIX时间值。请参阅用户手册[Time]页面的[UNIX timestamps]部分以了解更多信息。

另见

[time_close]

###### timeframe.change()



检测指定`timeframe`内的变动。



```
timeframe.change(timeframe) → series bool
```

参数

**timeframe (series string)** 根据[用户手册的时间周期字符串规范]格式化的字符串。



```
//@version=6
// Run this script on an intraday chart.
indicator("New day started", overlay = true)
// Highlights the first bar of the new day.
isNewDay = timeframe.change("1D")
bgcolor(isNewDay ? color.new(color.green, 80) : na)
```

返回值

在新的`timeframe`的第一根K线上返回`true`，否则返回`false`。

###### timeframe.from_seconds()

2过载



将秒数转换为有效的时间周期字符串。

语法和重载

[`timeframe.from_seconds(seconds) → simple string`][`timeframe.from_seconds(seconds) → series string`]

参数

**seconds (simple int)** 时间周期内的秒数。



```
//@version=6
indicator("HTF Close", "", true)
int chartTf = timeframe.in_seconds()
string tfTimes5 = timeframe.from_seconds(chartTf * 5)
float htfClose = request.security(syminfo.tickerid, tfTimes5, close)
plot(htfClose)
```

返回值

符合[timeframe string specifications]的时间周期字符串。

备注

如果所提供的秒数不存在有效时间周期，则将返回下一个更高的有效时间周期。因此，一秒或更少将返回“1S”，2-5秒将返回“5S”，604,799秒（小于7天的一秒）将返回“7D”。

如果秒准确地代表两个或多个有效时间周期，则将使用具有较大基本单位的时间周期。因此604,800秒（7天）返回“1W”，而不是“7D”。

所有高于31,622,400（366 天）的值都会返回“12M”。

另见

[timeframe.in_seconds()][request.security][request.security_lower_tf]

###### timeframe.in_seconds()

2过载



将时间周期字符串转换为秒。

语法和重载

[`timeframe.in_seconds(timeframe) → simple int`][`timeframe.in_seconds(timeframe) → series int`]

参数

**timeframe (simple string)** [timeframe string specifications]格式的时间周期字符串。可选。默认值为[timeframe.period]。



```
//@version=6
indicator("`timeframe_in_seconds()`"),

// Get a user-selected timeframe.
tfInput = input.timeframe("1D")

// Convert it into an "int" number of seconds.
secondsInTf = timeframe.in_seconds(tfInput)

plot(secondsInTf)
```

返回值

时间周期字符串中秒数的“int”表示形式。

备注

当时间周期为“1M”或更大时，计算使用2628003作为一个月的秒数，即30.4167(365/12)天。

另见

[input.timeframe()][timeframe.period][timeframe.from_seconds()]

###### timestamp()

6过载



时间戳功能返回UNIX时间的指定日期和时间。

语法和重载

[`timestamp(dateString) → const int`][`timestamp(dateString) → series int`][`timestamp(year, month, day, hour, minute, second) → simple int`][`timestamp(year, month, day, hour, minute, second) → series int`][`timestamp(timezone, year, month, day, hour, minute, second) → simple int`][`timestamp(timezone, year, month, day, hour, minute, second) → series int`]

参数

**dateString (const string)** 一个字符串，其中包含日期以及可选的时间和时区。其格式必须符合[IETF RFC 2822]或[ISO 8601]标准（“DD MMM YYYY hh:mm:ss±hhmm”或“YYYY-MM-DDThh:mm:ss±hh:mm”，因此是“20 Feb 2020”或“2020-02-20”）。如果未提供时间，则使用“00:00”。如果未提供任何时区，则将使用GMT+0。请注意，这与函数通常的行为不同，后者返回交易所所在时区的时间。



```
//@version=6
indicator("timestamp")
plot(timestamp(2016, 01, 19, 09, 30), linewidth=3, color=color.green)
plot(timestamp(syminfo.timezone, 2016, 01, 19, 09, 30), color=color.blue)
plot(timestamp(2016, 01, 19, 09, 30), color=color.yellow)
plot(timestamp("GMT+6", 2016, 01, 19, 09, 30))
plot(timestamp(2019, 06, 19, 09, 30, 15), color=color.lime)
plot(timestamp("GMT+3", 2019, 06, 19, 09, 30, 15), color=color.fuchsia)
plot(timestamp("Feb 01 2020 22:10:05"))
plot(timestamp("2011-10-10T14:48:00"))
plot(timestamp("04 Dec 1995 00:12:00 GMT+5"))
```

返回值

Unix时间。

备注

UNIX时间是自1970年1月1日UTC 00:00:00起已经过去的毫秒数。

另见

[time()][time][timenow][syminfo.timezone]

###### volume_row.buy_volume()



Calculates the total "buy" volume for the volume footprint row represented by a [volume_row] object.



```
volume_row.buy_volume(id) → series float
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

The total "buy" volume for the footprint row.

###### volume_row.delta()



计算由[volume_row]对象表示的成交量轨迹的成交量差值。该值表示该行“买入”成交量与“卖出”成交量之差。正值表示该行的“买入”成交量大于“卖出”成交量，负值则表示相反的情况。



```
volume_row.delta(id) → series float
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

The volume delta for the footprint row.

###### volume_row.down_price()



Retrieves the lower price level of the volume footprint row represented by a [volume_row] object.



```
volume_row.down_price(id) → series float
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

The lower boundary of the footprint row's price range.

###### volume_row.has_buy_imbalance()



检查由[volume_row]对象表示的成交量占比行是否存在“买入”失衡，该失衡基于该对象所依赖的[request.footprint()]调用的`imbalance_percent`参数。如果该行的“买入”成交量超过其下方行的“卖出”成交量达到指定百分比，则返回`true`；否则返回`false`。



```
volume_row.has_buy_imbalance(id) → series bool
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

A value of `true` if the footprint row has a detected buy imbalance, and `false` otherwise.

###### volume_row.has_sell_imbalance()



检查由[volume_row]对象表示的成交量占比行是否存在卖出失衡，检查依据是该对象所依赖的[request.footprint()]调用的`imbalance_percent`参数。如果该行的“卖出”成交量超过其上方成交量行的“买入”成交量达到指定百分比，则返回`true`；否则返回`false`。



```
volume_row.has_sell_imbalance(id) → series bool
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

A value of `true` if the footprint row has a detected sell imbalance, and `false` otherwise.

###### volume_row.sell_volume()



Calculates the total "sell" volume for the volume footprint row represented by a [volume_row] object.



```
volume_row.sell_volume(id) → series float
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

The total "sell" volume for the footprint row.

###### volume_row.total_volume()



Calculates the sum of the "buy" and "sell" volume for the volume footprint row represented by a [volume_row] object.



```
volume_row.total_volume(id) → series float
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

The total volume for the footprint row.

###### volume_row.up_price()



Retrieves the upper price level of the volume footprint row represented by a [volume_row] object.



```
volume_row.up_price(id) → series float
```

参数

**id (volume_row)** The reference (ID) of the [volume_row] object to analyze.

返回值

The upper boundary of the footprint row's price range.

###### weekofyear()



根据UNIX时间戳计算指定时区内一年中的周数。



```
weekofyear(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的UNIX时间戳。

**timezone (series string)** 可选。指定返回的周号的时区。该值可以是采用UTC/GMT偏移量表示法（例如“UTC-5”）或IANA时区数据库表示法（例如“America/New_York”）的时区字符串。默认值为[syminfo.timezone]。

返回值

计算出的周数，以指定的时区表示。

备注

[UNIX时间戳] 表示自1970-01-01 00:00 UTC以来经过的毫秒数。UNIX时间戳的含义不会相对于任何时区变化。UNIX时间戳的含义不会相对于任何时区变化。

另见

[weekofyear][dayofmonth()][dayofweek()][time()][year()][month()][hour()][minute()][second()]

###### year()

```
year(time, timezone) → series int
```

参数

**time (series int)** 以毫秒为单位的unix时间。

**timezone (series string)** 允许将返回值调整为以UTC/GMT表示法（例如，“UTC-5”、“GMT+0530”）或IANA时区数据库名称（例如，“America/New_York”）指定的时区。可选。默认值为[syminfo.timezone]。

返回值

提供UNIX时间的年份(交换时区)。

> UNIX时间是自1970年1月1日UTC 00:00:00起已经过去的毫秒数。
>

请注意，此函数根据K线的打开时间返回年份。对于隔夜交易时段（例如EURUSD周一交易时段从周日17:00 UTC-4开始），该值可以比交易日的年份低1。

#### 关键词

###### and

逻辑 AND。适用于布尔表达式。

```
expr1 and expr2
```

> 返回值
>
> 布尔值，或一系列布尔值。
>

如果`expr1`计算结果为`false`，则`and`运算符将返回`false`而不计算`expr2`。

###### enum

该关键字允许创建枚举，简称enum。

枚举是保存预定义常量组的独特结构。

枚举中的每个字段都有一个`const string`标题。脚本可以使用点表示法访问枚举中的字段，类似于访问用户定义类型的字段。

每个字段代表`enumName`枚举的一个值。脚本可以使用可选的`const string`标题声明`enum`中的每个字段。如果未指定字段的标题，则其标题是其名称的字符串表示形式。在枚举字段上使用[str.tostring()]来检索其标题。

```js
[export ]enum <enumName> 
<field_1> [= <title_1>] 
<field_2> [= <title_2>] 
... 
<field_N> [= <title_N>]
```

借助`input.enum()`函数，可以使用枚举快速创建下拉输入。下拉列表中显示的选项代表枚举字段的标题。

```js
//@version=6
indicator("Session highlight", overlay = true)

enum tz
    utc  = "UTC"
    exch = ""
    ny   = "America/New_York"
    chi  = "America/Chicago"
    lon  = "Europe/London"
    tok  = "Asia/Tokyo"

//@variable The session string.
selectedSession = input.session("1200-1500", "Session")
//@variable The selected timezone. The input's dropdown contains the fields in the `tz` enum.
selectedTimezone = input.enum(tz.utc, "Session Timezone")

bool inSession = false
if not na(time("", selectedSession, str.tostring(selectedTimezone)))
    inSession := true

bgcolor(inSession ? color.new(color.green, 90) : na, title = "Active session highlight")
```

此外，还可以在集合的类型模板中使用枚举来限制其允许作为元素的值。在类型模板中使用时，集合将仅接受属于指定枚举的字段。

```js
//@version=6
indicator("Map with enum keys")

//@enum        Contains fields with titles representing ticker IDs.
//@field aapl  Has an Apple ticker ID as its title.
//@field tsla  Has a Tesla ticker ID as its title.
//@field amzn  Has an Amazon ticker ID as its title.
enum symbols
    aapl = "NASDAQ:AAPL"
    tsla = "NASDAQ:TSLA"
    amzn = "NASDAQ:AMZN"

//@variable A map that accepts fields from the `symbols` enum as keys and "float" values.
map<symbols, float> data = map.new<symbols, float>()
// Put key-value pairs into the `data` map.
data.put(symbols.aapl, request.security(str.tostring(symbols.aapl), timeframe.period, close))
data.put(symbols.tsla, request.security(str.tostring(symbols.tsla), timeframe.period, close))
data.put(symbols.amzn, request.security(str.tostring(symbols.amzn), timeframe.period, close))
// Plot the value from the `data` map accessed by the `symbols.aapl` key.
plot(data.get(symbols.aapl))
```

###### export

在库中用于函数声明或用户定义的类型定义的前缀，这些定义可从导入库的其它脚本中获得。

```js
//@version=6
//@description Library of debugging functions.
library("Debugging_library", overlay = true)
//@function Displays a string as a table cell for debugging purposes.
//@param txt String to display.
//@returns Void.
export print(string txt) =>
    var table t = table.new(position.middle_right, 1, 1)
    table.cell(t, 0, 0, txt, bgcolor = color.yellow)
// Using the function from inside the library to show an example on the published chart.
// This has no impact on scripts using the library.
print("Library Test")
```

每个库必须至少有一个导出函数或用户定义类型(UDT)。

如果导出函数是阵列、可变变量（使用`:=`重新分配）或“input”形式的变量，则导出函数不能使用全局范围内的变量。

导出的函数不能使用 `request.*()` 函数。

导出的函数必须显式声明每个参数的类型，并且所有参数都必须在函数体中使用。默认情况下，传递给导出函数的所有参数都是[series]形式，除非它们在函数的签名中明确指定为[simple]。

@description、@function、@param、@type、@field和@returns编译器注释用于自动生成库的描述和发行说明，以及Pine Script®编辑器的工具提示。

###### for

创建一个计数控制循环，该循环使用计数器变量来管理其本地代码块的迭代执行。

循环继续进行新的迭代，直到计数器达到指定的最终值。

```
[variables =|:=] for counter = from_num to to_num [by step_num]
    statements | continue | break
    return_expression
```

**variables (return_expression type)**可选。一个变量或元组，用于保存循环终止后最后一次求值`return_expression`的值或引用。脚本只能在结果类型不为“void”时将循环返回的结果赋值给变量。如果循环条件阻止迭代，或者没有迭代求值`return_expression`，则变量的赋值或引用为`na`；如果返回类型为“bool”，则为`false`。

**counter (series int/float)**计数器变量。循环在每次迭代后将变量的值从初始值(`from_num`)增加到最终值(`to_num`)，增量为固定量(`step_num`)。当变量的值达到`to_num`值时，将发生最后一次可能的迭代。

**from_num (series int/float)**循环第一次迭代时`counter`变量的值。

**to_num (series int/float)**循环头允许新迭代的最终`counter`值。循环将`counter`值增加`step_num`，直到达到或超过此值。如果脚本在循环迭代期间修改此值，则循环头将使用新值来控制允许的后续迭代。

**step_num (series int/float)**可选。一个正值，指定`counter`值增加或减少的量，直到达到或超过`to_num`值。如果`from_num`值大于初始`to_num`值，则循环在每次迭代后从`counter`值中减去此量。否则，循环在每次迭代后添加此量。默认值为1。

**statements**循环体内的代码语句和表达式，即循环头下方的缩进代码块。

**return_expression (any type)**循环主体中的最后一个表达式或语句。循环在最后一次迭代后返回此代码的结果。如果循环由于`continue`或`break`语句而提前停止，则返回的值或引用是执行此代码的最新迭代的值或引用。要使用循环的返回结果，请将其赋值给变量或元组。

**continue**循环特定的关键字，指示脚本跳过当前循环迭代的剩余部分并继续下一次迭代。

**break**循环特定的关键字，提示脚本停止当前迭代并完全退出循环。

```js
//@version=6
indicator("Basic `for` loop")

//@function Calculates the number of bars in the last `length` bars that have their `close` above the current `close`.
//@param length The number of bars used in the calculation.
greaterCloseCount(length) =>
    int result = 0
    for i = 1 to length
        if close[i] > close
            result += 1
    result

plot(greaterCloseCount(14))
```

```js
//@version=6
indicator("`for` loop with a step")

a = array.from(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = 0.0

for i = 0 to 9 by 5
    // Because the step is set to 5, we are adding only the first (0) and the sixth (5) value from the array `a`.
    sum += array.get(a, i)

plot(sum)
```

在迭代过程中修改循环的`to_num`值不会改变循环计数器的方向。对于向上计数的循环，在迭代中将`to_num`设置为小于`from_num`值的值会在迭代结束后立即停止循环。同样，向下计数的循环会在`to_num`值大于`from_num`值的迭代后停止。

如果脚本使用循环结果初始化使用 [var]或[varip]声明的变量，则循环会在*第一次*迭代后停止，即使标头的条件允许更多次迭代。与其直接使用此结构的结果初始化变量，不如先声明变量，然后使用[:=]将其更新为结果。或者，将循环移至[声明函数]，并使用对该函数的调用来初始化变量。

请参阅我们的用户手册的[循环]页面，了解有关循环及其工作原理的更多信息。

###### for...in

创建一个由集合控制的循环，该循环按顺序迭代[array]的 *元素*、[matrix]的*行*或[map]的*键值对*。

循环的本地代码块将对指定集合中的每个元素、行或对执行一次。

```js
[variables = | :=] for item in collection_id
    statements | continue | break
    return_expression

[variables = | :=] for [index, item] in collection_id
    statements | continue | break
    return_expression
```

**variables (return_expression type)** - 可选。一个变量或元组，用于保存循环终止后最后一次求值`return_expression`的值或引用。脚本只能在结果类型不为“void”时将循环返回的结果赋值给变量。如果循环条件阻止迭代，或者没有迭代求值`return_expression`，则变量的赋值或引用为`na`；如果返回类型为“bool”，则为`false`。

**index** - 用于跟踪当前迭代的数组元素索引、矩阵行索引或映射键的变量。循环无法使用重新赋值或复合赋值运算符修改此变量。此变量仅在循环结构的第二种形式中有效。

**item** - 用于跟踪当前迭代的数组元素、矩阵行或映射值元素的变量。循环无法使用重新赋值或复合赋值运算符修改此变量。

**collection_id (array/matrix/map)** - 循环迭代其项目的数组、矩阵或映射的ID。

**statements** - 循环体内的代码语句和表达式，即循环头下方缩进的代码块。

**return_expression (any type)** - 循环主体中的最后一个表达式或语句。循环在最后一次迭代后返回此代码的结果。如果循环因`continue`或`break`语句而提前停止，则返回的值或引用是执行此代码的最新一次迭代的值或引用。要使用循环的返回结果，请将其赋值给变量或元组。

**continue** - 循环特定的关键字，指示脚本跳过当前循环迭代的剩余部分并继续下一次迭代。

**break** - 循环特定的关键字，提示脚本停止当前迭代并完全退出循环。

下面的示例使用`for...in`循环的第一种形式来计算大于指定值的数组元素值的数量：

```js
//@version=6
indicator("'for...in' array (first form) demo")

//@function Counts the number of 'id' array elements that are greater than the specified value. 
numGreaterThan(array<float> id, float value) =>
    int result = 0
    for element in id
        if element > value
            result += 1
    result

//@variable References an array containing the current bar's OHLC values. 
array<float> ohlcValues = array.from(open, high, low, close)

// Plot the number of 'ohlcValues' elements that are greater than the 20-bar SMA of 'close'. 
plot(numGreaterThan(ohlcValues, ta.sma(close, 20)))
```

下面的示例使用循环结构的第二种形式在两个数组之间执行元素加法：

```js
//@version=6
indicator("`for...in` array (second form) demo")

//@function Creates a new array whose elements are the sums of corresponding elements in the `id1` and `id2` arrays. 
elementWiseAdd(array<float> id1, array<float> id2) =>
    array<float> result = array.new<float>()
    // Loop through the `id1` array while tracking each element's index *and* value.
    for [index, element1] in id1
        // Use `index` to retrieve the corresponding element in the `id2` array, then push the sum into the new array.
        float element2 = id2.get(index)
        result.push(element1 + element2)
    result

if barstate.isfirst
    // Create two arrays for which to perform element-wise addition.
    array<float> array1 = array.from(1.0, 2.0, 3.0, 4.0)
    array<float> array2 = array.from(2.0, 3.0, 4.0, 5.0)

    //@variable References the resulting array of element-wise sums. 
    array<float> sums = elementWiseAdd(array1, array2)
    // Log a string representation of the `sums` array's contents in the Pine Logs pane. 
    log.info(str.tostring(sums))
```

此示例使用循环结构的第一种形式遍历矩阵的行，并创建一个包含每行和的数组。标题的循环变量`rowArrayID`引用一个包含当前行值的数组：

```js
//@version=6
indicator("`for...in` matrix (first form) demo")

//@function Creates a matrix that organizes the contents of the `arrayID` array into a specified shape.
matrixFromArray(array<float> arrayID, int rows, int columns) =>
    matrix<float> result = matrix.new<float>()
    result.add_row(0, arrayID)
    result.reshape(rows, columns)
    result

//@function Creates an array containing the sum of elements in each row of the `matrixID` matrix.
calcRowSums(matrix<float> matrixID) =>
    array<float> result = array.new<float>()
    // Iterate over the matrix rows, where `rowArrayID` references an *array* containing the current row's values. 
    for rowArrayID in matrixID
        // Push the sum of `rowArrayID` elements into the `result` array. 
        result.push(rowArrayID.sum())
    result
    
if barstate.isfirst
    // Create a 2x2 matrix of pseudorandom values.
    array<float>  randArray = array.from(math.random(), math.random(), math.random(), math.random())  
    matrix<float> randMat   = matrixFromArray(randArray, 2, 2)
    // Log string representation of the `randMat` matrix and the calculated array of row sums in the Pine Logs pane.
    log.info("\n" + str.tostring(randMat))
    log.info(str.tostring(calcRowSums(randMat)))
```

以下示例使用`for...in`循环来迭代映射的键值对并构建其内容的自定义字符串表示形式：

```js
//@version=6
indicator("`for...in` map demo")

//@function Creates a custom string representation of a map containing "string" keys and "float" values. 
toString(map<string, float> id) =>
    string result = "{"
    // Iterate through the key-value pairs of the `id` map, in insertion order. 
    for [key, value] in id
        result += str.format("''{0}'': {1}, ", key, value)
    result += "}"
    result := str.replace(result, ", }", "}")

if barstate.islastconfirmedhistory
    //@variable References a map to store "float" OHLC values with corresponding "string" keys. 
    map<string, float> ohlcMap = map.new<string, float>()
    // Put key-value pairs into the map. 
    ohlcMap.put("Open",  open)
    ohlcMap.put("High",  high)
    ohlcMap.put("Low",   low)
    ohlcMap.put("Close", close)
    // Log the `toString()` result for the map referenced by `ohlcMap`.
    log.info(toString(ohlcMap))
```

只有`for...in`循环的*第二种*形式与Map兼容。该循环按照键的*插入顺序*对Map中的键值对迭代。

脚本可以在使用`for...in`循环迭代数组和矩阵内容时修改其大小。但是，脚本无法在使用此结构直接循环遍历地图时修改地图的大小。要在使用`for...in`循环时修改地图，请对地图的副本或地图的[map.keys()]数组使用该循环。

如果脚本使用循环结果初始化使用 [var]或[varip]声明的变量，则循环会在*第一次*迭代后停止，即使标头的条件允许更多次迭代。与其直接使用此结构的结果初始化变量，不如先声明变量，然后使用[:=]将其更新为结果。或者，将循环移至[声明函数]，并使用对该函数的调用来初始化变量。

###### if

If语句定义了在满足表达式条件时必须执行的语句块。

要访问和使用if语句，应在代码的第一行中指定>= 2的Pine Script®语言版本，例如：//@version=6

Pine Script®语言的第四版允许您使用“else if”语法。

通用编码来自：

```js
var_declarationX = if condition
    var_decl_then0
    var_decl_then1
    …
    var_decl_thenN
else if [optional block]
    var_decl_else0
    var_decl_else1
    …
    var_decl_elseN
else
    var_decl_else0
    var_decl_else1
    …
    var_decl_elseN
    return_expression_else
```

**var_declarationX** - 此变量获取if语句的值

**condition** — 如果条件为true，则使用block ‘then’中的逻辑(var_decl_then0, var_decl_then1, 等)。

如果条件为false，则使用block 'else'中的逻辑(var_decl_else0, var_decl_else1, 等)。

**return_expression_then**，**return_expression_else** - 模块中的最后一个表达式或者来自块else的表达式将返回语句的最终值。 如果变量的声明在最后，它的值将是结果值。

if语句的返回值的类型取决于return_expression_then和return_expression_else类型（它们的类型必须匹配：从那时起，当你在else块中有一个字符串值时，不可能返回一个整数值）。

```js
//@version=6
indicator("if")
// This code compiles
x = if close > open
    close
else
    open

// This code doesn’t compile
// y = if close > open
//     close
// else
//     "open"
plot(x)
```

可以省略`else`块。在这种情况下，如果条件为false，则会为var_declarationX变量分配一个“empty”值（na、false 或“”）：

```js
//@version=6
indicator("if")
x = if close > open
    close
// If current close > current open, then x = close.
// Otherwise the x = na.
plot(x)
```

可以使用多个“else if”块或根本不使用。“then”、“else if”、“else”块被移动了四个空格：

```js
//@version=6
indicator("if")
x = if open > close
    5
else if high > low
    close
else
    open
plot(x)
```

可以忽略`if`语句的结果值（“var_declarationX=”可以省略）。如果您需要表达式的副作用，它可能很有用，例如在策略交易中：

```js
//@version=6
strategy("if")
if (ta.crossover(high, low))
    strategy.entry("BBandLE", strategy.long, stop=low, oca_name="BollingerBands", oca_type=strategy.oca.cancel, comment="BBandLE")
else
    strategy.cancel(id="BBandLE")
```

If语句可以相互包含：

```js
//@version=6
indicator("if")
float x = na
if close > open
    if close > close[1]
        x := close
    else
        x := close[1]
else
    x := open
plot(x)
```

###### import

用于将外部[library()]加载到脚本中并将其函数绑定到命名空间。导入脚本可以是指标、策略或其他库。库必须先发布（私密或公开），然后才能导入。

```
import {username}/{libraryName}/{libraryVersion} as {alias}
```

参数

**username (literal string)** 脚本库作者的用户名。

**libraryName (literal string)** 导入脚本库的名称，对应于作者在其库脚本中使用的`title`参数。

**libraryVersion (literal int)** 导入脚本库的版本号。

**alias (literal string)** 用作命名空间来引用库函数的非数字标识符。可选。默认值是`libraryName`字符串。

```js
//@version=6
indicator("num_methods import")
// Import the first version of the username’s "num_methods" library and assign it to the "m" namespace",
import username/num_methods/1 as m
// Call the “sinh()” function from the imported library
y = m.sinh(3.14)
// Plot value returned by the "sinh()" function",
plot(y)
```

允许使用替换内置命名空间的别名，例如math.*或strategy.*，但如果脚本库包含隐藏 Pine Script®内置函数的函数名称，则内置函数将不可用。同一版本的脚本库只能导入一次。 每个导入的脚本库别名必须不同。调用脚本库函数时，不允许将其参数转换为其声明类型以外的类型。import语句不能使用“as”或“import”作为`username`、`libraryName` 或`alias`标识符。

###### method

此关键字用于为函数声明添加前缀，表明可以通过将其名称附加到其第一个参数类型的变量，并省略第一个参数来使用点表示法调用它。或者，声明为方法的函数，也可以像普通的用户定义函数一样被调用。在这种情况下，必须为其第一个参数提供一个参数。

方法声明的第一个参数必须明确类型化。

```
[export] method <functionName>(<paramType> <paramName> [= <defaultValue>], …) =>
    <functionBlock>
```

```js
//@version=6
indicator("")

var prices = array.new<float>()

//@function Pushes a new value into the array and removes the first one if the resulting array is greater than `maxSize`. Can be used as a method.
method maintainArray(array<float> id, maxSize, value) =>
    id.push(value)
    if id.size() > maxSize
        id.shift()

prices.maintainArray(50, close)
// The method can also be called like a function, without using dot notation.
// In this case an argument must be supplied for its first parameter.
// maintainArray(prices, 50, close)

// This calls the `array.avg()` built-in using dot notation with the `prices` array.
// It is possible because built-in functions belonging to some namespaces that are a special Pine type
// can be invoked with method notation when the function's first parameter is an ID of that type.
// Those namespaces are: `array`, `matrix`, `line`, `linefill`, `label`, `box`, and `table`.
plot(prices.avg())
```

###### not

逻辑求反(NOT)。 适用于布尔表达式。

```
not expr1
```

> 返回值
>
> 布尔值，或一系列布尔值。
>

###### or

逻辑 OR。适用于布尔表达式。

```
expr1 or expr2
```

返回值

布尔值，或一系列布尔值。

如果`expr1`计算结果为`true`，则`or`运算符将返回`true`而不计算`expr2`。

###### switch

switch运算符根据条件和表达式的值将控制权转移到几个语句之一

```
[variable_declaration = ] switch expression
    value1 => local_block
    value2 => local_block
    …
    => default_local_block

[variable_declaration = ] switch
    condition1 => local_block
    condition2 => local_block
    …
    => default_local_block
```

带表达式的switch：

```js
//@version=6
indicator("Switch using an expression")

string i_maType = input.string("EMA", "MA type", options = ["EMA", "SMA", "RMA", "WMA"`

float ma = switch i_maType
    "EMA" => ta.ema(close, 10)
    "SMA" => ta.sma(close, 10)
    "RMA" => ta.rma(close, 10)
    // Default used when the three first cases do not match.
    => ta.wma(close, 10)

plot(ma)
```

不带表达式的switch：

```js
//@version=6
strategy("Switch without an expression", overlay = true)

bool longCondition  = ta.crossover( ta.sma(close, 14), ta.sma(close, 28))
bool shortCondition = ta.crossunder(ta.sma(close, 14), ta.sma(close, 28))

switch
    longCondition  => strategy.entry("Long ID", strategy.long)
    shortCondition => strategy.entry("Short ID", strategy.short)
```

返回值

执行的本地语句块中最后一个表达式的值。

> 只能执行`local_block`实例或`default_local_block`之一。`default_local_block`单独与`=>`代币一起引入，并且仅当前面的块均未执行时才执行。如果将`switch`语句的结果分配给变量且未指定`default_local_block`，则在未执行`local_block`的情况下，该语句将返回`na`。 将`switch`语句的结果分配给变量时，所有`local_block`实例必须返回相同类型的值。
>

###### type

此关字允许声明用户定义类型 (UDT)，脚本可以从中实例化对象。UDT是复合类型，包含任意数量的任何内置或用户定义类型的字段，包括定义的UDT本身。定义UDT的语法是：

```
[export ]type <UDT_identifier>
    [varip ]<field_type> <field_name> [= <value>]
    …
```

一旦定义了UDT，脚本就可以使用`UDT_identifier.new()`构造从中实例化对象。创建新类型实例时，生成的对象的字段将使用UDT定义中的默认值进行初始化。任何没有指定默认值的类型字段都将初始化为`na`。或者，用户可以在`*.new()`方法中将初始值作为参数传递，以覆盖类型的默认值。例如，`newFooObject = foo.new(x = true)`将新的`foo`对象分配给`newFooObject` 变量，其`x`字段使用`true`值进行初始化。

字段声明可以包含[varip]关键字，在这种情况下，字段值在同一根K线上的连续脚本迭代之间保持不变。

有关详细信息，请参阅用户手册中关于[定义 UDT]和[使用对象]的部分。

脚本库可以导出UDT。请参阅我们的用户手册的[脚本库]页面，了解更多信息。

```js
//@version=6
indicator("Multi Time Period Chart", overlay = true)

timeframeInput = input.timeframe("1D")

type bar
    float o = open
    float h = high
    float l = low
    float c = close
    int   t = time

drawBox(bar b, right) =>
    color boxColor = b.c >= b.o ? color.green : color.red
    box.new(b.t, b.h, right, b.l, boxColor, xloc = xloc.bar_time, bgcolor = color.new(boxColor, 90))

updateBox(box boxId, bar b) =>
    color boxColor = b.c >= b.o ? color.green : color.red
    box.set_border_color(boxId, boxColor)
    box.set_bgcolor(boxId, color.new(boxColor, 90))
    box.set_top(boxId, b.h)
    box.set_bottom(boxId, b.l)
    box.set_right(boxId, time)

secBar = request.security(syminfo.tickerid, timeframeInput, bar.new())

if not na(secBar)
    // To avoid a runtime error, only process data when an object exists.
    if not barstate.islast
        if timeframe.change(timeframeInput)
            // On historical bars, draw a new box in the past when the HTF closes.
            drawBox(secBar, time[1`
    else
        var box lastBox = na
        if na(lastBox) or timeframe.change(timeframeInput)
            // On the last bar, only draw a new current box the first time we get there or when HTF changes.
            lastBox := drawBox(secBar, time)
        else
            // On other chart updates, use setters to modify the current box.
            updateBox(lastBox, secBar)
```

###### var

**var**是用于分配和一次性初始化变量的关键字。

通常，不包含关键字var的变量赋值语法会导致每次更新数据时都会覆盖变量的值。 与此相反，当使用关键字var分配变量时，尽管数据更新，它们仍可以“保持状态”，只有在满足if-expressions中的条件时才更改它。

```
var variable_name = expression
```

哪里：

**variable_name** - Pine Script®中允许的用户变量的任何名称（可以包含大写和小写拉丁字符、数字和下划线 (_)，但不能以数字开头）。

**expression** - 任何算术表达式，就像定义常规变量一样。 将计算表达式并将其分配给变量一次。

```
//@version=6
indicator("Var keyword example")
var a = close
var b = 0.0
var c = 0.0
var green_bars_count = 0
if close > open
    var x = close
    b := x
    green_bars_count := green_bars_count + 1
    if green_bars_count >= 10
        var y = close
        c := y
plot(a)
plot(b)
plot(c)
```

变量 'a' 保持系列中每根K线的第一根K线的收盘价。

变量 'b' 保持系列中第一根“绿色”K线的收盘价。

变量 'c' 保持系列中第十根“绿色”K线的收盘价。

###### varip

**varip**(var intrabar persist)是用于对用户定义的[type]的变量或字段进行赋值和一次性初始化的关键字。它与[var]关键字类似，但使用[varip]声明的变量和字段在同一根K线上的脚本执行之间保留其值。

```
varip [<variable_type> ]<variable_name> = <expression>

[export ]type <UDT_identifier>
    varip <field_type> <field_name> [= <value>]
```

哪里：

**variable_type** - 可选的基本类型（[int]、[float]、[bool]、[color]、[string]）或用户定义的类型，或者这些类型之一的数组或矩阵。特殊类型与此关键字不兼容。

**variable_name** - [有效标识符]。该变量也可以是从UDT创建的对象。

**expression** - 任何算术表达式，就像定义常规变量一样。表达式将仅在第一根K线上计算一次并分配给变量。

**UDT_identifier, field_type, field_name, value** - 与用户定义类型相关的构造，如[type]部分中所述。

```js
//@version=6
indicator("varip")
varip int v = -1
v := v + 1
plot(v)
```

对[var]，`v`将等于[bar_index]的值。在历史K线上，脚本仅对每个图表K线计算一次，`v`的值与[var]的值相同。然而，在实时K线上，脚本将计算每个新图表更新上的表达式，产生不同的结果。

```js
//@version=6
indicator("varip with types")
type barData
    int index = -1
    varip int ticks = -1

var currBar = barData.new()
currBar.index += 1
currBar.ticks += 1

// Will be equal to bar_index on all bars
plot(currBar.index)
// In real time, will increment per every tick on the chart
plot(currBar.ticks)
```

对`index`和`ticks`字段应用相同的[+=]操作会产生不同的实时值，因为`ticks`在每次图表更新时都会增加，而`index`每根K线只增加一次。请注意`currBar`对象不使用[varip]关键字。对象的`ticks`字段可以在每个tick上递增，但引用本身定义一次，然后保持不变。如果我们使用[varip]声明`currBar`，则`index`的行为将保持不变，因为虽然对类型实例的引用在图表更新之间会持续存在，但对象的`index`字段不会。

备注

当使用[varip]声明策略中可能在每个历史图表K线上执行多次的变量时，这些变量的值将在同一根K线上的脚本连续迭代中保留。

[varip]的作用，消除了在同一根K线上每次连续执行脚本之前变量的[回滚]。

###### while

创建一个条件控制循环，其局部代码块在条件表达式的值保持为`true`时重复执行。当条件表达式的值变为`false`时，循环迭代结束。

```
[variables = | :=] while condition
    statements | continue | break
    return_expression
```

**variables (return_expression type)** - 可选。一个变量或元组，用于保存循环终止后最后一次求值`return_expression`的值或引用。脚本只能在结果类型不为“void”时将循环返回的结果赋值给变量。如果循环条件阻止迭代，或者没有迭代求值`return_expression`，则变量的赋值或引用为`na`；如果返回类型为“bool”，则为`false`。

**condition (series bool)** - 控制循环迭代的条件表达式。如果为`true`，则脚本执行新的迭代。如果为`false`，则脚本退出循环而不执行新的迭代。

**statements** - 循环体内的代码语句和表达式，即循环头下方缩进的代码块。

**return_expression (any type)** - 循环主体中的最后一个表达式或语句。循环在最后一次迭代后返回此代码的结果。如果循环因`continue`或`break`语句而提前停止，则返回的值或引用是执行此代码的最新一次迭代的值或引用。要使用循环的返回结果，请将其赋值给变量或元组。

**continue** - 循环特定的关键字，指示脚本跳过当前循环迭代的剩余部分并继续下一次迭代。

**break** - 循环特定的关键字，提示脚本停止当前迭代并完全退出循环。

```js
//@version=6
indicator("`while` demo")

//@variable The number for which to calculate the factorial (N!).
//          The factorial is the product of all integers from 1 to `n`, with the exception (0! == 1).
int n = input.int(10, "N", 0)

//@variable The current value to multiply in the factorial calculation. 
var int counter = n
//@variable The factorial value.
var int factorial = 1

if barstate.isfirst
    // Repeatedly multiply `factorial` by `counter` and decrease the `counter` value by 1.
    // The loop ends after the value of `counter` becomes 0.  
    while counter > 0
        factorial *= counter
        counter   -= 1

plot(factorial, "N!")
```

如果脚本使用循环结果初始化使用 [var]或[varip]声明的变量，则循环会在*第一次*迭代后停止，即使标头的条件允许更多次迭代。与其直接使用此结构的结果初始化变量，不如先声明变量，然后使用[:=]将其更新为结果。或者，将循环移至[声明函数]，并使用对该函数的调用来初始化变量。

请参阅我们的用户手册的[循环]页面，了解有关循环及其工作原理的更多信息。

#### 类型

###### array

用于显式声明变量或参数的"array"类型的关键字。可以使用[array.new()]、[array.from()]函数创建阵列对象（或ID）。

```js
//@version=6
indicator("array", overlay=true)
array<float> a = na
a := array.new<float>(1, close)
plot(array.get(a, 0))
```

阵列对象总是“系列”形式。

###### bool

用于明确声明变量或参数的“bool”（布尔）类型的关键字。“Bool”变量可以具有值`true`或`false`。

```js
//@version=6
indicator("bool")
bool b = true    // Same as `b = true`
plot(b ? open : close)
```

在变量声明中明确提及类型是可选的。在用户手册页面的[类型系统]中了解有关Pine Script®类型的更多信息。

###### box

用于显式声明变量或参数的"box"类型的关键字。可以使用[box.new()]函数创建box对象（或ID）。

```js
//@version=6
indicator("box")
// Empty `box1` box ID.
var box box1 = na
// `box` type is unnecessary because `box.new()` returns a "box" type.
var box2 = box.new(na, na, na, na)
box3 = box.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time)
```

备注

box对象总是"series"形式。

###### chart.point

用于将变量或参数的类型显式声明为`chart.point`的关键字。脚本可以使用[chart.point.from_time()]、[chart.point.from_index()]、[chart.point.now()]和[chart.point.new()]函数生成`chart.point`实例。

字段

**index (series int)** 点的x坐标，表示为K线索引值。

**time (series int)** 点的x坐标，表示为UNIX时间值。

**price (series float)** 点的y坐标。

###### color

用于显式声明变量或参数的"color"类型的关键字。

```js
//@version=6
indicator("color", overlay = true)

color textColor = color.green
color labelColor = #FF000080 // Red color (FF0000) with 50% transparency (80 which is half of FF).
if barstate.islastconfirmedhistory
    label.new(bar_index, high, text = "Label", color = labelColor, textcolor = textColor)

// When declaring variables with color literals, built-in constants(color.green) or functions (color.new(), color.rgb()), the "color" keyword for the type can be omitted.
c = color.rgb(0,255,0,0)
plot(close, color = c)
```

颜色文字具有以下格式：#RRGGBB 或 #RRGGBBAA。 字母对代表00到FF的十六进制值（十进制的0到255），其中RR、GG和BB对是颜色的红色、绿色和蓝色分量的值。AA是颜色透明度（或alpha分量）的可选值，其中00不可见，FF不透明。 当没有提供AA对时，使用FF。十六进制字母可以是大写或小写。

在变量声明中明确提及类型是可选的，除非使用`na`进行初始化。要了解有关Pine Script®类型的更多信息，请参阅[类型系统]上的用户手册页面。

###### const

`const`关键字显式地将“const”类型限定符分配给变量和非导出函数的参数。带有“const”限定符参考值的变量和参数在编译时建立，在脚本执行中永远不会改变。

在变量声明中，编译器通常可以根据分配给变量的值自动推断限定类型，并且可以在必要时自动将变量的限定符更改为更强的限定符。类型限定符层次结构为“const”<“input”<“simple”<“series”，其中“const”最弱。

使用`const`关键字显式声明变量会将类型限定符限制为“const”，这意味着该变量不能接受具有更强限定符的值（例如“input”），分配给变量的值也不能在脚本执行的任何时刻发生变化。

当使用此关键字指定类型限定符时，还必须使用type关键字来声明允许的类型。

```
[method ]<functionName>`const <paramType> ]<paramName>[ = <defaultValue>`

[var/varip ]const <variableType> <variableName> = <variableValue>
```

```js
//@version=6
indicator("custom plot title")

//@function Concatenates two "const string" values.
concatStrings(const string x, const string y) =>
    const string result = x + y

//@variable The title of the plot.
const string myTitle = concatStrings("My ", "Plot")

plot(close, myTitle)
```

```js
//@version=6
indicator("can't assign input to const")

//@variable A variable declared as "const float" that attempts to assign the result of `input.float()` as its value.
//          This declaration causes an error. The "input float" qualified type is stronger than "const float".
const float myVar = input.float(2.0)

plot(myVar)
```

要了解更多信息，请参阅我们的用户手册中有关[类型限定符]的部分。

###### float

用于显式声明变量或参数的“float”（浮点）类型的关键字。

```js
//@version=6
indicator("float")
float f = 3.14    // Same as `f = 3.14`
f := na
plot(f)
```

在变量声明中明确提及类型是可选的，除非使用`na`进行初始化。要了解有关Pine Script®类型的更多信息，请参阅[类型系统]上的用户手册页面。

###### footprint

一个关键字，用于显式声明变量或参数的类型为`footprint`。脚本通过调用[request.footprint()]函数创建`footprint`类型的对象。脚本可以使用此类型的ID和内置的`footprint.*()`函数来检索[成交量轨迹]数据，包括足迹行、分类成交量总和以及成交量增量。

###### int

用于显式声明变量或参数的“int”（整数）类型的关键字。

```js
//@version=6
indicator("int")
int i = 14    // Same as `i = 14`
i := na
plot(i)
```

在变量声明中明确提及类型是可选的，除非使用`na`进行初始化。要了解有关Pine Script®类型的更多信息，请参阅[类型系统]上的用户手册页面。

###### label

用于显式声明变量或参数的"label"类型的关键字。可以使用[label.new()]函数创建标签对象（或ID）。

```js
//@version=6
indicator("label")
// Empty `label1` label ID.
var label label1 = na
// `label` type is unnecessary because `label.new()` returns "label" type.
var label2 = label.new(na, na, na)
if barstate.islastconfirmedhistory
    label3 = label.new(bar_index, high, text = "label3 text")
```

标签对象总是"series"形式。

###### line

用于显式声明变量或参数的"line"类型的关键字。可以使用[line.new()]函数创建线条对象（或ID）。

```js
//@version=6
indicator("line")
// Empty `line1` line ID.
var line line1 = na
// `line` type is unnecessary because `line.new()` returns "line" type.
var line2 = line.new(na, na, na, na)
line3 = line.new(bar_index - 1, high, bar_index, high, extend = extend.right)
```

线条对象总是"series"形式。

###### linefill

用于显式声明变量或参数的“linefill”类型的关键字。可以使用[linefill.new()]函数创建行linefill对象（或ID）。

```js
//@version=6
indicator("linefill", overlay=true)
// Empty `linefill1` line ID.
var linefill linefill1 = na
// `linefill` type is unnecessary because `linefill.new()` returns "linefill" type.
var linefill2 = linefill.new(na, na, na)

if barstate.islastconfirmedhistory
    line1 = line.new(bar_index - 10, high+1, bar_index, high+1, extend = extend.right)
    line2 = line.new(bar_index - 10, low+1, bar_index, low+1, extend = extend.right)
    linefill3 = linefill.new(line1, line2, color = color.new(color.green, 80))
```

Linefill对象始终是"series"形式。

###### map

用于显式声明变量或参数的“map”类型的关键字。可以使用 [map.new()]函数创建map对象（或 ID）。

```js
//@version=6
indicator("map", overlay=true)
map<int, float> a = na
a := map.new<int, float>()
a.put(bar_index, close)
label.new(bar_index, a.get(bar_index), "Current close")
```

Map地图对象始终为[series]形式。

###### matrix

用于显式声明变量或参数的"matrix"类型的关键字。可以使用[matrix.new()] 函数创建矩阵对象（或 ID）。

```js
//@version=6
indicator("matrix example")

// Create `m1` matrix of `int` type.
matrix<int> m1 = matrix.new<int>(2, 3, 0)

// `matrix<int>` is unnecessary because the `matrix.new<int>()` function returns an `int` type matrix object.
m2 = matrix.new<int>(2, 3, 0)

// Display matrix using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m2))
```

矩阵对象总是“系列”形式。

###### polyline

用于将变量或参数的类型显式声明为`polyline`的关键字。脚本可以使用[polyline.new()]函数生成`polyline`实例。

###### series

`series`关键字显式地将“series”类型限定符分配给变量和函数参数。使用“series”限定符的变量和参数，可以引用在脚本执行过程中发生变化的值。

在声明库导出函数的参数时，通常不需要显式使用`series`关键字，因为编译器通常可以自动检测参数是否与"series"或"simple"限定值兼容。默认情况下，所有导出的函数参数都尽可能限定为"series"。

在变量声明中，编译器通常可以根据分配给变量的值自动推断限定类型，并且可以在必要时自动将变量的限定符更改为更强的限定符。类型限定符层次结构为“const”<“input”<“simple”<“series”，其中“series”最强。

使用`series`关键字显式声明变量会将类型限定符限制为“series”，这意味着脚本无法将其值传递给需要具有较弱限定符（“const”、“input”或"simple"）。

当使用此关键字指定类型限定符时，还必须使用type关键字来声明允许的类型。

```
export [method ]<functionName>`[series ]<paramType>] <paramName>[ = <defaultValue>`

[method ]<functionName>`series <paramType> ]<paramName>[ = <defaultValue>`

[var/varip ]series <variableType> <variableName> = <variableValue>
```

```js
//@version=6
//@description A library with custom functions.
library("CustomFunctions", overlay = true)

//@function Finds the highest `source` value over `length` bars, filtered by the `cond` condition.
export conditionalHighest(series float source, series bool cond, series int length) =>
    //@variable The highest `source` value from when the `cond` was `true` over `length` bars.
    series float result = na
    // Loop to find the highest value.
    for i = 0 to length - 1
        if cond[i]
            value   = source[i]
            result := math.max(nz(result, value), value)
    // Return the `result`.
    result

//@variable Is `true` once every five bars.
series bool condition = bar_index % 5 == 0

//@variable The highest `close` value from every fifth bar over the last 100 bars.
series float hiValue = conditionalHighest(close, condition, 100)

plot(hiValue)
bgcolor(condition ? color.new(color.teal, 80) : na)
```

```js
//@version=6
indicator("series variable not allowed")

//@variable A variable declared as "series int" with a value of 5.
series int myVar = 5

// This call causes an error.
// The `histbase` accepts "input int/float". It can't accept the stronger "series int" qualified type.
plot(close, style = plot.style_histogram, histbase = myVar)
```

要了解更多信息，请参阅我们的用户手册中有关[类型限定符]的部分。

###### simple

`simple`关键字显式地将“simple”类型限定符分配给变量和函数参数。使用“simple”限定符的变量和参数可以引用在脚本执行开始时建立的值，这些值以后不会更改。

要将库导出函数中的参数限制为仅允许具有"simple"或更弱类型限定符的值，通常需要在声明参数时使用`simple`关键字，因为默认情况下库会自动将所有参数限定为"series"。显式限制函数接受"simple"参数还允许它们在某些情况下返回"simple"值，具体取决于它们执行的操作，从而使它们可以与不允许"series"参数的内置函数的参数一起使用。

在变量声明中，编译器通常可以根据分配给变量的值自动推断限定类型，并且可以在必要时自动将变量的限定符更改为更强的限定符。类型限定符层次结构为“const”<“input”<“simple”<“series”，其中“simple”比“input”和“const”更强。

使用`simple`关键字显式声明变量会将类型限定符限制为“simple”，这意味着脚本无法将其值传递给需要具有较弱限定符（“const”或“input”）的值的任何变量或函数参数。此外，不能将"series"值分配给使用`simple`关键字显式声明的变量。

当使用此关键字指定类型限定符时，还必须使用type关键字来声明允许的类型。

```
export [method ]<functionName>`[simple ]<paramType>] <paramName>[ = <defaultValue>`

[method ]<functionName>`simple <paramType> ]<paramName>[ = <defaultValue>`

[var/varip ]simple <variableType> <variableName> = <variableValue></variableValue>
```

```js
//@version=6
//@description A library with custom functions.
library("CustomFunctions", overlay = true)

//@function         Calculates the length values for a ribbon of four EMAs by multiplying the `baseLength`.
//@param baseLength The initial EMA length. Requires "simple int" because you can't use "series int" in `ta.ema()`.
//@returns          A tuple of length values.
export ribbonLengths(simple int baseLength) =>
    simple int length1 = baseLength
    simple int length2 = baseLength * 2
    simple int length3 = baseLength * 3
    simple int length4 = baseLength * 4
    [length1, length2, length3, length4]

// Get a tuple of "simple int" length values.
[len1, len2, len3, len4] = ribbonLengths(14)

// Plot four EMAs using the values from the tuple.
plot(ta.ema(close, len1), "EMA 1", color = color.red)
plot(ta.ema(close, len2), "EMA 1", color = color.orange)
plot(ta.ema(close, len3), "EMA 1", color = color.green)
plot(ta.ema(close, len4), "EMA 1", color = color.blue)
```

```js
//@version=6
indicator("can't change simple to series")

//@variable A variable declared as "simple float" with a value of 5.0.
simple float myVar = 5.0

// This reassignment causes an error.
// The `close` variable returns a "series float" value. Since `myVar` is restricted to "simple" values, it cannot
// change its qualifier to "series".
myVar := close

plot(myVar)
```

要了解更多信息，请参阅我们的用户手册中有关[类型限定符]的部分

###### string

用于显式声明变量或参数的"string"类型的关键字

```js
//@version=6
indicator("string")
string s = "Hello World!"    // Same as `s = "Hello world!"`
// string s = na // same as ""
plot(na, title=s)
```

在变量声明中明确提及类型是可选的，除非使用`na`进行初始化。要了解有关Pine Script®类型的更多信息，请参阅[类型系统]上的用户手册页面。

###### table

用于显式声明变量或参数的"table"类型的关键字。可以使用[table.new()]函数创建表格对象（或ID）。

```js
//@version=6
indicator("table")
// Empty `table1` table ID.
var table table1 = na
// `table` type is unnecessary because `table.new()` returns "table" type.
var table2 = table.new(position.top_left, na, na)

if barstate.islastconfirmedhistory
    var table3 = table.new(position = position.top_right, columns = 1, rows = 1, bgcolor = color.yellow, border_width = 1)
    table.cell(table_id = table3, column = 0, row = 0, text = "table3 text")
```

表格对象总是"series"形式。

###### volume_row

一个关键字，明确地将变量或参数的类型声明为`volume_row`。所有从[footprint]对象检索行数据的`footprint.*()`函数都会返回`volume_row`类型的ID。脚本可以使用这种类型的ID和内置的`volume_row.*()`函数来检索有关所请求的足迹行的信息，包括该行的价格水平、分类成交量、成交量变化和不平衡情况。

### 运算子

##### -

减法或一元负号。 适用于数值表达式。

```js
expr1 - expr2
```

返回值

返回整数或浮点值，或一系列值：

二进制`-`返回expr1减expr2。

一元`-`返回expr的负值。

> 您可以使用带数字的算术运算符以及变量数列。 在使用数列的情况下，操作符应用于元素。
>

##### -=

减法指派。适用于数值表达式

```
expr1 -= expr2
```

```js
//@version=6
indicator("-=")
// Equals to expr1 = expr1 - expr2.
a = 2
b = 3
a -= b
// Result: a = -1.
plot(a)
```

> 返回值
>
> 整数或浮点值，或一系列值。
>

##### :=

重新分配运算符。它用于为先前声明的变量分配新值。

```
<var_name> := <new_value>
```

```js
//@version=6
indicator("My script")

myVar = 10

if close > open
    // Modifies the existing global scope `myVar` variable by changing its value from 10 to 20.
    myVar := 20
    // Creates a new `myVar` variable local to the `if` condition and unreachable from the global scope.
    // Does not affect the `myVar` declared in global scope.
    myVar = 30

plot(myVar)
```

##### !=

不平等运营商。返回`true`如果操作数不相等，否则为`false`。

该操作员与所有值类型兼容，包括“ int”，“ float”，“ bool”，“ color”和“ string”。操作员还可以比较两行或标签ID。

```
expr1 != expr2
```

返回值

布尔值，或一系列布尔值。

备注

该运算符将“浮点”操作数四舍五入为九位小数。

##### ?:

三元条件运算符。

```
expr1 ? expr2 : expr3
```

```js
//@version=6
indicator("?:")
// Draw circles at the bars where open crosses close
s2 = ta.cross(open, close) ? math.avg(open,close) : na
plot(s2, style=plot.style_circles, linewidth=2, color=color.red)

// Combination of ?: operators for 'switch'-like logic
c = timeframe.isintraday ? color.red : timeframe.isdaily ? color.green : timeframe.isweekly ? color.blue : color.gray
plot(hl2, color=c)
```

> 返回值
>
> 如果expr1被评估为true，则expr2，否则为expr3。 零值(0和NaN，+ Infinity，-Infinity)被视为false，其他值皆为true。
>

如果您不需要，请使用`na`作为“else”分支。

您可以结合使用两个或多个[?:]运算符，以实现类似于“switch”的语句（请参见上面的示例）。

您可以使用带数字的算术运算符以及变量数列。 在使用数列的情况下，操作符应用于元素。

##### []

系列下标。 提供对expr1系列的以前值的访问。 expr2是过去k线的数目，必须是数值。 浮动将被向下舍入。

```
expr1[expr2]
```

```js
//@version=6
indicator("[]")
// [] can be used to "save" variable value between bars
a = 0.0 // declare `a`
a := a[1] // immediately set current value to the same as previous. `na` in the beginning of history
if high == low // if some condition - change `a` value to another
    a := low
plot(a)
```

> 返回值
>
> 一系列数值。
>

##### *

乘法。适用于数值表达式。

```
expr1 * expr2
```

> 返回值
>
> 整数或浮点值，或一系列值。
>

##### *=

乘法指派。适用于数值表达式。

```
expr1 *= expr2
```

```js
//@version=6
indicator("*=")
// Equals to expr1 = expr1 * expr2.
a = 2
b = 3
a *= b
// Result: a = 6.
plot(a)
```

> 返回值
>
> 整数或浮点值，或一系列值。
>

##### /

除法。适用于数值表达式。

```
expr1 / expr2
```

返回值

整数或浮点值，或一系列值。

##### /=

除法指派。适用于数值表达式。

```
expr1 /= expr2
```

```js
//@version=6
indicator("/=")
// Equals to expr1 = expr1 / expr2.
float a = 3.0
b = 3
a /= b
// Result: a = 1.
plot(a)
```

> 返回值
>
> 整数或浮点值，或一系列值。
>

##### %

模数(整数余数)。 适用于数值表达式。

```
expr1 % expr2
```

返回值

整数或浮点值，或一系列值。

备注

在Pine Script®中，计算整数余数时，商数会被截断，即向最低绝对值舍入。结果值将与股息具有相同的符号。

示例：`-1 % 9 = -1 - 9 * int(-1/9) = -1 - 9 * int(-0.111) = -1 - 9 * 0 = -1.`

##### %=

模数指派。适用于数值表达式。

```
expr1 %= expr2
```

```js
//@version=6
indicator("%=")
// Equals to expr1 = expr1 % expr2.
a = 3
b = 3
a %= b
// Result: a = 0.
plot(a)
```

> 返回值
>
> 整数或浮点值，或一系列值。
>

##### +

添加或一元正号。适用于数值表达式或字符串。

```
expr1 + expr2
```

返回值

字符串的二进制`+`返回expr1和expr2的合并

数字返回整数或浮点值，或一系列值：

二进制`+`返回expr1加expr2。

一元`+`返回expr （只是为了一元的对称性，而没有添加任何内容 — 运算符的对称性）。

> 您可以使用带数字的算术运算符以及变量数列。 在使用数列的情况下，操作符应用于元素。
>

##### +=

加法指派。适用于数值表达式或字符串

```
expr1 += expr2
```

```js
//@version=6
indicator("+=")
// Equals to expr1 = expr1 + expr2.
a = 2
b = 3
a += b
// Result: a = 5.
plot(a)
```

返回值

对于字符串，返回expr1和expr2的串联。对于数字，返回整数或浮点值，或一系列值

> 您可以使用带数字的算术运算符以及变量数列。 在使用数列的情况下，操作符应用于元素。
>

##### <

小于

适用于数值表达式

```
expr1 < expr2
```

> 返回值
>
> 布尔值，或一系列布尔值
>

##### <=

小于或等于

适用于数值表达式

```
expr1 <= expr2
```

> 返回值
>
> 布尔值，或一系列布尔值。
>

##### =

赋值运算符

为已声明的变量分配初始值或引用。它的意思是“这是一个新变量，并且它以该值开始”。

```
<var_name> := <initial_value>
```

```js
//@version=6
indicator("`=` showcase")
// The following are all valid variable declarations.
i = 1
MS_IN_ONE_MINUTE = 1000 * 60
showPlotInput = input.bool(true, "Show plots")
pHi = ta.pivothigh(5, 5)
plotColor = color.green

plot(pHi, color = plotColor, display = showPlotInput ? display.all : display.none, precision = i)
```

##### ==

平等操作

返回`true`如果操作数被认为相等，否则为`false`。

该操作员与所有值类型兼容，包括“ int”，“ float”，“ bool”，“ color”和“ string”。操作员还可以比较两行或标签ID

```
expr1 == expr2
```

> 返回值
>

> 布尔值，或一系列布尔值。
>

该运算符将“浮点”操作数四舍五入为九位小数。

##### =>

`=>`运算符用于用户定义的函数声明和[switch]语句中。

函数声明语法是：

```
<identifier>`<parameter_name>[=<default_value>]], ...) =>
    <local_block>
    <function_result>
```

<local_block>是零个或多个Pine Script®语句。

<function_result>是一个变量、一个表达式或一个元组。

```js
//@version=6
indicator("=>")
// single-line function
f1(x, y) => x + y
// multi-line function
f2(x, y) =>
    sum = x + y
    sumChange = ta.change(sum, 10)
    // Function automatically returns the last expression used in it
plot(f1(30, 8) + f2(1, 3))
```

##### >

大于

> 适用于数值表达式

```
expr1 > expr2
```

> 返回值
>
> 布尔值，或一系列布尔值
>

##### >=

大于或等于

> 适用于数值表达式

```
expr1 >= expr2
```

返回值:布尔值，或一系列布尔值

### 注释

###### @description

为使用[library()]声明语句的脚本设置自定义描述。随此注释提供的文本将用于发布对话框中预先填写的“描述”字段。

```js
//@version=6
// @description Provides a tool to quickly output a label on the chart.
library("MyLibrary")

// @function Outputs a label with `labelText` on the bar's high.
// @param labelText (series string) The text to display on the label.
// @returns Drawn label.
export drawLabel(string labelText) =>
    label.new(bar_index, high, text = labelText)
```

###### @enum

如果放置在枚举声明上方，它会为枚举添加自定义描述。

Pine编辑器的自动建议会使用此描述，并在用户将鼠标悬停在枚举名称上时显示它。在库脚本中使用时，使用`export`关键字的所有枚举描述，将预先填充发布对话框中的“描述”字段。

```js
//@version=6
indicator("Session highlight", overlay = true)

//@enum       Contains fields with popular timezones as titles.
//@field exch Has an empty string as the title to represent the chart timezone.
enum tz
    utc  = "UTC"
    exch = ""
    ny   = "America/New_York"
    chi  = "America/Chicago"
    lon  = "Europe/London"
    tok  = "Asia/Tokyo"

//@variable The session string.
selectedSession = input.session("1200-1500", "Session")
//@variable The selected timezone. The input's dropdown contains the fields in the `tz` enum.
selectedTimezone = input.enum(tz.utc, "Session Timezone")

//@variable Is `true` if the current bar's time is in the specified session.
bool inSession = false
if not na(time("", selectedSession, str.tostring(selectedTimezone)))
    inSession := true

// Highlight the background when `inSession` is `true`.
bgcolor(inSession ? color.new(color.green, 90) : na, title = "Active session highlight")
```

###### @field

如果放置在[type]或[enum]声明之上，它会为类型/枚举的字段添加自定义描述。

在注释之后，用户应指定字段名称，然后是其描述。

Pine编辑器的自动建议使用此描述，并在用户将鼠标悬停在类型或字段名称上时显示它。当在[library()]脚本中使用时，使用[export]关键字的所有类型的描述，将预先填充发布对话框中的“描述”字段。

```js
//@version=6
indicator("New high over the last 20 bars", overlay = true)

//@type A point on a chart.
//@field index The index of the bar where the point is located, i.e., its `x` coordinate.
//@field price The price where the point is located, i.e., its `y` coordinate.
type Point
    int index
    float price

//@variable If the current `high` is the highest over the last 20 bars, returns a new `Point` instance, `na` otherwise.
Point highest = na

if ta.highestbars(high, 20) == 0
    highest := Point.new(bar_index, high)
    label.new(highest.index, highest.price, str.tostring(highest.price))
```

###### @function

如果放置在函数声明之上，它会添加该函数的自定义描述。

Pine编辑器的自动建议使用此描述，并在用户将鼠标悬停在函数名称上时显示它。

当在[library()]脚本中使用时，使用[export]关键字的所有函数的描述，将预先填充发布对话框中的“描述”字段。

```js
//@version=6
library("MyLibrary")

export drawLabel(string labelText) =>
    label.new(bar_index, high, text = labelText)
```

###### @param

如果放置在函数声明上方，它将添加函数参数的自定义描述。在注释之后，用户应该指定参数名称，然后指定其描述。

Pine编辑器的自动建议使用此描述，并在用户将鼠标悬停在函数名称上时显示它。

当在[library()]脚本中使用时，使用[export]关键字的所有函数的描述，将预先填充发布对话框中的“描述”字段。

```js
//@version=6
library("MyLibrary")

export drawLabel(string labelText) =>
    label.new(bar_index, high, text = labelText)
```

###### @returns

如果放置在函数声明之上，它会添加该函数返回内容的自定义描述。

Pine编辑器的自动建议使用此描述，并在用户将鼠标悬停在函数名称上时显示它。当在[library()]脚本中使用时，使用[export]关键字的所有函数的描述，将预先填充发布对话框中的“描述”字段。

```js
//@version=6
// @description Provides a tool to quickly output a label on the chart.
library("MyLibrary")

// @function Outputs a label with `labelText` on the bar's high.
// @param labelText (series string) The text to display on the label.
// @returns Drawn label.
export drawLabel(string labelText) =>
    label.new(bar_index, high, text = labelText)
```

###### @strategy_alert_message

如果在[strategy()]脚本中使用，它会提供默认消息来预填充警报创建对话框中的“消息”字段。

```
//@version=6
strategy("My strategy", overlay=true, margin_long=100, margin_short=100)
//@strategy_alert_message Strategy alert on symbol {{ticker}}

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    strategy.entry("My Long Entry Id", strategy.long)
strategy.exit("Exit", "My Long Entry Id", profit = 10 / syminfo.mintick, loss = 10 / syminfo.mintick)
```

###### @type

如果放置在类型声明之上，它将添加该类型的自定义描述。

Pine编辑器的自动建议使用此描述，并在用户将鼠标悬停在类型名称上时显示它。当在`library()`脚本中使用时，使用`export`关键字的所有类型的描述，将预先填充发布对话框中的“描述”字段。

```js
//@version=6
indicator("New high over the last 20 bars", overlay = true)

//@type A point on a chart.
//@field index The index of the bar where the point is located, i.e., its `x` coordinate.
//@field price The price where the point is located, i.e., its `y` coordinate.
type Point
    int index
    float price

//@variable If the current `high` is the highest over the last 20 bars, returns a new `Point` instance, `na` otherwise.
Point highest = na

if ta.highestbars(high, 20) == 0
    highest := Point.new(bar_index, high)
    label.new(highest.index, highest.price, str.tostring(highest.price))
```

###### @variable

如果放置在变量声明之上，它会添加变量的自定义描述。

Pine编辑器的自动建议使用此描述，并在用户将鼠标悬停在变量名称上时显示它。

```js
//@version=6
indicator("New high over the last 20 bars", overlay = true)

//@type A point on a chart.
//@field index The index of the bar where the point is located, i.e., its `x` coordinate.
//@field price The price where the point is located, i.e., its `y` coordinate.
type Point
    int index
    float price

//@variable If the current `high` is the highest over the last 20 bars, returns a new `Point` instance, `na` otherwise.
Point highest = na

if ta.highestbars(high, 20) == 0
    highest := Point.new(bar_index, high)
    label.new(highest.index, highest.price, str.tostring(highest.price))
```

###### @version=

指定脚本将使用的PineScript™版本。

此注释中的数字不应与脚本的修订号混淆，该修订号会在每次保存的代码更改时更新

```js
//@version=6
indicator("Pine v6 Indicator")
plot(close)
```

```js
//This indicator has no version annotation, so it will try to use v1.
//Pine Script® v1 has no function named `indicator()`, so the script will not compile.
indicator("Pine v1 Indicator")
plot(close)
```

> 应始终指定版本。
>
> 否则，出于兼容性原因，脚本将使用PineScript™ v1进行编译，该版本缺乏大部分较新的功能，并且必然会造成混乱。
>
> 此注释可以位于脚本中的任何位置，但我们建议将其放置在代码的顶部以提高可读性