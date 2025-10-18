

##### 视频处理

###### webm视频转mp4格式

```py
import os 
import subprocess 
 
def convert_webm_to_mp4(folder_path):
    # 检查FFmpeg可用性
    try:
        subprocess.run(["ffmpeg",  "-version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("错误：请先安装FFmpeg并添加到系统环境变量")
        print("下载地址：https://ffmpeg.org/download.html") 
        return 
 
    # 遍历所有深层文件 [5]()[13]()
    for root, dirs, files in os.walk(folder_path): 
        for file in files:
            if file.endswith(".webm"): 
                input_path = os.path.join(root,  file)
                output_path = os.path.splitext(input_path)[0]()   + ".mp4"
                
                # 执行转换命令 [6]()
                cmd = [
                    "ffmpeg",
                    "-y",  # 覆盖已存在文件 
                    "-i", input_path,
                    "-loglevel", "error",  # 仅显示错误日志 
                    output_path 
                ]
                
                try:
                    # 执行转换并等待完成 [9]()
                    result = subprocess.run(cmd,  check=True, capture_output=True, text=True)
                    
                    # 转换成功则删除源文件 
                    if result.returncode  == 0 and os.path.exists(output_path): 
                        os.remove(input_path) 
                        print(f"已转换并删除：{input_path}")
                except subprocess.CalledProcessError as e:
                    print(f"转换失败：{file}\n错误信息：{e.stderr}") 
 
if __name__ == "__main__":
    target_folder = r"D:\Blender\教程_Video"  # 修改为你的文件夹路径 
    convert_webm_to_mp4(target_folder)

```

###### 小宝影院

```python
import requests
import os
import re

m3u8_url = "https://m3u8.hmrvideo.com/play/fddc840a02024fbeabcece58f49f23e4.m3u8"

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'origin': 'https://xiaoxintv.cc',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

m3u8_content = requests.get(url=m3u8_url,headers=headers).text

# 解析 M3U8 文件内容，提取 TS 片段 URL
ts_urls = re.sub('#E.*', '', m3u8_content).split()

# 创建下载目录
download_dir = './download'
os.makedirs(download_dir, exist_ok=True)

# 下载 TS 片段
for i, ts_url in enumerate(ts_urls):
    filename = os.path.join(download_dir, f'segment_{i}.ts')
    with requests.get(ts_url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    # 写入状态
    print(f'已写入片段 {i}')

# 完成提示
print('完成！')

```

##### 图片处理

###### webp转为png格式

```py
from PIL import Image
import os

# 指定目录路径
directory_path = r"D:\笔记整理\Photography\photo_insert"

# 获取目录下的所有 .webp 文件
webp_files = [f for f in os.listdir(directory_path) if f.endswith('.webp')]

# 遍历 .webp 文件并转换为 .png 文件
for webp_file in webp_files:
    # 构建 .webp 文件的完整路径
    webp_path = os.path.join(directory_path, webp_file)
    
    # 打开 .webp 文件
    with Image.open(webp_path) as img:
        # 构建 .png 文件的完整路径
        png_file = os.path.splitext(webp_file)[0] + '.png'
        png_path = os.path.join(directory_path, png_file)
        
        # 将图片保存为 .png 格式
        img.save(png_path, 'PNG')
        print(f"转换: {webp_path} 到 {png_path}")

```

##### 文件夹处理

###### 文件夹名翻译

```py
from googletrans import Translator
import os

# 初始化翻译器
translator = Translator()

# 指定文件夹路径
folder_path = "F:/Interior"

# 获取指定文件夹中的所有项目
items = os.listdir(folder_path)

# 遍历文件夹中的所有项目
for item in items:
    # 构建项目的完整路径
    item_path = os.path.join(folder_path, item)
    # 判断项目是否为文件夹
    if os.path.isdir(item_path):
        # 判断文件夹名是否包含中文字符
        if any('\u4e00' <= char <= '\u9fff' for char in item):
            # 中文文件夹名，不需要翻译
            print(f"{item} 是中文文件夹")
        else:
            # 如果文件夹名中含有下划线，则使用下划线分割单词
            folder_name_parts = item.split('_')
            # 将单词首字母大写，其余字母小写
            folder_name_parts = [part.capitalize() for part in folder_name_parts]
            # 将单词连接起来
            translated_name = ' '.join(folder_name_parts)
            # 将英文文件夹名翻译为中文
            translated_name = translator.translate(translated_name, src='en', dest='zh-cn').text
            # 构建文件夹的完整路径
            old_folder_path = os.path.join(folder_path, item)
            new_folder_path = os.path.join(folder_path, translated_name)
            # 重命名文件夹
            os.rename(old_folder_path, new_folder_path)
            print(f"已将文件夹 {item} 改名为 {translated_name}")

```

