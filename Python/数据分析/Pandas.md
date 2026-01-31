# Pandas 库

##### Pandas 安装

```
pip install pandas
```

版本查看

##### `pandas.__version__`

```
>>> import pandas
>>> pandas.__version__  # 查看版本
'1.1.5'
```

## 数据结构 Series

类似于一维数组或列表，是由一组数据以及与之相关的数据标签（索引）构成。Series 可以看作是 DataFrame 中的一列，也可以是单独存在的一维数据结构。

![img](https://www.runoob.com/wp-content/uploads/2023/12/628084-20201205212241597-1156923446.png)

使用Pandas 库来创建一个 Series 对象，并且可以为其指定索引（Index）、名称（Name）以及值（Values）：

![img](https://www.runoob.com/wp-content/uploads/2021/04/1_fgFKkClAfRMEsUtJvDtXAQ.png)

```python
import pandas as pd

# 创建一个Series对象，指定名称为'A'，值分别为1, 2, 3, 4
# 默认索引为0, 1, 2, 3
series = pd.Series([1, 2, 3, 4], name='A')

# 显示Series对象
print(series)

# 如果你想要显式地设置索引，可以这样做：
custom_index = [1, 2, 3, 4]  # 自定义索引
series_with_index = pd.Series([1, 2, 3, 4], index=custom_index, name='A')

# 显示带有自定义索引的Series对象
print(series_with_index)
```

###### pandas.Series()

```
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```

- `data`：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
- `index`：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `dtype`：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 `np.int64`、`np.float64` 等。如果不提供此参数，则根据数据自动推断数据类型。
- `name`：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
- `copy`：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
- `fastpath`：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。

```python
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar)
```

索引值

```python
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar[1])
```

使用 key/value 对象，类似字典来创建 Series

```python
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites)

print(myvar)
```

##### Series 方法

| **方法名称**                 | **功能描述**                                           |
| :--------------------------- | :----------------------------------------------------- |
| `index`                      | 获取 Series 的索引                                     |
| `values`                     | 获取 Series 的数据部分（返回 NumPy 数组）              |
| `head(n)`                    | 返回 Series 的前 n 行（默认为 5）                      |
| `tail(n)`                    | 返回 Series 的后 n 行（默认为 5）                      |
| `dtype`                      | 返回 Series 中数据的类型                               |
| `shape`                      | 返回 Series 的形状（行数）                             |
| `describe()`                 | 返回 Series 的统计描述（如均值、标准差、最小值等）     |
| `isnull()`                   | 返回一个布尔 Series，表示每个元素是否为 NaN            |
| `notnull()`                  | 返回一个布尔 Series，表示每个元素是否不是 NaN          |
| `unique()`                   | 返回 Series 中的唯一值（去重）                         |
| `value_counts()`             | 返回 Series 中每个唯一值的出现次数                     |
| `map(func)`                  | 将指定函数应用于 Series 中的每个元素                   |
| `apply(func)`                | 将指定函数应用于 Series 中的每个元素，常用于自定义操作 |
| `astype(dtype)`              | 将 Series 转换为指定的类型                             |
| `sort_values()`              | 对 Series 中的元素进行排序（按值排序）                 |
| `sort_index()`               | 对 Series 的索引进行排序                               |
| `dropna()`                   | 删除 Series 中的缺失值（NaN）                          |
| `fillna(value)`              | 填充 Series 中的缺失值（NaN）                          |
| `replace(to_replace, value)` | 替换 Series 中指定的值                                 |
| `cumsum()`                   | 返回 Series 的累计求和                                 |
| `cumprod()`                  | 返回 Series 的累计乘积                                 |
| `shift(periods)`             | 将 Series 中的元素按指定的步数进行位移                 |
| `rank()`                     | 返回 Series 中元素的排名                               |
| `corr(other)`                | 计算 Series 与另一个 Series 的相关性（皮尔逊相关系数） |
| `cov(other)`                 | 计算 Series 与另一个 Series 的协方差                   |
| `to_list()`                  | 将 Series 转换为 Python 列表                           |
| `to_frame()`                 | 将 Series 转换为 DataFrame                             |
| `iloc[]`                     | 通过位置索引来选择数据                                 |
| `loc[]`                      | 通过标签索引来选择数据                                 |

方法使用实例

```python
import pandas as pd

# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

# 查看基本信息
print("索引：", s.index)
print("数据：", s.values)
print("数据类型：", s.dtype)
print("前两行数据：", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2)
print("元素加倍后：", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("累计求和：", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("缺失值判断：", s.isnull())

# 排序
sorted_s = s.sort_values()
print("排序后的 Series：", sorted_s)
```

**使用列表、字典或数组创建一个默认索引的 Series**

```python
# 使用列表创建 Series
s = pd.Series([1, 2, 3, 4])

# 使用 NumPy 数组创建 Series
s = pd.Series(np.array([1, 2, 3, 4]))

# 使用字典创建 Series
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# 指定索引创建 Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 获取值
value = s[2]  # 获取索引为2的值
print(s['a'])  # 返回索引标签 'a' 对应的元素

# 获取多个值
subset = s[1:4]  # 获取索引为1到3的值

# 使用自定义索引
value = s['b']  # 获取索引为'b'的值

# 索引和值的对应关系
for index, value in s.items():
    print(f"Index: {index}, Value: {value}")


# 使用切片语法来访问 Series 的一部分
print(s['a':'c'])  # 返回索引标签 'a' 到 'c' 之间的元素
print(s[:3])  # 返回前三个元素

# 为特定的索引标签赋值
s['a'] = 10  # 将索引标签 'a' 对应的元素修改为 10

# 通过赋值给新的索引标签来添加元素
s['e'] = 5  # 在 Series 中添加一个新的元素，索引标签为 'e'

# 使用 del 删除指定索引标签的元素。
del s['a']  # 删除索引标签 'a' 对应的元素

# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
s_dropped = s.drop(['b'])  # 返回一个删除了索引标签 'b' 的新 Series

```

**基本运算**

```python
# 算术运算
result = series * 2  # 所有元素乘以2

# 过滤
filtered_series = series[series > 2]  # 选择大于2的元素

# 数学函数
import numpy as np
result = np.sqrt(series)  # 对每个元素取平方根
```

**计算统计数据**

> 使用 Series 的方法来计算描述性统计。

```python
print(s.sum())  # 输出 Series 的总和
print(s.mean())  # 输出 Series 的平均值
print(s.max())  # 输出 Series 的最大值
print(s.min())  # 输出 Series 的最小值
print(s.std())  # 输出 Series 的标准差
```

**属性和方法：**

```python
# 获取索引
index = s.index

# 获取值数组
values = s.values

# 获取描述统计信息
stats = s.describe()

# 获取最大值和最小值的索引
max_index = s.idxmax()
min_index = s.idxmin()

# 其他属性和方法
print(s.dtype)   # 数据类型
print(s.shape)   # 形状
print(s.size)    # 元素个数
print(s.head())  # 前几个元素，默认是前 5 个
print(s.tail())  # 后几个元素，默认是后 5 个
print(s.sum())   # 求和
print(s.mean())  # 平均值
print(s.std())   # 标准差
print(s.min())   # 最小值
print(s.max())   # 最大值

```

- `Series` 中的数据是有序的。
- 可以将 `Series` 视为带有索引的一维数组。
- 索引可以是唯一的，但不是必须的。
- 数据可以是标量、列表、NumPy 数组等。

## 数据结构 DataFrame

类似于一个二维表格，它是 Pandas 中最重要的数据结构。DataFrame 可以看作是由多个 Series 按列排列构成的表格，它既有行索引也有列索引，因此可以方便地进行行列选择、过滤、合并等操作。

![img](https://www.runoob.com/wp-content/uploads/2023/12/01_table_dataframe.svg)

DataFrame 可视为由多个 Series 组成的数据结构：

![img](https://www.runoob.com/wp-content/uploads/2021/04/pandas-DataStructure.png)

两个 Series 对象相加得到一个 DataFrame 对象

![img](https://www.runoob.com/wp-content/uploads/2023/12/object_creation_01.png)

DataFrame 由 Index、Key、Value 组成：

![img](https://www.runoob.com/wp-content/uploads/2023/12/object_creation_02.png)

DataFrame 构造方法如下：

```
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```

- `data`：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
- `index`：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `columns`：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `dtype`：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 `np.int64`、`np.float64` 等。如果不提供此参数，则根据数据自动推断数据类型。
- `copy`：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。

###### 使用列表创建

```python
import pandas as pd

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)

print(df)
```

###### 使用字典来创建

```python
import pandas as pd

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)
```

###### 使用 ndarrays 创建

```python
import numpy as np
import pandas as pd

# 创建一个包含网站和年龄的二维ndarray
ndarray_data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])

# 使用DataFrame构造函数创建数据帧
df = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])

# 打印数据帧
print(df)
```

###### pandas.DataFrame.loc()

Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
```

返回结果其实就是一个 Pandas Series 数据。

也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开：

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行和第二行
print(df.loc[[0, 1]])
```

**DataFrame 方法**

| **方法名称**        | **功能描述**                                                |
| :------------------ | :---------------------------------------------------------- |
| `head(n)`           | 返回 DataFrame 的前 n 行数据（默认前 5 行）                 |
| `tail(n)`           | 返回 DataFrame 的后 n 行数据（默认后 5 行）                 |
| `info()`            | 显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等 |
| `describe()`        | 返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等   |
| `shape`             | 返回 DataFrame 的行数和列数（行数, 列数）                   |
| `columns`           | 返回 DataFrame 的所有列名                                   |
| `index`             | 返回 DataFrame 的行索引                                     |
| `dtypes`            | 返回每一列的数值数据类型                                    |
| `sort_values(by)`   | 按照指定列排序                                              |
| `sort_index()`      | 按行索引排序                                                |
| `dropna()`          | 删除含有缺失值（NaN）的行或列                               |
| `fillna(value)`     | 用指定的值填充缺失值                                        |
| `isnull()`          | 判断缺失值，返回一个布尔值 DataFrame                        |
| `notnull()`         | 判断非缺失值，返回一个布尔值 DataFrame                      |
| `loc[]`             | 按标签索引选择数据                                          |
| `iloc[]`            | 按位置索引选择数据                                          |
| `at[]`              | 访问 DataFrame 中单个元素（比 `loc[]` 更高效）              |
| `iat[]`             | 访问 DataFrame 中单个元素（比 `iloc[]` 更高效）             |
| `apply(func)`       | 对 DataFrame 或 Series 应用一个函数                         |
| `applymap(func)`    | 对 DataFrame 的每个元素应用函数（仅对 DataFrame）           |
| `groupby(by)`       | 分组操作，用于按某一列分组进行汇总统计                      |
| `pivot_table()`     | 创建透视表                                                  |
| `merge()`           | 合并多个 DataFrame（类似 SQL 的 JOIN 操作）                 |
| `concat()`          | 按行或按列连接多个 DataFrame                                |
| `to_csv()`          | 将 DataFrame 导出为 CSV 文件                                |
| `to_excel()`        | 将 DataFrame 导出为 Excel 文件                              |
| `to_json()`         | 将 DataFrame 导出为 JSON 格式                               |
| `to_sql()`          | 将 DataFrame 导出为 SQL 数据库                              |
| `query()`           | 使用 SQL 风格的语法查询 DataFrame                           |
| `duplicated()`      | 返回布尔值 DataFrame，指示每行是否是重复的                  |
| `drop_duplicates()` | 删除重复的行                                                |
| `set_index()`       | 设置 DataFrame 的索引                                       |
| `reset_index()`     | 重置 DataFrame 的索引                                       |
| `transpose()`       | 转置 DataFrame（行列交换）                                  |

方法实例

```python
import pandas as pd

# 创建 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# 查看前两行数据
print(df.head(2))

# 查看 DataFrame 的基本信息
print(df.info())

# 获取描述统计信息
print(df.describe())

# 按年龄排序
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)

# 选择指定列
print(df[['Name', 'Age']])

# 按索引选择行
print(df.iloc[1:3])  # 选择第二到第三行（按位置）

# 按标签选择行
print(df.loc[1:2])  # 选择第二到第三行（按标签）

# 计算分组统计（按城市分组，计算平均年龄）
print(df.groupby('City')['Age'].mean())

# 处理缺失值（填充缺失值）
df['Age'] = df['Age'].fillna(30)

# 导出为 CSV 文件
df.to_csv('output.csv', index=False)
```

###### 创建 DataFrame

从字典创建：字典的键成为列名，值成为列数据。

```python
import pandas as pd

# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
```

###### 修改 DataFrame

```python
# 直接对列进行赋值
df['Column1'] = [10, 11, 12]

# 给新列赋值
df['NewColumn'] = [100, 200, 300]

# 添加新行
# 使用 loc、append 或 concat 方法。
# 使用 loc 为特定索引添加新行
df.loc[3] = [13, 14, 15, 16]

# 使用 append 添加新行到末尾
new_row = {'Column1': 13, 'Column2': 14, 'NewColumn': 16}
df = df.append(new_row, ignore_index=True)
```

###### 删除 DataFrame 元素

**删除列：**使用 drop 方法。

```
df_dropped = df.drop('Column1', axis=1)
```

**删除行：**同样使用 drop 方法。

```
df_dropped = df.drop(0)  # 删除索引为 0 的行
```

###### DataFrame 的统计分析

**描述性统计：**使用 **.describe()** 查看数值列的统计摘要。

```
df.describe()
```

**计算统计数据：**使用聚合函数如 **.sum()、.mean()、.max()** 等。

```
df['Column1'].sum()
df.mean()
```

###### DataFrame 的索引操作

**重置索引：**使用 **.reset_index()**。

```
df_reset = df.reset_index(drop=True)
```

**设置索引：**使用 **.set_index()**。

```
df_set = df.set_index('Column1')
```

###### DataFrame 的布尔索引

使用布尔表达式：根据条件过滤 DataFrame。

```
df[df['Column1'] > 2]
```

###### DataFrame 的数据类型

查看数据类型：使用 **dtypes** 属性。

```
df.dtypes
```

**转换数据类型：**使用 **astype** 方法。

```
df['Column1'] = df['Column1'].astype('float64')
```

###### DataFrame 的合并与分割

**合并：**使用 **concat** 或 **merge** 方法。

```
# 纵向合并
pd.concat([df1, df2], ignore_index=True)

# 横向合并
pd.merge(df1, df2, on='Column1')
```

**分割：**使用 **pivot、melt** 或自定义函数。

```
# 长格式转宽格式
df_pivot = df.pivot(index='Column1', columns='Column2', values='Column3')

# 宽格式转长格式
df_melt = df.melt(id_vars='Column1', value_vars=['Column2', 'Column3'])
```

###### 索引和切片

DataFrame 支持对行和列进行索引和切片操作。

###### 注意事项

- `DataFrame` 是一种灵活的数据结构，可以容纳不同数据类型的列。
- 列名和行索引可以是字符串、整数等。
- `DataFrame` 可以通过多种方式进行数据选择、过滤、修改和分析。
- 通过对 `DataFrame` 的操作，可以进行数据清洗、转换、分析和可视化等工作。

## CSV 文件

| **方法名称**         | **功能描述**                          | **常用参数**                                                 |
| :------------------- | :------------------------------------ | :----------------------------------------------------------- |
| `pd.read_csv()`      | 从 CSV 文件读取数据并加载为 DataFrame | `filepath_or_buffer` (路径或文件对象)，`sep` (分隔符)，`header` (行标题)，`names` (自定义列名)，`dtype` (数据类型)，`index_col` (索引列) |
| `DataFrame.to_csv()` | 将 DataFrame 写入到 CSV 文件          | `path_or_buffer` (目标路径或文件对象)，`sep` (分隔符)，`index` (是否写入索引)，`columns` (指定列)，`header` (是否写入列名)，`mode` (写入模式) |

###### pd.read_csv() 

> 读取 CSV 文件

```python
import pandas as pd

# 读取 CSV 文件，并自定义列名和分隔符
df = pd.read_csv('data.csv', sep=';', header=0, names=['A', 'B', 'C'], dtype={'A': int, 'B': float})
print(df)
```

read_csv 常用参数

| **参数**             | **说明**                                                     | **默认值** |
| :------------------- | :----------------------------------------------------------- | :--------- |
| `filepath_or_buffer` | CSV 文件的路径或文件对象（支持 URL、文件路径、文件对象等）   | 必需参数   |
| `sep`                | 定义字段分隔符，默认是逗号（`,`），可以改为其他字符，如制表符（`\t`） | `','`      |
| `header`             | 指定行号作为列标题，默认为 0（表示第一行），或者设置为 `None` 没有标题 | `0`        |
| `names`              | 自定义列名，传入列名列表                                     | `None`     |
| `index_col`          | 用作行索引的列的列号或列名                                   | `None`     |
| `usecols`            | 读取指定的列，可以是列的名称或列的索引                       | `None`     |
| `dtype`              | 强制将列转换为指定的数据类型                                 | `None`     |
| `skiprows`           | 跳过文件开头的指定行数，或者传入一个行号的列表               | `None`     |
| `nrows`              | 读取前 N 行数据                                              | `None`     |
| `na_values`          | 指定哪些值应视为缺失值（NaN）                                | `None`     |
| `skipfooter`         | 跳过文件结尾的指定行数                                       | `0`        |
| `encoding`           | 文件的编码格式（如 `utf-8`，`latin1` 等）                    | `None`     |

###### df.to_csv()

将 DataFrame 写入 CSV 文件

```python
import pandas as pd

# 假设 df 是一个已有的 DataFrame
df.to_csv('output.csv', index=False, header=True, columns=['A', 'B'])
```

| **参数**          | **说明**                                                     | **默认值** |
| :---------------- | :----------------------------------------------------------- | :--------- |
| `path_or_buffer`  | CSV 文件的路径或文件对象（支持文件路径、文件对象）           | 必需参数   |
| `sep`             | 定义字段分隔符，默认是逗号（`,`），可以改为其他字符，如制表符（`\t`） | `','`      |
| `index`           | 是否写入行索引，默认 `True` 表示写入索引                     | `True`     |
| `columns`         | 指定写入的列，可以是列的名称列表                             | `None`     |
| `header`          | 是否写入列名，默认 `True` 表示写入列名，设置为 `False` 表示不写列名 | `True`     |
| `mode`            | 写入文件的模式，默认是 `w`（写模式），可以设置为 `a`（追加模式） | `'w'`      |
| `encoding`        | 文件的编码格式，如 `utf-8`，`latin1` 等                      | `None`     |
| `line_terminator` | 定义行结束符，默认为 `\n`                                    | `None`     |
| `quoting`         | 设置如何对文件中的数据进行引号处理（0-3，具体引用方式可查文档） | `None`     |
| `quotechar`       | 设置用于引用的字符，默认为双引号 `"`                         | `'"'`      |
| `date_format`     | 自定义日期格式，如果列包含日期数据，则可以使用此参数指定日期格式 | `None`     |
| `doublequote`     | 如果为 `True`，则在写入时会将包含引号的文本使用双引号括起来  | `True`     |

使用 **to_csv()** 方法将 DataFrame 存储为 csv 文件

```python
import pandas as pd 
   
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag} 
     
df = pd.DataFrame(dict)
  
# 保存 dataframe
df.to_csv('site.csv')
```

###### read_csv.head()

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head())
```

###### tail()

tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail())
```

###### info()

info() 方法返回表格的一些基本信息：

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.info())
```

## Excel 文件操作

| **操作**                      | **方法**               | **说明**                                   |
| :---------------------------- | :--------------------- | :----------------------------------------- |
| 读取Excel文件                 | `pd.read_excel()`      | 读取Excel文件，返回DataFrame               |
| 将 DataFrame 写入 Excel       | `DataFrame.to_excel()` | 将 DataFrame 写入 Excel 文件               |
| 加载Excel文件                 | `pd.ExcelFile()`       | 加载Excel文件并访问多个表单                |
| 使用 ExcelWriter 编写多个表单 | `pd.ExcelWriter()`     | 读取多个DataFrame到相同Excel文件的不同表单 |

###### pd.read_excel() 

读取 Excel 文件
pd.read_excel() 方法用于从 Excel 文件中读取数据并加载为 DataFrame。它支持读取 .xls 和 .xlsx 格式的文件。

```python
pandas.read_excel(io, sheet_name=0, *, header=0, names=None, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=<no_default>, date_format=None, thousands=None, decimal='.', comment=None, skipfooter=0, storage_options=None, dtype_backend=<no_default>, engine_kwargs=None)
```

| 参数          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| `io`          | Excel 文件路径（字符串）、文件对象或 `BytesIO`。例如：`'data.xlsx'` |
| `sheet_name`  | 要读取的工作表： • `0`（默认，第一个表） • `'Sheet1'`（表名） • `[0, 'Sales']`（读多个表，返回字典） • `None`（读所有表） |
| `header`      | 指定哪一行作为列名，默认 `0`（第一行）。设为 `None` 表示无列名，自动生成 `0,1,2...` |
| `names`       | 自定义列名（需与数据列数一致），会覆盖 `header`              |
| `index_col`   | 指定某列作为行索引，如 `index_col=0` 或 `index_col='ID'`     |
| `usecols`     | 读取指定列： • `'A:C'`（A 到 C 列） • `'A,C,E'` • `[0,1,2]`（按索引） • `'A:D,F'`（混合） |
| `skiprows`    | 跳过开头若干行，或传入行号列表（从 0 开始）                  |
| `nrows`       | 最多读取多少行（从有效数据开始算）                           |
| `na_values`   | 自定义哪些值视为缺失值，如 `na_values=['N/A', 'NULL']`       |
| `dtype`       | 指定列的数据类型，如 `{'age': int, 'name': str}`             |
| `parse_dates` | 自动解析日期列： • `True`：尝试解析索引 • `['date_col']`：解析指定列 • `{ 'new_date': ['year', 'month', 'day'] }`：合并多列 |
| `engine`      | 读取引擎： • `'openpyxl'`（推荐用于 `.xlsx`） • `'xlrd'`（仅支持 `.xls`，新版 xlrd 不支持 xlsx） • `'odf'`（用于 OpenDocument） 通常可省略，pandas 自动选择 |

实例

```python
import pandas as pd

# 读取 data.xlsx 文件
df = pd.read_excel('runoob_pandas_data.xlsx')

# 打印读取的 DataFrame
print(df)
```

###### DataFrame.to_excel()

将 DataFrame 写入 Excel 文件

```python
DataFrame.to_excel(excel_writer, *, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, inf_rep='inf', freeze_panes=None, storage_options=None, engine_kwargs=None)
```

```python
import pandas as pd

# 创建一个简单的 DataFrame
df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 写入 Excel 文件，写入 'Sheet1' 表单
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# 写入多个表单，使用 ExcelWriter
with pd.ExcelWriter('output.xlsx') as writer:
df.to_excel(writer, sheet_name='Sheet1', index=False)
df.to_excel(writer, sheet_name='Sheet2', index=False)
```

###### ExcelFile

加载 Excel 文件
ExcelFile 是一个用于读取 Excel 文件的类，它可以处理多个表单，并在不重新打开文件的情况下访问其中的数据。

语法格式如下：

```
excel_file = pd.ExcelFile('data.xlsx')
```

| **方法**            | **功能描述**                     |
| :------------------ | :------------------------------- |
| `sheet_names`       | 返回文件中所有表单的名称列表     |
| `parse(sheet_name)` | 解析指定表单并返回一个 DataFrame |
| `close()`           | 关闭文件，以释放资源             |

```python
import pandas as pd

# 使用 ExcelFile 加载 Excel 文件
excel_file = pd.ExcelFile('data.xlsx')

# 查看所有表单的名称
print(excel_file.sheet_names)

# 读取指定的表单
df = excel_file.parse('Sheet1')
print(df)

# 关闭文件
excel_file.close()
```

###### ExcelWriter

写入 Excel 文件

```
pandas.ExcelWriter(path, engine=None, date_format=None, datetime_format=None, mode='w', storage_options=None, if_sheet_exists=None, engine_kwargs=None)
```

- `pythonpath`：这是必需的参数，指定了要写入的 Excel 文件的路径、URL 或文件对象。可以是本地文件路径、远程存储路径（如 S3）、URL 链接或已打开的文件对象。
- `engine`：这是一个可选参数，用于指定写入 Excel 文件的引擎。如果为 `None`，则 pandas 会自动选择一个可用的引擎（默认优先选择 `openpyxl`，如果不可用则选择其他可用引擎）。常见的引擎包括 `'openpyxl'`（用于 `.xlsx` 文件）、`'xlsxwriter'`（提供高级格式化和图表功能）、`'odf'`（用于 OpenDocument 格式如 `.ods`）等。
- `date_format`：这是一个可选参数，指定写入 Excel 文件中日期的格式字符串，例如 `"YYYY-MM-DD"`。
- `datetime_format`：这是一个可选参数，指定写入 Excel 文件中日期时间对象的格式字符串，例如 `"YYYY-MM-DD HH:MM:SS"`。
- `mode`：这是一个可选参数，默认为 `'w'`，表示写入模式。如果设置为 `'a'`，则表示追加模式，向现有文件中添加数据（仅支持部分引擎，如 `openpyxl`）。
- `storage_options`：这是一个可选参数，用于指定与存储后端连接的额外选项，例如认证信息、访问权限等，适用于写入远程存储（如 S3、GCS）。
- `if_sheet_exists`：这是一个可选参数，默认为 `'error'`，指定如果工作表已经存在时的行为。选项包括 `'error'`（抛出错误）、`'new'`（创建一个新工作表）、`'replace'`（替换现有工作表的内容）、`'overlay'`（在现有工作表上覆盖写入）。
- `engine_kwargs`：这是一个可选参数，用于传递给引擎的其他关键字参数。这些参数会传递给相应引擎的函数，例如 `xlsxwriter.Workbook(file, **engine_kwargs)` 或 `openpyxl.Workbook(**engine_kwargs)` 等。

###### 创建 ExcelWriter 对象

```python
with ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
```

```python
df1 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])  
df2 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1")  
    df2.to_excel(writer, sheet_name="Sheet2")
```

设置日期格式或日期时间格式：

```python
from datetime import date, datetime  
df = pd.DataFrame(
    [
        [date(2014, 1, 31), date(1999, 9, 24)],
        [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)  
with pd.ExcelWriter(
    "path_to_file.xlsx",
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS"
) as writer:
    df.to_excel(writer)
```

使用 if_sheet_exists 参数替换已存在的工作表

```python
with ExcelWriter(
    "path_to_file.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="replace",
) as writer:
    df.to_excel(writer, sheet_name="Sheet1")
```

## Pandas JSON

| **操作**                    | **方法**              | **说明**                                              |
| :-------------------------- | :-------------------- | :---------------------------------------------------- |
| 从 JSON 文件/字符串读取数据 | `pd.read_json()`      | 从JSON数据中读取并加载为DataFrame                     |
| 将 DataFrame 转换为 JSON    | `DataFrame.to_json()` | 将 DataFrame 转换为 JSON 格式的数据，可以指定格式方式 |
| 支持JSON格式                | `orient`参数          | 支持多种包装方式，如`split`、`records`、`columns`     |

###### pd.read_json() 

读取 JSON 数据

```
import pandas as pd

df = pd.read_json(
    path_or_buffer,      # JSON 文件路径、JSON 字符串或 URL
    orient=None,         # JSON 数据的结构方式，默认是 'columns'
    dtype=None,          # 强制指定列的数据类型
    convert_axes=True,   # 是否转换行列索引
    convert_dates=True,  # 是否将日期解析为日期类型
    keep_default_na=True # 是否保留默认的缺失值标记
)
```

| **参数**          | **说明**                                                     | **默认值**                 |
| :---------------- | :----------------------------------------------------------- | :------------------------- |
| `path_or_buffer`  | JSON文件的路径、JSON字符串或URL                              | 简单参数                   |
| `orient`          | 定义JSON数据的格式方式。常见值有`split`、`records`、`index`、`columns`、`values`。 | `None`（根据文件自动推断） |
| `dtype`           | 强制指定列的数据类型                                         | `None`                     |
| `convert_axes`    | 是否将轴转换为正确的数据类型                                 | `True`                     |
| `convert_dates`   | 是否将日期解析为日期类型                                     | `True`                     |
| `keep_default_na` | 是否保留默认的缺失值标记（如`NaN`）                          | `True`                     |

**常见的 orient 参数选项:**

| **orient 值** | **JSON 格式示例**                                            | **描述**                                 |
| :------------ | :----------------------------------------------------------- | :--------------------------------------- |
| `split`       | `{"index":["a","b"],"columns":["A","B"],"data":[[1,2],[3,4]]}` | 使用键 `index`、`columns` 和 `data` 结构 |
| `records`     | `[{"A":1,"B":2},{"A":3,"B":4}]`                              | 每个记录是一个字典，表示一行数据         |
| `index`       | `{"a":{"A":1,"B":2},"b":{"A":3,"B":4}}`                      | 使用索引为键，值为字典的方式             |
| `columns`     | `{"A":{"a":1,"b":3},"B":{"a":2,"b":4}}`                      | 使用列名为键，值为字典的方式             |
| `values`      | `[[1,2],[3,4]]`                                              | 只返回数据，不包括索引和列名             |

从JSON文件加载数据

```py
import pandas as pd

df = pd.read_json('sites.json')
   
print(df.to_string())
```

**to_string()** 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串

```python
import pandas as pd

data =[
    {
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]
df = pd.DataFrame(data)

print(df)
```

从 JSON 数据读取（指定 orient 为 records）

```python
import pandas as pd

# JSON 数据
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据，指定 orient='records'
df = pd.read_json(json_data, orient='records')

print(df)
```

###### 内嵌的 JSON 数据

假设有一组内嵌的 JSON 数据文件 nested_list.json

```json
{
    "school_name": "ABC primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```

###### json_normalize()

将内嵌的数据完整的解析出来

```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)
```

嵌套了列表和字典

该数据嵌套了列表和字典，数据文件 nested_mix.json 如下

```json
{
    "school_name": "local primary school",
    "class": "Year 1",
    "info": {
      "president": "John Kasich",
      "address": "ABC road, London, UK",
      "contacts": {
        "email": "admin@e.com",
        "tel": "123456789"
      }
    },
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```

###### 读取内嵌数据中的一组数据

这里我们需要使用到 **glom** 模块来处理数据套嵌，**glom** 模块允许我们使用 **.** 来访问内嵌对象的属性。

第一次使用我们需要安装 glom：

```
pip3 install glom
```

###### DataFrame.to_json()

将 DataFrame 转换为 JSON

to_json() 方法用于将 DataFrame 转换为 JSON 格式的数据，可以指定 JSON 的结构化方式。

语法格式：

```
df.to_json(
    path_or_buffer=None,    # 输出的文件路径或文件对象，如果是 None 则返回 JSON 字符串
    orient=None,            # JSON 格式方式，支持 'split', 'records', 'index', 'columns', 'values'
    date_format=None,       # 日期格式，支持 'epoch', 'iso'
    default_handler=None,   # 自定义非标准类型的处理函数
    lines=False,            # 是否将每行数据作为一行（适用于 'records' 或 'split'）
    encoding='utf-8'        # 编码格式
)
```

**参数说明：**

| **参数**          | **说明**                                                     | **默认值**                 |
| :---------------- | :----------------------------------------------------------- | :------------------------- |
| `path_or_buffer`  | 输出的文件路径或文件对象，若为 `None`，则返回 JSON 字符串    | `None`                     |
| `orient`          | 指定 JSON 格式结构，支持 `split`、`records`、`index`、`columns`、`values` | `None`（默认是 `columns`） |
| `date_format`     | 日期格式，支持 `'epoch'` 或 `'iso'` 格式                     | `None`                     |
| `default_handler` | 自定义处理非标准类型（如 `datetime` 等）的处理函数           | `None`                     |
| `lines`           | 是否将每行数据作为一行输出（适用于 `records` 或 `split`）    | `False`                    |
| `encoding`        | 输出文件的编码格式                                           | `'utf-8'`                  |

```py
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 转换为 JSON 字符串
json_str = df.to_json()

print(json_str)
```

将 DataFrame 转换为 JSON 文件（指定 orient='records'）：

```py
import** pandas **as** pd

\# 创建 DataFrame
df = pd.DataFrame({
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Los Angeles', 'Chicago']
})

\# 将 DataFrame 转换为 JSON 文件，指定 orient='records'
df.to_json('data.json', orient='records', lines=True)

\# 输出生成的文件内容：
\# [
\#  {"Name":"Alice","Age":25,"City":"New York"},
\#  {"Name":"Bob","Age":30,"City":"Los Angeles"},
\#  {"Name":"Charlie","Age":35,"City":"Chicago"}
\# ]
```

将 DataFrame 转换为 JSON 并指定日期格式：

```py
import pandas as pd

\# 创建 DataFrame，包含日期数据
df = pd.DataFrame({
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Date': pd.to_datetime(['2021-01-01', '2022-02-01', '2023-03-01']),
  'Age': [25, 30, 35]
})

\# 将 DataFrame 转换为 JSON，并指定日期格式为 'iso'
json_str = df.to_json(date_format='iso')

**print**(json_str)
<p>
```

## Pandas 数据清洗

###### **dropna()**清洗空值

```
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

- axis：默认为 **0**，表示逢空值剔除整行，如果设置参数 **axis＝1** 表示逢空值去掉整列。
- how：默认为 **'any'** 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 **how='all'** 一行（或列）都是 NA 才去掉这整行。
- thresh：设置需要多少非空值的数据才可以保留下来的。
- subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
- inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

###### isnull()

判断各个单元格是否为空

```py
import pandas as pd

df = pd.read_csv('property-data.csv')

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
```

######  fillna()

来替换一些空字段

```py
import pandas as pd

df = pd.read_csv('property-data.csv')

df.fillna(12345, inplace = True)

print(df.to_string())
```

替换空单元格的常用方法是计算列的均值、中位数值或众数。

Pandas使用 mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。

###### mean() 

计算列的均值并替换空单元格

```py
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].mean()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```

###### median() 

计算列的中位数并替换空单元格

```py
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].median()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```

###### mode()

计算列的众数并替换空单元格

```py
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].mode()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```

##### 清洗格式错误数据

数据格式错误的单元格会使数据分析变得困难，甚至不可能。

我们可以通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据

```py
import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())
```

##### 清洗错误数据

我们可以对错误的数据进行替换或移除

```py
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

df.loc[2, 'age'] = 30 # 修改数据

print(df.to_string())
```

##### 清洗重复数据

###### duplicated() 

```py
import pandas as pd

person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)

print(df.duplicated())
```

###### drop_duplicates() 

删除重复数据，可以直接使用drop_duplicates() 方法

```py
import pandas as pd

persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}

