import os
import sys
from pathlib import Path

def remove_duplicate_filenames(root_folder):
    """
    遍历 root_folder 下所有文件，对文件名（含扩展名）相同的文件，
    保留第一个遇到的，删除其余。
    
    参数:
        root_folder (str): 要处理的根文件夹路径
    """
    seen_files = {}  # key: filename (e.g., "image.jpg"), value: full path of the kept file

    root = Path(root_folder)
    if not root.exists() or not root.is_dir():
        print(f"错误：路径 '{root_folder}' 不存在或不是文件夹。")
        return

    # 收集所有文件
    all_files = []
    for file_path in root.rglob('*'):
        if file_path.is_file():
            all_files.append(file_path)

    # 按路径排序（确保遍历顺序一致，可选）
    all_files.sort()

    for file_path in all_files:
        filename = file_path.name  # 包含后缀，如 "report.pdf"

        if filename in seen_files:
            # 已经存在同名文件，删除当前这个
            print(f"删除重复文件: {file_path}")
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"  删除失败: {e}")
        else:
            # 第一次见到这个文件名，保留
            seen_files[filename] = file_path
            print(f"保留文件: {file_path}")

    print("\n处理完成。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python remove_duplicates.py <文件夹路径>")
        sys.exit(1)

    folder_path = sys.argv[1]
    remove_duplicate_filenames(folder_path)