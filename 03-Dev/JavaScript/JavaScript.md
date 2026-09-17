##### 输出

###### console.log()

> 向浏览器控制台输出信息，用于调试

```js
console.log("Hello, world!");
console.log(42, { name: "Alice" });
```

- `console.error()`：输出错误信息（通常为红色）
- `console.warn()`：输出警告信息（通常为黄色）
- `console.info()`：输出提示信息
- `console.debug()`：输出调试信息（部分浏览器需开启 debug 日志）

###### alert()

> 弹出一个模态对话框显示消息
>
> 会阻塞脚本执行，直到用户点击确定

```js
alert("This is an alert!");
```

###### document.write()

> 直接向 HTML 文档写入内容
>
> 如果在页面加载完成后调用，会覆盖整个文档！不推荐在现代开发中使用

```js
document.write("<p>Hello from JS!</p>");
```

###### 操作 DOM 元素

> 动态更新页面内容，是现代 Web 开发的标准做法

```js
document.getElementById("output").textContent = "New content!";
// 或
document.querySelector("#output").innerHTML = "<strong>Bold text</strong>";
```

##### 语法

###### 变量

```js
var x,y
```

> js对大小写敏感
>
> 函数 **getElementById** 与 **getElementbyID** 是不同的。
>
> 同样，变量 **myVariable** 与 **MyVariable** 也是不同的。

###### 声明变量

> 可以使用 **var**、**let** 和 **const** 关键字来声明变量

- var：ES5 引入的变量声明方式，具有函数作用域。

- let：ES6 引入的变量声明方式，具有块级作用域。

- const：ES6 引入的常量声明方式，具有块级作用域，且值不可变。

###### 语句分隔

```js
x = 5 + 6;
y = x * 10;
```

###### 代码块

```js
function myFunction()
{
    document.getElementById("demo").innerHTML="你好Dolly";
    document.getElementById("myDIV").innerHTML="你最近怎么样?";
}
```

> JavaScript 可以分批地组合起来。
>
> 代码块以左花括号开始，以右花括号结束

###### 注释

```js
// 注释

/*
多行
注释
*/
```

###### 代码换行

```js
document.write("你好 \
世界!");
```

###### 数据类型

```js
var length = 16;                                  // Number 通过数字字面量赋值 
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值
```

类型检测

```js
typeof "John"                // 返回 string
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```

###### 空格

> JavaScript 会忽略多余的空格。您可以向脚本添加空格，来提高其可读性。

```js
var person="runoob";
var person = "runoob";
```

##### 语句

###### 语句标识符

| 语句         | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| break        | 用于跳出循环。                                               |
| catch        | 语句块，在 try 语句块执行出错时执行 catch 语句块。           |
| continue     | 跳过循环中的一个迭代。                                       |
| do ... while | 执行一个语句块，在条件语句为 true 时继续执行该语句块。       |
| for          | 在条件语句为 true 时，可以将代码块执行指定的次数。           |
| for ... in   | 用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。 |
| function     | 定义一个函数                                                 |
| if ... else  | 用于基于不同的条件来执行不同的动作。                         |
| return       | 返回结果，并退出函数                                         |
| switch       | 用于基于不同的条件来执行不同的动作。                         |
| throw        | 抛出（生成）错误 。                                          |
| try          | 实现错误处理，与 catch 一同使用。                            |
| var          | 声明一个变量。                                               |
| while        | 当条件语句为 true 时，执行语句块。                           |

##### 字符串

###### 字符串创建

```js
const str1 = 'Hello';
const str2 = "World";
const str3 = `Template: ${str1} ${str2}`; // 模板字符串（ES6+）
```

###### 字符串方法

查找判断

| 方法                          | 说明                                | 示例                                |
| :---------------------------- | :---------------------------------- | :---------------------------------- |
| `indexOf(search, fromIndex)`  | 返回首次出现的索引，未找到返回 `-1` | `'hello'.indexOf('l')` → `2`        |
| `lastIndexOf(search)`         | 从后往前查找                        | `'hello'.lastIndexOf('l')` → `3`    |
| `includes(search, fromIndex)` | 是否包含子串（ES6+）                | `'hello'.includes('he')` → `true`   |
| `startsWith(prefix)`          | 是否以某字符串开头（ES6+）          | `'hello'.startsWith('he')` → `true` |
| `endsWith(suffix)`            | 是否以某字符串结尾（ES6+）          | `'hello'.endsWith('lo')` → `true`   |
| `match(regexp)`               | 使用正则匹配，返回数组或 `null`     | `'abc123'.match(/\d+/)` → `['123']` |
| `search(regexp)`              | 返回匹配正则的索引                  | `'abc123'.search(/\d/)` → `3`       |