df = pd.DataFrame(persons)

df.drop_duplicates(inplace = True)
print(df)
```

| **操作**               | **方法/步骤**                | **说明**                                                     | **常用函数/方法**                                        |
| :--------------------- | :--------------------------- | :----------------------------------------------------------- | :------------------------------------------------------- |
| **缺失值处理**         | 填充缺失值                   | 使用指定的值（如均值、中位数、众数等）填充缺失值。           | `df.fillna(value)`                                       |
|                        | 删除缺失值                   | 删除包含缺失值的行或列。                                     | `df.dropna()`                                            |
| **重复数据处理**       | 删除重复数据                 | 删除 DataFrame 中的重复行。                                  | `df.drop_duplicates()`                                   |
| **异常值处理**         | 异常值检测（基于统计方法）   | 通过 Z-score 或 IQR 方法识别并处理异常值。                   | 自定义函数（如基于 Z-score 或 IQR）                      |
|                        | 替换异常值                   | 使用合适的值（如均值或中位数）替换异常值。                   | 自定义函数（如替换异常值）                               |
| **数据格式转换**       | 转换数据类型                 | 将数据类型从一个类型转换为另一个类型，如将字符串转换为日期。 | `df.astype()`                                            |
|                        | 日期时间格式转换             | 转换字符串或数字为日期时间类型。                             | `pd.to_datetime()`                                       |
| **标准化与归一化**     | 标准化                       | 将数据转换为均值为0，标准差为1的分布。                       | `StandardScaler()`                                       |
|                        | 归一化                       | 将数据缩放到指定的范围（如 [0, 1]）。                        | `MinMaxScaler()`                                         |
| **类别数据编码**       | 标签编码                     | 将类别变量转换为整数形式。                                   | `LabelEncoder()`                                         |
|                        | 独热编码（One-Hot Encoding） | 将每个类别转换为一个新的二进制特征。                         | `pd.get_dummies()`                                       |
| **文本数据处理**       | 去除停用词                   | 从文本中去除无关紧要的词，如 "the" 、 "is" 等。              | 自定义函数（基于 `nltk` 或 `spaCy`）                     |
|                        | 词干化与词形还原             | 提取词干或恢复单词的基本形式。                               | `nltk.stem.PorterStemmer()`                              |
|                        | 分词                         | 将文本分割成单词或子词。                                     | `nltk.word_tokenize()`                                   |
| **数据抽样**           | 随机抽样                     | 从数据中随机抽取一定比例的样本。                             | `df.sample()`                                            |
|                        | 上采样与下采样               | 通过过采样（复制少数类样本）或欠采样（减少多数类样本）来平衡数据集中的类别分布。 | `SMOTE()`（上采样）； `RandomUnderSampler()`（下采样）   |
| **特征工程**           | 特征选择                     | 选择对目标变量有影响的特征，去除冗余或无关特征。             | `SelectKBest()`                                          |
|                        | 特征提取                     | 从原始数据中创建新的特征，提升模型的预测能力。               | `PolynomialFeatures()`                                   |
|                        | 特征缩放                     | 对数值特征进行缩放，使其具有相同的量级。                     | `MinMaxScaler()` 、 `StandardScaler()`                   |
| **类别特征映射**       | 特征映射                     | 将类别变量映射为对应的数字编码。                             | 自定义映射函数                                           |
| **数据合并与连接**     | 合并数据                     | 将多个 DataFrame 按照某些列合并在一起，支持内连接、外连接、左连接、右连接等。 | `pd.merge()`                                             |
|                        | 连接数据                     | 将多个 DataFrame 进行行或列拼接。                            | `pd.concat()`                                            |
| **数据重塑**           | 数据透视表                   | 将数据根据某些维度进行分组并计算聚合结果。                   | `pd.pivot_table()`                                       |
|                        | 数据变形                     | 改变数据的形状，如从长格式转为宽格式或从宽格式转为长格式。   | `df.melt()` 、 `df.pivot()`                              |
| **数据类型转换与处理** | 字符串处理                   | 对字符串数据进行处理，如去除空格、转换大小写等。             | `str.replace()` 、 `str.upper()` 等                      |
|                        | 分组计算                     | 按照某个特征分组后进行聚合计算。                             | `df.groupby()`                                           |
| **缺失值预测填充**     | 使用模型预测填充缺失值       | 使用机器学习模型（如回归模型）预测缺失值，并填充缺失数据。   | 自定义模型（如 `sklearn.linear_model.LinearRegression`） |
| **时间序列处理**       | 时间序列缺失值填充           | 使用时间序列的方法（如前向填充、后向填充）填充缺失值。       | `df.fillna(method='ffill')`                              |
|                        | 滚动窗口计算                 | 使用滑动窗口进行时间序列数据的统计计算（如均值、标准差等）。 | `df.rolling(window=5).mean()`                            |
| **数据转换与映射**     | 数据映射与替换               | 将数据中的某些值替换为其他值。                               | `df.replace()`                                           |

###### 填充缺失值

```python
import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, None, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 填充缺失的 "Age" 为均值
df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df)
```

## Pandas 常用函数

###### pd.read_sql()

```
pd.read_sql(query, connection_object)
```

从 SQL 数据库读取数据

###### pd.read_json()

```
pd.read_json(json_string)
```



###### pd.read_html()

```
pd.read_html(url)
```

从 HTML 页面中读取数据

##### 查看数据

| 函数          | 说明                                                       |
| :------------ | :--------------------------------------------------------- |
| df.head(n)    | 显示前 n 行数据；                                          |
| df.tail(n)    | 显示后 n 行数据；                                          |
| df.info()     | 显示数据的信息，包括列名、数据类型、缺失值等；             |
| df.describe() | 显示数据的基本统计信息，包括均值、方差、最大值、最小值等； |
| df.shape      | 显示数据的行数和列数。                                     |

```python
# 显示前五行数据
df.head()

