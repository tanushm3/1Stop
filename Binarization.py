from PIL import Image
import cv2
import numpy as np

# Declaring important Variables
th0 = 128
th1 = 100
th2 = 150

# #Using  Image
# im = np.array(Image.open('data/src/lena_square.png').convert('L').resize((256, 256)))
# print(type(im))
# # <class 'numpy.ndarray'>
# im_bool = im > th
# print(im_bool)



# Loading Camera
cap = cv2.VideoCapture(0)
_, fr = cap.read()
print(fr.shape)



# Displaying Video Feed
while True:
    x, f = cap.read()
    image = cv2.flip(f,1)
    # We use cvtColor, to convert to grayscale 
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    #Do Your Calculations on Frame Here:
    frame128 = ((frame > th0) * 255).astype(np.uint8)
    frame64 = ((frame > th1) * 255).astype(np.uint8)
    frame192 = ((frame > th2) * 255).astype(np.uint8)
    # frame128=frame128.astype(np.uint8)
    
        
    
    
    # Displaying Video Feeds
    # Original:
    cv2.imshow("Input", frame)
    # Calcualed Outputs:
    cv2.imshow("frame128",frame128)
    cv2.imshow("frame64", frame64)
    cv2.imshow("frame192", frame192)
    
    
    #End Video
    key = cv2.waitKey(1)
    if key == ord('x'):
        break


# Releasing The Video Cam and Closing all Windows
cv2.destroyAllWindows()
cap.release()












