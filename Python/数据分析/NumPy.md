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

###### numpy.reshape
```python
numpy.reshape(arr, newshape, order='C')
```
arr：要修改形状的数组
newshape：
```python
import numpy as np
 
a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)

```
###### numpy.ndarray.flat
numpy.ndarray.flat 是一个数组元素迭代器
```python
import numpy as np
 
a = np.arange(9).reshape(3,3) 
print ('原始数组：')
for row in a:
    print (row)
 
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print ('迭代后的数组：')
for element in a.flat:
    print (element)
```
###### numpy.ndarray.flatten
返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
```python
ndarray.flatten(order='C')
```
例子
```python
import numpy as np
 
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
# 默认按行
 
print ('展开的数组：')
print (a.flatten())
print ('\n')
 
print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))
```
###### numpy.ravel
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图
```python
numpy.ravel(a, order='C')
```
示例
```python
import numpy as np
 
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 ravel 函数之后：')
print (a.ravel())
print ('\n')
 
print ('以 F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))
```
翻转数组
函数	描述
transpose	对换数组的维度
ndarray.T	和 self.transpose() 相同
rollaxis	向后滚动指定的轴
swapaxes	对换数组的两个轴
###### numpy.transpose
对换数组的维度
```
numpy.transpose(arr, axes)
```
例子
```python
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))
```
###### numpy.rollaxis

```
numpy.rollaxis(arr, axis, start)
```

```python
import numpy as np
 
# 创建了三维的 ndarray
a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('获取数组中一个值：')
print(np.where(a==6))   
print(a[1,1,0])  # 为 6
print ('\n')
 
 
# 将轴 2 滚动到轴 0（宽度到深度）
 
print ('调用 rollaxis 函数：')
b = np.rollaxis(a,2,0)
print (b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b==6))   
print ('\n')
 
# 将轴 2 滚动到轴 1：（宽度到高度）
 
print ('调用 rollaxis 函数：')
c = np.rollaxis(a,2,1)
print (c)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c==6))   
print ('\n')
```
###### numpy.swapaxes
```
numpy.swapaxes(arr, axis1, axis2)
```
- arr：输入的数组
- axis1：对应第一个轴的整数
- axis2：对应第二个轴的整数
```python
import numpy as np
 
# 创建了三维的 ndarray
a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
 
print ('调用 swapaxes 函数后的数组：')
print (np.swapaxes(a, 2, 0))
```
###### numpy.broadcast
用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
```python
import numpy as np
 
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])  
 
# 对 y 广播 x
b = np.broadcast(x,y)  
# 它拥有 iterator 属性，基于自身组件的迭代器元组
 
print ('对 y 广播 x：')
r,c = b.iters
 
# Python3.x 为 next(context) ，Python2.x 为 context.next()
print (next(r), next(c))
print (next(r), next(c))
print ('\n')
# shape 属性返回广播对象的形状
 
print ('广播对象的形状：')
print (b.shape)
print ('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x,y)
c = np.empty(b.shape)
 
print ('手动使用 broadcast 将 x 与 y 相加：')
print (c.shape)
print ('\n')
c.flat = [u + v for (u,v) in b]
 
print ('调用 flat 函数：')
print (c)
print ('\n')
# 获得了和 NumPy 内建的广播支持相同的结果
 
print ('x 与 y 的和：')
print (x + y)
```
###### numpy.broadcast_to
广播到新形状
```
numpy.broadcast_to(array, shape, subok)
```
1
```python
import numpy as np
 
a = np.arange(4).reshape(1,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 broadcast_to 函数之后：')
print (np.broadcast_to(a,(4,4)))
```
###### numpy.expand_dims
```
 numpy.expand_dims(arr, axis)
```
1
```python
import numpy as np
 
x = np.array(([1,2],[3,4]))
 
print ('数组 x：')
print (x)
print ('\n')
y = np.expand_dims(x, axis = 0)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)
print ('\n')
# 在位置 1 插入轴
y = np.expand_dims(x, axis = 1)
 
print ('在位置 1 插入轴之后的数组 y：')
print (y)
print ('\n')
 
print ('x.ndim 和 y.ndim：')
print (x.ndim,y.ndim)
print ('\n')
 
print ('x.shape 和 y.shape：')
print (x.shape, y.shape)
```
###### numpy.squeeze
numpy.squeeze 函数从给定数组的形状中删除一维的条目
```
numpy.squeeze(arr, axis)
```
1
```python
import numpy as np
 
x = np.arange(9).reshape(1,3,3)
 
print ('数组 x：')
print (x)
print ('\n')
y = np.squeeze(x)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)
```
**连接数组**
###### numpy.concatenate
```
numpy.concatenate((a1, a2, ...), axis)
```
参数
```python
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
# 两个数组的维度相同
 
print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b)))
print ('\n')
 
print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))
```
###### numpy.stack
```
numpy.stack(arrays, axis)
```
折叠
```python
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('沿轴 0 堆叠两个数组：')
print (np.stack((a,b),0))
print ('\n')
 
print ('沿轴 1 堆叠两个数组：')
print (np.stack((a,b),1))
```
###### numpy.hstack
numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
```python
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('水平堆叠：')
c = np.hstack((a,b))
print (c)
print ('\n')
```
###### numpy.vstack

