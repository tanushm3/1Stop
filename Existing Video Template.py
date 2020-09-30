"""Existing Vid Template"""

import cv2
import numpy as np
import dlib
from math import hypot
from moviepy import *
from scipy import ndimage
import random
import os
import copy


ipFileName = "Guitar"
cap = cv2.VideoCapture(f"E:/Bennett Pdfs/College Project/1Stop/Imports/{ipFileName}.mp4",0)
# cap = cv2.VideoCapture(0);
_, fr = cap.read()
print(fr.shape)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fxName = "BetterEdgeDetection"
fps = 20
code = 0
badName = random.randint(1,10000)
out = cv2.VideoWriter(f'{badName}.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height),isColor=False)
out1 = cv2.VideoWriter(f'{badName}1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height),isColor=False)

"""
        EXISTING VIDEO LOOP
"""
threshLow1=50
threshLow2=100
threshHigh1=120
threshHigh2=200

# Using Existing Video
while(cap.isOpened()):

    
    ret, frame = cap.read()

    if (ret):
            
        #Do Your Calculations on Frame Here:
        
        # Converting the image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Using the Canny filter to get contours
        edges = cv2.Canny(gray, threshLow1, threshLow2)
        # Using the Canny filter with different parameters
        edges_high_thresh = cv2.Canny(gray, threshHigh1, threshHigh2)
        # Stacking the images to print them together
        # For comparison
        
        
        # Display the resulting frame
        # cv2.imshow('Frame', frame1)    
        """Hough Lines"""
        # img = cv2.imread(cv.samples.findFile('sudoku.png'))
        # gray = cv2.cvtColor(img,cv.COLOR_BGR2GRAY)
        # edges = cv2.Canny(gray,50,150,apertureSize = 3)
        # lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
        # for line in lines:
        #     x1,y1,x2,y2 = line[0]
        #     cv2.line(edges,(x1,y1),(x2,y2),(0,255,0),2)

        frame1 = np.hstack((gray, edges, edges_high_thresh))
        # print() 
        
        cv2.imshow('fram1',frame1)
        
         
        # frame1 = cv2.rotate(frame1, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # both = np.concatenate((frame, frame1), axis=1)
    
        # cv2.imshow('Frame', both)
        # cv2.imshow("frame",frame)
        # cv2.imshow('fram1',frame1)
        out.write(edges)
        # out1.write(edges_high_thresh)
        # print('written')
    
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


""" 
            ENDING 
"""

out.release()
out1.release()
# Renaming Files
os.rename(f'{badName}.avi',f'E:/Bennett Pdfs/College Project/1Stop/ExportedVids/{ipFileName}_{fxName}HOUGH_Thresh({threshLow1},{threshLow2})_v{badName}.avi')
os.rename(f'{badName}1.avi',f'E:/Bennett Pdfs/College Project/1Stop/ExportedVids/{ipFileName}_{fxName}HighThresh_Thresh({threshHigh1},{threshHigh2})_v{badName}.avi')



# Releasing The Video Cam and Closing all Windows
cv2.destroyAllWindows()

cap.release()