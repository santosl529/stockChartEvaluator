# stockChartEvaluator
python data.py
python dataSorter.py
yolo classify train data=dataset model=yolov8n-cls.yaml epochs=100 imgsz=40
change path to best model
python predict.py 
STOCKS END UP IN bestStocks.txt and goodStocks.txt