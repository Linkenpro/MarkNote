#### Numpy

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

> 一个强大的N维数组对象 ndarray

##### 安装

```python
pip install numpy
```

###### `numpy.__version__`

查询numpy库版本

```python
import numpy as np

print(np.__version__)
```

##### ndarray 对象

###### 创建ndarray

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

| 名称   | 描述                                                      | 参数 |
| :----- | :-------------------------------------------------------- | ---- |
| object | 数组或嵌套的数列                                          |      |
| dtype  | 数组元素的数据类型，可选参数                              |      |
| copy   | 对象是否需要复制，可选参数                                |      |
| order  | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |      |
| subok  | 默认返回一个与基类类型一致的数组                          |      |
| ndmin  | 指定生成数组的最小维度                                    |      |

```python
import numpy as np

a = np.array([1,2,3])  # 创建一个一维数组
print (a)

b = np.array([[1,  2],  [3,  4]])  # 创建一个二维数组
print (b)

c = np.array([1, 2, 3, 4, 5], ndmin =  2)  # 创建一个二维数组
print (c)

d = np.array([1,  2,  3], dtype = complex)  # 创建一个复数数组
print (d)
```

##### numpy 数据类型

###### int整数类型

| 类型    | 别名 / 等价写法         | 字节   | 取值范围                        |
| ------- | ----------------------- | ------ | ------------------------------- |
| `int8`  | `np.byte`               | 1      | -128 ～ 127                     |
| `int16` | `np.short`              | 2      | -32,768 ～ 32,767               |
| `int32` | `np.intc`（C int）      | 4      | -2,147,483,648 ～ 2,147,483,647 |
| `int64` | `np.int_`（默认）       | 8      | -9.2e18 ～ 9.2e18               |
| `intp`  | 平台指针大小（32/64位） | 4 或 8 | 同 `int32` 或 `int64`           |

###### uint无符号整型

| 类型     | 别名       | 字节 | 取值范围                   |
| -------- | ---------- | ---- | -------------------------- |
| `uint8`  | `np.ubyte` | 1    | 0 ～ 255（常用于图像像素） |
| `uint16` | —          | 2    | 0 ～ 65,535                |
| `uint32` | —          | 4    | 0 ～ 4,294,967,295         |
| `uint64` | —          | 8    | 0 ～ 1.8e19                |

###### float浮点型

| 类型      | 说明                 | 字节 | 精度              |
| --------- | -------------------- | ---- | ----------------- |
| `float16` | 半精度（IEEE 754）   | 2    | 3～4 位有效数字   |
| `float32` | 单精度（C `float`）  | 4    | 6～7 位有效数字   |
| `float64` | 双精度（C `double`） | 8    | 15～16 位有效数字 |
| `float_`  | 等价于 `float64`     | 8    | —                 |

###### complex复数类型

| 类型         | 组成           | 总字节 | 说明                               |
| ------------ | -------------- | ------ | ---------------------------------- |
| `complex64`  | 2 × `float32`  | 8      | 实部+虚部各 4 字节                 |
| `complex128` | 2 × `float64`  | 16     | 实部+虚部各 8 字节（默认复数类型） |
| `complex_`   | = `complex128` | 16     | —                                  |

###### bool布尔型

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
print (a.ndim)

b = a.reshape(2,4,3)
print (b.ndim)
```

###### ndarray.shape

> 表示数组的维度
>
> 返回一个元组，这个元组的长度就是维度的数目，即ndim属性(秩)

```python
import numpy as np  

a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)
```

###### ndarray.itemsize

> 只读属性
>
> 返回数组中每个元素所占的字节数（bytes）

```python
import numpy as np 
 
x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)

y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)
```

###### ndarray.flags

> 用于描述数组的内存布局和行为特性

```python
import numpy as np 
 
x = np.array([1,2,3,4,5])  
print (x.flags)
```

##### numpy创建数组

###### numpy.empty

> 用于快速创建未初始化数组的函数

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

> 创建指定形状、数据类型，并用 0 填充的数组
>
> 科学计算场景中更常见

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

x = np.zeros(5) 
print(x)

y = np.zeros((5,), dtype = int) 
print(y)

z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
```

###### numpy.ones

> 创建指定形状的数组，数组元素以 1 来填充

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

x = np.ones(5)
print(x)

x = np.ones([2,2], dtype = int)
print(x)
```

###### numpy.zeros_like

> 创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充

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

> 创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充

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

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

ones_arr = np.ones_like(arr)
print(ones_arr)
```

##### 从已有数组创建

###### numpy.asarray

> 将输入数据（如列表、元组、其他数组等）转换为 ndarray

```python
numpy.asarray(a, dtype = None, order = None)
```

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组 |
| dtype | 数据类型，(可选)                                             |
| order | 可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

```python
import numpy as np 
 
x = [1,2,3]
a = np.asarray(x)  
print (a)
```

###### numpy.frombuffer

> 用于实现动态数组
>

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

> 用于从可迭代对象（如生成器、列表、元组、集合等）高效创建一维数组的函数
>
> 适用于**内存受限或数据量大**的场景，因为它可以避免先将整个可迭代对象转为列表再创建数组，从而节省内存

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

list=range(5)
it=iter(list)

