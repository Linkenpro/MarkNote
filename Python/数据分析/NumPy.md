#### Numpy

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

> 一个强大的N维数组对象 ndarray

##### 安装与版本查询

```python
# 按装numpy
pip install numpy

# 导入库
import numpy as np
print(np.__version__)
```

##### ndarray 对象

###### 创建ndarray

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

| 名称   | 描述                                                      |
| :----- | :-------------------------------------------------------- |
| object | 数组或嵌套的数列                                          |
| dtype  | 数组元素的数据类型，可选参数                              |
| copy   | 对象是否需要复制，可选参数                                |
| order  | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |
| subok  | 默认返回一个与基类类型一致的数组                          |
| ndmin  | 指定生成数组的最小维度                                    |

```python
# 导入numpy
import numpy as np

a = np.array([1,2,3])  
print (a)

b = np.array([[1,  2],  [3,  4]])  
print (b)

c = np.array([1, 2, 3, 4, 5], ndmin =  2)  
print (c)

# dtype 参数  
d = np.array([1,  2,  3], dtype = complex)  
print (d)
```

##### numpy 数据类型

###### 整数类型

| 类型（NumPy） | 别名 / 等价写法         | 字节（Bytes） | 取值范围                        |
| ------------- | ----------------------- | ------------- | ------------------------------- |
| `int8`        | `np.byte`               | 1             | -128 ～ 127                     |
| `int16`       | `np.short`              | 2             | -32,768 ～ 32,767               |
| `int32`       | `np.intc`（C int）      | 4             | -2,147,483,648 ～ 2,147,483,647 |
| `int64`       | `np.int_`（默认）       | 8             | -9.2e18 ～ 9.2e18               |
| `intp`        | 平台指针大小（32/64位） | 4 或 8        | 同 `int32` 或 `int64`           |

###### 无符号整型

| 类型     | 别名       | 字节 | 取值范围                   |
| -------- | ---------- | ---- | -------------------------- |
| `uint8`  | `np.ubyte` | 1    | 0 ～ 255（常用于图像像素） |
| `uint16` | —          | 2    | 0 ～ 65,535                |
| `uint32` | —          | 4    | 0 ～ 4,294,967,295         |
| `uint64` | —          | 8    | 0 ～ 1.8e19                |

###### 浮点型

| 类型      | 别名 / 说明          | 字节 | 精度（约）        | 默认？         |
| --------- | -------------------- | ---- | ----------------- | -------------- |
| `float16` | 半精度（IEEE 754）   | 2    | 3～4 位有效数字   | ❌              |
| `float32` | 单精度（C `float`）  | 4    | 6～7 位有效数字   | ❌              |
| `float64` | 双精度（C `double`） | 8    | 15～16 位有效数字 | ✅ 默认浮点类型 |
| `float_`  | 等价于 `float64`     | 8    | —                 | ✅              |

###### 复数

| 类型         | 组成           | 总字节 | 说明                               |
| ------------ | -------------- | ------ | ---------------------------------- |
| `complex64`  | 2 × `float32`  | 8      | 实部+虚部各 4 字节                 |
| `complex128` | 2 × `float64`  | 16     | 实部+虚部各 8 字节（默认复数类型） |
| `complex_`   | = `complex128` | 16     | —                                  |

###### 布尔型

| 类型   | 字节 | 取值             |
| ------ | ---- | ---------------- |
| `bool` | 1    | `True` / `False` |

###### numpy.dtype

数据类型转换

```python
numpy.dtype(object, align, copy)
```

- object - 要转换为的数据类型对象
- align - 如果为 true，填充字段使其类似 C 的结构体。
- copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用

##### numpy 数组属性

| 属性               | 说明                                                         |
| :----------------- | :----------------------------------------------------------- |
| `ndarray.ndim`     | 数组的秩（rank），即数组的维度数量或轴的数量。               |
| `ndarray.shape`    | 数组的维度，表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数。 |
| `ndarray.size`     | 数组中元素的总个数，等于 `ndarray.shape` 中各个轴上大小的乘积。 |
| `ndarray.dtype`    | 数组中元素的数据类型。                                       |
| `ndarray.itemsize` | 数组中每个元素的大小，以字节为单位。                         |
| `ndarray.flags`    | 包含有关内存布局的信息，如是否为 C 或 Fortran 连续存储，是否为只读等。 |
| `ndarray.real`     | 数组中每个元素的实部（如果元素类型为复数）。                 |
| `ndarray.imag`     | 数组中每个元素的虚部（如果元素类型为复数）。                 |
| `ndarray.data`     | 实际存储数组元素的缓冲区，一般通过索引访问元素，不直接使用该属性。 |

