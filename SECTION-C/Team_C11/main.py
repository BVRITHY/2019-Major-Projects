from tkinter import *
import tkinter
from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np
import imutils

import cv2
#Importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import glob
from moviepy.editor import VideoFileClip
from tkinter.filedialog import askopenfilename
import laneDetection as ld
from PIL import Image, ImageTk


main = tkinter.Tk()
main.title(" Lane Detection")
main.geometry("500x400")

global video_file,output

def uploadVideo():
    global video_file
    video_file = askopenfilename(initialdir = "test_videos")
    pathlabel.config(text=video_file+' loaded')

def detection():
    global video_file
    global output
    #print("vsdbvsdv")
    path = os.path.dirname(os.path.abspath(video_file))
    test = os.path.basename(video_file)
    output = output = os.path.splitext(test)[0]+"_output1"+os.path.splitext(test)[1]
    ld.process_video(test,output)
    show_frame()  #Display

def show_frame():
       global output
       print(output)
       # Create a VideoCapture object and read from input file 
       cap = cv2.VideoCapture(os.path.join('output_videos', output)) 
   
       # Check if camera opened successfully 
       if (cap.isOpened()== False):  
           print("Error opening video  file") 
   
       # Read until video is completed 
       while(cap.isOpened()): 
      
            # Capture frame-by-frame 
            ret, frame = cap.read() 
            if ret == True: 
   
               # Display the resulting frame 
               cv2.imshow('Frame', frame) 
   
               # Press Q on keyboard to  exit 
               if cv2.waitKey(25) & 0xFF == ord('q'): 
                   break
   
            # Break the loop 
            else:  
                break
   
       # When everything done, release  
       # the video capture object 
       cap.release() 
   
       # Closes all the frames 
       cv2.destroyAllWindows() 

font = ('times', 16, 'bold')
title = Label(main, text='Lane Detection Using OpenCV',anchor=W, justify=LEFT)
title.config(bg='black', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)


font1 = ('times', 14, 'bold')
#upload = Button(main, text="Start Behaviour Monitoring Using Webcam", command=startMonitoring)
#upload.place(x=50,y=200)
#upload.config(font=font1)

videoButton = Button(main, text="Upload Test Video", command=uploadVideo)
videoButton.place(x=50,y=250)
videoButton.config(font=font1)

laneButton = Button(main, text="Start Lane Detection", command=detection)
laneButton.place(x=50,y=350)
laneButton.config(font=font1)

pathlabel = Label(main)
pathlabel.config(bg='DarkOrange1', fg='white')  
pathlabel.config(font=font1)           
pathlabel.place(x=50,y=300)


main.config(bg='chocolate1')
main.mainloop()
