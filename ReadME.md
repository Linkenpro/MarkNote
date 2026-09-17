# MarkNote — 软件技巧笔记备忘录

个人学习和工作中积累的软件技巧笔记，涵盖工业设计、图形图像、前后端开发、系统运维等多个领域。

## 目录结构

采用「领域 / 软件」两层结构（2026-09-17 重组）。每个软件目录内的 `png/` 存放该笔记的配图，与 md 用相对路径（`./png/xxx.png`）绑定——**搬迁时需整个软件目录一起移动**，不要单独挪 md。

| 一级领域 | 含义 | 二级目录 |
|---------|------|---------|
| **01-Design** | 设计与影像 | Adobe（Ae / Ai / Ps / Xd / Substance）、Axure、Photography、ffmpeg |
| **02-3D** | 三维与建模 | Blender、Autodesk（CAD / SketchUp / 3dMax）、Rhino、Grasshopper、Marvelous Designer、Materialize |
| **03-Dev** | 开发编程 | Python、Frontend（HTML / CSS / Vue3）、JavaScript、CSharp、Code、Git、SVN |
| **04-System** | 系统与运维 | Windows、Mac、Debian、VPS、NAS、Cloudflare、Docker、CMD |
| **05-Quant** | 量化与交易 | CCXT、TA-lib、TradingView、Quant、Trade |
| **06-Office** | 办公与文档 | PPT、Excel、MarkDown、OfficeTool |

归档原则：**一级看领域，二级看软件**。新增笔记时按「它属于哪个领域 → 用哪个软件」定位；同一软件的多个笔记放在该软件目录下，配图统一进 `png/`。

## 主要内容

- **设计建模**: Rhino 参数化建模、Grasshopper 运算器、Blender 渲染/雕刻/几何节点、Substance 3D 材质
- **图形图像**: Photoshop 精修合成、Illustrator 矢量绘图、摄影构图、PBR 材质生成
- **编程开发**: Python（数据分析/爬虫/Flask/异步）、JavaScript、C#、HTML/CSS/Vue3
- **量化交易**: CCXT 加密货币接口、TA-Lib 技术分析、TradingView Pine Script
- **系统运维**: Windows/Linux/macOS 配置、Docker、VPS 运维、NAS 搭建、Cloudflare CDN
- **多媒体处理**: FFmpeg 格式转换与压缩、ImageMagick 图片处理