x=np.fromiter(it, dtype=float)
print(x)
```

###### numpy.arange

> 用于创建等差一维数组（类似 Python 内置的 range，但返回的是 ndarray）的核心函数
>
> 生成数值序列、索引、坐标轴等方面应用极为广泛

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

> 在指定区间内生成等间距数值序列的函数
>
> 适合需要精确控制端点或避免浮点误差的场景

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

> 用于在对数尺度上生成等比（几何）序列的函数
>
> 常用于需要指数级变化的场景，如频率扫描、学习率衰减、对数坐标轴等

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

#### numpy切片和索引

```python
import numpy as np
 
a = np.arange(10)
b = a[2:7:2]
print(b)
```

###### 整数数组索引

```python
import numpy as np 
 
x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  
print (y)
```

###### 布尔索引

```python
import numpy as np 
 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：')
print (x)
print ('\n')

print  ('大于 5 的元素是：')
print (x[x >  5])
```

###### np.isnan

> **~**（取补运算符）来过滤 NaN
>
> 用于检测数组元素是否为NaN（Not a Number）的函数
>
> 在数据清洗、科学计算和机器学习中非常常用，因为 NaN 值会干扰统计计算、模型训练等过程

```python
import numpy as np 

a = np.array([np.nan,  1,2,np.nan,3,4,5])  
print (a[~np.isnan(a)])
```

###### np.iscomplex

> 用于检测数组元素是否为复数（complex）类型的函数
>
> 返回一个布尔数组，标识每个元素是否具有非零虚部

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

print("读取下标对应的行")
print (x[[4,2,1,7]])
```

传入倒序索引数组

```python
import numpy as np 
 
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])
```

#### NumPy 广播

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

> 一个高效、灵活的多维数组迭代器对象
>
> 对**内存布局、数据类型转换、读写控制、多数组广播迭代**等高级功能的支持，特别适合需要高性能或复杂迭代逻辑的场景

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

arr = np.array([[1, 2], [3, 4]])
for x in np.nditer(arr):
    print(x, end=' ')
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
    print (x, end=", ")
```

#### Numpy 数组操作

###### numpy.reshape

> 是 NumPy 中用于改变数组形状（shape）而不改变其数据的核心函数
>
> 它返回一个具有新形状的视图（view）（如果可能），而非副本，因此非常高效

```python
numpy.reshape(arr, newshape, order='C')
```
| 参数       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| `a`        | 输入数组（`ndarray`）                                        |
| `newshape` | 新形状：整数或整数元组（如 `(2, 3)`）。元素总数必须与原数组相同 |
| `order`    | 内存读取/写入顺序： • `'C'`：C 风格（行优先，默认） • `'F'`：Fortran 风格（列优先） • `'A'`：若原数组是 F 连续且非 C 连续，则用 `'F'`，否则用 `'C'` |

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
###### numpy.flat
> 是 NumPy 数组的一个属性，它返回一个 **`numpy.flatiter` **对象
>
> 该对象提供了一种**高效、内存友好**的方式来遍历数组的所有元素

```python
import numpy as np

a = np.arange(9).reshape(3,3) 
print ('原始数组：')
for row in a:
    print (row)

print ('迭代后的数组：')
for element in a.flat:
    print (element)
```
###### numpy.flatten

> 用于将多维数组展平为一维数组
>
> flatten() 总是返回一个全新的副本，修改展平后的数组不会影响原始数据

```python
ndarray.flatten(order='C')
```
| 参数    | 默认值 | 说明                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| `order` | `'C'`  | 元素读取顺序： • `'C'`：C 风格（行优先） • `'F'`：Fortran 风格（列优先） • `'A'`：若原数组是 F 连续则用 `'F'`，否则 `'C'` • `'K'`：按内存中实际存储顺序 |

```python
import numpy as np

a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')

print ('展开的数组：')
print (a.flatten())
print ('\n')

print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))
```
###### numpy.ravel
> numpy.ravel()展平的数组元素，顺序通常是"C风格"，返回的是数组视图

```python
numpy.ravel(a, order='C')
```
| 参数    | 默认值 | 说明                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| `order` | `'C'`  | 元素读取顺序： • `'C'`：C 风格（行优先） • `'F'`：Fortran 风格（列优先） • `'A'`：若原数组是 F 连续则用 `'F'`，否则 `'C'` • `'K'`：按内存中实际存储顺序 |

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
###### numpy.transpose
> 用于交换数组轴（维度）顺序的核心函数

```
numpy.transpose(arr, axes=None)
```
| 参数   | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| `a`    | 输入数组（`ndarray`）                                        |
| `axes` | 可选，指定新轴的顺序： • `None`（默认）：反转所有轴（如 `(0,1,2)` → `(2,1,0)`） • 元组：如 `(2, 0, 1)` 表示原第2轴→新第0轴，原第0轴→新第1轴，等等 |

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

> 用于将指定轴“滚动”到新位置的函数

```python
numpy.rollaxis(arr, axis, start=0)
```
| 参数    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| `a`     | 输入数组（`ndarray`）                                        |
| `axis`  | 要移动的轴（整数，可为负数）                                 |
| `start` | 目标位置（默认 `0`）： • 移动后的 `axis` 将位于 `start` 之前 • 若 `start <= axis`，则 `axis` 插入到 `start` 位置 • 若 `start > axis`，则 `axis` 插入到 `start - 1` 位置 |

```python
import numpy as np

