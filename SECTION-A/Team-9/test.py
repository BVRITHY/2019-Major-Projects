import numpy as np
import dlib
import cv2
from keras.models import load_model
from tensorflow.keras.utils import img_to_array
from scipy.spatial import distance as dist
import imutils
import matplotlib.pyplot as plt
from imutils import face_utils

global points, points_lip, emotion_classifier, detector, predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/arady/aradya/Stress-Detector/shape_predictor_68_face_landmarks.dat")
emotion_classifier = load_model("C:/Users/arady/aradya/emotion_detection_model1.h5")
    
points=[]; points_lip=[]

def ebdist(leye,reye):
    eyedist = dist.euclidean(leye,reye)
    points.append(int(eyedist))
    return eyedist

def lpdist(l_lower,l_upper):
    lipdist = dist.euclidean(l_lower, l_upper)
    points_lip.append(int(lipdist))
    return lipdist


def emotion_finder(faces,frame):
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised","neutral"]
    x,y,w,h = face_utils.rect_to_bb(faces)
    frame = frame[y:y+h,x:x+w]
    roi = cv2.resize(frame,(48,48))
    roi = roi.astype("float") / 255.0
    roi = img_to_array(roi)
    roi = np.expand_dims(roi,axis=0)
    preds = emotion_classifier.predict(roi)[0]
    emotion_probability = np.max(preds)
    label = EMOTIONS[preds.argmax()]
    emtn = label
    if label in ['scared','sad','angry','disgust']:
        label = 'Stressed'
    else:
        label = 'Not Stressed'
    return label,emtn


def normalize_values(points,disp,points_lip,dis_lip):
    normalize_value_lip = abs(dis_lip - np.min(points_lip))/abs(np.max(points_lip) - np.min(points_lip))
    normalized_value_eye =abs(disp - np.min(points))/abs(np.max(points) - np.min(points))
    normalized_value =( normalized_value_eye + normalize_value_lip)/2
    stress_value = (np.exp(-(normalized_value)))
    if stress_value>=0.75:
        stress_label="High Stress"
    else:
        stress_label="Low Stress"
    return stress_value,stress_label
  

class VideoCamera(object):
    def _init_(cap):
        cap.video = cv2.VideoCapture(0)
    def _del_(cap):
        cv2.VideoCapture.release()
        
    def get_frame(cap):
        ret,frame = cv2.VideoCapture(0).read()
        frame = cv2.flip(frame,1)
        frame = imutils.resize(frame, width=500,height=500)
        (lBegin, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eyebrow"]
        (rBegin, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eyebrow"]
        (l_lower, l_upper) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        detections = detector(gray,0)
        for detection in detections:
            emotion,emtn= emotion_finder(detection,gray)
            shape = predictor(frame,detection)
            shape = face_utils.shape_to_np(shape)
               
            leyebrow = shape[lBegin:lEnd]
            reyebrow = shape[rBegin:rEnd]
            openmouth = shape[l_lower:l_upper]
            
            reyebrowhull = cv2.convexHull(reyebrow)
            leyebrowhull = cv2.convexHull(leyebrow)
            openmouthhull = cv2.convexHull(openmouth) 
    
            cv2.drawContours(frame, [reyebrowhull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [leyebrowhull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [openmouthhull], -1, (0, 255, 0), 1)
            
            lipdist = lpdist(openmouthhull[-1][0],openmouthhull[0][0])
            eyedist = ebdist(leyebrow[-1],reyebrow[0])
            
            stress_value,stress_label = normalize_values(points,eyedist, points_lip, lipdist)
           
            cv2.putText(frame, emotion, (10,10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (235, 52, 52), 2)
            cv2.putText(frame,emtn,(10,25),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,255),2)
            cv2.putText(frame,"stress value:{}".format(str(int(stress_value*100))),(10,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (51, 66, 232), 2)
            cv2.putText(frame,"Stress level:{}".format((stress_label)),(10,60),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (35, 189, 25), 2)
            if(emotion == "Stressed"):
                if(emtn == "sad"):
                    cv2.putText(frame,"Medidate for a while",(10,80),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,53), 1)
                elif(emtn=="scared"):
                    cv2.putText(frame,"Relax",(10,80),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,53), 1)
                else:
                    cv2.putText(frame,"Calm down",(10,80),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,53), 1)
            else:
                cv2.putText(frame,"Doing Great",(10,80),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,53), 1)
        frame = cv2.resize(frame,(600,500))
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
