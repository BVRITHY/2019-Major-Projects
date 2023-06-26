# Import the necessary packages 
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from EAR_calculator import *
from imutils import face_utils 
from imutils.video import VideoStream
import matplotlib.pyplot as plt
import matplotlib.animation as animate
from matplotlib import style 
import imutils 
import dlib
import time 
import argparse 
import cv2 
from playsound import playsound
from scipy.spatial import distance as dist
import os 
import csv
import numpy as np
import pandas as pd
from datetime import datetime

style.use('fivethirtyeight')
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
ear_list=[]
total_ear=[]
mar_list=[]
total_mar=[]
ts=[]
total_ts=[]
ap = argparse.ArgumentParser() 
ap.add_argument("-p", "--shape_predictor", required = True, help = "path to dlib's facial landmark predictor")
ap.add_argument("-r", "--picamera", type = int, default = -1, help = "whether raspberry pi camera shall be used or not")
args = vars(ap.parse_args())

EAR_THRESHOLD = 0.25
CONSECUTIVE_FRAMES = 3 
MAR_THRESHOLD = 13
BLINK_COUNT = 0 
FRAME_COUNT = 0 

print("[INFO]Loading the predictor.....")
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor(args["shape_predictor"])

(lstart, lend) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rstart, rend) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mstart, mend) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

print("[INFO]Loading Camera.....")
vs = VideoStream(usePiCamera = args["picamera"] > 0).start()
time.sleep(2) 

assure_path_exists("dataset/")
count_sleep = 0
count_yawn = 0 

while True: 
    frame = vs.read()
    cv2.putText(frame, "PRESS 'q' TO EXIT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3) 
    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(frame, 1)
    for (i, rect) in enumerate(rects): 
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (x, y, w, h) = face_utils.rect_to_bb(rect) 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Driver", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        leftEye = shape[lstart:lend]
        rightEye = shape[rstart:rend] 
        mouth = shape[mstart:mend]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        EAR = (leftEAR + rightEAR) / 2.0
        ear_list.append(EAR)

        ts.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        if EAR < EAR_THRESHOLD: 
            FRAME_COUNT += 1

            cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)

            if FRAME_COUNT >= CONSECUTIVE_FRAMES: 
                count_sleep += 1
                cv2.imwrite("dataset/frame_sleep%d.jpg" % count_sleep, frame)
                playsound('sound files/warning.mp3')
                cv2.putText(frame, "DROWSINESS ALERT!", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             else: 
#                 if FRAME_COUNT >= CONSECUTIVE_FRAMES: 
#                     playsound('sound files/warning.mp3')
#             FRAME_COUNT = 0
        else:
#                 if FRAME_COUNT >= CONSECUTIVE_FRAMES: 
#                     playsound('sound files/warning.mp3')
            FRAME_COUNT=0
        cv2.putText(frame, "EAR: {:.2f}".format(EAR), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.drawContours(frame, [mouth], -1, (0, 255, 0), 1)

        MAR = mouth_aspect_ratio(mouth)
        mar_list.append(MAR/10)
        
        print(MAR)
        cv2.putText(frame, "MAR: {:.2f}".format(MAR), (650, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        
        
        if MAR > MAR_THRESHOLD:
            count_yawn += 1
            print("count_yawn"+str(count_yawn))
            cv2.drawContours(frame, [mouth], -1, (0, 0, 255), 1) 
            cv2.putText(frame, "DROWSINESS ALERT!", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.imwrite("dataset/frame_yawn%d.jpg" % count_yawn, frame)
# #             playsound('sound files/alarm.mp3')
#                 playsound('sound files/warning_yawn.mp3')
                




    for i in ear_list:
        total_ear.append(i)
    for i in mar_list:
        total_mar.append(i)
    for i in ts:
        total_ts.append(i)
    cv2.imshow("Output", frame)
    key = cv2.waitKey(1) & 0xFF 



    if key == ord('q'):
        break

a = total_ear
b=total_mar
c = total_ts

df = pd.DataFrame({"EAR" : a, "MAR":b,"TIME" : c})
df.to_csv("op_webcam.csv", index=False)
df=pd.read_csv("op_webcam.csv")

df.plot(x='TIME',y=['EAR','MAR'])

plt.subplots_adjust(bottom=0.30)
plt.title('EAR & MAR calculation over time of webcam')
plt.ylabel('EAR & MAR')
plt.gca().axes.get_xaxis().set_visible(False)
plt.show()
cv2.destroyAllWindows()
vs.stop()
