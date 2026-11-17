###### 绘制命令

L (Line)：直线

PL (PLine)：多段线

C (Circle)：圆

REC (Rectangle)：矩形

A (Arc)：圆弧

EL (Ellipse)：椭圆

T / MT (MText)：多行文字

###### 修改命令

M (Move)：移动

CO / CP (Copy)：复制

RO (Rotate)：旋转

SC (Scale)：缩放

X (Explode)：炸开

TR (Trim)：修剪

EX (Extend)：延伸

F (Fillet)：圆角

O (Offset)：偏移

MI (Mirror)：镜像

###### 标注与测量

DLI (DimLinear)：线性标注

DAL (DimAligned)：对齐标注（标注斜线）

DRA (DimRadius)：半径标注

DDI (DimDiameter)：直径标注

DAN (DimAngular)：角度标注

D (DimStyle)：打开标注样式管理器

> 修改测量比例 10 倍

###### 界面与系统管理

ST (Style)：文字样式（切换宋体、取消“大字体”的地方）

LA (Layer)：图层管理器

PR / Ctrl + 1：特性面板（修改选定对象的旋转、坐标、颜色等所有细节）

RE (Regen)：重新生成（当圆看起来像多边形时，输入它刷新）

PU (Purge)：清理无用垃圾（缩小文件体积）

MA (MatchProp)：特性匹配（也就是“格式刷”，从有字体的文件刷给没字体的文件）



##### 输出PDF

> 鼠标右键点击**布局1**,选择**页面设置管理器**
>
> 确保选中当前布局，点击右侧的 “修改 ”
>
> - 打印机/绘图仪，AutoCAD PDF (General Documentation).pc3
>
> - 图纸尺寸，ISO full bleed A3 (420.00 x 297.00 MM)，选 Full Bleed 能消除灰色虚线，让画布完全可用
>
> - 打印范围，布局，自动对齐白纸边缘，不用手动框选。
>
> - 打印偏移，0.00, 0.00，确保你的 `(0,0)` 矩形真正贴合纸张左下角。
>
> - 打印比例，1：1
>
> - 打印样式表：monochrome.ctb，黑白稿
>
>   保留你设置的颜色，acad.ctb
>
> - 打印选项：
>
>   > 勾选 **“打印对象线宽”**（确保壳体轮廓有厚度感）。
>
>   > 勾选 **“打印图纸空间最后”**。
>
>   PDF选项
>
>   特性 (Properties)” -> “自定义特性” -> “PDF 选项”-> 确保 **“捕获图形中使用的字体”** 是勾选状态