# 显示后五行数据
df.tail()

# 显示数据信息
df.info()

# 显示基本统计信息
df.describe()

# 显示数据的行数和列数
df.shape
```

##### 数据清洗

| 函数                             | 说明                     |
| :------------------------------- | :----------------------- |
| df.dropna()                      | 删除包含缺失值的行或列； |
| df.fillna(value)                 | 将缺失值替换为指定的值； |
| df.replace(old_value, new_value) | 将指定值替换为新值；     |
| df.duplicated()                  | 检查是否有重复的数据；   |
| df.drop_duplicates()             | 删除重复的数据。         |

```python
# 删除包含缺失值的行或列
df.dropna()

# 将缺失值替换为指定的值
df.fillna(0)

# 将指定值替换为新值
df.replace('old_value', 'new_value')

# 检查是否有重复的数据
df.duplicated()

# 删除重复的数据
df.drop_duplicates()
```

##### 数据选择和切片

| 函数                                          | 说明                         |
| :-------------------------------------------- | :--------------------------- |
| df[column_name]                               | 选择指定的列；               |
| df.loc[row_index, column_name]                | 通过标签选择数据；           |
| df.iloc[row_index, column_index]              | 通过位置选择数据；           |
| df.ix[row_index, column_name]                 | 通过标签或位置选择数据；     |
| df.filter(items=[column_name1, column_name2]) | 选择指定的列；               |
| df.filter(regex='regex')                      | 选择列名匹配正则表达式的列； |
| df.sample(n)                                  | 随机选择 n 行数据。          |

```python
# 选择指定的列
df['column_name']

