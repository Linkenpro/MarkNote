# CSV

电子表格和数据库中最常见的输入、输出文件格式

###### csv.reader(）

```python
csv.reader(iterable, dialect='excel', **fmtparams)
```

| 参数        | 类型                                               | 默认值    | 说明                                                         |
| ----------- | -------------------------------------------------- | --------- | ------------------------------------------------------------ |
| `iterable`  | 文件对象或可迭代对象（如 `open()` 返回的文件句柄） | —         | 必须提供。通常是一个以文本模式（如 `'r'`）打开的文件。       |
| `dialect`   | str 或 Dialect 子类                                | `'excel'` | 指定 CSV 格式的“方言”，预定义包括 `'excel'`、`'excel-tab'` 等，用于统一设置分隔符、引号等规则。 |
| `fmtparams` | 关键字参数                                         | —         | 可覆盖 `dialect` 中的特定格式参数，常用包括： • `delimiter`：字段分隔符（默认 `','`） • `quotechar`：引用字符（默认 `'"'`） • `quoting`：引用规则 • `skipinitialspace`：是否跳过分隔符后的空格 |

```python
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

###### csv.writer(）

> 将数据写入 CSV（逗号分隔值）文件或类文件对象
>
> 自动处理字段中的特殊字符（如逗号、换行符、引号），确保生成的 CSV 格式正确

```python
csv.writer(fileobj, dialect='excel', **fmtparams)
```

| 参数        | 类型                | 默认值    | 说明                                                         |
| ----------- | ------------------- | --------- | ------------------------------------------------------------ |
| `fileobj`   | 文件对象（可写）    | —         | 必须提供。通常是以文本模式（如 `'w'` 或 `'a'`）打开的文件。  |
| `dialect`   | str 或 Dialect 子类 | `'excel'` | 指定 CSV 输出格式的“方言”，如 `'excel'`（默认）、`'excel-tab'` 等。 |
| `fmtparams` | 关键字参数          | —         | 可覆盖 `dialect` 中的格式设置，常用包括： • `delimiter`：字段分隔符（默认 `','`） • `quotechar`：引用字符（默认 `'"'`） • `quoting`：何时加引号（见下方说明） • `lineterminator`：行结束符（默认 `'\r\n'`，但建议显式设为 `'\n'`） |

```python

```



###### csv.register_dialect(）

###### csv.unregister_dialect()

###### csv.get_dialect()

###### csv.list_dialects()

###### csv.field_size_limit()

###### csv.DictWriter()

###### csv.Dialect()

###### csv.excel

###### csv.excel_tab

###### csv.unix_dialect

###### csv.Sniffer

###### csv.QUOTE_ALL

###### csv.QUOTE_MINIMAL

###### csv.QUOTE_NONNUMERIC

###### csv.QUOTE_NONE

###### csv.QUOTE_NOTNULL

###### csv.QUOTE_STRINGS

###### csv.Error

#### Dialect

###### Dialect.delimiter

###### Dialect.doublequote

###### Dialect.escapechar

###### Dialect.lineterminator

###### Dialect.quotechar

###### Dialect.quoting

###### Dialect.skipinitialspace

###### Dialect.strict

#### Reader对象

###### `reader.__next__()`

###### reader.dialect()

###### reader.line_num()

###### reader.fieldnames()

#### Writer对象

###### writer.writerow()

###### writer.writerows()

###### writer.dialect()

###### Writer.writeheader()
