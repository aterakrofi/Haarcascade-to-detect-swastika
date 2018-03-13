#Import libraries, classifier and and input image in grayscale mode  
# coding: utf-8 on
import numpy as np  
import cv2  
   
My_classifier = cv2.CascadeClassifier('cascade.xml')    
img = cv2.imread('test.jpg')   
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
 
#Locating the swastika's in the supplied image. If swastika's are found, the script returns the positions of detected swastika’s as Rect(x,y,w,h).   
#Once we get these locations, we can create a Regions of Interest (ROI) for the Swastika   
 
detector = My_classifier.detectMultiScale(gray, 1.3, 5)  
for (x,y,w,h) in detector:  
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  
    roi_gray = gray[y:y+h, x:x+w]  
    roi_color = img[y:y+h, x:x+w] 
#using a solution proposed on Stackoverflow https://stackoverflow.com/questions/18064914/how-to-use-op#encv-python-to-blur-faces    
#Create a clone of image and create a sub-rectangle with the same coordinates of the detected image  
    result_image = img.copy()   
    sub_img = img[y:y+h, x:x+w]  
      
# apply a gaussian blur on this new rectangle image  
    sub_img = cv2.GaussianBlur(sub_img,(173, 173), 70)  
      
# merge this blurry rectangle to our final image  
    result_image[y:y+sub_img.shape[0], x:x+sub_img.shape[1]] = sub_img  
    img_file_name = "./SWT_" + str(y) + ".jpg"  
    
cv2.imwrite('result.jpg', result_image) 