# 通过标签选择数据
df.loc[row_index, column_name]

# 通过位置选择数据
df.iloc[row_index, column_index]

# 通过标签或位置选择数据
df.ix[row_index, column_name]

# 选择指定的列
df.filter(items=['column_name1', 'column_name2'])

# 选择列名匹配正则表达式的列
df.filter(regex='regex')

# 随机选择 n 行数据
df.sample(n=5)
```

##### 数据排序

| 函数                                                         | 说明                 |
| :----------------------------------------------------------- | :------------------- |
| df.sort_values(column_name)                                  | 按照指定列的值排序； |
| df.sort_values([column_name1, column_name2], ascending=[True, False]) | 按照多个列的值排序； |
| df.sort_index()                                              | 按照索引排序。       |

```python
# 按照指定列的值排序
df.sort_values('column_name')

# 按照多个列的值排序
df.sort_values(['column_name1', 'column_name2'], ascending=[True, False])

# 按照索引排序
df.sort_index()
```

##### 数据分组和聚合

| 函数                                            | 说明                         |
| :---------------------------------------------- | :--------------------------- |
| df.groupby(column_name)                         | 按照指定列进行分组；         |
| df.aggregate(function_name)                     | 对分组后的数据进行聚合操作； |
| df.pivot_table(values, index, columns, aggfunc) | 生成透视表。                 |

```python
# 按照指定列进行分组
df.groupby('column_name')

