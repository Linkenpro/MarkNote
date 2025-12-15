#### 编辑器快捷键

| 功能               | 快捷键                                                  |
| ------------------ | ------------------------------------------------------- |
| 新建窗口           | `Ctrl+N`                                                |
| 打开文件           | `Ctrl+O`                                                |
| 重新打开关闭的文件 | `Ctrl+Shift+T`                                          |
| 保存               | `Ctrl+S`                                                |
| 另存为             | `Ctrl+Shift+S`                                          |
| 打印               | `Ctrl+Alt+P`                                            |
| 偏好设置           | `Ctrl+,`                                                |
| 关闭标签页         | `Ctrl+W`                                                |
| 撤销               | `Ctrl+Z`                                                |
| 重做               | `Ctrl+Y`                                                |
| 剪切               | `Ctrl+X`                                                |
| 复制               | `Ctrl+C`                                                |
| 粘贴               | `Ctrl+V`                                                |
| 复制为 Markdown    | `Ctrl+Shift+C`                                          |
| 粘贴为纯文本       | `Ctrl+Shift+V`（注：原文为 Ctrl+Shift+C，疑误，已修正） |
| 全选               | `Ctrl+A`                                                |
| 选中段落/块        | `Alt+Ctrl+P`                                            |
| 选中当前行         | `Ctrl+L`                                                |
| 选中当前格式文本   | `Ctrl+E`                                                |
| 选中当前词         | `Ctrl+D`                                                |
| 跳转到文首         | `Ctrl+Home`                                             |
| 跳转到文末         | `Ctrl+End`                                              |
| 删除块             | `Alt+Ctrl+Shift+P`                                      |
| 删除当前行         | `Alt+Ctrl+Shift+L`                                      |
| 删除当前格式文本   | `Alt+Ctrl+Shift+E`                                      |
| 删除当前词         | `Ctrl+Shift+D`                                          |
| 查找               | `Ctrl+F`                                                |
| 查找下一个         | `F3`                                                    |
| 查找上一个         | `Shift+F3`                                              |
| 替换               | `Ctrl+H`                                                |
| 插入表情/符号      | `Win+.`                                                 |

> 一级标题：`Ctrl+1`
>
> 二级标题：`Ctrl+2`
>
> 六级标题：`Ctrl+6`
>
> 段落（清除格式）：`Ctrl+0`
>
> 表格：无快捷键（通常通过菜单）
>
> 代码块：`Ctrl+Shift+K`
>
> 公式块：`Ctrl+Shift+M`

------

#### 数学公式语法

##### 基础用法

行内公式`$E = mc^2$`

##### **独立居中公式**

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

##### 上标与下标与组合

###### 上标：

$$
x^2
$$

###### 下标

$$
x_1
$$

###### 组合

$$
x^{10}
$$

###### 嵌套

$$
x^{y^z}
$$

##### 括号

- 普通：`( )`, `[ ]`
- 大括号：`\{ \}` 或 `\lbrace \rbrace`
- 自适应大小：`\left( \frac{a}{b} \right)` → (*b**a*)
- 尖括号：`\langle x \rangle` → ⟨*x*⟩

##### 分式与根式

$$
\frac{a}{b}        → $\frac{a}{b}$
\cfrac{a}{b}       → $\cfrac{a}{b}$（用于连分数）
\sqrt{x}           → $\sqrt{x}$
\sqrt[n]{x+y}      → $\sqrt[n]{x+y}$
$$



##### 求和、积分、连乘

$$
\sum_{i=1}^n i^2   → $\sum_{i=1}^n i^2$
\int_0^\infty f(x)dx → $\int_0^\infty f(x)dx$
\prod_{k=1}^n a_k  → $\prod_{k=1}^n a_k$
\bigcup, \bigcap   → $\bigcup, \bigcap$
$$



##### 多行公式与对齐

$$
\begin{aligned}
a &= b + c \\
  &= d + e + f
\end{aligned}
$$

##### 分段函数

$$
f(x) = 
\begin{cases}
x^2, & x \geq 0 \\
-x,  & x < 0
\end{cases}
$$

##### 矩阵

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

> `pmatrix`（圆括号）、`Bmatrix`（花括号）、`vmatrix`（行列式）

##### 常用符号速查

| 类别     | 符号       | LaTeX                                 |
| -------- | ---------- | ------------------------------------- |
| 比较     | ≤, ≥, ≠    | `\le`, `\ge`, `\ne`                   |
| 集合     | ∈, ∪, ∩, ∅ | `\in`, `\cup`, `\cap`, `\emptyset`    |
| 逻辑     | ∧, ∨, ¬, ∀ | `\land`, `\lor`, `\lnot`, `\forall`   |
| 箭头     | →, ←, ⇒    | `\to`, `\leftarrow`, `\Rightarrow`    |
| 希腊字母 | α, β, γ, Δ | `\alpha`, `\beta`, `\gamma`, `\Delta` |
| 特殊     | ∞, ∇, ℜ, ℵ | `\infty`, `\nabla`, `\Re`, `\aleph`   |

##### 公式标记与引用

$$
E = mc^2 \tag{1}
$$



##### 字体控制

- 黑板粗体（数集）：`\mathbb{R}` → R, `\mathbb{Z}` → Z
- 粗体：`\mathbf{x}` → **x**
- 打字机字体：`\mathtt{code}` → code

------

###### 金融公式

$$
DIF = EMA_{12} - EMA_{26}
$$
