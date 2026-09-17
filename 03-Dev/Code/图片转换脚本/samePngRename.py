import os

def rename_duplicate_pngs_global():
    while True:
        folder_path = input("请输入要递归扫描的根目录路径: ").strip()
        folder_path = folder_path.replace('"', '').replace("'", "")

        if os.path.exists(folder_path):
            break
        else:
            print(f"路径不存在，请检查后重新输入。")

    total_scanned = 0
    rename_count = 0
    
    # 【关键修改】将记录字典放在循环外，实现全局唯一性检查
    seen_names = {}

    print(f"\n[任务启动] 开始全局深度扫描: {folder_path}")
    print("注意：如果不同文件夹下存在同名文件，也将被改名以保证全局唯一。")
    print("-" * 80)

    for root, dirs, files in os.walk(folder_path):
        # 筛选当前目录下的 png
        png_files = [f for f in files if f.lower().endswith('.png')]
        
        for filename in png_files:
            total_scanned += 1
            name_part, extension = os.path.splitext(filename)
            
            # 统一转为小写进行比对，防止 "Image.png" 和 "image.png" 逃过检查
            name_lower = name_part.lower()
            
            if name_lower in seen_names:
                # 获取该名字出现的次数，构造新名字
                suffix_idx = seen_names[name_lower]
                new_name = f"{name_part}重名-{suffix_idx}{extension}"
                
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)
                
                try:
                    os.rename(old_path, new_path)
                    relative_path = os.path.relpath(old_path, folder_path)
                    print(f"-> [冲突改名] {relative_path}  \n          => {new_name}")
                    
                    seen_names[name_lower] += 1
                    rename_count += 1
                except Exception as e:
                    print(f"!! [错误] 无法重命名 {filename}: {e}")
            else:
                # 第一次记录这个文件名
                seen_names[name_lower] = 1

    print("-" * 80)
    print(f"总计扫描 PNG 数: {total_scanned}")
    print(f"全局修改重名数: {rename_count}")

if __name__ == "__main__":
    rename_duplicate_pngs_global()