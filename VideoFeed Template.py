import cv2
import numpy as np
import dlib
from math import hypot
from moviepy import *
from scipy import ndimage
import random
import os



ipFileName="Tanush"
cap = cv2.VideoCapture(0)
_, fr = cap.read()
print(fr.shape)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print(frame_width,frame_height)

fxName = "SmurfEffect"
fps = 30
code = 0
badName = random.randint(1,10000)

out = cv2.VideoWriter(f'E:\Bennett Pdfs\College Project\Sem 2\ExportedVids\{badName}.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))


# Displaying Video Feed
while True:
    x, f = cap.read()
    frame = cv2.flip(f,1)

    
    #Do Your Calculations on Frame Here:
    
        
    frame1 = frame
    
    
    # Displaying Video Feeds
    # Original:
    cv2.imshow("Input", frame)
    # Calcualed Outputs:
    cv2.imshow("Output", frame1)
    out.write(frame1)
    
    #End Video
    key = cv2.waitKey(1)
    if key == ord('x'):
        code+=1
        out.release()
        break




out.release()
# Renaming Files
os.rename(f'E:\Bennett Pdfs\College Project\Sem 2\ExportedVids\{badName}.avi',f'E:\Bennett Pdfs\College Project\Sem 2\ExportedVids\{ipFileName}_{fxName}_v{badName}.avi')



# Releasing The Video Cam and Closing all Windows
cv2.destroyAllWindows()

cap.release()