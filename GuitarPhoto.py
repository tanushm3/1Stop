import cv2
import numpy as np
import math
from PIL import Image
from matplotlib import pyplot as plt

filename = 'E:/Bennett Pdfs/College Project/1Stop/Imports/GuitarJPEG'

img = Image.open( filename + '.jpg' )
img2=img
img2 = img.resize((int(img.size[0]/3),int(img.size[1]/3)),Image.ANTIALIAS)
data = np.asarray( img2 )
bigImg = np.asarray(img)
frame = data
frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
bigImg = cv2.cvtColor(bigImg,cv2.COLOR_RGB2BGR)
blur = cv2.GaussianBlur(bigImg,(5,5),0)
frame2 = cv2.GaussianBlur(frame,(5,5),0.5)

# cv2.resize()



threshLow1=50
threshLow2=100
threshHigh1=60
threshHigh2=200


# #Do Your Calculations on Frame Here:

# Copy edges to the images that will display the results in BGR
cdst = frame.copy()
cdstP = frame.copy()

        
# # Converting the image to grayscale.
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

# Using the Canny filter to get contours
edges = cv2.Canny(gray, threshLow1, threshLow2)
# edges = cv2.GaussianBlur(edges,(5,5),0.5)
edges2 = cv2.Canny(gray2, threshLow1, threshLow2)

# Using the Canny filter with different parameters
edges_high_thresh = cv2.Canny(gray, threshHigh1, threshHigh2,None,5)
edges_high_thresh2 = cv2.Canny(gray2, threshHigh1, threshHigh2)

angle_array=[]

# Probabilistic Line Transform
linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
linesP2 = cv2.HoughLinesP(edges_high_thresh2, 1, np.pi / 180, 50, None, 50, 10)



ones = np.ones((3,3),np.uint8)
eroder = np.ones((1,3),np.uint8)
grayBlur=cv2.GaussianBlur(gray,(3,3),0.5)
# ret, thImg = cv2.threshold(grayBlur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
ret,thImg = cv2.threshold(gray,90,150,cv2.THRESH_BINARY)
ret,thImgInv = cv2.threshold(gray,90,150,cv2.THRESH_BINARY_INV)

dilation = cv2.dilate(thImg,ones)
erosion = cv2.erode(thImgInv,eroder,iterations=5)
ret, erosion = cv2.threshold(erosion,90,150,cv2.THRESH_BINARY_INV)
edges = cv2.Canny(thImg,threshHigh1,threshHigh2)

# Draw the lines
if linesP is not None:
    for i in range(0, len(linesP2)):
        l = linesP[i][0]
        dy= l[3]-l[1]
        dx = l[2]-l[0]
        angle = (math.atan2(dy,dx))*180/np.pi
        angle_array.append(angle)
        
        l2 = linesP2[i][0]
        dy2= l2[3]-l2[1]
        dx2 = l2[2]-l2[0]
        angle2 = (math.atan2(dy2,dx2))*180/np.pi
        
        # if (angle<=10 and angle>=-10 and abs(dx) >70):
        #     cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 2, cv2.LINE_AA)
        # if ((angle<=-60 or angle>=60)):
            # cv2.line(cdstP, (l2[0], l2[1]), (l2[2], l2[3]), (0,255,0), 2, cv2.LINE_AA)
        cv2.line(cdstP, (l2[0], l2[1]), (l2[2], l2[3]), (0,255,0), 2, cv2.LINE_AA)



# x=300
# l=linesP[x][0]
# dy= l[3]-l[1]
# dx = l[2]-l[0]
# angle = (math.atan2(dy,dx))*180/np.pi
# print("ANGLE: ",angle)

# print("x0: ",linesP[x][0][0]) #y0q
# print("y0: ",linesP[x][0][1]) #x0
# print("x1: ",linesP[x][0][2]) #y1
# print("y1: ",linesP[x][0][3]) #x1


cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,255,0), 2, cv2.LINE_AA)

frame1 = np.hstack((gray, edges, edges_high_thresh))
frame2 = np.hstack((gray2, edges2, edges_high_thresh2))

# # # pr1int() 
# frame1 = gray

while(True):
    
    cv2.imshow('fram1',frame1)
    
    cv2.imshow('Probabalisticlines',cdstP)
    # cv2.imshow("Thresh",erosion)
    cv2.imshow("Dilation",dilation)
    cv2.imshow("Erosion",erosion)
    
    # cv2.imshow('Stdlines',cdst)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
    

