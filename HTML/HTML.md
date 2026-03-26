#### 标签

###### html

```html
<html>
</html>
```

包含head和body

样式

```html
无样式
```

###### head

```html
<head>
</head>
```

###### meta

定义关于 HTML 文档的元数据，常见属性

> charset：定义文档的字符编码
> name：与 content 属性结合，用于描述网页的元数据名称
> http-equiv：模拟 HTTP 响应头信息
> content：指定元数据的值

**字符编码声明**

```html
<meta charset="UTF-8">
```

**页面描述与关键词**

```html
<meta name="description" content="网页描述">
```

**视口设置**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**浏览器行为控制**

```html

```



###### link

定义当前文档与外部资源之间关系的标签，核心属性：

> rel：定义当前文档与被链接文档之间的关系，是必需属性
>
> - `stylesheet`：链接到外部样式表
> - `icon`：链接到网站图标
> - `prefetch`：规定应该对目标资源进行缓存
> - `preload`：用于预加载当前页面必需的资源
>
> href：指定被链接文档的位置。
> type：规定被链接文档的 MIME 类型。
> media：规定被链接文档将在什么设备上显示

**链接外部样式表**

```html
<link rel="stylesheet" href="styles.css">
```

**链接网站图标（favicon）**

```html
<link href = "//www.gstatic.com/images/branding/searchlogo/ico/favicon.ico" rel="icon">
```

**预加载资源**

```html

```

> <link> 标签必须放在文档的 <head> 部分，且可以出现多次。为了确保资源优先加载，建议将 <link> 标签放在 <head> 中

###### style

用于定义文档样式信息（CSS）的标签,属性：

1. **`type`**‌：
   - 该属性用于指定样式表的 MIME 类型，通常设置为 `text/css`。
   -  HTML5 中，此属性不再是必需的
2. ‌**`media`**‌：
   - 该属性用于指定样式表将应用于哪种媒体类型。
   - 例如：`media="screen"` 表示样式表仅应用于屏幕显示，`media="print"` 表示样式表仅应用于打印输出。
   - 可以指定多个媒体类型，用逗号分隔。
3. ‌**`scoped`**‌：
   - 这是 HTML5 中引入的一个属性，用于限制样式仅应用于 `<style>` 元素的父元素及其子元素。
   - 该属性允许为文档的特定部分定义样式，而不是整个文档。
   - 例如：`<style scoped>` 可以确保样式只影响当前 `<style>` 标签所在的元素及其后代元素。
4. ‌**`disabled`**‌：
   - 该属性用于禁用样式表，使其不生效。
   - 例如：`<style disabled>` 会阻止样式表中的规则被应用到页面上。
5. ‌**`title`**‌：
   - 该属性用于为样式表提供一个标题，通常用于用户选择不同的样式表时的标识。
   - 例如：`<style title="Alternative Stylesheet">` 可以帮助用户识别样式表的用途。

```html
<head>
  <style>
    /* CSS 规则 */
  </style>
</head>
```

> 嵌入式样式‌：在 HTML 文档的 <head> 部分使用 <style> 标签编写 CSS 规则，适用于样式较少且仅用于当前页面的情况。
> ‌多 <style> 标签‌：一个文档可以包含多个 <style> 标签。

###### title

用于定义网页标题的标签

1. **告诉访客文章或网站的主题**‌：标题标签告诉访问者该页面的内容主题。
2. ‌**告诉搜索引擎索引**‌：标题标签告诉搜索引擎蜘蛛该页面是以什么内容为主题的。
3. ‌**SEO 优化**‌：搜索引擎算法使用页面标题来决定在搜索结果中列出页面时的顺序。

```html
<head>
  <title>HTML 参考手册</title>
</head>
```

###### body

> - **唯一性**‌：一个 HTML 文档中只能有一个 `<body>` 标签。
> - ‌**内容容器**‌：包含所有可见内容，如文本、图像、链接、视频等。
> - ‌**位置要求**‌：必须位于 `<html>` 标签内部，且紧跟在 `<head>` 标签之后。

```html
<!DOCTYPE html>
<html>
<head>
  <title>网页标题</title>
</head>
<body>
  <!-- 这里是网页的主体内容 -->
  <h1>欢迎来到我的网站</h1>
  <p>这是一个段落，描述了一些信息。</p>
  <a href="https://www.example.com">访问示例网站</a>
</body>
</html>

```

默认样式：

```css
body {
  display: block;
  margin: 8px;
}
```

- `<body>` 标签必须位于 `<html>` 标签内部。
- 如果 `<body>` 标签放在 `<html>` 标签之外，浏览器会自动将其移动到正确位置。
- `<body>` 标签内可以包含几乎所有 HTML 元素。

###### h

标题标签 <h1> 到 <h6> 用于定义不同层级的标题

```
<h1>：默认字体大小最大，通常为 2em（约 32px，基于默认字体大小 16px）。
<h2>：默认字体大小次之，通常为 1.5em（约 24px）。
<h3>：默认字体大小为 1.17em（约 18.72px）。
<h4>：默认字体大小为 1em（约 16px）。
<h5>：默认字体大小为 0.83em（约 13.28px）。
<h6>：默认字体大小最小，通常为 0.67em（约 10.72px）。
```

默认样式

```css
h1 {
  display: block;
  font-size: 2em;
  margin-top: 0.67em;
  margin-bottom: 0.67em;
  margin-left: 0;
  margin-right: 0;
  font-weight: bold;
}
```

```
<h1>：默认上下外边距约为 0.67em。
<h2>：默认上下外边距约为 0.83em。
<h3>：默认上下外边距约为 1em。
<h4>：默认上下外边距约为 1.33em。
<h5>：默认上下外边距约为 1.67em。
<h6>：默认上下外边距约为 2.33em。
```

###### div

