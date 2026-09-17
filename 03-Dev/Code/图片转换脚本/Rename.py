import os

def batch_rename(folder_path):
    """
    将指定文件夹内的文件按szy-01、szy-02格式重命名
    :param folder_path: 目标文件夹路径
    """
    try:
        # 获取文件夹内所有文件
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f))]
        
        # 过滤掉隐藏文件（如.DS_Store等）
        files = [f for f in files if not f.startswith('.')]
        
        # 按文件名排序
        files.sort()
        
        # 开始重命名
        for index, filename in enumerate(files, start=1):
            # 获取文件扩展名
            ext = os.path.splitext(filename)[1]
            
            # 构造新文件名
            new_name = f"m17-{index:02d}{ext}"
            
            # 重命名文件
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            
        print(f"完成！共重命名 {len(files)} 个文件")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    folder = input("请输入文件夹路径: ")
    batch_rename(folder)
