import os
import shutil

def copy_first_n_files(source_dir, dest_dir, n=150):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 获取源目录中所有文件的列表，按名称排序
    files = sorted(os.listdir(source_dir))

    # 计数器，用于跟踪已经复制了多少文件
    copied_files_count = 0

    # 遍历文件列表
    for file in files:
        source_file_path = os.path.join(source_dir, file)
        dest_file_path = os.path.join(dest_dir, file)

        # 检查是否为文件（避免复制目录）
        if os.path.isfile(source_file_path):
            shutil.copy2(source_file_path, dest_file_path)
            copied_files_count += 1

            # 如果已经复制了足够的文件，就退出循环
            if copied_files_count >= n:
                break

# 使用示例
source_directory = '/yyq/rs/code/ultralytics-main/ultralytics/runs/obb/yolov8n_dota'
destination_directory = '/yyq/rs/code/ultralytics-main/ultralytics/runs/obb/yolov8n_dota_simple'

copy_first_n_files(source_directory, destination_directory)