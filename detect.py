import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO('yolov8_LSKblockAttention2.yaml')  # yolov8-TFF2-p2.yaml
    # model = YOLO('ultralytics/cfg/models/ours/yolov8.yaml')  # yolov8-TFF2-p2.yaml
    # model = YOLO('runs/train/ours_yolov8n_tt100k/weights/best.pt') # select your model.pt path
    # model = YOLO('runs/detect/train28/weights/best.pt')
    model = YOLO('runs/obb/train48/weights/best.pt')
    model.predict(source='/yyq/rs/datasets/split_ms_dota/images/val_100',
                  imgsz=512,
                  project='runs/obb',
                  name='yolov8n-dota',
                  save=True,
                #   visualize=True # visualize model features maps
                )