截取与提取

| 方法                    | 说明                         | 示例                                |
| :---------------------- | :--------------------------- | :---------------------------------- |
| `slice(start, end)`     | 提取子串（支持负数）         | `'hello'.slice(1, 4)` → `'ell'`     |
| `substring(start, end)` | 类似 `slice`，但负数视为 `0` | `'hello'.substring(1, 4)` → `'ell'` |
| `substr(start, length)` | ⚠️ 已废弃！用 `slice` 替代    | —                                   |
| `charAt(index)`         | 返回指定位置字符             | `'hello'.charAt(1)` → `'e'`         |
| `charCodeAt(index)`     | 返回 Unicode 编码            | `'A'.charCodeAt(0)` → `65`          |
| `at(index)`             | 支持负索引（ES2022+）        | `'hello'.at(-1)` → `'o'`            |

替换与修改

| 方法                                      | 说明                          | 示例                                     |
| :---------------------------------------- | :---------------------------- | :--------------------------------------- |
| `replace(search, replace)`                | 替换**第一个**匹配项          | `'aabb'.replace('a', 'x')` → `'xabb'`    |
| `replaceAll(search, replace)`             | 替换**所有**匹配项（ES2021+） | `'aabb'.replaceAll('a', 'x')` → `'xxbb'` |
| `replace(regexp, replace)`                | 支持正则全局替换              | `'a1b2'.replace(/\d/g, '#')` → `'a#b#'`  |
| `toLowerCase()` / `toUpperCase()`         | 转大小写                      | `'Hello'.toLowerCase()` → `'hello'`      |
| `trim()` / `trimStart()` / `trimEnd()`    | 去除空格（ES2019+）           | `'  hi  '.trim()` → `'hi'`               |
| `padStart(len, str)` / `padEnd(len, str)` | 补全字符串（ES2017+）         | `'5'.padStart(3, '0')` → `'005'`         |

拼接与分割

| 方法                      | 说明                        | 示例                                   |
| :------------------------ | :-------------------------- | :------------------------------------- |
| `concat(str1, str2, ...)` | 拼接字符串（可用 `+` 替代） | `'a'.concat('b')` → `'ab'`             |
| `split(separator, limit)` | 分割为数组                  | `'a,b,c'.split(',')` → `['a','b','c']` |
| 模板字符串 ` ${var} `     | 动态插入变量（ES6+）        | ` Hello ${name} `                      |

转换与编码

| 方法                      | 说明                                    | 示例                                    |
| :------------------------ | :-------------------------------------- | :-------------------------------------- |
| `toString()`              | 转为字符串（多数类型都有）              | `(123).toString()` → `'123'`            |
| `String(value)`           | 安全转字符串（处理 `null`/`undefined`） | `String(null)` → `'null'`               |
| `encodeURIComponent(str)` | URL 编码（推荐）                        | `encodeURIComponent('a b')` → `'a%20b'` |
| `decodeURIComponent(str)` | URL 解码                                | `decodeURIComponent('a%20b')` → `'a b'` |

###### 模板字符串

```js
const name = "Alice";
const age = 30;

// 多行 + 插值
const bio = `
  Name: ${name}
  Age: ${age}
  Next year: ${age + 1}
`;

// 标签模板（用于防注入、国际化等）
function highlight(strings, ...values) {
  return strings[0] + values.map(v => `<b>${v}</b>`).join('');
}
highlight`Hello ${name}`; // "Hello <b>Alice</b>"
```

###### 正则表达式常用搭配

```js
const str = "Email: user@example.com";

// 提取邮箱
const email = str.match(/[\w.-]+@[\w.-]+\.\w+/)?.[0];

// 验证格式
const isValid = /^\d{3}-\d{2}-\d{4}$/.test("123-45-6789");

// 全局替换
"color color".replace(/color/g, "colour");
```



##### 对象

```js
var person = {firstName:"John", 
              lastName:"Doe", 
              age:50, 
              eyeColor:"blue"};
```

###### 对象方法

```js
name = person.fullName();
// 对象属性
name = person.fullName;
```

##### 函数

###### 函数声明

```js
function greet(name) {
  return `Hello, ${name}!`;
}
```

> 特点：函数提升（hoisting），可在定义前调用
> 适合全局工具函数。

###### 函数表达式

```js
const greet = function(name) {
  return `Hello, ${name}!`;
};
```

