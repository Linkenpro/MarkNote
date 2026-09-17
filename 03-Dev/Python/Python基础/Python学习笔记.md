# Python语法基础

## 代码规范

##### 注释

> 基本写法
>
> 三引号为字符串

```py
# 单行注释

"""
多行注释
多行注释
多行注释
"""
```

注释快捷键：`Ctrl+/`

##### 语句分隔符

- 回车换行
- 分号

```python
# 不推荐写法
print("hello yuan");print("hello world")
```



##### 变量命名

###### 变量名规范

```python
# 小写+下划线
# 变量名，类方法，函数
lower_underscore = 0

# 大写+下划线
# 表示常量
UPPER_UNDERSCORE = 1

# 大驼峰命名
# 类的定义
CamelCase = 2

# 小驼峰命名
mixedCase = 3
```

```python
# 单下划线
# 弱私有变量
for _ in  range(10):
    print(random)
    
class Myclass:
    def __init_ (self):
        self. secret = 0

#双下划线
o = MyClass()
# 防君子不防小人
print(o._Myclass__secret)

#前后双下划线

```



###### 保留关键字（35个）

| **类别**     | **关键字** | **说明**                               |
| :----------- | :--------- | :------------------------------------- |
| **逻辑值**   | `True`     | 布尔真值                               |
|              | `False`    | 布尔假值                               |
|              | `None`     | 表示空值或无值                         |
| **逻辑运算** | `and`      | 逻辑与运算                             |
|              | `or`       | 逻辑或运算                             |
|              | `not`      | 逻辑非运算                             |
| **条件控制** | `if`       | 条件判断语句                           |
|              | `elif`     | 否则如果（else if 的缩写）             |
|              | `else`     | 否则分支                               |
| **循环控制** | `for`      | 迭代循环                               |
|              | `while`    | 条件循环                               |
|              | `break`    | 跳出循环                               |
|              | `continue` | 跳过当前循环的剩余部分，进入下一次迭代 |
| **异常处理** | `try`      | 尝试执行代码块                         |
|              | `except`   | 捕获异常                               |
|              | `finally`  | 无论是否发生异常都会执行的代码块       |
|              | `raise`    | 抛出异常                               |
| **函数定义** | `def`      | 定义函数                               |
|              | `return`   | 从函数返回值                           |
|              | `lambda`   | 创建匿名函数                           |
| **类与对象** | `class`    | 定义类                                 |
|              | `del`      | 删除对象引用                           |
| **模块导入** | `import`   | 导入模块                               |
|              | `from`     | 从模块导入特定部分                     |
|              | `as`       | 为导入的模块或对象创建别名             |
| **作用域**   | `global`   | 声明全局变量                           |
|              | `nonlocal` | 声明非局部变量（用于嵌套函数）         |
| **异步编程** | `async`    | 声明异步函数                           |
|              | `await`    | 等待异步操作完成                       |
| **其他**     | `assert`   | 断言，用于测试条件是否为真             |
|              | `in`       | 检查成员关系                           |
|              | `is`       | 检查对象身份（是否是同一个对象）       |
|              | `pass`     | 空语句，用于占位                       |
|              | `with`     | 上下文管理器，用于资源管理             |
|              | `yield`    | 从生成器函数返回值                     |

> 

##### python代码编码

Python源代码也是一个文本文件