arr = np.random.rand(2, 3, 4)

b = np.rollaxis(arr, axis=2, start=0)
print(b.shape)
```
###### numpy.swapaxes

> 用于交换数组的两个轴（维度） 的函数

```
numpy.swapaxes(arr, axis1, axis2)
```
| 参数    | 说明                               |
| ------- | ---------------------------------- |
| `a`     | 输入数组（`ndarray`）              |
| `axis1` | 第一个要交换的轴（整数，可为负数） |
| `axis2` | 第二个要交换的轴（整数，可为负数） |

```python
import numpy as np

a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('\n')

print ('调用 swapaxes 函数后的数组：')
print (np.swapaxes(a, 2, 0))
```
###### numpy.broadcast

```python
numpy.broadcast(*args)
```

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
> 用于将数组广播（broadcast）到指定新形状的函数
>
> 常用于在不实际复制数据的情况下扩展数组维度以匹配目标形状

```
numpy.broadcast_to(array, shape, subok=False)
```
| 参数    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| `array` | 输入数组（`ndarray` 或可转换对象）                           |
| `shape` | 目标形状（整数或整数元组）                                   |
| `subok` | 若为 `True`，允许子类通过；默认 `False`（返回基类 `ndarray`） |

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

> NumPy 中用于在指定位置插入一个长度为 1 的新轴（维度） 的函数

```
 numpy.expand_dims(arr, axis)
```
| 参数   | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| `a`    | 输入数组（`ndarray`）                                        |
| `axis` | 插入新轴的位置（整数或整数列表）： • 正数：从前往后索引（0 表示最前） • 负数：从后往前索引（-1 表示最后） |

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

> 用于移除数组中长度为 1 的轴（维度） 的函数
>
> 处理深度学习输出、广播结果或从文件加载的数据时非常有用，可以简化数组形状，使其更符合预期

numpy.squeeze 函数从给定数组的形状中删除一维的条目
```
numpy.squeeze(arr, axis=None)
```
| 参数   | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| `a`    | 输入数组（`ndarray`）                                        |
| `axis` | 可选，指定要移除的轴： • `None`（默认）：移除所有长度为 1 的轴 • 整数或整数元组：仅移除指定的轴（必须长度为 1） |

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
##### 连接数组

###### numpy.concatenate

> 沿指定轴连接（拼接）多个数组的核心函数
>
> 处理数组合并、批量数据组装、特征拼接

```python
numpy.concatenate(arrays, axis=0, out=None, dtype=None, casting="same_kind")
```
| 参数      | 默认值        | 说明                                                         |
| --------- | ------------- | ------------------------------------------------------------ |
| `arrays`  | —             | 数组序列（如列表或元组），所有数组必须具有兼容的形状（除拼接轴外，其他维度必须一致） |
| `axis`    | `0`           | 拼接的轴（整数，可为负数）；若为 `None`，则先展平所有数组再拼接 |
| `out`     | `None`        | 可选，指定输出数组（需预分配正确形状）                       |
| `dtype`   | `None`        | 输出数组的数据类型（NumPy ≥1.20）                            |
| `casting` | `"same_kind"` | 数据类型转换规则                                             |

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

print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b)))
print ('\n')
 
print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))
```
###### numpy.stack

> 用于沿新轴（新增维度）堆叠数组的函数
>
> 创建一个全新的维度，并将输入数组作为该维度上的“切片”
>
> 

```
numpy.stack(arrays, axis=0, out=None, dtype=None, casting="same_kind")
```
| 参数      | 默认值        | 说明                                            |
| --------- | ------------- | ----------------------------------------------- |
| `arrays`  | —             | 数组序列（列表/元组），所有数组必须形状完全相同 |
| `axis`    | `0`           | 新轴插入的位置（整数，可为负数）                |
| `out`     | `None`        | 可选，指定输出数组                              |
| `dtype`   | `None`        | 输出数据类型（NumPy ≥1.20）                     |
| `casting` | `"same_kind"` | 数据类型转换规则                                |

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

> numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组

```python
numpy.hstack(tup)
# tup：要拼接的数组序列（如列表或元组）
```

返回新数组（不修改原数组）
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

> 用于沿垂直方向（行方向）拼接数组的便捷函数
>
> 根据输入自动处理维度，常用于将多个向量堆叠成矩阵、合并数据行

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
##### 分割数组

###### numpy.split

> 用于**将数组沿指定轴分割成多个子数组**的函数
>
> 支持**等分**或**按指定位置切分**

```
numpy.split(ary, indices_or_sections, axis)
```
| 参数                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| `ary`                 | 输入数组（`ndarray`）                                        |
| `indices_or_sections` | 分割方式： • 整数 N：将轴等分为 N 份（必须整除） • 索引列表：在指定位置切分（如 `[2, 5]` 表示在索引 2 和 5 处切） |
| `axis`                | 分割的轴（默认 `0`，可为负数）                               |

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

> 用于沿水平方向（列方向）将数组分割成多个子数组的便捷函数

```python
numpy.hsplit(ary, indices_or_sections)
```

| 参数                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| `ary`                 | 输入数组（必须是 1D 或 ≥2D）                                 |
| `indices_or_sections` | 分割方式： • 整数 N：将列轴等分为 N 份（必须整除） • 索引列表：在指定列位置切分（如 `[2, 5]` 表示在第 2 列和第 5 列后切） |