> ❌无提升（必须先定义后调用）
> 常用于赋值、回调或模块化

###### 箭头函数

```js
const greet = (name) => `Hello, ${name}!`;

// 多参数 / 多行
const add = (a, b) => {
  console.log("Adding...");
  return a + b;
};
```

> ✅ 简洁语法，自动返回（单表达式时）
> ❌ 没有自己的 this、arguments、super 或 new.target
> 常用于回调、数组方法（如 map, filter）

###### 立即执行函数表达式

```js
(function() {
  console.log("IIFE runs immediately!");
})();

// 箭头版（较少用）
(() => {
  console.log("Arrow IIFE");
})();
```

> ✅ 创建私有作用域，避免污染全局变量
>
> 常用于模块初始化或隔离逻辑

###### 构造函数

```js
function Person(name) {
  this.name = name;
}
const p = new Person("Alice");
```

> 配合 `new` 使用，创建对象实例
>
> 现代开发中多被 **class** 替代

###### Generator 函数（生成器）

```js
function* countUp() {
  let i = 0;
  while (true) yield i++;
}

const counter = countUp();
console.log(counter.next().value); // 0
console.log(counter.next().value); // 1
```

> 用 `function*` 定义，通过 `yield` 暂停/恢复执行
>
> 适用于惰性计算、异步流程控制（早期 async 替代方案）

###### Async 函数（异步函数）

```js
async function fetchData() {
  const res = await fetch('/api/data');
  return res.json();
}
```

> 自动返回 Promise
> await 只能在 async 函数内使用
> 是处理异步操作的现代标准方式

###### 参数处理

```js
// 默认参数
function greet(name = "Guest") { ... }

//剩余参数
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3); // numbers = [1, 2, 3]
                                
//解构参数
function printUser({ name, age }) {
  console.log(`${name} is ${age}`);
}
printUser({ name: "Bob", age: 30 });
```

this 绑定

> 普通函数：this 由调用方式决定（可能为 window、对象或 undefined）
> 箭头函数：继承外层作用域的 this，常用于解决回调中 this 丢失问题。

###### 高阶函数

```js
[1, 2, 3].map(x => x * 2); // [2, 4, 6]
```

###### 示例

柯里化

```js
const add = a => b => a + b;
const add5 = add(5);
add5(3); // 8
```

函数防抖

```js
function debounce(func, delay) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), delay);
  };
}
```

函数节流

```js
function throttle(func, limit) {
  let inThrottle;
  return function() {
    if (!inThrottle) {
      func.apply(this, arguments);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}
```

##### 作用域

> 变量在函数内声明，变量为局部变量，具有局部作用域

###### 全局变量

###### 局部变量

##### 事件

###### HTML事件

- HTML 页面完成加载
- HTML input 字段改变时
- HTML 按钮被点击

| 事件        | 描述                                 |
| :---------- | :----------------------------------- |
| onchange    | HTML 元素改变                        |
| onclick     | 用户点击 HTML 元素                   |
| onmouseover | 鼠标指针移动到指定的元素上时发生     |
| onmouseout  | 用户从一个 HTML 元素上移开鼠标时发生 |
| onkeydown   | 用户按下键盘按键                     |
| onload      | 浏览器已完成页面的加载               |

##### 运算符

| 运算符 | 描述         | 例子  | x 运算结果 | y 运算结果 |
| :----- | :----------- | :---- | :--------- | :--------- |
| +      | 加法         | x=y+2 | 7          | 5          |
| -      | 减法         | x=y-2 | 3          | 5          |
| *      | 乘法         | x=y*2 | 10         | 5          |
| /      | 除法         | x=y/2 | 2.5        | 5          |
| %      | 取模（余数） | x=y%2 | 1          | 5          |
| ++     | 自增         | x=++y | 6          | 6          |
| --     | 自减         | x=--y | 4          | 4          |

###### 赋值运算符

| 运算符 | 例子                                                     | 等同于  | 运算结果 |
| :----- | :------------------------------------------------------- | :------ | :------- |
| =      | x=y                                                      |         | x=5      |
| +=     | x+=y                                                     | x=x+y   | x=15     |
| -=     | x-=y                                                     | x=x-y   | x=5      |
| *=     | x*=y                                                     | x=x*y   | x=50     |
| /=     | x/=y                                                     | x=x/y   | x=2      |
| %=     | x%=y                                                     | x=x%y   | x=0      |
| ==     | 等于                                                     | x==8    | *false*  |
| ===    | 绝对等于（值和类型均相等）                               | x==="5" | *false*  |
| !=     | 不等于                                                   | x!=8    | *true*   |
| !==    | 严格不等于运算符（值和类型有一个不相等，或两个都不相等） | x!=="5" | *true*   |
| >      | 大于                                                     | x>8     | *false*  |
| <      | 小于                                                     | x<8     | *true*   |
| >=     | 大于或等于                                               | x>=8    | *false*  |
| <=     | 小于或等于                                               | x<=8    | *true*   |

