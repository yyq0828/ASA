from ultralytics import YOLO
 
def main():
    model = YOLO("runs/detect/train30/weights/best.pt")
    model.val(data="cfg/datasets/vedai.yaml", imgsz=1024, batch=8, workers=4)
if __name__ == '__main__':
    main()
