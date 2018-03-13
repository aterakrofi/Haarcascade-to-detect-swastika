#coding: utf-8 on
#import numpy as np  
import cv2  
  
My_classifier = cv2.CascadeClassifier('cascade.xml')  
cap = cv2.VideoCapture(0)

while 1:  
    ret, cam = cap.read()  
    gray = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)  
    detector = My_classifier.detectMultiScale(gray, 1.3, 5)  
      
#Locate the swastika's in the supplied webcam feed. If swastika's are found, the script returns the positions   
#of detected swastika’s as Rect(x,y,w,h).   
#Once we get these locations, we can create a Regions of Interest (ROI) for the Swastika   
  
    for (x,y,w,h) in detector:  
        cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)  
        roi_gray = gray[y:y+h, x:x+w]  
        roi_color = cam[y:y+h, x:x+w]  
  
#Display detected image with rectangles around ROI     
  
    cv2.imshow('cam',cam)  
    k = cv2.waitKey(30) & 0xff  
    if k == 27:  
        break  
  
cap.release()  
cv2.destroyAllWindows() 