###### 字符串

```
txt1="What a very";
txt2="nice day";
txt3=txt1+txt2;
```

###### 逻辑运算

| 运算符 | 描述 | 例子                      |
| :----- | :--- | :------------------------ |
| &&     | and  | (x < 10 && y > 1) 为 true |
| \|\|   | or   | (x==5 \|\| y==5) 为 false |
| !      | not  | !(x==y) 为 true           |

##### 条件语句

if语句

```js
if (time<20)
{
    x="Good day";
}
```

if...else

```js
if (time<20)
{
    x="Good day";
}
else
{
    x="Good evening";
}
```

if...else if...else 语句

```js
if (time<10)
{
    document.write("<b>早上好</b>");
}
else if (time>=10 && time<20)
{
    document.write("<b>今天好</b>");
}
else
{
    document.write("<b>晚上好!</b>");
}
```

##### switch语句

```js
var d=new Date().getDay(); 
switch (d) 
{ 
  case 0:x="今天是星期日"; 
  break; 
  case 1:x="今天是星期一"; 
  break; 
  case 2:x="今天是星期二"; 
  break; 
  case 3:x="今天是星期三"; 
  break; 
  case 4:x="今天是星期四"; 
  break; 
  case 5:x="今天是星期五"; 
  break; 
  case 6:x="今天是星期六"; 
  break; 
}
```

default 关键词

```js
var d=new Date().getDay();
switch (d)
{
    case 6:x="今天是星期六";
    break;
    case 0:x="今天是星期日";
    break;
    default:
    x="期待周末";
}
document.getElementById("demo").innerHTML=x;
```

##### 循环

###### for

```js
for (var i=0;i<cars.length;i++)
{ 
    document.write(cars[i] + "<br>");
}
```

- **or** - 循环代码块一定的次数
- **for/in** - 循环遍历对象的属性
- **while** - 当指定的条件为 true 时循环指定的代码块
- **do/while** - 同样当指定的条件为 true 时循环指定的代码块

###### For/In 循环

```js
var person={fname:"Bill",lname:"Gates",age:56}; 
 
for (x in person)  // x 为属性名
{
    txt=txt + person[x];
}
```

###### while

```js
while (i<5)
{
    x=x + "The number is " + i + "<br>";
    i++;
}
```

###### do while

```js
do
{
    x=x + "The number is " + i + "<br>";
    i++;
}
while (i<5);
```

##### break 和 continue 语句

###### break

```js
for (i=0;i<10;i++)
{
    if (i==3) break;
    x=x + "The number is " + i + "<br>";
}
```

###### continue

```js
while (i < 10){
  if (i == 3){
    i++;    //加入i++不会进入死循环
    continue;
  }
  x= x + "该数字为 " + i + "<br>";
  i++;
}
```

##### typeof, null, 和 undefined

###### typeof

```js
typeof "John"                // 返回 string 
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```

| 表达式                | 返回值      | 说明                 |
| :-------------------- | :---------- | :------------------- |
| `typeof undefined`    | "undefined" | 未定义的值           |
| `typeof true`         | "boolean"   | 布尔值               |
| `typeof 42`           | "number"    | 所有数字类型         |
| `typeof "text"`       | "string"    | 字符串               |
| `typeof {a:1}`        | "object"    | 对象、数组、null     |
| `typeof function(){}` | "function"  | 函数                 |
| `typeof Symbol()`     | "symbol"    | ES6新增符号类型      |
| `typeof BigInt(10)`   | "bigint"    | ES2020新增大整数类型 |

###### null

```js
typeof undefined   // undefined
typeof null   // object
null === undefined   // false
null == undefined    // true
```

##### 类型转换

###### constructor 属性

```js
"John".constructor                 
// 返回函数 String()  { [native code] }
(3.14).constructor                 
// 返回函数 Number()  { [native code] }
false.constructor                 
// 返回函数 Boolean() { [native code] }
[1,2,3,4].constructor             
// 返回函数 Array()   { [native code] }
{name:'John', age:34}.constructor 
// 返回函数 Object()  { [native code] }
	new Date().constructor            
// 返回函数 Date()    { [native code] }
function () {}.constructor        
// 返回函数 Function(){ [native code] }
```

