import os
import shutil

# 源文件夹路径
source_folder = '/yyq/rs/datasets/split_ms_dota/images/val'
# 目标文件夹路径
target_folder = '/yyq/rs/datasets/split_ms_dota/images/val_100'

# 如果目标文件夹不存在，则创建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 获取源文件夹中所有文件的列表
files = os.listdir(source_folder)
# 确保列表按名称排序
files.sort()

# 用于计数的变量
counter = 0

# 遍历文件列表
for index, file in enumerate(files):
    # 只处理图片，这里假设图片扩展名为.jpg，可根据实际情况调整
    if file.endswith('.png'):
        # 检查是否应该复制当前文件
        if index % 98 == counter:
            # 构建完整的文件路径
            src_file = os.path.join(source_folder, file)
            dst_file = os.path.join(target_folder, file)
            # 复制文件
            shutil.copy2(src_file, dst_file)
            print(f'Copied {file}')
            # 当达到100个文件时停止
            counter += 1
            if counter >= 100:
                break

print('Done.')