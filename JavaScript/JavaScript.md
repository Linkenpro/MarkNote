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