| 方法            | 描述                                                 |
| :-------------- | :--------------------------------------------------- |
| toExponential() | 把对象的值转换为指数计数法。                         |
| toFixed()       | 把数字转换为字符串，结果的小数点后有指定位数的数字。 |
| toPrecision()   | 把数字格式化为指定的长度。                           |

###### 将日期转换为字符串

| 方法              | 描述                                        |
| :---------------- | :------------------------------------------ |
| getDate()         | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。 |
| getDay()          | 从 Date 对象返回一周中的某一天 (0 ~ 6)。    |
| getFullYear()     | 从 Date 对象以四位数字返回年份。            |
| getHours()        | 返回 Date 对象的小时 (0 ~ 23)。             |
| getMilliseconds() | 返回 Date 对象的毫秒(0 ~ 999)。             |
| getMinutes()      | 返回 Date 对象的分钟 (0 ~ 59)。             |
| getMonth()        | 从 Date 对象返回月份 (0 ~ 11)。             |
| getSeconds()      | 返回 Date 对象的秒数 (0 ~ 59)。             |
| getTime()         | 返回 1970 年 1 月 1 日至今的毫秒数。        |

###### 自动转换为字符串

| 原始值              | 转换为数字 | 转换为字符串      | 转换为布尔值 |
| :------------------ | :--------- | :---------------- | :----------- |
| false               | 0          | "false"           | false        |
| true                | 1          | "true"            | true         |
| 0                   | 0          | "0"               | false        |
| 1                   | 1          | "1"               | true         |
| "0"                 | 0          | "0"               | true         |
| "000"               | 0          | "000"             | true         |
| "1"                 | 1          | "1"               | true         |
| NaN                 | NaN        | "NaN"             | false        |
| Infinity            | Infinity   | "Infinity"        | true         |
| -Infinity           | -Infinity  | "-Infinity"       | true         |
| ""                  | 0          | ""                | false        |
| "20"                | 20         | "20"              | true         |
| "Runoob"            | NaN        | "Runoob"          | true         |
| [ ]                 | 0          | ""                | true         |
| [20]                | 20         | "20"              | true         |
| [10,20]             | NaN        | "10,20"           | true         |
| ["Runoob"]          | NaN        | "Runoob"          | true         |
| ["Runoob","Google"] | NaN        | "Runoob,Google"   | true         |
| function(){}        | NaN        | "function(){}"    | true         |
| { }                 | NaN        | "[object Object]" | true         |
| null                | 0          | "null"            | false        |
| undefined           | NaN        | "undefined"       | false        |

##### 正则表达式

###### search() 方法

使用正则表达式

```js
var str = "Visit Runoob!"; 
var n = str.search(/Runoob/i);
```

###### replace() 方法

```js
var str = document.getElementById("demo").innerHTML; 
var txt = str.replace(/microsoft/i,"Runoob");
```

###### 修饰符

| 修饰符 | 描述                                                     |
| :----- | :------------------------------------------------------- |
| i      | 执行对大小写不敏感的匹配。                               |
| g      | 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。 |
| m      | 执行多行匹配。                                           |

| 表达式 | 描述                       |
| :----- | :------------------------- |
| [abc]  | 查找方括号之间的任何字符。 |
| [0-9]  | 查找任何从 0 至 9 的数字。 |
| (x\|y) | 查找任何以 \| 分隔的选项。 |

| 元字符 | 描述                                        |
| :----- | :------------------------------------------ |
| \d     | 查找数字。                                  |
| \s     | 查找空白字符。                              |
| \b     | 匹配单词边界。                              |
| \uxxxx | 查找以十六进制数 xxxx 规定的 Unicode 字符。 |

| 量词 | 描述                                  |
| :--- | :------------------------------------ |
| n+   | 匹配任何包含至少一个 *n* 的字符串。   |
| n*   | 匹配任何包含零个或多个 *n* 的字符串。 |
| n?   | 匹配任何包含零个或一个 *n* 的字符串。 |

###### test()

于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false。

```js
var patt = /e/;
patt.test("The best things in life are free!");
```

###### exec()

用于检索字符串中的正则表达式的匹配

```
/e/.exec("The best things in life are free!");
```

##### 错误 - throw、try 和 catch

- **try** 语句测试代码块的错误。
- **catch** 语句处理错误。
- **throw** 语句创建自定义错误。
- **finally** 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。

