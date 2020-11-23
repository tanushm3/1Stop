from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2
# from PIL import Image as PILImage
import fretboard
import numpy as np
import pandas as pd
import math
# import cairosvg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM



cList = pd.read_excel('1Stop-master/Data/chordFingers3.xlsx', index_col=0)
# cList.head()

def makeChord(root,chordType):
    #name = Chord Root
    #name = chord type
    getter=cList.loc[(cList['CHORD_ROOT'] == root) &(cList['CLASS'] == 'OPEN') & (cList['CHORD_TYPE'] == chordType) & (cList['ADVANCED_OR_NO']=='NOT_ADVANCED')]
    getter.head()

    pos = getter.iloc[0,3].split(sep=",")
    fingers = getter.iloc[0,6].split(sep=",")

    sFingers=""
    sPos=""
    for i in pos:
        sPos+=i
    for j in fingers:
        if(j=="x"):
            j="-"
        
        sFingers+=j
    
#     print("Fingers",sFingers)
#     print("Positions",sPos)
    chord = fretboard.Chord(positions=sPos, fingers=sFingers)
    chord.save('temp.svg')
    # cairosvg.svg2png(url='temp.svg', write_to='temp.png')
    drawing = svg2rlg("temp.svg")
    # renderPDF.drawToFile(drawing, "file.pdf")
    renderPM.drawToFile(drawing, "temp.png", fmt="PNG")

    
makeChord("A#","maj")  
class CamApp(App):

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        
        #cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        frame = cv2.flip(frame, 0)
        frame = cv2.flip(frame, 1)
        
        makeChord('A#','maj')
        
        # first_image = Image.open("red_image.png")
        # second_image = Image.open("green_image.png")
        # Load two imagesd
        img1 = frame
        img2 = cv2.imread('temp.png')
        img2 = cv2.flip(img2, 0)
        # img2 = cv2.resize()
        scale_percent = 60 # percent of original size
        width = int(img2.shape[1] * scale_percent / 100)
        height = int(img2.shape[0] * scale_percent / 100)
        dim = (width, height) 
        img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
        # img2 = cv2.flip(img2, 1)
        if img2 is not None:
        
            # I want to put logo on top-left corner, So I create a ROI
            rows,cols,channels = img2.shape
            # roi = img1[0:rows, 0:cols ]
            roi = img1[img1.shape[0]-rows:img1.shape[0], 0:cols ]
            
            # Now create a mask of logo and create its inverse mask also
            img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            
            # Now black-out the area of logo in ROI
            img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
            
            # Take only region of logo from logo image.
            img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
            
            # Put logo in ROI and modify the main image
            dst = cv2.add(img1_bg,img2_fg)
            img1[img1.shape[0]-rows:img1.shape[0], 0:cols ] = dst
        # else:
            
        
        # dst = frame
        buf1 = img1
        # cv2.imshow('res',img1)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        
        # display image from the texture
        self.img1.texture = texture1


CamApp().run()
cv2.destroyAllWindows()