# 对分组后的数据进行聚合操作
df.aggregate('function_name')

# 生成透视表
df.pivot_table(values='value', index='index_column', columns='column_name', aggfunc='function_name')
```

##### 数据合并

| 函数                               | 说明                             |
| :--------------------------------- | :------------------------------- |
| pd.concat([df1, df2])              | 将多个数据框按照行或列进行合并； |
| pd.merge(df1, df2, on=column_name) | 按照指定列将两个数据框进行合并。 |

```python
# 将多个数据框按照行或列进行合并
df = pd.concat([df1, df2])

# 按照指定列将两个数据框进行合并
df = pd.merge(df1, df2, on='column_name')
```

##### 数据选择和过滤

| 函数                                 | 说明                                   |
| :----------------------------------- | :------------------------------------- |
| df.loc[row_indexer, column_indexer]  | 按标签选择行和列。                     |
| df.iloc[row_indexer, column_indexer] | 按位置选择行和列。                     |
| df[df['column_name'] > value]        | 选择列中满足条件的行。                 |
| df.query('column_name > value')      | 使用字符串表达式选择列中满足条件的行。 |

##### 数据统计和描述

| 函数          | 说明                                                 |
| :------------ | :--------------------------------------------------- |
| df.describe() | 计算基本统计信息，如均值、标准差、最小值、最大值等。 |
| df.mean()     | 计算每列的平均值。                                   |
| df.median()   | 计算每列的中位数。                                   |
| df.mode()     | 计算每列的众数。                                     |
| df.count()    | 计算每列非缺失值的数量。                             |

## Pandas 相关性分析

###### DataFrame.corr()

```
df.corr(method='pearson', min_periods=1)
```

```py
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

