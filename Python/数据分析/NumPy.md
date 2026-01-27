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