###### ndarray.ndim

> 获取数组的维度数量

```python
import numpy as np 
 
a = np.arange(24)  
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)
```

###### ndarray.shape

> 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)

```python
import numpy as np  
 
a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)
```

###### ndarray.itemsize



```python
import numpy as np 
 
# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)
 
# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)
```

###### ndarray.flags

```python
import numpy as np 
 
x = np.array([1,2,3,4,5])  
print (x.flags)
```

##### numpy创建数组

###### numpy.empty

```python
numpy.empty(shape, dtype = float, order = 'C')
```

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| shape | 数组形状                                                     |
| dtype | 数据类型，可选参数                                           |
| order | 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

```python
import numpy as np 

x = np.empty([3,2], dtype = int) 
print (x)
```

###### numpy.zeros

```python
numpy.zeros(shape, dtype = float, order = 'C')
```

| 参数  | 描述                                                |
| :---- | :-------------------------------------------------- |
| shape | 数组形状                                            |
| dtype | 数据类型，可选                                      |
| order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |

```python
import numpy as np
 
# 默认为浮点数
x = np.zeros(5) 
print(x)
 
# 设置类型为整数
y = np.zeros((5,), dtype = int) 
print(y)
 
# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
```

###### numpy.ones

```python
numpy.ones(shape, dtype = None, order = 'C')
```

| 参数  | 描述                                                |
| :---- | :-------------------------------------------------- |
| shape | 数组形状                                            |
| dtype | 数据类型，可选                                      |
| order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |

```python
import numpy as np
 
# 默认为浮点数
x = np.ones(5) 
print(x)
 
# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)
```

###### numpy.zeros_like

```python
numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
```

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 给定要创建相同形状的数组                                     |
| dtype | 创建的数组的数据类型                                         |
| order | 数组在内存中的存储顺序，可选值为 'C'（按行优先）或 'F'（按列优先），默认为 'K'（保留输入数组的存储顺序） |
| subok | 是否允许返回子类，如果为 True，则返回一个子类对象，否则返回一个与 a 数组具有相同数据类型和存储顺序的数组 |
| shape | 创建的数组的形状，如果不指定，则默认为 a 数组的形状。        |

```python
import numpy as np
 
# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)
```

###### numpy.ones_like

```python
numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)
```

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 给定要创建相同形状的数组                                     |
| dtype | 创建的数组的数据类型                                         |
| order | 数组在内存中的存储顺序，可选值为 'C'（按行优先）或 'F'（按列优先），默认为 'K'（保留输入数组的存储顺序） |
| subok | 是否允许返回子类，如果为 True，则返回一个子类对象，否则返回一个与 a 数组具有相同数据类型和存储顺序的数组 |
| shape | 创建的数组的形状，如果不指定，则默认为 a 数组的形状。        |

```python
import numpy as np
 
# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)
```

###### numpy.asarray

```python
numpy.asarray(a, dtype = None, order = None)
```

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组 |
| dtype | 数据类型，可选                                               |
| order | 可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

```python
import numpy as np 
 
x =  [1,2,3] 
a = np.asarray(x)  
print (a)
```

###### numpy.frombuffer

用于实现动态数组

```python
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
```

| 参数   | 描述                                     |
| :----- | :--------------------------------------- |
| buffer | 可以是任意对象，会以流的形式读入。       |
| dtype  | 返回数组的数据类型，可选                 |
| count  | 读取的数据数量，默认为-1，读取所有数据。 |
| offset | 读取的起始位置，默认为0。                |

```python
import numpy as np 
 
s =  b'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print (a)
```

###### numpy.fromiter

```python
numpy.fromiter(iterable, dtype, count=-1)
```

| 参数     | 描述                                   |
| :------- | :------------------------------------- |
| iterable | 可迭代对象                             |
| dtype    | 返回数组的数据类型                     |
| count    | 读取的数据数量，默认为-1，读取所有数据 |

```python
import numpy as np 
 
# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)
 
# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float)
print(x)
```

###### numpy.arange

```python
numpy.arange(start, stop, step, dtype)
```