# 计算皮尔逊相关系数
correlation = df.corr(method='pearson')
print(correlation)
```

###### DataFrame.cov()

## Pandas 数据排序与聚合

| **操作**       | **方法**                              | **说明**                                     | **常用函数/方法**                                          |
| :------------- | :------------------------------------ | :------------------------------------------- | :--------------------------------------------------------- |
| **排序**       | `sort_values(by, ascending)`          | 根据某列的值进行排序，`ascending` 控制升降序 | `df.sort_values(by='column')`                              |
| **排序**       | `sort_index(axis)`                    | 根据行或列的索引进行排序                     | `df.sort_index(axis=0)`                                    |
| **分组聚合**   | `groupby(by)`                         | 按照某列进行分组后，应用聚合函数             | `df.groupby('column')`                                     |
| **聚合函数**   | `agg()`                               | 聚合函数，如 `sum()`、`mean()`、`count()` 等 | `df.groupby('column').agg({'value': 'sum'})`               |
| **多重聚合**   | `agg([func1, func2])`                 | 对同一列应用多个聚合函数                     | `df.groupby('column').agg({'value': ['mean', 'sum']})`     |
| **分组后排序** | `apply(lambda x: x.sort_values(...))` | 在分组后进行排序                             | `df.groupby('column').apply(lambda x: x.sort_values(...))` |
| **透视表**     | `pivot_table()`                       | 创建透视表，根据行、列进行数据汇总           |                                                            |

##### 数据排序

- `sort_values()`：根据列的值进行排序。
- `sort_index()`：根据行或列的索引进行排序。

###### sort_values()

```python
import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# 按照 "Age" 列的值进行降序排序
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)
```

###### sort_index()

```python
# 按照行索引进行排序
df_sorted_by_index = df.sort_index(axis=0)
print(df_sorted_by_index)
```

##### 数据聚合

###### groupby()

| **操作**         | **方法**                             | **说明**                                                     | **示例**                                                    |
| :--------------- | :----------------------------------- | :----------------------------------------------------------- | :---------------------------------------------------------- |
| 按列分组并聚合   | `df.groupby(by).agg()`               | 按指定列（`by`）进行分组，`agg()` 可以传入不同的聚合函数，进行多种操作 | `df.groupby('Department').agg({'Salary': 'mean'})`          |
| 多重聚合函数应用 | `df.groupby(by).agg([func1, func2])` | 可以对同一列应用多个聚合函数，返回多种聚合结果               | `df.groupby('Department').agg({'Salary': ['mean', 'sum']})` |

```python
import pandas as pd

