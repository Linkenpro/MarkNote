import os
from pathlib import Path

def find_md_files(root_path):
    """递归查找root_path下所有.md文件，返回路径列表"""
    root = Path(root_path)
    if not root.exists() or not root.is_dir():
        raise ValueError("路径不存在或不是目录")
    return list(root.rglob("*.md"))

def main():
    while True:
        target = input("请输入目标路径: ").strip()
        if not target:
            print("路径不能为空，请重新输入。")
            continue
        try:
            md_files = find_md_files(target)
            break
        except ValueError as e:
            print(f"错误: {e}，请重新输入。")
    
    if not md_files:
        print("未找到任何.md文件。")
    else:
        print(f"\n找到 {len(md_files)} 个.md文件：")
        for file in md_files:
            print(file)

if __name__ == "__main__":
    main()