```js
var txt=""; 
function message() 
{ 
    try { 
        adddlert("Welcome guest!"); 
    } catch(err) { 
        txt="本页有一个错误。\n\n"; 
        txt+="错误描述：" + err.message + "\n\n"; 
        txt+="点击确定继续。\n\n"; 
        alert(txt); 
    } 
}
```

###### finally 语句

```js
function myFunction() {
  var message, x;
  message = document.getElementById("p01");
  message.innerHTML = "";
  x = document.getElementById("demo").value;
  try { 
    if(x == "") throw "值是空的";
    if(isNaN(x)) throw "值不是一个数字";
    x = Number(x);
    if(x > 10) throw "太大";
    if(x < 5) throw "太小";
  }
  catch(err) {
    message.innerHTML = "错误: " + err + ".";
  }
  finally {
    document.getElementById("demo").value = "";
  }
}
```

###### Throw 语句

```js
function myFunction() {
    var message, x;
    message = document.getElementById("message");
    message.innerHTML = "";
    x = document.getElementById("demo").value;
    try { 
        if(x == "")  throw "值为空";
        if(isNaN(x)) throw "不是数字";
        x = Number(x);
        if(x < 5)    throw "太小";
        if(x > 10)   throw "太大";
    }
    catch(err) {
        message.innerHTML = "错误: " + err;
    }
}
```

##### 声明提升

```js
x = 5; // 变量 x 设置为 5

elem = document.getElementById("demo"); // 查找元素 
elem.innerHTML = x;                     
// 在元素中显示 xvar x; // 声明 x
```

###### 严格模式(use strict)

```js
"use strict";myFunction();
function myFunction() {
     y = 3.14;   
 // 报错 (y 未定义)}
```

##### 表单

###### 表单验证

```js
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == null || x == "") {
        alert("需要输入名字。");
        return false;
    }
}
```

##### 验证 API

| Property            | Description                                                  |
| :------------------ | :----------------------------------------------------------- |
| checkValidity()     | 如果 input 元素中的数据是合法的返回 true，否则返回 false。   |
| setCustomValidity() | 设置 input 元素的 validationMessage 属性，用于自定义错误提示信息的方法。使用 setCustomValidity 设置了自定义提示后，validity.customError 就会变成 true，checkValidity 总是会返回 false。如果要重新判断需要取消自定义提示，方式如下：`setCustomValidity('')  setCustomValidity(null)  setCustomValidity(undefined)` |

```js
<input id="id1" type="number" min="100" max="300" required>
<button onclick="myFunction()">验证</button>
 
<p id="demo"></p>
 
<script>function myFunction() {
    var inpObj = document.getElementById("id1");
    if (inpObj.checkValidity() == false) {
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    }
}</script>
```

###### 约束验证 DOM 属性

| 属性              | 描述                                  |
| :---------------- | :------------------------------------ |
| validity          | 布尔属性值，返回 input 输入值是否合法 |
| validationMessage | 浏览器错误提示信息                    |
| willValidate      | 指定 input 是否需要验证               |

| 属性            | 描述                                                       |
| :-------------- | :--------------------------------------------------------- |
| customError     | 设置为 true, 如果设置了自定义的 validity 信息。            |
| patternMismatch | 设置为 true, 如果元素的值不匹配它的模式属性。              |
| rangeOverflow   | 设置为 true, 如果元素的值大于设置的最大值。                |
| rangeUnderflow  | 设置为 true, 如果元素的值小于它的最小值。                  |
| stepMismatch    | 设置为 true, 如果元素的值不是按照规定的 step 属性设置。    |
| tooLong         | 设置为 true, 如果元素的值超过了 maxLength 属性设置的长度。 |
| typeMismatch    | 设置为 true, 如果元素的值不是预期相匹配的类型。            |
| valueMissing    | 设置为 true，如果元素 (required 属性) 没有值。             |
| valid           | 设置为 true，如果元素的值是合法的。                        |

##### this 关键字

- 在方法中，this 表示该方法所属的对象。
- 如果单独使用，this 表示全局对象。
- 在函数中，this 表示全局对象。
- 在函数中，在严格模式下，this 是未定义的(undefined)。
- 在事件中，this 表示接收事件的元素。
- 类似 call() 和 apply() 方法可以将 this 引用到任何对象。

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

##### JSON

- JSON 英文全称 **J**ava**S**cript **O**bject **N**otation
- JSON 是一种轻量级的数据交换格式。
- JSON是独立的语言 *****
- JSON 易于理解。

```js
"sites":[
    {"name":"Runoob", "url":"www.runoob.com"}, 
    {"name":"Google", "url":"www.google.com"},
    {"name":"Taobao", "url":"www.taobao.com"}
]
```