# 示例数据
data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]}

df = pd.DataFrame(data)

# 按照部门分组，并计算每个部门的平均薪资
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)
```

##### 分组后的排序

##### 透视表

| **操作**   | **方法**                                          | **说明**                                                     | **示例**                                                     |
| :--------- | :------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 创建透视表 | `df.pivot_table(values, index, columns, aggfunc)` | 用指定的列进行行、列分类汇总，`values` 是需要聚合的值，`aggfunc` 是聚合函数 | `df.pivot_table(values='Salary', index='Department', aggfunc='mean')` |

```python
# 使用 pivot_table 计算每个部门的薪资平均值
pivot_table = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print(pivot_table)
```

## Pandas数据可视化

| **图表类型**   | **描述**                               | **方法**                                      |
| :------------- | :------------------------------------- | :-------------------------------------------- |
| **折线图**     | 显示数据随时间或其他连续变量的变化趋势 | `df.plot(kind='line')`                        |
| **柱状图**     | 比较不同类别的数据                     | `df.plot(kind='bar')`                         |
| **水平柱状图** | 比较不同类别的数据，但柱子水平排列     | `df.plot(kind='barh')`                        |
| **直方图**     | 显示数据的分布                         | `df.plot(kind='hist')`                        |
| **散点图**     | 显示数值型变量之间的关系               | `df.plot(kind='scatter', x='col1', y='col2')` |
| **箱线图**     | 显示数据分布，包括中分区、四分区等     | `df.plot(kind='box')`                         |
| **密度图**     | 显示数据的密度分布                     | `df.plot(kind='kde')`                         |
| **饼图**       | 在整体中的现场显示不同部分             | `df.plot(kind='pie')`                         |
| **区域图**     | 显示数据的总计                         | `df.plot(kind='area')`                        |

###### plot()

| **参数**  | **说明**                                                     |
| :-------- | :----------------------------------------------------------- |
| `kind`    | 图表类型，支持`'line'`, `'bar'`, `'barh'`, `'hist'`, `'box'`, `'kde'`, `'density'`, `'area'`,`'pie'`等类型 |
| `x`       | 设置 x 轴的数据列                                            |
| `y`       | 设置 y 轴的数据列                                            |
| `title`   | 图表的标题                                                   |
| `xlabel`  | x 轴的标签                                                   |
| `ylabel`  | y 轴的标签                                                   |
| `color`   | 设置图表的颜色                                               |
| `figsize` | 设置图表的大小（宽、高）                                     |
| `legend`  | 是否显示图例                                                 |

| **图表类型**   | **描述**                                             | **常用的方法**                                |
| :------------- | :--------------------------------------------------- | :-------------------------------------------- |
| **折线图**     | 用于显示随时间变化的数据趋势                         | `df.plot(kind='line')`                        |
| **柱状图**     | 用于显示类别之间的比较数据                           | `df.plot(kind='bar')`                         |
| **水平柱状图** | 与柱状图类似，但柱子是水平的                         | `df.plot(kind='barh')`                        |
| **直方图**     | 用于显示数据的分布（频率分布）                       | `df.plot(kind='hist')`                        |
| **散点图**     | 用于显示数值之间的关系                               | `df.plot(kind='scatter', x='col1', y='col2')` |
| **箱线图**     | 用于显示数据的分布、异常值及四分分布                 | `df.plot(kind='box')`                         |
| **密度图**     | 用于显示数据的密度分布                               | `df.plot(kind='kde')`                         |
| **饼图**       | 用于显示各部分占总体的比例                           | `df.plot(kind='pie')`                         |
| **区域图**     | 用于显示统计数值的图表（类似于折线图，但填充了颜色） | `df.plot(kind='area')`                        |

##### Seaborn 可视化

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 绘制热力图
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()
```

