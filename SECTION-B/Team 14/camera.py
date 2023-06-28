import cv2
from detection import AccidentDetectionModel
import numpy as np
from pushbullet import Pushbullet
import os

API_KEY = "o.PEnMZRgFzsNP34hEbYBSGpJHekgyaH1S"
model = AccidentDetectionModel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX
file = "msg.txt"


#model = AccidentDetectionModel("model.json", 'model_weights.h5')
#font = cv2.FONT_HERSHEY_SIMPLEX

def startapplication():
    video = cv2.VideoCapture('demo2.mp4') # for camera use video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))
        with open(file, mode='r') as f:
            text = f.read()

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if (pred == "Accident"):
            prob = (round(prob[0][0] * 100, 2))
            if (prob >= 99.9):
                pb = Pushbullet(API_KEY)
                push = pb.push_note('Emergency', text)

       # pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        #if(pred == "Accident"):
         #   prob = (round(prob[0][0]*100, 2))


            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred+" "+str(prob), (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            return
        cv2.imshow('Video', frame)  


if __name__ == '__main__':
    startapplication()

