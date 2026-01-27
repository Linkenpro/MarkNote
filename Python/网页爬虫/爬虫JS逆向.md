#### JS逆向

###### 头部签名验证

###### 请求参数签名验证

###### cookie验证

###### 响应数据验证

#### 基本爬虫构成

- http

  > 

- https

- wss

###### chrome浏览器——F12/Ctrl+Shift+I

元素：dom

控制台：

源代码：静态资源，html+css+js渲染

网络：不叫抓包，监听数据

- XHR：
- 文档：纯静态
- CSS
- JS
- 字体
- 图片
- 媒体
- 清单
- WS
- Wasm
- 其他

CURL：右键，复制为cURL(bash)

##### 数据加密

###### js存在混淆或者加密

> 发起程序：调用堆栈
>
> 在js代码中，方法的执行逻辑

###### 定位加密位置，或解密

> 带关键字
>
> 不可以是泛用的名字
>
> 外部一定需要有一个解密的方法或者函数(不可以是内置)x_ccccc(密文)
>
> - 解密的方法或者函数(t.密文).xxxx，调用
> - 解密方法或者方法(不是内置)(关键字)， 
> - t=关键字(密文)
> 
> x_ccccc(密文).name错误的方式

```js
function Kc(e) {
    return JSoN.parse(Vc("sjdqmp20161205#_316@gfmt", rr.decode(e),0,0,"012345677890123"，1))
}
```

重新整理代码——Ctrl+Alt+L

> 

##### python第三方库——pyexecjs

确保系统已安装Node.js

并且node命令可用

```py
data = {
    page':'1',
    'num':'20',
    'ca_uuid':'feef62bfdac45a94b9cd89aed5c235be',
}

# .json()
response = requests.post(url: 'https://wyiosapi.qmpsee.com/Web/getcaDetail'headers-headers, data=data).json()
encrypt_data = response['encrypt_data']

# 加载Node.js文件
with open('./encrypt_codeJs.js', 'r', encoding='utf-8') as f:
    js_code = f.read() 
    
#执行 Node.js 代码
result = pyexecjs.compile(js_code).call('Kc')

print(result)
```

###### 通用方法

**XHR/提取断点**

> 请求发送的位置
>
> 

```
点击加号
把路径添加进去
```

**作用域**

```
调试的输出信息
```

后端ajax渲染(JSON数据渲染网站 JSON.parse()数据类型转变)无混淆JS

- JSON.parse(数据类型转变不具备解密功能的

- 嵌套一个解密的方法或者函数(不是内置的方法或者函数)

  > JSON.parse(函数或方法(密文))——JSON.parse(Kf(密文))
  > a=函数或方法(密文)——json.parse(a)
  >
  > 错误：a =json.parse(xx）——方法或者函数(a)

- JSON.parse(解密的方法或者函数(密文))

- a=解密的方法或者函数(密文)

- 结合堆栈(XHR)使用不然很多文件都有这个方法

#### cookie反爬

###### 动态生成cookie

> 每次访问一个页面都会生成新的cookie
> 海关药监局工商xxx
> 瑞数6

###### 时效性cookie

> 一定时间内有效 容易过期
> boss直聘 51job xxx

###### 需要登录网站

> 服务器返回cookie中有特殊字段加密
> 批量登录

###### 接口请求对象当中

###### document (dom节点)

##### cookie加密

静态cookie处理
13二次加载cookie组成
同花顺v值加密

> cookie有v值

- 时效性cookie

- set-cookie对象

- 直接js代码生成在cookie当中的某一个字段

- 定位技巧 HOOK

  > 控制台注入hook做cookie
  > 在第一次使用的时候
  > 生成位置与使用位置空间隔了10几个栈
  >
  > 自己写的js代码，根据请求的内容区分对象：
  >
  > hook setheaders ->当中的关键字
  >
  > hook setcookie ->关键字
  >
  > JSON.parse(数据类型的转换) hook JSON
  >
  > hook data
  >
  > hook open 请求参数
  > hook 网页反调试

- 可以直接搜索关键字

源代码——代码段——自己写工具代码

cookie2hook

```js
//自执行函数
(function () {
    'use strict'
    Object.defineProperty(document, 'cookie', {
        get: function() {
            // debugger;
            return "";
        },
        set: function(value) {
            debugger;
            return value;
        },
    });
})()

(function () {
    var cookie_cache = document.cookie;
    Object.defineProperty(document, 'cookie', {
        get: function() {
            console.log('Get cookie');
            // debugger
            return cookie_cache;
        },
        set: function (val) {
            console.log('Set cookie', val);
            debugger; // Pause execution on every write
            return cookie_cache; 
        },
    });
})() 
```