```python
import numpy as np
 
harr = np.floor(10 * np.random.random((2, 6)))
print ('原array：')
print(harr)
 
print ('拆分后：')
print(np.hsplit(harr, 3))
```
###### numpy.vsplit

> 用于沿垂直方向（行方向）将数组分割成多个子数组的便捷函数
>
> 它是 np.split() 在 axis=0 上的特化版本，常用于按行拆分数据集、图像或矩阵

```python
numpy.vsplit(ary, indices_or_sections)
```

| 参数                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| `ary`                 | 输入数组（必须是 ≥2D，1D 数组会报错）                        |
| `indices_or_sections` | 分割方式： • 整数 N：将行轴等分为 N 份（必须整除） • 索引列表：在指定行位置切分（如 `[2, 5]` 表示在第 2 行和第 5 行后切） |

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
##### 数组元素的添加与删除

###### numpy.resize

> numpy.resize 函数返回指定大小的新数组

```python
numpy.resize(arr, shape)
```

| 参数    | 说明     |
| ------- | -------- |
| `ary`   | 输入数组 |
| `shape` | 形状     |

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

print ('修改第二个数组的大小：')
b = np.resize(a,(3,3))
print (b)
```

###### numpy.append

>  NumPy 中用于在数组末尾添加元素或子数组的函数
>
> 返回一个新数组

```
numpy.append(arr, values, axis=None)
```

| 参数     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| `arr`    | 输入数组（将被“追加到”的数组）                               |
| `values` | 要添加的值（数组或标量）                                     |
| `axis`   | 指定轴（默认 `None`）： • `None`：先展平所有输入，再拼接 • 整数：沿指定轴拼接（要求形状兼容） |

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

> 用于在指定位置插入元素或子数组的函数
>
> 返回一个新数组

```python
numpy.insert(arr, obj, values, axis=None)
```

| 参数     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| `arr`    | 输入数组                                                     |
| `obj`    | 插入位置： • 整数（如 `2`） • 列表/数组（如 `[1, 3]`） • 切片（如 `slice(1, 4)`） |
| `values` | 要插入的值（标量、列表或数组） • 若沿轴插入，需匹配目标形状  |
| `axis`   | 插入的轴（默认 `None`）： • `None`：先展平数组，再插入 • 整数：沿指定轴插入 |

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

> 用于**从数组中删除指定元素或子数组**的函数
>
> 

函数返回从输入数组中删除指定子数组的新数组

```
numpy.delete(arr, obj, axis=None)
```

| 参数   | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| `arr`  | 输入数组                                                     |
| `obj`  | 要删除的位置： • 整数（如 `2`） • 列表/数组（如 `[1, 3]`） • 切片（如 `slice(1, 4)` 或 `1:4`） |
| `axis` | 删除的轴（默认 `None`）： • `None`：先展平数组，再删除 • 整数：沿指定轴删除 |

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

> 用于**找出数组中的唯一值**（去重）的函数
>
> 可以返回唯一元素
>
> 提供**索引、逆映射和计数**等丰富信息，是数据清洗、类别分析和集合操作的核心工具

```
numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None, equal_nan=True)
```

| 参数             | 默认值  | 说明                                                         |
| ---------------- | ------- | ------------------------------------------------------------ |
| `ar`             | —       | 输入数组                                                     |
| `return_index`   | `False` | 是否返回唯一值在原数组中首次出现的索引                       |
| `return_inverse` | `False` | 是否返回重构原数组所需的逆映射索引                           |
| `return_counts`  | `False` | 是否返回每个唯一值的出现次数                                 |
| `axis`           | `None`  | 指定去重的轴： • `None`：展平后去重 • 整数：沿指定轴去重（如 `axis=0` 去重行） |
| `equal_nan`      | `True`  | 是否将所有 `NaN` 视为相等（NumPy ≥1.20）                     |

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

> 用于**对数组元素执行逐位“与”（bitwise AND）操作**的函数
>
> 适用于整数类型（包括布尔值），常用于掩码操作、标志位检查、图像处理

```
numpy.bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```



```python
import numpy as np 
 
print ('13 和 17 的二进制形式：')
a,b = 13,17
print (bin(a), bin(b))
print ('\n')
 
print ('13 和 17 的位与：')
print (np.bitwise_and(13, 17))
```

###### numpy.bitwise_or

> NumPy 中用于**对数组元素执行逐位“或”（bitwise OR）操作**的函数
>
> 作用于整数或布尔类型的数组，常用于掩码合并、标志位设置、图像合成等场景

```python
import numpy as np 

a,b = 13,17 
print ('13 和 17 的二进制形式：')
print (bin(a), bin(b))

print ('13 和 17 的位或：')
print (np.bitwise_or(13, 17))
```

###### numpy.invert

```python
numpy.invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

> invert() 函数对数组中整数进行位取反运算，即 0 变成 1，1 变成 0

```python
import numpy as np 

print ('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print (np.invert(np.array([13], dtype = np.uint8)))
print ('\n')

print ('13 的二进制表示：')
print (np.binary_repr(13, width = 8))
print ('\n')

print ('242 的二进制表示：')
print (np.binary_repr(242, width = 8))
```

