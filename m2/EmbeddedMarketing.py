from fileinput import filename
from gettext import install
from pydoc import synopsis
import sys
import cv2
import os
from datetime import datetime
def videoplay():
    os.chdir('E:/Embedded_Marketing/m2/')
    i = 1
    #wait = 0
    Video = cv2.VideoCapture('handbagvi.mp4')
    while True:
        ret, img = Video.read()
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, str(datetime.now()),(20,40),font,2,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('live video',img)
        key = cv2.waitKey(25)
        #wait = wait+1
        if key == ord('q'):
            filename = 'Frame.jpg'
            cv2.imwrite(filename,img)
            i = i+1
            cv2.waitKey()
            #wait = 0
            Video.release()
            cv2.destroyAllWindows()
            break
        if key == ord('e'):
            Video.release()
            cv2.destroyAllWindows()
            break