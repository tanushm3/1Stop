# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 00:38:27 2020

@author: TANUSH MAHAJAN

PERFORM ForeGround Selection:
    
"""

import cv2
import numpy as np
import math
from PIL import Image
import copy
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

# filename = 'verticalLines'

# img = Image.open( filename + '.jpeg' )
# # img2=img
# img2 = img.resize((int(img.size[0]),int(img.size[1])),Image.ANTIALIAS)

# data = np.asarray( img2 )
# frame = data
# frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

# frame = cv2.imread("VerticalLines.jpeg")
angle_array=[]
def filterHoriz(frame):
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    kernalV = [[-1,-2,-1],[0,0,0],[1,2,1]]
    kv = np.array(kernalV)
    filtImgV =cv2.filter2D(frame,-1,kv)
    return filtImgV

def filterVert(frame):
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    kernalH = [[-1,0,1],[-2,0,2],[-1,0,1]]
    kh = np.array(kernalH)
    filtImgH = cv2.filter2D(frame,-1,kh)
    return filtImgH
def CannyBlurAndErodeV(gray):
    kernelSm = np.ones((3,3),np.uint8)
    gray = cv2.GaussianBlur(gray,(5,5),0)
    gray = cv2.erode(gray,kernelSm,iterations=1)
    gray = cv2.dilate(gray,kernelSm,iterations=1)
    edges = cv2.Canny(gray,100,200)
    return edges
def CannyBlurAndErodeH(gray):
    kernelSmDil = np.ones((1,3),np.uint8)
    kernelSmErode = np.ones((3,3),np.uint8)
    gray = cv2.GaussianBlur(gray,(5,5),0)
    # laplacian = cv2.Laplacian(gray,cv2.CV_64F)
    # sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    # sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
    gray = cv2.erode(gray,kernelSmErode,iterations=1)
    # gray = cv2.dilate(gray,kernelSmDil,iterations=1)
    # laplacian = cv2.cvtColor(laplacian,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150)
    # data = copy.deepcopy(laplacian)
    # edges=laplacian
    return edges

# def findparallel(lines):

#     lines1 = []
#     for i in range(len(lines)):
#         for j in range(len(lines)):
#             if (i == j):continue
#             if (abs(lines[i][1] - lines[j][1]) <=50 ):          
#                  #You've found a parallel line!
#                  lines1.append((i,j))
#     return lines1
arr1=[]
arr2=[]
arr3=[]
finPts=[]
actualList=[]
def intersectior(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

frames_30=[]
def addFrames(frames_30,f):
    if(len(frames_30)<30):
        frames_30.append(f)
def sortFramesByLength(frames_30):
    for i in range(len(frames_30)-1):
        for j in range(i+1,len(frames_30)):
            if(len(frames_30[i])<len(frames_30[j])):
                temp =copy.deepcopy(frames_30[i])
                frames_30[i]=copy.deepcopy(frames_30[j])
                frames_30[j]=copy.deepcopy(temp)

                
    
def calibrate(x,y,frames_30):
    if (len(arr1)<=4):
        arr1.append([x,y])
    else:
        if(len(arr2)<=4):
            arr2.apped([x,y])
        else:
            if(len(arr3)<=4):
                arr3.append([x,y])
            else:
                a1=intersectior(arr1,arr2)
                a2=intersectior(arr2,arr3)
def bubbleSort(arr): 
    n = len(arr) 
    # arr = array[0]
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr.iloc[j,0] > arr.iloc[j+1,0] :
                temp = arr.iloc[j]
                arr.iloc[j]= arr.iloc[j+1]
                arr.iloc[j+1]=temp
                # arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr
  
 #(x,y) 
"""
def calibrateOrNot(frameArray,flag):
    if flag==True:
        finPts.clear()
    if (len(finPts)>=30):
        arr1 = finPts[0:6]
        arr2 = finPts[6:12]
        for i in arr1:
            #i = {(x,y), (x2,y2)}
            i1 = [0]
            i2=[1]
            # ls1 and ls 2
            '''
            ls1=ls1[0]+ls1[1]
            ls2=ls2[0]+ls2[1]
            sort(ls1)
            sort(ls2)
            starter=0
            for i in range(len(ls1)):
                for j in range(starter,len(ls2)):
                    if (ls1[j+50]>=ls2[i]):
                        starter=j-1
                        break
                    if(abs(ls1[i]-ls2[j])<1=0):
                        point=[a[i],b[i]]
                        mainList.add(point)
            REPEAT THE SAME LOOP FOR LS3 and LS4
            
                        
                        
            
            '''
            for j in arr2:
                #j = (x,y)
                i = i[0]+i[1]
                j = j[0]+j[1]     
                if(abs(i-j)<10):
                    actualList.append(i)
                    
        #calculate the cood and display
        
        
    else:
        #add frames to finPts
        finPts.append(frameArray)
        
 """                    

    
flag=0
cap = cv2.VideoCapture(0)
_,fgray=cap.read()
fgray= cv2.flip(fgray,1)
fgray = cv2.cvtColor(fgray,cv2.COLOR_BGR2GRAY)
kernelSm = np.ones((3,3),np.uint8)
kernelM = np.ones((7,5),np.uint8)
frameCount=0
# container_dataFrame=pd.DataFrame(['sum','x','y'],index=0)
container_dataFrame=pd.DataFrame(columns=['sum','x','y'])
while(True):
    
    frameCount +=1
    if(len(container_dataFrame)<10):
        frameCount=0
    _, frame = cap.read()
    frame= cv2.flip(frame,1)
    cdstP = copy.deepcopy(frame)
    gray=   cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    '''
    
    # fgray = cv2.cvtColor(fgray,cv2.COLOR_BGR2GRAY)
    difference = cv2.absdiff(gray,fgray)
    difference = cv2.GaussianBlur(difference,(5,5),0)
    # th2 = cv2.adaptiveThreshold(difference,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    #         cv2.THRESH_BINARY_INV,11,2)
    ret,th2 = cv2.threshold(difference,50,150,cv2.THRESH_BINARY)
    th2 = cv2.erode(th2,kernelSm,iterations=2)
    th2 = cv2.dilate(th2,kernelSm,iterations=2)
    result2=cv2.bitwise_and(frame,frame, mask=th2)
    # th1
    cv2.imshow("Frames",th2)
    '''
    filtImgV =filterVert(frame)
    filtImgH = filterHoriz(frame)
    
    edgesV = CannyBlurAndErodeV(filtImgV)
    # edges = CannyBlurAndErodeH(gray)
    edges = CannyBlurAndErodeH(filtImgH)
    # Probabilistic Line Transform
    linesP = cv2.HoughLinesP(edgesV, 1, np.pi / 180, 50, None, 50, 10)
    linesP2 = cv2.HoughLinesP(edgesV, 1, np.pi / 180, 50, None, 50, 10)
    # linesP = findparallel(linesP)
    # Draw the lines
    # linesP_DF = pd.DataFrame(linesP)
    
    
    if linesP is not None:
        linesP_Y1 = linesP[:,0,1]
        linesP_Y2 = linesP[:,0,3]
        # print("Length of Lines P: ",len(linesP))
        mean1 = np.mean(linesP_Y1)
        mean2 = np.mean(linesP_Y2)
    cv2.line(cdstP,(0,int(mean1-20)),(400,int(mean1-20)),(0,0,255),2,cv2.LINE_AA)
    
    cv2.line(cdstP,(0,int(mean2+100)),(400,int(mean2+100)),(255,0,0),2,cv2.LINE_AA)
    cv2.line(cdstP,(60,0),(60,600),(255,255,0),2,cv2.LINE_AA)
    cv2.line(cdstP,(340,0),(340,600),(255,255,0),2,cv2.LINE_AA)
    
    if linesP is not None and flag%2==0:
        flag=0
        # linesP_Y1 = linesP[:,0,1]
        # linesP_Y2 = linesP[:,0,3]
        # mean1 = np.mean(linesP_Y1)
        # mean2 = np.mean(linesP_Y2)
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            dy= l[3]-l[1]
            dx = l[2]-l[0]
            angle = (math.atan2(dy,dx))*180/np.pi
            if (flag==True):
                angle_array.append(angle)
            
            l2 = linesP2[i][0]
            dy2= l2[3]-l2[1]
            dx2 = l2[2]-l2[0]
            angle2 = (math.atan2(dy2,dx2))*180/np.pi
            
            # if (angle<=10 and angle>=-10 and abs(dx) >70):
            #     # linesHorizontal.append
            #     cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 2, cv2.LINE_AA)
            if ((angle<=-70 or angle>=70) and ((mean2-30)<=l[3]) and ((mean1+45)>=l[1]) ):
                cv2.line(cdstP, (l2[0], l2[1]), (l2[2], l2[3]), (0,255,0), 2, cv2.LINE_AA)
            # cv2.line(cdstP, (l2[0], l2[1]), (l2[2], l2[3]), (0,255,0), 2, cv2.LINE_AA)
    
    # circleImg=copy.deepcopy(edgesV)
    # blurcirc = cv2.GaussianBlur(circleImg,(5,5),0)
    # circleImg = cv2.HoughCircles(blurcirc,cv2.HOUGH_GRADIENT,1,4,param1=50,param2=30, minRadius=0,maxRadius=0)
    # if circleImg is not None:
    #     detected_circles = np.uint16(np.around(circleImg))
    #     if detected_circles is not None and linesP is not None  and flag%2==1:
    #         for (x,y,r) in detected_circles[0,:]:
    #             # if y<mean2 and y>mean1:
    #             cv2.circle(edgesV,(x,y),r,(0,0,255),2)
            
    # newImg = cv2.GaussianBlur(edgesV,(5,11),0)
    # _,newImg = cv2.threshold(filtImgV,100,200,cv2.THRESH_BINARY)
    
    
    _,filtImgV = cv2.threshold(filtImgV,50,200,cv2.THRESH_BINARY)
    # _,newImg = cv2.threshold(filtImgV,50,200,cv2.THRESH_BINARY)
    # filtImgV = cv2.GaussianBlur(filtImgV,(5,5),0)
    
    filtImgV = cv2.erode(filtImgV,kernelSm,iterations=1)
    filtImgV = cv2.dilate(filtImgV,kernelM,iterations=2)
    filtImgV = cv2.erode(filtImgV,kernelSm,iterations=1)
    filtImgV = cv2.medianBlur(filtImgV,5,0)
    filtImgV = cv2.dilate(filtImgV,kernelM,iterations=1)
    filtImgV = cv2.erode(filtImgV,kernelSm,iterations=1)
    # filtImgV = cv2.dilate(filtImgV,kernelM,iterations=1)
    # newImg = cv2.GaussianBlur(edgesV,(5,11),0)
    # _,newImg = cv2.threshold(filtImgV,100,200,cv2.THRESH_BINARY) 
    # newImg = cv2.erode(newImg,kernelSm,iterations=1)
    # Apply Hough transform on the blurred image. 
    # newImg = edgesV.copy()
    # # filtImgV = cv2.medianBlur(filtImgV,5,0)
    # detected_circles = cv2.HoughCircles(newImg,  
    #                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 100, 
    #                param2 = 30, minRadius = 1, maxRadius = 10) 
    
      
    # # Draw circles that are detected. 
    # if detected_circles is not None: 
      
    #     # Convert the circle parameters a, b and r to integers. 
    #     detected_circles = np.uint16(np.around(detected_circles)) 
      
    #     for pt in detected_circles[0, :]: 
    #         a, b, r = pt[0], pt[1], pt[2] 
      
    #         # Draw the circumference of the circle. 
    #         cv2.circle(newImg, (a, b), r, (0, 255, 0), 2) 
      
    #         # Draw a small circle (of radius 1) to show the center. 
    #         cv2.circle(newImg, (a, b), 1, (0, 0, 255), 3) 
    #         cv2.imshow("Detected Circle", newImg) 
    #         # cv2.waitKey(0) 
    
    # filtImgV = cv2.medianBlur(filtImgV,5,0)
    contours, _ = cv2.findContours(filtImgV,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    c_array=[]
    
    
    
    for contour in contours:
        # compute the center of the contour
        c=contour
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # cwidthARR.append(cY)
        area = cv2.contourArea(contour)
        if area < 200 and cY>(mean2) and cY<(mean1) and cX>=60 and cX<=340:
            cv2.drawContours(cdstP,contour,-1,(0,255,0),3)
            cv2.circle(cdstP,(cX,cY),2,(0,0,255))
            c_array.append([cX,cY])
            # cY_array.append(cY)
    
    # calibrateOrNot()
    cSum_Array=[]
    for x in c_array:
        s = x[0]+x[1]
        cSum_Array.append([s,x[0],x[1]])
    # bubbleSort(cSum_Array)
    # bubbleSort(cSum_Array)
    cSum_Array = pd.DataFrame(cSum_Array)
    # print(cSum_Array.iloc())
    cSum_Array.drop_duplicates(subset =[0], 
                     keep = 'first', inplace = True) 
    # print("LENGTH Before:",len(cSum_Array))
    cSum_Array = bubbleSort(cSum_Array)
    # print("LENGTH After:",len(cSum_Array))
    print("Data:")
    print(cSum_Array)
    print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    if(len(container_dataFrame)<150 ):
        print("entered")
        container_dataFrame.append(cSum_Array,ignore_index=True)
        print("Length:",len(container_dataFrame))
        if(len(container_dataFrame)>1):
            container_dataFrame.sort_values(container_dataFrame.columns[0])
    else:
        splitLen=int(len(container_dataFrame)/3)
        d1= container_dataFrame[0:splitLen].mode()
        d2= container_dataFrame[splitLen:splitLen*2].mode()
        d3= container_dataFrame[splitLen*2:splitLen*3].mode()
        # print("D1:")
        # print(d1)
        # print("---------------------------")
        
        # x = stats.mode(d1)
        # y = stats.mode(d2)
        # z = stats.mode(d3)
        
        
    # print("Co-Ordinate: ",cX_array)
    flag+=1
    
    if frame is None:
        break
    
    # cv2.imshow("Frames",difference)
    cv2.imshow("Frame",frame)
    cv2.imshow("Filtered Image Vertical",filtImgV)
    # cv2.imshow("Filtered Image Circles",circleImg)
    cv2.imshow("Vertical Edges",edgesV)
    cv2.imshow("CdstP",cdstP)
    # cv2.imshow("Horiz Edges",edges)
    # cv2.imshow("Filter Image Horizintol",filtImgH)
    
    
    k = cv2.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
    elif k == ord('c'):
        flag=True
        fgray=gray.copy()
        frameCount=0
        container_dataFrame=pd.DataFrame()
        
    
    
        
cv2.destroyAllWindows()
cap.release()