###### numpy.left_shift

> 对数组元素执行逐位左移（bitwise left shift）操作的函数
>
> 它等价于 x << n，常用于快速乘以 2 的幂、位打包、掩码生成等场景

```python
numpy.left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```



```python
import numpy as np 
 
print ('将 10 左移两位：')
print (np.left_shift(10,2))
print ('\n')
 
print ('10 的二进制表示：')
print (np.binary_repr(10, width = 8))
print ('\n')
 
print ('40 的二进制表示：')
print (np.binary_repr(40, width = 8))
#  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。
```

###### numpy.right_shift

> 用于对数组元素执行逐位右移（bitwise right shift）操作的函数
>
> 常用于快速除以 2 的幂、提取高位、数据压缩等场景

```python
numpy.right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```



```python
import numpy as np 
 
print ('将 40 右移两位：')
print (np.right_shift(40,2))
print ('\n')
 
print ('40 的二进制表示：')
print (np.binary_repr(40, width = 8))
print ('\n')
 
print ('10 的二进制表示：')
print (np.binary_repr(10, width = 8))
#  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。
```

##### NumPy 字符串函数

###### numpy.char.add()
> 依次对两个数组的元素进行字符串连接
>
> 用于**对字符串数组执行逐元素连接（拼接）操作**的函数

```python
numpy.char.add(x1, x2)
```

| 参数       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| `x1`, `x2` | 输入数组或标量（字符串类型） • 支持广播（broadcasting） • 可以是 Python 字符串、字节串或字符串数组 |

```python
import numpy as np 
 
print ('连接两个字符串：')
print (np.char.add(['hello'],[' xyz']))
print ('\n')
 
print ('连接示例：')
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))
```
###### numpy.char.multiply()

> 用于对字符串数组执行逐元素重复（乘法）操作的函数
>
> 高效处理字符串数组的重复操作而设计

```python
numpy.char.multiply(a, i)
```

| 参数 | 说明                                                  |
| ---- | ----------------------------------------------------- |
| `a`  | 输入字符串数组或标量（字符串/字节串）                 |
| `i`  | 重复次数（整数或整数数组） • 支持广播（broadcasting） |

```python
import numpy as np 
 
print (np.char.multiply('Runoob ',3))
```
###### numpy.char.center()

> 用于**对字符串数组中的每个元素进行居中对齐**的函数
>
> 专为高效处理字符串数组的格式化对齐操作而设计

```python
numpy.char.center(a, width, fillchar=' ')
```

用于将字符串居中，并使用指定字符在左侧和右侧进行填充
```python
import numpy as np 
 
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))
```
###### numpy.char.capitalize()

> 函数将字符串的第一个字母转换为大写
>
> 用于对字符串数组中的每个元素执行首字母大写操作的函数

```python
numpy.char.capitalize(a)
```

| 参数 | 说明                                                |
| ---- | --------------------------------------------------- |
| `a`  | 输入字符串数组或标量（支持 Unicode 字符串和字节串） |

```python
import numpy as np 

print (np.char.capitalize('runoob'))
```
###### numpy.char.title()
> 函数将字符串的每个单词的第一个字母转换为大写

```python
import numpy as np
 
print (np.char.title('i like runoob'))
```
###### numpy.char.lower()
> 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower

```python
import numpy as np 
 
#操作数组
print (np.char.lower(['RUNOOB','GOOGLE']))
 
# 操作字符串
print (np.char.lower('RUNOOB'))
```
###### numpy.char.upper()
> 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper

```python
import numpy as np 
 
#操作数组
print (np.char.upper(['runoob','google']))
 
# 操作字符串
print (np.char.upper('runoob'))
```
###### numpy.char.split()
> 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格

```python
import numpy as np 
 
# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))
```
###### numpy.char.splitlines()
> 函数以换行符作为分隔符来分割字符串，并返回数组

```python
import numpy as np 
 
# 换行符 \n
print (np.char.splitlines('i\nlike runoob?')) 
print (np.char.splitlines('i\rlike runoob?'))
```
###### numpy.char.strip()
> 函数用于移除开头或结尾处的特定字符

```python
import numpy as np 
 
# 移除字符串头尾的 a 字符
print (np.char.strip('ashok arunooba','a'))
 
# 移除数组元素头尾的 a 字符
print (np.char.strip(['arunooba','admin','java'],'a'))
```
###### numpy.char.join()
> 函数通过指定分隔符来连接数组中的元素或字符串

```python
import numpy as np 
 
# 操作字符串
print (np.char.join(':','runoob'))
 
# 指定多个分隔符操作数组元素
print (np.char.join([':','-'],['runoob','google']))
```
###### numpy.char.replace()
> 函数使用新字符串替换字符串中的所有子字符串

```python
import numpy as np 
 
print (np.char.replace ('i like runoob', 'oo', 'cc'))
```
###### numpy.char.encode()
> 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器

```python
import numpy as np 
 
a = np.char.encode('runoob', 'cp500') 
print (a)
```
###### numpy.char.decode()
> 函数对编码的元素进行 str.decode() 解码

```python
import numpy as np 
 
a = np.char.encode('runoob', 'cp500') 
print (a)
print (np.char.decode(a,'cp500'))
```
#### NumPy 数学函数