> 在源代码中写的中文输出可能会有乱码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```



## 数据类型

##### 整数`int`

##### 浮点数`float`

##### 布尔值`boolean`

##### 空值`None`

基础类型

Number类型

String类型

布尔型

##### 类型转换`type()`

## 数据结构

### 列表`List`

##### 增

| 列表方法                   | 说明                                              |
| :------------------------- | :------------------------------------------------ |
| `list.append(x)`           | 在列表末尾添加一个元素                            |
| `list.extend(iterable)`    | 将可迭代对象中的每个元素逐一添加到末尾            |
| `list.insert(i, x)`        | 在索引 `i` 处插入元素 `x`（原位置及之后元素后移） |
| `new_list = list1 + list2` | 创建新列表，不修改原列表                          |

```python
# 新增列表
lst = [1, 2]
lst.append(3)        # [1, 2, 3]
lst.extend([4, 5])   # [1, 2, 3, 4, 5]
lst.insert(0, 0)     # [0, 1, 2, 3, 4, 5]
```

##### 删

| 语法             | 说明                                                   |
| :--------------- | :----------------------------------------------------- |
| `list.remove(x)` | 删除第一个值为 `x` 的元素，若不存在则报错              |
| `list.pop(i)`    | 删除索引 `i` 处元素并返回它；默认 `pop()` 删除末尾元素 |
| `del list[i]`    | 删除指定索引的元素                                     |
| `list.clear()`   | 移除所有元素，变为空列表 `[]`                          |

```python
# 新增列表
lst = [1, 2, 3, 2]
lst.remove(2)    # [1, 3, 2] （只删第一个2）
lst.pop()        # 返回2，列表变为 [1, 3]
del lst[0]       # [3]
lst.clear()      # []
```



##### 改

| 语法                         | 说明                          |
| :--------------------------- | :---------------------------- |
| `list[i] = x`                | 将索引 `i` 处的元素替换为 `x` |
| `list[start:end] = iterable` | 用可迭代对象替换指定切片范围  |

```python
lst = [1, 2, 3]
lst[0] = 10          # [10, 2, 3]
lst[1:3] = [20, 30]  # [10, 20, 30]
```

##### 查

| 语法                   | 说明                                    |
| :--------------------- | :-------------------------------------- |
| `list[i]`              | 获取索引 `i` 处的元素                   |
| `list[start:end:step]` | 获取子列表（左闭右开）                  |
| `list.index(x)`        | 返回第一个值为 `x` 的索引，不存在则报错 |
| `x in list`            | 返回 `True/False`                       |
| `list.count(x)`        | 返回 `x` 在列表中出现的次数             |
| `len(list)`            | 返回列表元素个数                        |

###### 列表切片

```python
# 新增列表
l=[1,2,3,4,5]

# 取第二个
l[1]

# 取前三个，包含头部，但不含尾部
l[0:3]

# 从第一个取到最后一个
l[1:]
```

###### 列表长度查询`len()`

列表长度查询`len()`

### 元组`Tuple`

- 有序
- 不可变
- 允许重复元素

```python
classmates = ('Michael', 'Bob', 'Tracy')

# 创建空元组
tup1 = ()
```

##### 查：访问元组

| 操作       | 语法                | 说明                      |
| :--------- | :------------------ | :------------------------ |
| 按索引取值 | `t[i]`              | 获取索引 `i` 处的元素     |
| 切片       | `t[start:end:step]` | 返回新元组（原元组不变）  |
| 查找索引   | `t.index(x)`        | 返回第一个值为 `x` 的索引 |
| 统计次数   | `t.count(x)`        | 返回 `x` 出现的次数       |
| 判断存在   | `x in t`            | 返回 `True/False`         |
| 长度       | `len(t)`            | 元素个数                  |

```python
#!/usr/bin/python3
 
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
```

##### 删

```
删除元组
```



### 字典`Dict`

- 无序（Python 3.7+ 保持插入顺序）
- 可变
- 键唯一
- 值可重复
- 用 `{}` 表示
- 存储 **键值对（key: value）**

##### 增

| 操作                   | 语法                         | 说明                                                   |
| :--------------------- | :--------------------------- | :----------------------------------------------------- |
| 添加/修改单个键值对    | `d[key] = value`             | 若 key 不存在则新增，存在则更新                        |
| 批量添加/更新          | `d.update(other_dict)`       | 合并另一个字典，相同键会被覆盖                         |
| 设置默认值（若不存在） | `d.setdefault(key, default)` | 若 key 不存在，设为 default 并返回；存在则直接返回原值 |

##### 删

| 操作                 | 语法          | 说明                                                   |
| -------------------- | ------------- | ------------------------------------------------------ |
| 删除指定键           | `del d[key]`  | 若 key 不存在会报错                                    |
| 删除并返回值         | `d.pop(key)`  | 若 key 不存在可设默认值：`pop(key, default)`           |
| 弹出最后一项（LIFO） | `d.popitem()` | 返回 `(key, value)` 元组（Python 3.7+ 为最后插入的项） |
| 清空字典             | `d.clear()`   | 移除所有键值对，变为空字典 `{}`                        |

##### 改

```python
d['existing_key'] = new_value
```

##### 查

| 操作           | 语法                  | 说明                                                         |
| -------------- | --------------------- | ------------------------------------------------------------ |
| 按键取值       | `d[key]`              | 若 key 不存在会报 `KeyError`                                 |
| 安全取值       | `d.get(key, default)` | key 不存在时返回 `default`（默认为 `None`）                  |
| 判断键是否存在 | `key in d`            | 返回 `True/False`（只查键，不查值！）                        |
| 获取所有键     | `d.keys()`            | 返回 `dict_keys` 视图对象                                    |
| 获取所有值     | `d.values()`          | 返回 `dict_values` 视图对象                                  |
| 获取所有键值对 | `d.items()`           | 返回 `dict_items` 视图对象（每个元素是 `(key, value)` 元组） |
| 获取长度       | `len(d)`              | 键值对数量                                                   |

### 集合`Set`



## 条件控制语句

#### `if`判断

```python
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句

