# WebPack逆向

Webpack是一个现代的静态模块打包工具，它主要用于前端开发中的模块化打包和构建。通过Webpack，开发者可以将多个模块(包括JavaScript、CSS、图片等)进行打包，生成优化后的静态资源文件，以供在浏览器中加载和运行。

###### 目的

完成功能模块的调用

```js
/*
!function(形参){加载器}([模块1，模块2,...])

!function(形参){加载器}({"k1":"模块1","k2":"模块2"})
*/
```

> 概念了解：匿名函数
>
> !：分隔符

```js
//匿名函数
!(function(x:number[]):void {
    console.Log("foo...",x)
    ]})(x:[1,2,3])
    
!(function (x: {name: string}):void {
    console.Log("foo...",x)
    ]})(x:[1,2,3])
```

加载器逻辑——构建一个对象，能够轻松调用所有的功能函数

> 闭包

###### 1.数组格式

```js
!function (e:(...)[]):void {
    //加载器逻辑:构建一个对象，能够轻松调用所有的功能函数
    var t: {} = {};	//缓存对象

    //加载器函数
    function n(r):any {
        //判断缓存池里面有没有，是否是第一次调用
        if(t[r])
            return t[r].exports;
        
        //2.
        var o:{...} = t[r]= {
            i: r,
            l: !1,
            exports: {}
        };
        
        // 3.真正的功能调用
        e[r].call(o.exports, o, o.exports, n);
        return o.exports.exports;
    }
        
    //调用第一个函数
    n(r:0)

}([
    function ():void {
        console.Log("foo功能!")
    },
        
    function ():void {
        console.Log("bar功能!")
    },

])
```

###### 2.object格式

```js
!function (e) {
    var t = {};
    
    function n(r) {
        if(t[r])
            return t[r].exports;
        var o = t[r] = {
            i:r,
            1: !1,
            exports:{}
        };
        
        e[r].call(o.exports, o, o.exports, n);
        return o.exports.exports; //返回 o.exports.exports,而不是整个 o.exports 对象
    }
    
    window.loader = n;
    
    n("1002");
    
}({
    "1001":function () {
        console.log("foo");
        this.exports = 100; //直接修改 exports变量
    },
    "1002":function () {
        console.log("bar");
        this.exports = 200; //直接修改 exports变量
    }
});

```

逆向webpack视频30：23