##### 三角函数

###### numpy.sin()

###### numpy.cos()

###### numpy.tan()

NumPy 提供了标准的三角函数：sin()、cos()、tan()。
```python
import numpy as np
 
a = np.array([0,30,45,60,90])
print ('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度  
print (np.sin(a*np.pi/180))
print ('\n')
print ('数组中角度的余弦值：')
print (np.cos(a*np.pi/180))
print ('\n')
print ('数组中角度的正切值：')
print (np.tan(a*np.pi/180))
```

###### numpy.around()

> 用于**对数组元素进行四舍五入**的函数
>
> 提供了灵活的精度控制，是数值计算、数据展示和精度处理中的常用工具

```
numpy.around(a, decimals=0, out=None)
```
| 参数       | 默认值 | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| `a`        | —      | 输入数组或标量                                               |
| `decimals` | `0`    | 保留的小数位数： • 正数：小数点后位数 • `0`：整数 • 负数：小数点前位数（十位、百位等） |
| `out`      | `None` | 可选输出数组（就地操作）                                     |

```python
import numpy as np
 
a = np.array([1.0,5.55,  123,  0.567,  25.532])  
print  ('原数组：')
print (a)
print ('\n')
print ('舍入后：')
print (np.around(a))
print (np.around(a, decimals =  1))
print (np.around(a, decimals =  -1))
```
###### numpy.floor()

```python
numpy.floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

> 用于对数组元素执行向下取整（floor）操作的函数
>
> 将每个元素替换为不大于该元素的最大整数，是数值处理、离散化和数学计算中的基础工具

返回小于或者等于指定表达式的最大整数，即向下取整
```python
import numpy as np
 
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print ('提供的数组：')
print (a)
print ('\n')
print ('修改后的数组：')
print (np.floor(a))
```
###### numpy.ceil()

> 用于对数组元素执行向上取整（ceiling）操作的函数
>
> 将每个元素替换为不小于该元素的最小整数，是数值处理、离散化和数学计算中的基础工具

```python
numpy.ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

返回大于或者等于指定表达式的最小整数，即向上取整
```python
import numpy as np
 
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])  
print  ('提供的数组：')
print (a)
print ('\n')
print ('修改后的数组：')
print (np.ceil(a))
```
##### NumPy 算术函数

###### numpy.add()

```python
numpy.add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

###### numpy.subtract()

> 用于**对两个数组（或标量）执行逐元素减法操作**的通用函数（ufunc）
>
> 它等价于使用 `-` 运算符，但在需要显式函数调用或高级控制时非常有用

```python
numpy.subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

###### numpy.multiply()

> 用于**对两个数组（或标量）执行逐元素乘法操作**的通用函数
>
> 它等价于使用 `*` 运算符，是数值计算中最基础且高频使用的函数之一

```python
numpy.multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

###### numpy.divide()

> 用于**对两个数组（或标量）执行逐元素真除法（true division）操作**的通用函数
>
> 它等价于使用 `/` 运算符，始终返回浮点结果（即使输入是整数），是数值计算中的基础工具

```python
numpy.divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

包含简单的加减乘除: add()，subtract()，multiply() 和 divide()
```python
import numpy as np 
 
a = np.arange(9, dtype = np.float_).reshape(3,3)  
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
b = np.array([10,10,10])  
print (b)
print ('\n')
print ('两个数组相加：')
print (np.add(a,b))
print ('\n')
print ('两个数组相减：')
print (np.subtract(a,b))
print ('\n')
print ('两个数组相乘：')
print (np.multiply(a,b))
print ('\n')
print ('两个数组相除：')
print (np.divide(a,b))
```
###### numpy.reciprocal()

> 用于计算数组中每个元素的倒数

```python
numpy.reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

函数返回参数逐元素的倒数。如 1/4 倒数为 4/1。
```python
import numpy as np

a = np.array([0.25,  1.33,  1,  100])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 reciprocal 函数：')
print (np.reciprocal(a))
```
###### numpy.power()

```python
numpy.power(x1, x2, /, out=None, *, where=True, dtype=None, **kwargs)
```

> 函数将第一个输入数组中的元素作为底数
>
> 计算它与第二个输入数组中相应元素的幂

```python
import numpy as np 

a = np.array([10,100,1000])  
print ('我们的数组是；')
print (a)
print ('\n') 
print ('调用 power 函数：')
print (np.power(a,2))
print ('\n')
print ('第二个数组：')

b = np.array([1,2,3])  
print (b)
print ('\n')
print ('再次调用 power 函数：')
print (np.power(a,b))
```
###### numpy.mod()

```python
numpy.mod(x1, x2, /, out=None, *, where=True, dtype=None, **kwargs)
```

> 计算输入数组中相应元素的相除后的余数
>
> 函数numpy.remainder() 也产生相同的结果

```python
import numpy as np
 
a = np.array([10,20,30]) 
b = np.array([3,5,7])  
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
print (b)
print ('\n')

