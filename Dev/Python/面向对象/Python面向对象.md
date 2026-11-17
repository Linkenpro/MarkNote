#### 面向对象编程

##### 类和对象

```python
Class Dog:
    # 类里面的变量称为：对象属性
    legs_num = 4
    has_tari = True
    has_hair = True
    
    # 类里面的函数称为：对象方法
    def eat(self):
        pass
    
    def bark(self):
        pass
    
    def sleep(self):
        pass
    
alex = Dog()
peiQi = Dog()
```

##### self

> 代表当前类的实例对象本身

当你调用一个实例方法时，Python会自动将实例作为第一个参数传给方法

```python
alex = Dog()	# 等同于
```

> alex作为变量>>>self
>
> self指向alex对象

##### 构造方法`__init__`

```

```



##### 万物皆对象

```

```



##### 类对象

```python

```



##### 类方法

```python
class Car(object):
    # 类属性
    total_cars = 0
    
    # 初始化构造
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__class__.total_cars += 1
    
    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")
        
    # 类方法
    @classmethod
    def show_total_cars(cls):
        print(id(cls))
        print(f"当前的total_cars:{Car.total_cars}")
        
print(id(Car))
Car.show_total_cars()
```

> Car写死了
>
> cls替换Car
>
> 构造方法中用self.__class__

```python
 # 类方法
    @classmethod
    def show_total_cars(cls):
        print(id(cls))
        print(f"当前的total_cars:{cls.total_cars}")
```

##### 静态方法

> @staticmethod

```python
class Cal:
    @staticmethod
    def add(x,y):
        return x + y

# 实例对象调用
c = Cal()
print(c.add(10,20))

# 类调用
Cal.add(23,45)
```

