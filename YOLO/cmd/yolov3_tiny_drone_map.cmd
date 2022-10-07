darknet.exe detector map data/obj_drone.data data/yolov3-tiny_drone4.cfg backup/yolov3-tiny_drone5_4000.weights -iou_thresh 0.2
darknet.exe detector map data/obj_drone.data data/yolov3-tiny_drone4.cfg backup/yolov3-tiny_drone5_5000.weights -iou_thresh 0.2
darknet.exe detector map data/obj_drone.data data/yolov3-tiny_drone4.cfg backup/yolov3-tiny_drone5_6000.weights -iou_thresh 0.2
darknet.exe detector map data/obj_drone.data data/yolov3-tiny_drone4.cfg backup/yolov3-tiny_drone5_12000.weights -iou_thresh 0.2

pause