```

| 操作符 | 描述                     |
| :----- | :----------------------- |
| `<`    | 小于                     |
| `<=`   | 小于或等于               |
| `>`    | 大于                     |
| `>=`   | 大于或等于               |
| `==`   | 等于，比较两个值是否相等 |
| `!=`   | 不等于                   |

#### `match case`

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))
```



## 循环语句

#### for循环

###### 

###### 少写for循环

```python
from timeit import timeit

# 写法1
def with_for():
    lst = []
    for i in range(100):
        lst.append(2 * i) # 函数拖慢了运行速度
    return lst

# 写法2
def without_for():
    return [2 * i for i in range(100)]

print(f"with:    {timeit(with_for, number=10000)}")
print(f"without:     {timeit(without_for, number=10000)}")
```

python自带的builtin库，max()函数，比自己写的要快

#### while

```python
while 判断条件(condition)：
    执行语句(statements)……

```

## 迭代器



## 生成器



## 文件操作

### with

```python
with 表达式 [as 变量]:
    代码块
```

读和写文件

```python
open(filename, mode)

```

- filename：包含了你要访问的文件名称的字符串值。
- mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

|    模式    |  r   |  r+  |  w   |  w+  |  a   |  a+  |
| :--------: | :--: | :--: | :--: | :--: | :--: | :--: |
|     读     |  +   |  +   |      |  +   |      |  +   |
|     写     |      |  +   |  +   |  +   |  +   |  +   |
|    创建    |      |      |  +   |  +   |  +   |  +   |
|    覆盖    |      |      |  +   |  +   |      |      |
| 指针在开始 |  +   |  +   |  +   |  +   |      |      |
| 指针在结尾 |      |      |      |      |  +   |  +   |

###### 1.文件操作

```python
# 自动打开并关闭文件（无需手动 close()）
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    # ... 处理内容

# 文件会在 with 块结束时自动关闭（即使出错！）
```

> **优势**：避免忘记 `f.close()`，防止资源泄漏

###### 2.线程锁

```python
import threading
lock = threading.Lock()

with lock:
    # 临界区代码（自动加锁/解锁）
    shared_resource += 1
```

###### 3.临时改变工作目录

```python
from contextlib import chdir
with chdir('/tmp'):
    # 在 /tmp 目录下执行操作
    pass
# 自动切回原目录
```

###### 4.抑制特定异常

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')  # 文件不存在也不报错
```

###### 5.计时

```python
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"耗时: {time.time() - start:.2f}秒")

with timer():
    time.sleep(1)  # 输出：耗时: 1.00秒
```

###### 6.多资源同时管理

```python
# 方式1：嵌套（不推荐）
with open('in.txt') as fin:
    with open('out.txt', 'w') as fout:
        fout.write(fin.read())

# 方式2：一行写多个（推荐）
with open('in.txt') as fin, open('out.txt', 'w') as fout:
    fout.write(fin.read())
