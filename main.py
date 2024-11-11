from yolov5 import train

# Set path to dataset and specify model architecture (YOLOv5s for small model)
train.run(
    data="data.yaml",
    imgsz=640,
    batch_size=16,
    epochs=100,
    weights="yolov5s.pt",
    name="road_detection",
)

from yolov5 import val

val.run(
    data="data.yaml",
    weights="runs/train/road_detection/weights/best.pt",
    imgsz=640,
    batch_size=16,
)

from yolov5 import detect

detect.run(
    weights="runs/train/road_detection/weights/best.pt",
    source="path/to/test_images",
    imgsz=640,
    conf_thres=0.25,
)

