# HTML

## 注释

```html
<!-- 这是一个注释 -->
```

超文本标记语言

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>我的第一个标题</h1>
    <p>我的第一个段落。</p>
</body>
</html>
```

- **<!DOCTYPE html>** 声明为 HTML5 文档,不区分
- **<html>** 元素是 HTML 页面的根元素
- **<head>** 元素包含了文档的元（meta）数据，如 **<meta charset="utf-8">** 定义网页编码格式为 **utf-8**。
- **<title>** 元素描述了文档的标题
- **<body>** 元素包含了可见的页面内容
- **<h1>** 元素定义一个大标题
- **<p>** 元素定义一个段落   



##### body

```html
<body>
<p>这是第一个段落。</p>
</body>
```

#### 标题

##### h标签

```html
<h1>1</h1>
<h2>2</h2>
<h3>3</h3>
<h4>4</h4>
<h5>5</h5>
<h6>6</h6>
```

##### hr标签

在 HTML 页面中创建水平线

```html
<p>这是一个段落。</p>
<hr>
<p>这是一个段落。</p>
<hr>
<p>这是一个段落。</p>
```

#### 段落

##### p标签

```html
<p>这是一个段落。</p>
```

#### 链接

##### a标签

```html
<a href="https://www.runoob.com">这是一个链接</a>
```

#### 图像

##### img标签

```html
<img src="/images/logo.png" width="258" height="39" />
```

- src：用于 `<img>`, `<script>`, `<iframe>` 等元素
- alt：为图像提供替代文本

#### 换行

##### br标签

```
<br>
```

### 属性

| 属性名        | 适用元素                                          | 说明                                                         |
| :------------ | :------------------------------------------------ | :----------------------------------------------------------- |
| `id`          | 所有元素                                          | 为元素指定唯一的标识符。                                     |
| `class`       | 所有元素                                          | 为元素指定一个或多个类名，用于 CSS 或 JavaScript 选择。      |
| `style`       | 所有元素                                          | 直接在元素上应用 CSS 样式。                                  |
| `title`       | 所有元素                                          | 为元素提供额外的提示信息，通常在鼠标悬停时显示。             |
| `data-*`      | 所有元素                                          | 用于存储自定义数据，通常通过 JavaScript 访问。               |
| `href`        | `<a>`, `<link>`                                   | 指定链接的目标 URL。                                         |
| `src`         | `<img>`, `<script>`, `<iframe>`                   | 指定外部资源（如图片、脚本、框架）的 URL。                   |
| `alt`         | `<img>`                                           | 为图像提供替代文本，当图像无法显示时显示。                   |
| `type`        | `<input>`, `<button>`                             | 指定输入控件的类型（如 `text`, `password`, `checkbox` 等）。 |
| `value`       | `<input>`, `<button>`, `<option>`                 | 指定元素的初始值。                                           |
| `disabled`    | 表单元素                                          | 禁用元素，使其不可交互。                                     |
| `checked`     | `<input type="checkbox">`, `<input type="radio">` | 指定复选框或单选按钮是否被选中。                             |
| `placeholder` | `<input>`, `<textarea>`                           | 在输入框中显示提示文本。                                     |
| `target`      | `<a>`, `<form>`                                   | 指定链接或表单提交的目标窗口或框架（如 `_blank` 表示新标签页）。 |
| `readonly`    | 表单元素                                          | 使输入框只读。                                               |
| `required`    | 表单元素                                          | 指定输入字段为必填项。                                       |
| `autoplay`    | `<audio>`, `<video>`                              | 自动播放媒体。                                               |
| `onclick`     | 所有元素                                          | 当用户点击元素时触发 JavaScript 事件。                       |
| `onmouseover` | 所有元素                                          | 当用户将鼠标悬停在元素上时触发 JavaScript 事件。             |
| `onchange`    | 表单元素                                          | 当元素的值发生变化时触发 JavaScript 事件。                   |

#### 全局属性

##### id

全局属性是所有 HTML 元素都可以使用的属性。

id：**为元素指定唯一的标识符**

```html
<div id="header">This is the header</div>
```

##### class

为元素指定一个或多个类名，用于 CSS 或 JavaScript 选择

```html
<p class="text highlight">This is a highlighted text.</p>
```

##### style

用于直接在元素上应用 CSS 样式

```html
<p style="color: blue; font-size: 14px;">This is a styled paragraph.</p>
```

##### title

为元素提供额外的提示信息，通常在鼠标悬停时显示

```html
<abbr title="HyperText Markup Language">HTML</abbr>
```

**data-\***

用于存储自定义数据，通常通过 JavaScript 访问。

```html
<div data-user-id="12345">User Info</div>
```

##### type

用于 `<input>` 和 `<button>` 元素

指定输入控件的类型

```html
<input type="text" placeholder="Enter your name">
```

##### value

用于 `<input>`, `<button>`, `<option>` 等元素

```html
<input type="text" value="Default Value">
```

##### disabled

（用于表单元素）：禁用元素，使其不可交互。

```html
<input type="text" disabled>
```

##### checked

用于 `<input type="checkbox">` 和 `<input type="radio">`

指定复选框或单选按钮是否被选中

```html
<input type="checkbox" checked>
```

##### placeholder

用于 `<input>` 和 `<textarea>` 元素

在输入框中显示提示文本

```html
<input type="text" placeholder="Enter your email">
```

##### target

用于 `<a>` 和 `<form>` 元素

指定链接或表单提交的目标窗口或框架

```html
<a href="https://www.example.com" target="_blank">Open in new tab</a>
```

#### 不需要值的属性

###### disabled

禁用元素

```html
<input type="text" disabled>z
```

###### readonly

使输入框只读

```html
<input type="text" readonly>
```

###### required

指定输入字段为必填项

```html
<input type="text" required>
```

###### autoplay

用于 `<audio>` 和 `<video>` 元素

自动播放媒体

```html
<video src="video.mp4" autoplay></video>
```

#### 自定义属性

###### data-*

用于存储自定义数据

```html
<div data-user-id="12345" data-role="admin">User Info</div>
```

#### 事件处理属性

##### onclick

当用户点击元素时触发

```html
<button onclick="alert('Button clicked!')">Click Me</button>
```

##### onmouseover

当用户将鼠标悬停在元素上时触发

```html
<div onmouseover="this.style.backgroundColor='yellow'">Hover over me</div>
```

##### onchange

当元素的值发生变化时触发

```html
<input type="text" onchange="alert('Value changed!')">
```

