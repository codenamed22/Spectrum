import numpy as np
import cv2
import os

file = os.path.abspath("C:\\Users\\naanan\\Documents\\user_pref.txt")

f = open(file)
allColors=f.readline()
borderColor=f.readline()
colorToDetect=""
if str(allColors) == 'False\n':
	colorToDetect=f.readline()

f.close()

if borderColor == 'Blue\n':
	borderColorHSV = (255,0,0)
elif borderColor == 'Red\n':
	borderColorHSV = (0,0,255)
elif borderColor == 'Green\n':
	borderColorHSV = (0,255,0)
elif borderColor == 'White\n':
	borderColorHSV = (255,255,255)
elif borderColor == 'Black\n':
	borderColorHSV = (0,0,0)
else:
	borderColorHSV = (255,255,255)

dictionary ={
                    'White':([0, 0, 146], [180, 34, 255]),
                    'Gray':([0, 0, 22], [180, 34, 146]),
                    'Light-red':([0,157, 25], [6,255,255]),
                    'Light-Pink':([0,0, 25], [6,157,255]),
                    'Orange':([6, 33, 168], [23, 255, 255]),
                    'Brown':([6, 33, 25], [23, 255, 168]),
                    'Yellow':([23, 33, 25], [32, 255, 255]),
                    'Green':([32, 33, 25], [75, 255, 255]), 
                    'Blue-Green':([75, 33, 25], [90, 255, 255]), 
                    'Blue':([90,33, 45], [123, 255, 255]),
                    'Purple':([123, 112, 25], [155, 255, 255]),
                    'Light-Purple':([123, 33, 25], [155, 125, 255]),                   
                    'Pink':([155,34, 25], [180,225,255]),
                    'Deep-Pink':([175,0, 25], [180,157,255]),
                    'Deep-red':([175,157, 25], [180,255,255]),    
                    'Black':([0, 0, 0], [180, 255, 26]),      
                    }

dictionarySmall ={
                    'Light-red':([0,157, 25], [6,255,255]),
                    'Orange':([6, 33, 168], [23, 255, 255]),
                    'Brown':([6, 33, 25], [23, 255, 168]),
                    'Yellow':([23, 33, 25], [32, 255, 255]),
                    'Green':([32, 33, 25], [75, 255, 255]), 
                    'Blue-Green':([75, 33, 25], [90, 255, 255]), 
                    'Blue':([90,33, 45], [123, 255, 255]),                   
                    'Pink':([155,34, 25], [180,225,255]),
                    'Deep-Pink':([175,0, 25], [180,157,255]),
                    'Deep-red':([175,157, 25], [180,255,255]),    
                    }   
    
color_name = []
color_count =[]

cap = cv2.VideoCapture(0)
(ret, image) = cap.read()

cv2.namedWindow('image')

while(1):
    (ret, image) = cap.read()
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if (allColors == 'False\n'):
	    key=colorToDetect
	    #lower=[90, 33, 45]
	    #upper=[123, 255, 255]
	    lower=dictionary[key][0]
	    upper=dictionary[key][1]

	    lower = np.array(lower, dtype = "uint8")
	    upper = np.array(upper, dtype = "uint8")
	    mask = cv2.inRange(image_HSV, lower, upper)
	    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	    for contour in contours:
	        area = cv2.contourArea(contour)
	        if(area>2000):
	            M = cv2.moments(contour)
	            cX = int((M["m10"] / M["m00"]))
	            cY = int((M["m01"] / M["m00"]))
	            cv2.drawContours(image, contour, -1, borderColorHSV, 2)
	            cv2.putText(image, key, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	    cv2.imshow('image',image)
	    k = cv2.waitKey(20) & 0xFF
	    if k == 27:
	        break
    else:
    	for key in dictionarySmall:
		    lower=dictionary[key][0]
		    upper=dictionary[key][1]

		    lower = np.array(lower, dtype = "uint8")
		    upper = np.array(upper, dtype = "uint8")
		    mask = cv2.inRange(image_HSV, lower, upper)
		    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		    for contour in contours:
		        area = cv2.contourArea(contour)
		        if(area>2000):
		            M = cv2.moments(contour)
		            cX = int((M["m10"] / M["m00"]))
		            cY = int((M["m01"] / M["m00"]))
		            cv2.drawContours(image, contour, -1, borderColorHSV, 2)
		            cv2.putText(image, key, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
		    cv2.imshow('image',image)
		    k = cv2.waitKey(20) & 0xFF
		    if k == 27:
		        break

cap.release()
cv2.destroyAllWindows()
