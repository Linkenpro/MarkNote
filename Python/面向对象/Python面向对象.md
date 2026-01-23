##### 面向对象编程

```py
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

###### self

```py
alex.bark()
```

> alex作为变量>>>self
>
> self指向alex对象