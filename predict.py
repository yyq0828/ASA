from ultralytics import YOLO

model = YOLO("yolov8n-obb.pt")
#model = YOLO("runs/obb/train5/weights/best.pt")  # 模型文件路径

results = model("P0079.png", visualize=True)  # 要预测图片路径和使用可视化

