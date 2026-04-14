import os
import shutil
from pathlib import Path

def collect_svg_files(source_dir, target_dir):
    # 转换为绝对路径并标准化
    source_path = os.path.abspath(source_dir)
    target_path = os.path.abspath(target_dir)

    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"[*] 已创建目标目录: {target_path}")

    count = 0
    print(f"正在启动扫描: {source_path}")
    print(f"{'源文件完整路径':<70} -> {'新文件名'}")
    print("-" * 100)

    # 改用 os.walk，它在处理磁盘根目录时通常比 rglob 更稳健
    for root, dirs, files in os.walk(source_path):
        # 排除目标文件夹，防止无限扫描
        if target_path in os.path.abspath(root):
            continue

        for file in files:
            if file.lower().endswith('.svg'):
                src_file_path = os.path.join(root, file)
                
                try:
                    # 准备目标文件名（处理冲突）
                    base_name = file
                    dest_file_path = os.path.join(target_path, base_name)
                    
                    if os.path.exists(dest_file_path):
                        stem, suffix = os.path.splitext(file)
                        i = 1
                        while os.path.exists(os.path.join(target_path, f"{stem}_{i}{suffix}")):
                            i += 1
                        dest_file_path = os.path.join(target_path, f"{stem}_{i}{suffix}")

                    # 打印移动信息
                    print(f"{src_file_path:<70} -> {os.path.basename(dest_file_path)}")

                    # 执行移动
                    shutil.move(src_file_path, dest_file_path)
                    count += 1
                except Exception as e:
                    print(f"\n[!] 跳过文件 {file} (原因: {e})")

    print("-" * 100)
    print(f"扫描完毕,总计移动文件数: {count}")

if __name__ == "__main__":
    # 如果还是 0，建议先测试一个更小的文件夹，例如 "D:/Github"
    SOURCE = "D:/" 
    TARGET = "D:/SVG_Collection"
    
    collect_svg_files(SOURCE, TARGET)