```



## 函数

###### 语法

```python
def func_name(param1, param2=默认值, *args, **kwargs):
    """文档字符串（可选）"""
    # 函数体
    return 结果  # 可选，无 return 则返回 None
```

###### 参数

| 类型           | 写法               | 说明                          |
| :------------- | :----------------- | :---------------------------- |
| 位置参数       | `def f(a, b):`     | 调用时按顺序传入              |
| 默认参数       | `def f(a, b=10):`  | 有默认值，调用时可省略        |
| 可变位置参数   | `def f(*args):`    | 接收任意多个位置参数 → 元组   |
| 可变关键字参数 | `def f(**kwargs):` | 接收任意多个关键字参数 → 字典 |

###### 函数返回值

- `return value`：返回单个值
- `return a, b`：自动打包为元组 `(a, b)`
- 无 `return` 或 `return` 后无值 → 返回 `None`

```python
def get_name_age():
    return "Tom", 25  # 实际返回元组

name, age = get_name_age()  # 自动解包
```

###### 函数作用域（LEGB 规则）

- **L**ocal（局部）→ **E**nclosing（嵌套函数）→ **G**lobal（全局）→ **B**uilt-in（内置）
- 修改全局变量需用 `global`
- 修改外层嵌套变量需用 `nonlocal`

```python
x = 10
def outer():
    y = 20
    def inner():
        global x
        nonlocal y
        x = 100   # 修改全局 x
        y = 200   # 修改外层 y
    inner()
```

###  Lambda 表达式

匿名函数

```python
square = lambda x: x ** 2

# 等价于 
def square(x): 
    return x**2
```

### 函数作为参数（高阶函数）

```python
numbers = [3, 1, 4]
sorted(numbers, key=lambda x: -x)  # 按降序排
```

### 函数装饰器（@语法糖）

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def say_hello():
    print("Hello!")
```

### 内置函数

| 函数                     | 用途         |
| :----------------------- | :----------- |
| `len()`                  | 获取长度     |
| `type()`                 | 查看类型     |
| `isinstance(obj, cls)`   | 判断类型     |
| `map(func, iterable)`    | 映射处理     |
| `filter(func, iterable)` | 过滤元素     |
| `zip(*iterables)`        | 并行迭代     |
| `help(func)`             | 查看帮助文档 |

## 模块、库

## ` __name`__和`__main__`

```python
# 这样的 Python 代码
if __name__ == "__main__":
    main() 
    # 这里的代码只有在模块作为主程序运行时才会执行

```

__name__ 是一个内置变量，用于表示当前模块的名称。

__name__ 的值取决于模块是如何被使用的：

当模块作为主程序运行时：__name__ 的值被设置为 "__main__"。

当模块被导入时：__name__ 的值被设置为模块的文件名（不包括 .py 扩展名）

## 输入输出

##### `input()`

```python
age = int(input("年龄: "))      # 转为整数
height = float(input("身高: ")) # 转为浮点数
```

##### `print()`

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("Hello")                # Hello
print("a", "b", "c")          # a b c（默认空格分隔）
```

| 参数       | 类型               | 默认值                           | 说明                                             |
| ---------- | ------------------ | -------------------------------- | ------------------------------------------------ |
| `*objects` | 任意数量的位置参数 | —                                | 要打印的对象（可以是任意类型，会自动转为字符串） |
| `sep`      | str                | `' '`（空格）                    | 多个对象之间的分隔符                             |
| `end`      | str                | `'\n'`（换行符）                 | 所有对象打印完后的结尾字符                       |
| `file`     | 文件类对象         | `sys.stdout`（标准输出，即屏幕） | 指定输出目标（如文件、`sys.stderr` 等）          |
| `flush`    | bool               | `False`                          | 是否立即刷新输出缓冲区（`True` 表示强制刷新）    |

###### 1.f-string

```python
name = "Tom"
age = 25
print(f"姓名: {name}, 年龄: {age}")
print(f"平方: {age ** 2}")  # 支持表达式
```

###### 2..format()

```python
print("姓名: {}, 年龄: {}".format(name, age))
print("姓名: {0}, 年龄: {1}".format(name, age))
```

## 错误和异常
