import os
from pathlib import Path
from PIL import Image
import imageio.v2 as imageio

# 支持的输入格式与对应的读取方式
SUPPORTED_FORMATS = {
    '.webp': 'pil',
    '.avif': 'imageio',
}

def safe_remove(file_path: Path):
    """安全删除文件，带异常处理"""
    try:
        file_path.unlink()
        print(f"🗑️  已删除: {file_path}")
    except OSError as e:
        print(f"⚠️  无法删除 {file_path}: {e}")

def convert_with_pil(input_path: Path, output_path: Path):
    """使用 PIL 转换图像（如 WebP）"""
    with Image.open(input_path) as img:
        # 如果是 RGBA 且目标为 PNG，保留透明通道
        img.save(output_path, 'PNG')

def convert_with_imageio(input_path: Path, output_path: Path):
    """使用 imageio 转换图像（如 AVIF）"""
    image = imageio.imread(str(input_path))  # imageio 需要字符串路径
    imageio.imwrite(str(output_path), image)

def convert_image(input_path: Path):
    """通用图像转换函数：根据扩展名选择转换器，并处理输出/删除"""
    suffix = input_path.suffix.lower()
    method = SUPPORTED_FORMATS.get(suffix)
    if not method:
        return False  # 不支持的格式

    output_path = input_path.with_suffix('.png')

    # 防止覆盖已存在的 PNG（可选：也可加编号）
    if output_path.exists():
        print(f"⚠️  目标文件已存在，跳过: {output_path}")
        return False

    try:
        if method == 'pil':
            convert_with_pil(input_path, output_path)
        elif method == 'imageio':
            convert_with_imageio(input_path, output_path)
        else:
            print(f"❌ 未知转换方法: {method}")
            return False

        print(f"✅ 已转换: {input_path} → {output_path}")
        safe_remove(input_path)
        return True

    except Exception as e:
        print(f"❌ 转换失败 {input_path}: {e}")
        return False

def process_directory(root_dir: str):
    root = Path(root_dir).resolve()
    if not root.is_dir():
        print(f"❌ 路径无效或不是目录: {root}")
        return

    converted_count = 0
    total_files = 0

    # 使用 rglob 递归查找所有匹配文件
    all_files = []
    for ext in SUPPORTED_FORMATS:
        all_files.extend(root.rglob(f'*{ext}'))
        all_files.extend(root.rglob(f'*{ext.upper()}'))  # 兼容大写扩展名

    # 去重（虽然 unlikely，但安全起见）
    all_files = list(set(all_files))

    if not all_files:
        print(f"⚠️  在 '{root}' 及其子目录中未找到 .webp 或 .avif 文件。")
        return

    print(f"🔍 找到 {len(all_files)} 个待处理文件，开始转换...")

    for file_path in sorted(all_files):  # 排序便于观察进度
        if file_path.is_file():
            total_files += 1
            if convert_image(file_path):
                converted_count += 1

    print(f"\n✅ 转换完成！成功: {converted_count}/{total_files} 个文件。")

if __name__ == "__main__":
    # C:\Users\源恒\Desktop
    target = input("请输入要转换的文件夹路径：").strip().strip('"')
    process_directory(target)