###### 根据后缀名分类文件

```python
"""
扫描指定文件夹中的所有文件
然后将它们根据文件后缀名移动到相应的文件夹内。
"""
import os
import shutil

# 源文件夹路径
source_folder = "C:/Your/Source/Folder"

# 目标文件夹路径
target_folder = "C:/Your/Target/Folder"

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 获取文件的完整路径
    file_path = os.path.join(source_folder, filename)
    # 判断是否为文件
    if os.path.isfile(file_path):
        # 获取文件后缀名
        _, file_extension = os.path.splitext(filename)
        # 定义目标文件夹路径
        destination_folder = os.path.join(target_folder, file_extension[1:].lower())
        # 如果目标文件夹不存在，则创建它
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # 移动文件到目标文件夹
        shutil.move(file_path, os.path.join(destination_folder, filename))

print("文件已归类完成。")

```

###### 遍历删除指定目录文件夹

```python
import os

# 指定文件夹路径
# E:/Texture/Fabric/CG_Fabric
folder_path = "E:/Texture/Fabric/CG_Fabric"

# 遍历指定目录及其子目录下的所有文件夹和文件
for root, dirs, files in os.walk(folder_path):
    # 遍历当前目录下的所有文件
    for file_name in files:
        # 构建文件的完整路径
        file_path = os.path.join(root, file_name)
        # 如果是文件且后缀不是 .hdr 或 .exr
        if os.path.isfile(file_path) and not file_name.lower().endswith(('.jpg', '.png')):
            # 删除文件
            os.remove(file_path)

print("删除完成。")
```

###### 重命名文件夹

```
import os

# 指定文件夹路径
folder_path = "G:/产品设计Alan/2023年/12月份"

# 遍历文件夹中的所有文件夹
for folder_name in os.listdir(folder_path):
    # 构建文件夹的完整路径
    folder_full_path = os.path.join(folder_path, folder_name)
    # 检查是否是文件夹
    if os.path.isdir(folder_full_path):
        # 将文件夹名称中的点（.）替换为下划线（_）
        new_folder_name = folder_name.replace(".", "_")
        # 构建新的文件夹完整路径
        new_folder_full_path = os.path.join(folder_path, new_folder_name)
        # 重命名文件夹
        os.rename(folder_full_path, new_folder_full_path)
        print(f"重命名文件夹: {folder_name} to {new_folder_name}")
```

###### 提取文件夹内3dm后缀文件

```
import os
import shutil

# 指定源文件夹路径和目标文件夹路径
source_folder = r'G:\产品设计Alan\Work'
target_folder = r'G:\产品设计Alan\Copy'

# 如果目标文件夹不存在，则创建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹及其子文件夹
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith('.3dm'):
            # 构建源文件路径
            source_file = os.path.join(root, file)
            # 构建目标文件路径
            target_file = os.path.join(target_folder, file)
            
            # 如果目标文件已存在，处理文件重名问题
            if os.path.exists(target_file):
                base, extension = os.path.splitext(file)
                counter = 1
                new_target_file = os.path.join(target_folder, f"{base}_{counter}{extension}")
                while os.path.exists(new_target_file):
                    counter += 1
                    new_target_file = os.path.join(target_folder, f"{base}_{counter}{extension}")
                target_file = new_target_file
            
            # 复制文件到目标文件夹
            shutil.copy2(source_file, target_file)
            print(f"已将文件 {source_file} 复制到 {target_file}")

print("复制完成。")

```