| 参数    | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| `start` | 起始值，默认为`0`                                            |
| `stop`  | 终止值（不包含）                                             |
| `step`  | 步长，默认为`1`                                              |
| `dtype` | 返回`ndarray`的数据类型，如果没有提供，则会使用输入数据的类型。 |

```python
import numpy as np
 
x = np.arange(5)  
print (x)
```

###### numpy.linspace

数组是一个等差数列构成的

```python
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
```

| 参数       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| `start`    | 序列的起始值                                                 |
| `stop`     | 序列的终止值，如果`endpoint`为`true`，该值包含于数列中       |
| `num`      | 要生成的等步长的样本数量，默认为`50`                         |
| `endpoint` | 该值为 `true` 时，数列中包含`stop`值，反之不包含，默认是True。 |
| `retstep`  | 如果为 True 时，生成的数组中会显示间距，反之不显示。         |
| `dtype`    | `ndarray` 的数据类型                                         |

```python
import numpy as np
a = np.linspace(1,10,10)
print(a)
```

###### numpy.logspace

函数用于创建一个于等比数列

```python
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
```

| 参数       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| `start`    | 序列的起始值为：base ** start                                |
| `stop`     | 序列的终止值为：base ** stop。如果`endpoint`为`true`，该值包含于数列中 |
| `num`      | 要生成的等步长的样本数量，默认为`50`                         |
| `endpoint` | 该值为 `true` 时，数列中中包含`stop`值，反之不包含，默认是True。 |
| `base`     | 对数 log 的底数。                                            |
| `dtype`    | `ndarray` 的数据类型                                         |

##### numpy 切片和索引

```python
import numpy as np
 
a = np.arange(10)  
# 分隔切片参数 start:stop:step
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
```

###### 整数数组索引

```python
import numpy as np 
 
x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  
print (y)

# [1  4  5]
```

###### 布尔索引

```python
import numpy as np 
 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素  
print  ('大于 5 的元素是：')
print (x[x >  5])
```

###### np.isnan

**~**（取补运算符）来过滤 NaN

```python
import numpy as np 
 
a = np.array([np.nan,  1,2,np.nan,3,4,5])  
print (a[~np.isnan(a)])
```

###### np.iscomplex

```python
import numpy as np 
 
a = np.array([1,  2+6j,  5,  3.5+5j])  
print (a[np.iscomplex(a)])
```

###### 二维数组

```python
import numpy as np 
 
x=np.arange(32).reshape((8,4))
print(x)
# 二维数组读取指定下标对应的行
print("-------读取下标对应的行-------")
print (x[[4,2,1,7]])
```

传入倒序索引数组

```python
import numpy as np 
 
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])
```

##### NumPy 广播

当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制

```python
import numpy as np 
 
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a + b)
```

##### 迭代数组

###### numpy.nditer

```python
numpy.nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K', ...)
```

| 参数        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| `op`        | 要迭代的数组（或数组元组，用于多数组广播迭代）               |
| `flags`     | 控制迭代行为的标志（如 `'multi_index'`, `'c_index'`, `'refs_ok'` 等） |
| `op_flags`  | 每个操作数的访问权限（如 `['readonly']`, `['readwrite']`, `['writeonly']`） |
| `op_dtypes` | 指定迭代时使用的数据类型（常用于类型转换）                   |
| `order`     | 内存访问顺序：`'C'`（行优先）、`'F'`（列优先）、`'K'`（保持原布局，默认） |

```python
import numpy as np
 
a = np.arange(6).reshape(2,3)
print ('原始数组是：')
print (a)
print ('\n')

print ('迭代输出元素：')
for x in np.nditer(a):
    print (x, end=", " )
print ('\n')
```

- `for x in np.nditer(a, order='F'):`Fortran order，即是列序优先；
- `for x in np.nditer(a.T, order='C'):`C order，即是行序优先；

```python
import numpy as np
 
a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print ('原始数组是：') 
print (a) 
print ('\n') 
print ('原始数组的转置是：') 
b = a.T 
print (b) 
print ('\n') 
print ('以 C 风格顺序排序：') 
c = b.copy(order='C')  
print (c)
for x in np.nditer(c):  
    print (x, end=", " )
print  ('\n') 
print  ('以 F 风格顺序排序：')
c = b.copy(order='F')  
print (c)
for x in np.nditer(c):  
    print (x, end=", " )
```

##### Numpy 数组操作

修改数组形状
翻转数组
修改数组维度
连接数组
分割数组
数组元素的添加与删除
