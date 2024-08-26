from ultralytics import YOLO
import os
def main():
    #model = YOLO('cfg/models/v8/yolov8n.yaml')  # build from YAML and transfer weights
    model = YOLO('yolov8_LSKblockAttention2.yaml',task='obb').load('yolov8n-obb.pt')
    model.train(data='cfg/datasets/HRSC.yaml', epochs=200, imgsz=1024, batch=16, workers=8)
    model.val(batch=8, workers=4, imgsz=1024, epochs=300, data='cfg/datasets/HRSC.yaml')
if __name__ == '__main__':
    #os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    main()