| 函数                                                         | 描述                                           |
| :----------------------------------------------------------- | :--------------------------------------------- |
| [JSON.parse()](https://www.runoob.com/js/javascript-json-parse.html) | 用于将一个 JSON 字符串转换为 JavaScript 对象。 |
| [JSON.stringify()](https://www.runoob.com/js/javascript-json-stringify.html) | 用于将 JavaScript 值转换为 JSON 字符串。       |

##### javascript:void(0) 

```
<a href="javascript:void(0)">单击此处什么也不会发生</a>
```

##### 异步编程

###### 回调函数

```js
function print() {
    document.getElementById("demo").innerHTML="RUNOOB!";
}
setTimeout(print, 3000);
```

###### 异步 AJAX

```js
var xhr = new XMLHttpRequest();
 
xhr.onload = function () {
    // 输出接收到的文字数据
    document.getElementById("demo").innerHTML=xhr.responseText;
}
 
xhr.onerror = function () {
    document.getElementById("demo").innerHTML="请求出错";
}
 
// 发送异步 GET 请求
xhr.open("GET", "https://www.runoob.com/try/ajax/ajax_info.txt", true);
xhr.send();
```

##### Promise 使用方法

###### then() 方法

then() 方法用于指定 Promise 状态变为 fulfilled 或 rejected 时的回调函数。

```js
myPromise.then(
  (result) => {
    // 处理成功情况
    console.log('成功:', result);
  },
  (error) => {
    // 处理失败情况
    console.error('失败:', error);
  }
);
```

###### catch() 方法

catch() 方法专门用于处理 Promise 被拒绝的情况

```js
myPromise
  .then((result) => {
    console.log('成功:', result);
  })
  .catch((error) => {
    console.error('失败:', error);
  });
```

###### Promise 的链式调用

```js
doFirstThing()
  .then((result) => doSecondThing(result))
  .then((newResult) => doThirdThing(newResult))
  .then((finalResult) => {
    console.log('最终结果:', finalResult);
  })
  .catch((error) => {
    console.error('链中某处出错:', error);
  });
```

###### Promise 的静态方法

Promise.all()

```js
Promise.all([promise1, promise2, promise3])
  .then((results) => {
    // results 是一个包含所有 Promise 结果的数组
    console.log(results);
  })
  .catch((error) => {
    // 任一 Promise 失败就会进入这里
    console.error(error);
  });
```

###### Promise.race()

返回最先完成（无论成功或失败）的 Promise 的结果。

```js
Promise.race([promise1, promise2, promise3])
  .then((result) => {
    // 使用最先完成的 Promise 的结果
    console.log(result);
  })
  .catch((error) => {
    // 如果最先完成的 Promise 是失败的
    console.error(error);
  });
```

#### js函数

##### 函数定义

##### 函数参数

##### 函数调用

##### 闭包

#### js类

##### 类

##### 类继承

##### 静态方法

#### js HTML DOM



#### js高级教程

##### 对象

##### prototype

##### number对象

##### string

##### Date

##### Array

##### Boolean

##### Math

##### RegExp

#### js浏览器BOM

##### window 对象（全局对象）

所有全局变量和函数都是 `window` 的属性/方法

```js
console.log(window.innerHeight); // 浏览器视口高度
window.alert('Hello');
```

| 属性/方法                          | 说明                                                |
| :--------------------------------- | :-------------------------------------------------- |
| `window.innerWidth / innerHeight`  | 视口（viewport）宽高（不含工具栏、滚动条）          |
| `window.outerWidth / outerHeight`  | 浏览器窗口总宽高（含工具栏、菜单栏等）              |
| `window.screenX / screenY`         | 窗口相对于屏幕左上角的位置                          |
| `window.scrollTo(x, y)`            | 滚动到指定位置                                      |
| `window.scrollBy(dx, dy)`          | 相对当前滚动位置偏移                                |
| `window.open(url, name, features)` | 打开新窗口                                          |
| `window.close()`                   | 关闭当前窗口（仅对 `window.open()` 打开的窗口有效） |

##### `screen` 对象

提供用户屏幕信息

```js
console.log(screen.width);   // 屏幕宽度（像素）
console.log(screen.height);  // 屏幕高度
console.log(screen.availWidth);  // 可用宽度（排除任务栏等）
console.log(screen.colorDepth);  // 色深（如 24）
```

##### location 对象

表示当前 URL 信息，并可用于页面跳转

| 属性       | 值                                                        |
| :--------- | :-------------------------------------------------------- |
| `href`     | 完整 URL：`"https://example.com:8080/path?search=1#hash"` |
| `protocol` | `"https:"`                                                |
| `host`     | `"example.com:8080"`                                      |
| `hostname` | `"example.com"`                                           |
| `port`     | `"8080"`                                                  |
| `pathname` | `"/path"`                                                 |
| `search`   | `"?search=1"`                                             |
| `hash`     | `"#hash"`                                                 |

```js
location.assign("https://google.com"); // 跳转（可后退）
location.replace("https://google.com"); // 替换当前页（不可后退）
location.reload(); // 刷新页面
```

##### history 对象

操作浏览器会话历史记录

```js
history.back();    // 后退
history.forward(); // 前进
history.go(-2);    // 向后跳 2 页，go(1) 相当于 forward()

// HTML5 新增（用于 SPA 路由）
history.pushState(state, title, url); // 添加新历史记录（不刷新）
history.replaceState(state, title, url); // 替换当前历史记录

// 监听 popstate 事件（前进/后退触发）
window.addEventListener('popstate', (e) => {
  console.log(e.state); // pushState 传入的 state
});
```

##### navigator 对象

提供浏览器和系统相关信息

```js
navigator.userAgent;     // 浏览器标识字符串（慎用于 UA 检测）
navigator.language;      // 用户首选语言，如 "zh-CN"
navigator.onLine;        // 是否在线（true/false）
navigator.geolocation;   // 地理位置 API
navigator.clipboard;     // 剪贴板 API（需 HTTPS）
```

检测网络状态

```js
window.addEventListener('online', () => console.log('网络已连接'));
window.addEventListener('offline', () => console.log('网络已断开'));
```

##### 其他常用 BOM 功能

定时器（属于 window）

```js
let id = setTimeout(() => {}, 1000);   // 延迟执行
let id2 = setInterval(() => {}, 1000); // 循环执行

clearTimeout(id);
clearInterval(id2);
```

对话框（阻塞式，慎用）

```js
alert("提示");
let ok = confirm("确定？"); // 返回 true/false
let input = prompt("请输入：", "默认值");
```

页面可见性（Page Visibility API）

```js
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    console.log('页面不可见');
  } else {
    console.log('页面可见');
  }
});
```



#### JavaScript 库

###### 通用工具库

- **Lodash**：提供实用函数（如 `map`、`filter`、`debounce`、`cloneDeep` 等），增强原生 JavaScript 能力。
- **Underscore.js**：类似 Lodash，但更轻量，早期流行。
- **Ramda**：专注于函数式编程，支持自动柯里化、不可变数据等

###### DOM 操作与 UI

jQuery：曾是 Web 开发标配，简化 DOM 操作、事件处理、AJAX 等（现代项目中使用减少）。
Alpine.js：轻量级响应式框架，类似 Vue 的语法，适合渐进增强。

###### 数据请求

- **Axios**：基于 Promise 的 HTTP 客户端，支持浏览器和 Node.js，常用于 API 调用。
- **Fetch API**（原生）：现代浏览器内置，但需手动处理错误和 JSON。
- **SuperAgent**：Node.js 和浏览器通用的 HTTP 请求库。

###### 数据可视化

- **D3.js**：强大的数据驱动文档库，用于创建复杂、交互式图表。
- **Chart.js**：简单易用，适合快速绘制折线图、柱状图、饼图等。
- **ECharts**（百度出品）：功能丰富，支持大数据量和多种交互。

###### 日期与时间处理

- **date-fns**：模块化、轻量、不可变的日期工具库。
- **Day.js**：类似 Moment.js 但更小更快（Moment 已进入维护模式）。
- **Luxon**：由 Moment 团队开发，支持时区、国际化。

###### 表单与验证

- **Yup**：用于对象 schema 验证，常与 React Hook Form 配合。
- **Zod**：TypeScript 优先的 schema 验证库，支持类型推导。

###### 测试

- **Jest**：Facebook 出品，集测试运行器、断言、Mock 于一体。
- **Mocha + Chai**：灵活组合，Mocha 为测试框架，Chai 为断言库。
- **Vitest**：面向 Vite 项目的极速测试框架，兼容 Jest API。

###### 状态管理（常用于前端框架）

- **Redux**：集中式状态管理，适用于 React 等。
- **Zustand**：轻量、简单、无样板代码的状态管理库。
- **MobX**：响应式状态管理，自动追踪依赖。

###### 构建与工具链相关

- **Vite**：新一代构建工具，极快的开发服务器。
- **Webpack / Rollup**：模块打包器。