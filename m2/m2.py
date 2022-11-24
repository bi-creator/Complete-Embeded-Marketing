import cv2
import matplotlib.pyplot as plt
from EmbeddedMarketing import videoplay
from postimg import postimg

videoplay()
image = cv2.imread("E:/Embedded_Marketing/m2/Frame.jpg")
height, width = image.shape[:2]
resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)
fig = plt.gcf()
fig.set_size_inches(18, 10)
plt.axis("off")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
img = 'E:\\Embedded_Marketing\\m2\\Frame.jpg'  # or file, Path, PIL, OpenCV, numpy, list
results = model(img)
crops = results.crop(save=True)  # or .show(), .save(), .print(), .pandas(), etc.
postimg()