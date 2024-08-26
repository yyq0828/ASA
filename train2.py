from ultralytics import YOLO
import os
def main():
    model = YOLO('cfg/models/v8/yolov8n-obb.yaml')  # build from YAML and transfer weights
    #model = YOLO('yolov8_LSKblockAttention1.yaml',task='obb')
    model.train(data='cfg/datasets/DOTAv1.yaml', epochs=300, imgsz=1024, batch=8, workers=4)
   # model.val(batch=8, workers=4, imgsz=1024, epochs=300, data='cfg/datasets/DOTAv1.yaml')
if __name__ == '__main__':
   # os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    main()
