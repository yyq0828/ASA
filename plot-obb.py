import cv2
import numpy as np


def parse_obb_line(line):
    parts = line.strip().split()
    points = [(int(float(parts[i])), int(float(parts[i + 1]))) for i in range(0, 8, 2)]
    category = parts[8]
    extra_info = int(parts[9])
    return np.array(points, dtype=np.int32), category, extra_info


# 图片路径
image_path = 'F:/Paper/dataset/dotav1/val/images/P0019.png'

# .txt文件路径
txt_path = 'F:/Paper/dataset/dotav1/val/Val_Task2_gt/valset_reclabelTxt/P0019.txt'
output_path = 'test.jpg'

# 读取图片
img = cv2.imread(image_path)

# 读取.txt文件
with open(txt_path, 'r') as file:
    lines = file.readlines()

# 遍历每一行数据
for line in lines:
    obb_points, category, extra_info = parse_obb_line(line)

    # 绘制OBB
    cv2.polylines(img, [obb_points], isClosed=True, color=(0, 255, 0), thickness=2)

    # 在图片上添加类别标签
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, category, tuple(obb_points[0]), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# 显示图片
cv2.imshow('Image with OBBs', img)
cv2.imwrite(output_path, img)
cv2.waitKey(0)
cv2.destroyAllWindows()