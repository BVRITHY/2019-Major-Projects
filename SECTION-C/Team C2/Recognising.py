#Importing Required Libraries
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from datetime import date
import pandas as pd

# Initialising variables for list of images, list of names, path of images
# path = 'Images_Attendance'
path = 'Dataset'
images = []
classNames = []
myList = os.listdir(path)
# print(myList)

#Appending images and names to the list
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# print(classNames)

datetoday = date.today().strftime("%d_%m_%y")
subname = input('Enter the Subject : ')
def totalreg():
    return len(os.listdir('Dataset'))

#Creating Attendance folder
if not os.path.isdir('Attendance_Data'):
    os.makedirs('Attendance_Data')

#Creating Day-wise Attendance .csv file in Attendance Folder
if f'Attendance_Data-{datetoday}-{subname}.csv' not in os.listdir('Attendance_Data'):
    with open(f'Attendance_Data/Attendance_Data-{datetoday}-{subname}.csv','w') as f:
        f.write('Name, Roll, Time, Subject')

#Finding Encodings of registered images
def findEncodings(images):
    encodeList =[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


    
#Function to Mark Attendance for recognised faces
def markAttendance(name,subname):
    username = name.split('-')[0]
    userid = name.split('-')[1]
    # sname = subname
    current_time = datetime.now().strftime("%H:%M:%S")
    df = pd.read_csv(f'Attendance_Data/Attendance_Data-{datetoday}-{subname}.csv')
    if username not in list(df['Name']):
        with open(f'Attendance_Data/Attendance_Data-{datetoday}-{subname}.csv','a') as f:
            f.write(f'\n{username},{userid},{current_time},{subname}')

#Creating list of Encodings of known faces
encodeListKnown = findEncodings(images)
# print('Encoding Complete')
print('Recording Attendance')

#Starting Camera
cap = cv2.VideoCapture(0)

while True:
    #Taking Frame
    success, img = cap.read()
    #Resizing Image
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    #Converting image from BGR TO RGB
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    #Detecting or Locating Faces in the image
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    #Taking the encodings and location of each face detected and compare with encodings of known faces
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)
        #Finding closest match
        if faceDis[matchIndex] < 0.4:
            name = classNames[matchIndex].upper()
            # print(name)
            #Once a match is found a rectangle is drawn around the face and name is added at the bottom
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, name.split('-')[0], (x1, y2-180), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, 'ID : ' + name.split('-')[1], (x1-6, y2+30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name,subname)
        #If no nearest match is found, naming the face as unkown
        else:
            # print("Unknown")
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, "Unknown", (x1, y2-180), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('webcam', img)
    #If we press Esc camera stops
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()