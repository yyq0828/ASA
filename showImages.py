import random

import cv2
import os
import tkinter as tk


def txtShow(img, txt, save=True):
    image = cv2.imread(img)
    height, width = image.shape[:2]  # 获取原始图像的高和宽

    # 读取classes类别信息
    # with open('./classes.txt', 'r') as f:
    #     classes = f.read().splitlines()
    # ['Leconte', 'Boerner', 'linnaeus', 'armandi', 'coleoptera', 'acuminatus', 'Linnaeus']
    classes=['Car', 'Truck', 'Boat', 'Tractor', 'Camping (Van)', 'Pickup', 'Plane', 'Others', 'Vans']
    # 读取yolo格式标注的txt信息
    with open(txt, 'r') as f:
        labels = f.read().splitlines()
    # ['0 0.403646 0.485491 0.103423 0.110863', '1 0.658482 0.425595 0.09375 0.099702', '2 0.482515 0.603795 0.061756 0.045387', '3 0.594122 0.610863 0.063244 0.052083', '4 0.496652 0.387649 0.064732 0.049107']

    ob = []  # 存放目标信息
    for i in labels:
        cl, x_centre, y_centre, w, h,*_  = i.split(' ')

        # 需要将数据类型转换成数字型
        cl, x_centre, y_centre, w, h = int(cl), float(x_centre), float(y_centre), float(w), float(h)
        name = classes[cl]  # 根据classes文件获取真实目标
        xmin = int(x_centre * width - w * width / 2)  # 坐标转换
        ymin = int(y_centre * height - h * height / 2)
        xmax = int(x_centre * width + w * width / 2)
        ymax = int(y_centre * height + h * height / 2)

        tmp = [name, xmin, ymin, xmax, ymax]  # 单个检测框
        ob.append(tmp)

    # 绘制检测框
    index = 2
    for name, x1, y1, x2, y2 in ob:
        cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)  # 绘制矩形框
        cv2.putText(image, name, (x1, y1-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.7, thickness=2, color=(0, 255, 0))
    # 保存图像
    if save:
        # 使用range生成指定范围内的随机数（可指定步长）
        random_int_in_range = random.randrange(0, 101, 5)
        cv2.imwrite(str(random_int_in_range)+'result.png', image)

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    print("屏幕宽度:", screen_width, "屏幕高度:", screen_height)
    # 展示图像
    # 调整图像大小以适应屏幕分辨率
    resized_image = cv2.resize(image, (screen_width, screen_height))
    cv2.imshow('test', resized_image)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # img_paths = os.listdir('F:/Paper/dataset/vedai/vedai_yolo/val/images/00001253.png')
    # img_path = 'train2017/13.jpg'  # 传入图片 , '711.jpg' '751.jpg', '2456.jpg', '8558.jpg', '13917.jpg', '27548.jpg', '68945.jpg', '16549.jpg'
    img_paths = ['/yyq/rs/datasets/split_ms_dota/images/val/P0019__1__0___1048.png']
    for img_name in img_paths:

        # label_path = img_path.replace('images', 'labels')
        img_path = os.path.join('/yyq/rs/datasets/split_ms_dota/images/val/', img_name)
        label_path = os.path.join('/yyq/rs/datasets/split_ms_dota/labels/val/', img_name)
        label_path = label_path.replace('.png', '.txt')  # 自动获取相应的txt标签文件
        label_path = label_path.replace('images', 'labels')  # 自动获取相应的txt标签文件
        txtShow(img=img_path, txt=label_path, save=True)