```python
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('竖直堆叠：')
c = np.vstack((a,b))
print (c)
```
**分割数组**
###### numpy.split
```
numpy.split(ary, indices_or_sections, axis)
```
例子
```python
import numpy as np
 
a = np.arange(9)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('将数组分为三个大小相等的子数组：')
b = np.split(a,3)
print (b)
print ('\n')
 
print ('将数组在一维数组中表明的位置分割：')
b = np.split(a,[4,7])
print (b)
```
###### numpy.hsplit
numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组
```python
import numpy as np
 
harr = np.floor(10 * np.random.random((2, 6)))
print ('原array：')
print(harr)
 
print ('拆分后：')
print(np.hsplit(harr, 3))
```
###### numpy.vsplit
numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同
```python
import numpy as np
 
a = np.arange(16).reshape(4,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('竖直分割：')
b = np.vsplit(a,2)
print (b)
```
**数组元素的添加与删除**
###### numpy.resize
numpy.resize 函数返回指定大小的新数组
```
numpy.resize(arr, shape)
```

- `arr`：要修改大小的数组
- `shape`：返回数组的新形状

```python
import numpy as np
 
a = np.array([[1,2,3],[4,5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('第一个数组的形状：')
print (a.shape)
print ('\n')
b = np.resize(a, (3,2))
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('第二个数组的形状：')
print (b.shape)
print ('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
 
print ('修改第二个数组的大小：')
b = np.resize(a,(3,3))
print (b)
```

###### numpy.append

```
numpy.append(arr, values, axis=None)
```

示例

```python
import numpy as np
 
a = np.array([[1,2,3],[4,5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('向数组添加元素：')
print (np.append(a, [7,8,9]))
print ('\n')
 
print ('沿轴 0 添加元素：')
print (np.append(a, [[7,8,9]],axis = 0))
print ('\n')
 
print ('沿轴 1 添加元素：')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))
```

###### numpy.insert

```
numpy.insert(arr, obj, values, axis)
```

- `arr`：输入数组
- `obj`：在其之前插入值的索引
- `values`：要插入的值
- `axis`：沿着它插入的轴，如果未提供，则输入数组会被展开

```python
import numpy as np
 
a = np.array([[1,2],[3,4],[5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('未传递 Axis 参数。 在删除之前输入数组会被展开。')
print (np.insert(a,3,[11,12]))
print ('\n')
print ('传递了 Axis 参数。 会广播值数组来配输入数组。')
 
print ('沿轴 0 广播：')
print (np.insert(a,1,[11],axis = 0))
print ('\n')
 
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))
```

###### numpy.delete

函数返回从输入数组中删除指定子数组的新数组

```
Numpy.delete(arr, obj, axis)
```

- `arr`：输入数组
- `obj`：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
- `axis`：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开

```python
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print (np.delete(a,5))
print ('\n')
 
print ('删除第二列：')
print (np.delete(a,1,axis = 1))
print ('\n')
 
print ('包含从数组中删除的替代值的切片：')
a = np.array([1,2,3,4,5,6,7,8,9,10])
print (np.delete(a, np.s_[::2]))
```

###### numpy.unique

```
numpy.unique(arr, return_index, return_inverse, return_counts)
```

- `arr`：输入数组，如果不是一维数组则会展开
- `return_index`：如果为`true`，返回新列表元素在旧列表中的位置（下标），并以列表形式储
- `return_inverse`：如果为`true`，返回旧列表元素在新列表中的位置（下标），并以列表形式储
- `return_counts`：如果为`true`，返回去重数组中的元素在原数组中的出现次数

```python
import numpy as np
 
a = np.array([5,2,6,2,7,5,6,8,2,9])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('第一个数组的去重值：')
u = np.unique(a)
print (u)
print ('\n')
 
print ('去重数组的索引数组：')
u,indices = np.unique(a, return_index = True)
print (indices)
print ('\n')
 
print ('我们可以看到每个和原数组下标对应的数值：')
print (a)
print ('\n')
 
print ('去重数组的下标：')
u,indices = np.unique(a,return_inverse = True)
print (u)
print ('\n')
 
print ('下标为：')
print (indices)
print ('\n')
 
print ('使用下标重构原数组：')
print (u[indices])
print ('\n')
 
print ('返回去重元素的重复数量：')
u,indices = np.unique(a,return_counts = True)
print (u)
print (indices)
```

##### NumPy 位运算

| 操作     | 函数/运算符                 | 描述                                     |
| :------- | :-------------------------- | :--------------------------------------- |
| 按位与   | `numpy.bitwise_and(x1, x2)` | 对数组的每个元素执行逐位与操作。         |
| 按位或   | `numpy.bitwise_or(x1, x2)`  | 对数组的每个元素执行逐位或操作。         |
| 按位异或 | `numpy.bitwise_xor(x1, x2)` | 对数组的每个元素执行逐位异或操作。       |
| 按位取反 | `numpy.invert(x)`           | 对数组的每个元素执行逐位取反（按位非）。 |
| 左移     | `numpy.left_shift(x1, x2)`  | 将数组的每个元素左移指定的位数。         |
| 右移     | `numpy.right_shift(x1, x2)` | 将数组的每个元素右移指定的位数。         |

###### numpy.bitwise_and

函数对数组中整数的二进制形式执行位与运算

```python
import numpy as np 
 
print ('13 和 17 的二进制形式：')
a,b = 13,17
print (bin(a), bin(b))
print ('\n')
 
print ('13 和 17 的位与：')
print (np.bitwise_and(13, 17))
```

