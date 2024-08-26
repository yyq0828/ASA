import cv2
import numpy as np

# 假设这是从txt文件中读取的一行数据
line = "1648.0 53.0 1710.0 53.0 1710.0 88.0 1648.0 88.0 small-vehicle 0"

def parse_obb_line(line):
    parts = line.strip().split()
    points = [(int(float(parts[i])), int(float(parts[i + 1]))) for i in range(0, 8, 2)]
    category = parts[8]
    extra_info = int(parts[9])
    return np.array(points, dtype=np.int32), category, extra_info

# 解析这一行数据
obb_points, category, extra_info = parse_obb_line(line)

# 读取图片，假设图像路径为'image_path'
image_path = 'P0019__1__0___1048.png'
img = cv2.imread(image_path)

# 绘制OBB
cv2.polylines(img, [obb_points], isClosed=True, color=(0, 255, 0), thickness=2)

# 添加类别标签
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, category, tuple(obb_points[0]), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# 显示和保存图片
cv2.imshow('Image with OBB', img)
cv2.imwrite('output_with_obb.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()