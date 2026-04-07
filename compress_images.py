from PIL import Image
import os

def compress_image(input_path, output_path, quality=70, max_width=800):
    """压缩图片"""
    with Image.open(input_path) as img:
        # 转换为RGB模式（去除透明通道）
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # 等比例缩放
        width, height = img.size
        if width > max_width:
            ratio = max_width / width
            new_height = int(height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # 保存压缩后的图片
        img.save(output_path, 'JPEG', quality=quality, optimize=True)

# 图片目录
images_dir = 'images'
compressed_dir = 'images_compressed'

# 创建压缩目录
if not os.path.exists(compressed_dir):
    os.makedirs(compressed_dir)

# 压缩所有图片
for filename in os.listdir(images_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(images_dir, filename)
        output_path = os.path.join(compressed_dir, filename)

        # 根据图片类型设置不同的压缩参数
        if 'banner' in filename.lower():
            # Banner图保持较高质量
            compress_image(input_path, output_path, quality=75, max_width=750)
        else:
            # 其他图片可以压缩更多
            compress_image(input_path, output_path, quality=65, max_width=750)

        # 显示压缩结果
        original_size = os.path.getsize(input_path) / 1024
        compressed_size = os.path.getsize(output_path) / 1024
        print(f"{filename}: {original_size:.1f}KB -> {compressed_size:.1f}KB ({compressed_size/original_size*100:.1f}%)")

print("\n压缩完成！")