print ('调用 mod() 函数：')
print (np.mod(a,b))
print ('\n')
print ('调用 remainder() 函数：')
print (np.remainder(a,b))
```
#### NumPy统计函数
提供了很多统计函数，用于从数组中查找最小元素，最大元素，百分位标准差和方差等
###### numpy.amin()

> numpy.amin() 用于计算数组中的元素沿指定轴的最小值

```python
numpy.amin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
```

###### numpy.amax()

> numpy.amax() 用于计算数组中的元素沿指定轴的最大值

```python
numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
```

```python
import numpy as np 
 
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 amin() 函数：')
print (np.amin(a,1))
print ('\n')
print ('再次调用 amin() 函数：')
print (np.amin(a,0))
print ('\n')
print ('调用 amax() 函数：')
print (np.amax(a))
print ('\n')
print ('再次调用 amax() 函数：')
print (np.amax(a, axis =  0))
```
###### numpy.ptp()

> 函数计算数组中元素最大值与最小值的差（最大值 - 最小值）

```python
numpy.ptp(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
```

```python
import numpy as np 
 
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 ptp() 函数：')
print (np.ptp(a))
print ('\n')
print ('沿轴 1 调用 ptp() 函数：')
print (np.ptp(a, axis =  1))
print ('\n')
print ('沿轴 0 调用 ptp() 函数：')
print (np.ptp(a, axis =  0))
```
###### numpy.percentile()

> 位数是统计中使用的度量，表示小于这个值的观察值的百分比。
>
> 函数numpy.percentile()接受以下参数

```python
numpy.percentile(a, q, axis)
```
示例
```python
import numpy as np 
 
a = np.array([[10, 7, 4], [3, 2, 1]])
print ('我们的数组是：')
print (a)
 
print ('调用 percentile() 函数：')
print (np.percentile(a, 50)) 

print (np.percentile(a, 50, axis=0)) 

print (np.percentile(a, 50, axis=1)) 

print (np.percentile(a, 50, axis=1, keepdims=True))
```
###### numpy.median()
> numpy.median() 函数用于计算数组 a 中元素的中位数（中值）

```
numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=<no value>)
```
```python
import numpy as np 
 
a = np.array([[30,65,70],[80,95,10],[50,90,60]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 median() 函数：')
print (np.median(a))
print ('\n')
print ('沿轴 0 调用 median() 函数：')
print (np.median(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 median() 函数：')
print (np.median(a, axis =  1))
```
###### numpy.mean()
> 函数返回数组中元素的算术平均值，如果提供了轴，则沿其计算

```python
numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)
```
示例
```python
import numpy as np 
 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 mean() 函数：')
print (np.mean(a))
print ('\n')
print ('沿轴 0 调用 mean() 函数：')
print (np.mean(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 mean() 函数：')
print (np.mean(a, axis =  1))
```

######  numpy.average()

> 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
>

```
numpy.average(a, axis=None, weights=None, returned=False)
```

- `a`: 输入的数组，可以是一个 NumPy 数组或类似数组的对象。
- `axis`: 可选参数，用于指定在哪个轴上计算加权平均值。如果不提供此参数，则计算整个数组的加权平均值。可以是一个整数表示轴的索引，也可以是一个元组表示多个轴。
- `weights`: 可选参数，用于指定对应数据点的权重。如果不提供权重数组，则默认为等权重。
- `returned`: 可选参数，如果为True，将同时返回加权平均值和权重总和

```python
import numpy as np 
 
a = np.array([1,2,3,4])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 average() 函数：')
print (np.average(a))
print ('\n')
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])  
print ('再次调用 average() 函数：')
print (np.average(a,weights = wts))
print ('\n')
# 如果 returned 参数设为 true，则返回权重的和  
print ('权重的和：')
print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))
```

###### numpy.std()

> 标准差是一组数据平均值分散程度的一种度量
>

```
std = sqrt(mean((x - x.mean())**2))
```

示例

```python
import numpy as np 
 
print (np.std([1,2,3,4]))
```

###### numpy.var()

> 方差
>

```python
import numpy as np
 
print (np.var([1,2,3,4]))
```

#### NumPy 字节交换
###### numpy.ndarray.byteswap()
函数将 ndarray 中每个元素中的字节进行大小端转换
```python
import numpy as np 
 
a = np.array([1,  256,  8755], dtype = np.int16)  
print ('我们的数组是：')
print (a)
print ('以十六进制表示内存中的数据：')
print (map(hex,a))
# byteswap() 函数通过传入 true 来原地交换 
print ('调用 byteswap() 函数：')
print (a.byteswap(True))
print ('十六进制形式：')
print (map(hex,a))
# 我们可以看到字节已经交换了
```
##### NumPy 副本和视图
- 副本是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置。

- 视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。

如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置

###### 无复制
简单的赋值不会创建数组对象的副本。 相反，它使用原始数组的相同id()来访问它。 
```python
import numpy as np 
 
a = np.arange(6)  
print ('我们的数组是：')
print (a)
print ('调用 id() 函数：')
print (id(a))
print ('a 赋值给 b：')
b = a 
print (b)
print ('b 拥有相同 id()：')
print (id(b))
print ('修改 b 的形状：')
b.shape =  3,2  
print (b)
print ('a 的形状也修改了：')
print (a)
```
###### 视图或浅拷贝
ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数变化不会改变原始数据的维数。
```python
import numpy as np 
 
# 最开始 a 是个 3X2 的数组
a = np.arange(6).reshape(3,2)  
print ('数组 a：')
print (a)
print ('创建 a 的视图：')
b = a.view()  
print (b)
print ('两个数组的 id() 不同：')
print ('a 的 id()：')
print (id(a))
print ('b 的 id()：' )
print (id(b))
# 修改 b 的形状，并不会修改 a
b.shape =  2,3
print ('b 的形状：')
print (b)
print ('a 的形状：')
print (a)
```

使用切片创建视图修改数据会影响到原始数组
```python
import numpy as np 
 
arr = np.arange(12)
print ('我们的数组：')
print (arr)
print ('创建切片：')
a=arr[3:]
b=arr[3:]
a[1]=123
b[2]=234
print(arr)
print(id(a),id(b),id(arr[3:]))
```
###### 副本或深拷贝
ndarray.copy() 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。
```python
import numpy as np 
 
a = np.array([[10,10],  [2,3],  [4,5]])  
print ('数组 a：')
print (a)
print ('创建 a 的深层副本：')
b = a.copy()  
print ('数组 b：')
print (b)
# b 与 a 不共享任何内容  
print ('我们能够写入 b 来写入 a 吗？')
print (b is a)
print ('修改 b 的内容：')
b[0,0]  =  100  
print ('修改后的数组 b：')
print (b)
print ('a 保持不变：')
print (a)
```
##### NumPy 矩阵库(Matrix)
NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。
###### 转置矩阵
NumPy 中除了可以使用 numpy.transpose 函数来对换数组的维度，还可以使用 T 属性。
```python
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)
```
###### matlib.empty()
matlib.empty() 函数返回一个新的矩阵，语法格式为：
```
numpy.matlib.empty(shape, dtype, order)
```
示例
```python
import numpy.matlib 
import numpy as np
 