## Pandas 高级功能

###### merge()

 数据库风格的连接

| **参数**   | **说明**                                                     |
| :--------- | :----------------------------------------------------------- |
| `left`     | 左侧 DataFrame                                               |
| `right`    | 右侧 DataFrame                                               |
| `how`      | 合并方式，支持 `'inner'`, `'outer'`, `'left'`, `'right'`     |
| `on`       | 连接的列名（如果两侧列名不同，可使用 `left_on` 和 `right_on`） |
| `left_on`  | 左侧 DataFrame 的连接列                                      |
| `right_on` | 右侧 DataFrame 的连接列                                      |
| `suffixes` | 添加后缀，以区分重复的列名                                   |

```python
import pandas as pd

# 示例数据
left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})

# 使用 merge 进行内连接
result = pd.merge(left, right, on='ID', how='inner')
print(result)
```

###### concat()

沿轴连接

| **参数**       | **说明**                                     |
| :------------- | :------------------------------------------- |
| `objs`         | 需要合并的 DataFrame 列表                    |
| `axis`         | 合并的轴，`0` 表示按行合并，`1` 表示按列合并 |
| `ignore_index` | 是否忽略索引，重新生成索引（默认为 `False`） |
| `keys`         | 为合并的对象提供层次化索引                   |

```python
import pandas as pd

# 示例数据
df1 = pd.DataFrame({'A': [1, 2, 3]})
df2 = pd.DataFrame({'A': [4, 5, 6]})

# 行合并
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)
```

###### join()

`join()` 方法是 Pandas 中的简化连接操作，通常用于基于索引将多个 DataFrame 连接。

| **参数** | **说明**                                                 |
| :------- | :------------------------------------------------------- |
| `other`  | 需要连接的另一个 DataFrame                               |
| `how`    | 合并方式，支持 `'left'`, `'right'`, `'outer'`, `'inner'` |
| `on`     | 使用的连接列，默认基于索引                               |

```python
import pandas as pd

# 示例数据
left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])

# 使用 join 进行连接
result = left.join(right, how='inner')
print(result)
```

###### pivot_table()

创建透视表

| **参数**     | **说明**                                          |
| :----------- | :------------------------------------------------ |
| `data`       | 输入的数据                                        |
| `values`     | 要汇总的列                                        |
| `index`      | 用作行索引的列                                    |
| `columns`    | 用作列索引的列                                    |
| `aggfunc`    | 聚合函数，默认为 `mean`，可以是 `sum`, `count` 等 |
| `fill_value` | 填充缺失值                                        |

```python
import pandas as pd

# 示例数据
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250]}
df = pd.DataFrame(data)

# 创建透视表
pivot_table = pd.pivot_table(df, values='Sales', index='Date', columns='Category', aggfunc='sum', fill_value=0)
print(pivot_table)
```

###### crosstab()

创建交叉表

| **参数**  | **说明**               |
| :-------- | :--------------------- |
| `index`   | 行标签                 |
| `columns` | 列标签                 |
| `values`  | 用于计算的数据（可选） |
| `aggfunc` | 聚合函数，默认 `count` |

```python
import pandas as pd

# 示例数据
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pd.DataFrame(data)

# 创建交叉表
cross_table = pd.crosstab(df['Category'], df['Region'])
print(cross_table)
```

###### apply()

应用函数到 DataFrame 或 Series 上

| **参数**      | **说明**                                           |
| :------------ | :------------------------------------------------- |
| `func`        | 需要应用的函数                                     |
| `axis`        | 默认为 `0`，表示按列应用；`1` 表示按行应用         |
| `raw`         | 是否传递原始数据（默认为 `False`）                 |
| `result_type` | 定义输出的类型，如 `expand`, `reduce`, `broadcast` |

```python
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# 定义自定义函数
def custom_func(x):
    return x * 2

# 在列上应用函数
df['A'] = df['A'].apply(custom_func)
print(df)
```

###### applymap()

在整个 DataFrame 上应用函数

`applymap()` 只能应用于 DataFrame，作用于 DataFrame 中的每个元素

```python
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# 在 DataFrame 上应用自定义函数
df = df.applymap(lambda x: x ** 2)
print(df)
```

###### map()

应用函数到 Series 上

```python
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': ['cat', 'dog', 'rabbit']})

# 使用字典进行映射
df['A'] = df['A'].map({'cat': 'kitten', 'dog': 'puppy'})
print(df)
```

###### agg()

`agg()` 用于执行复杂的聚合操作，可以传入多个函数来同时计算多个聚合值

```python
import pandas as pd

# 示例数据
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
})

# 使用 agg() 来进行多个聚合操作
grouped = df.groupby('Category')['Value'].agg([sum, min, max])
print(grouped)
```

##### 时间序列处理

###### `date_range()`

生成时间序列

| **参数**  | **说明**                              |
| :-------- | :------------------------------------ |
| `start`   | 起始日期                              |
| `end`     | 结束日期                              |
| `periods` | 生成的时间点数                        |
| `freq`    | 频率（如 `D` 表示天，`H` 表示小时等） |

```python
import pandas as pd

# 生成时间序列
date_range = pd.date_range(start='2024-01-01', periods=5, freq='D')
print(date_range)
```

###### pd.Timedelta() 

```python
import pandas as pd

# 日期偏移
date = pd.to_datetime('2024-01-01')
new_date = date + pd.Timedelta(days=10)
print(new_date)
```

###### rolling()

| **方法**      | **说明**                           |
| :------------ | :--------------------------------- |
| `rolling()`   | 计算滚动窗口操作，常用于移动平均等 |
| `expanding()` | 计算扩展窗口操作，累计值           |

###### expanding()

##### 缺失值处理

| **方法**   | **说明**               |
| :--------- | :--------------------- |
| `isna()`   | 检查缺失值，返回布尔值 |
| `fillna()` | 填充缺失值             |
| `dropna()` | 删除包含缺失值的行或列 |

##### 多重索引

| **参数** | **说明**                   |
| :------- | :------------------------- |
| `tuples` | 每个元组对应一个索引值     |
| `names`  | 每个索引级别的名称（可选） |

###### pd.MultiIndex.from_product()

###### set_index()

`set_index()` 方法可以将 DataFrame 的列转换为多重索引，适用于从已有的数据创建多重索引

```python
import pandas as pd

# 示例数据
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# 设置多重索引
df.set_index(['Letter', 'Number'], inplace=True)
print(df)
```

###### xs()

获取交叉数据

```python
# 使用 xs 获取 'Number' 为 1 的所有数据
print(df.xs(1, level='Number'))
```

###### sort_index()

支持对多重索引进行排序

```python
# 按照多重索引排序
df_sorted = df.sort_index(level=['Letter', 'Number'], ascending=[True, False])
print(df_sorted)
```

###### reset_index()

将多重索引重置为普通的列

```python
# 重设索引
df_reset = df.reset_index()
print(df_reset)
```

###### fillna()

```python
# 示例数据中引入缺失值
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, None, 30, 40]
}

df = pd.DataFrame(data)
df.set_index(['Letter', 'Number'], inplace=True)

# 填充缺失值
df_filled = df.fillna(0)
print(df_filled)
```

