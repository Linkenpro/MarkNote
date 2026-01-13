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