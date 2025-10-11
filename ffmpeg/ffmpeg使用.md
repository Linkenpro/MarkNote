##### ffmpeg图片压缩

###### 压缩图片大小

可通过调整分辨率、质量参数或结合编码优化实现

```
ffmpeg -i input.jpg  -q:v 30 output_compressed.jpg  
```

> -q:v 30（1为最高质量，100为最低质量），数值越低文件越大

###### 调整图片分辨率

```
ffmpeg -i input.jpg  -vf "scale=1920:1080" -q:v 50 output_scaled.jpg  
```

###### 图片格式优化

转换为更高效的图片格式（如WebP），或调整编码参数

```
ffmpeg -i input.jpg  -c:v libwebp -quality 80 output.webp 
```

###### 色彩空间优化

减少色彩采样（如YUV420p）：

```
ffmpeg -i input.jpg  -pix_fmt yuv420p -q:v 40 output_yuv.jpg  
```