print (np.matlib.empty((2,2)))
# 填充为随机数据
```
###### numpy.matlib.zeros()
numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.zeros((2,2)))
```
###### numpy.matlib.ones()
numpy.matlib.ones()函数创建一个以 1 填充的矩阵。
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.ones((2,2)))
```
###### numpy.matlib.eye()
numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
```python
# numpy.matlib.eye(n, M,k, dtype)

import numpy.matlib 
import numpy as np 
 
print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))
```
###### numpy.matlib.identity()
numpy.matlib.identity() 函数返回给定大小的单位矩阵。
```python
import numpy.matlib 
import numpy as np 
 
# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))
```
###### numpy.matlib.rand()
numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.rand(3,3))

i=np.martix(＇1,2;3,4＇)
print(i)

```
#### NumPy 线性代数

NumPy 提供了线性代数函数库 linalg，该库包含了线性代数所需的所有功能
###### numpy.dot()
对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和
```python
# numpy.dot(a, b, out=None) 

import numpy.matlib
import numpy as np
 
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))
```
###### numpy.vdot()
numpy.vdot() 函数是两个向量的点积
```python
import numpy as np 
 
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
 
# vdot 将数组展开计算内积
print (np.vdot(a,b))
```
###### numpy.inner()
numpy.inner() 函数返回一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积
```python
import numpy as np 
 
print (np.inner(np.array([1,2,3]),np.array([0,1,0])))
# 等价于 1*0+2*1+3*0
```
###### numpy.matmul
numpy.matmul 函数返回两个数组的矩阵乘积
```python
import numpy.matlib 
import numpy as np 
 
a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print (np.matmul(a,b))
```
###### numpy.linalg.det()
numpy.linalg.det() 函数计算输入矩阵的行列式。
行列式在线性代数中是非常有用的值。
```python
import numpy as np
a = np.array([[1,2], [3,4]]) 
 
print (np.linalg.det(a))
```
###### numpy.linalg.solve()
numpy.linalg.solve() 函数给出了矩阵形式的线性方程的解。
###### numpy.linalg.inv()
numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵。
```python
import numpy as np 
 
x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print (x)
print (y)
print (np.dot(x,y))
```
##### NumPy IO
Numpy 可以读写磁盘上的文本数据或二进制数据
###### numpy.save()
```
numpy.save(file, arr, allow_pickle=True, fix_imports=True)
```
###### numpy.load()
读取数据
```python
import numpy as np 
 
b = np.load('outfile.npy')  
print (b)
```

###### numpy.savez()

```
numpy.savez(file, *args, **kwds)
```

- **file**：要保存的文件，扩展名为 **.npz**，如果文件路径末尾没有扩展名 **.npz**，该扩展名会被自动加上。
- **args**: 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名为 **arr_0**, **arr_1**, …　。
- **kwds**: 要保存的数组使用关键字名称。

```python
import numpy as np 
 
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sin_array
np.savez("runoob.npz", a, b, sin_array = c)
r = np.load("runoob.npz")  
print(r.files) # 查看各个数组名称
print(r["arr_0"]) # 数组 a
print(r["arr_1"]) # 数组 b
print(r["sin_array"]) # 数组 c
```

###### numpy.savetxt()

> 

```
np.loadtxt(FILENAME, dtype=int, delimiter=' ')
np.savetxt(FILENAME, a, fmt="%d", delimiter=",")
```

示例

```python
import numpy as np 
 
a = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt')  
 
print(b)
```

使用 delimiter 参数

```python
import numpy as np 
 
 
a=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt("out.txt",a,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
b = np.loadtxt("out.txt",delimiter=",") # load 时也要指定为逗号分隔
print(b)
```

