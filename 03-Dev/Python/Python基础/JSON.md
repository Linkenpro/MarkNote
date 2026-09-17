JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式

| Python 类型      | ↔    | JSON 类型        |
| :--------------- | :--- | :--------------- |
| `dict`           | ↔    | object           |
| `list`, `tuple`  | ↔    | array            |
| `str`            | ↔    | string           |
| `int`, `float`   | ↔    | number           |
| `True` / `False` | ↔    | `true` / `false` |
| `None`           | ↔    | `null`           |

```python
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'https://www.runoob.com'
}
 
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
```

##### JSON 字符串 → Python 对象

反序列化

```python
data = json.loads('{"name": "Tom", "age": 25, "hobbies": ["读书", "跑步"]}')
# 结果: {'name': 'Tom', 'age': 25, 'hobbies': ['读书', '跑步']}
```

##### Python 对象 → JSON 字符串

序列化

```python
obj = {"score": 95.5, "passed": True, "remark": None}
json_str = json.dumps(obj)
# 结果: '{"score": 95.5, "passed": true, "remark": null}'

# 格式化输出（带缩进，便于阅读）
json_str = json.dumps(obj, indent=2, ensure_ascii=False)
```

###### `dumps()` 

| 参数                    | 说明                                                   |
| :---------------------- | :----------------------------------------------------- |
| `indent=2`              | 美化输出，缩进空格数                                   |
| `ensure_ascii=False`    | 允许中文等非 ASCII 字符直接显示（默认会转为 `\uXXXX`） |
| `sort_keys=True`        | 按键排序输出                                           |
| `separators=(',', ':')` | 自定义分隔符（去空格可减小体积）                       |

######  1.读取JSON 文件 → Python 对象

```python
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # 注意：是 load（无 s）
```

###### Python 对象 → JSON 文件

```python
data = {"version": "1.0", "debug": False}

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)  # 注意：是 dump（无 s）
```

- **`load` / `dump`** → 操作 **文件对象**（File）
- **`loads` / `dumps`** → 操作 **字符串**（String）

