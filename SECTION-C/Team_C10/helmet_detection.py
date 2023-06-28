#from main import app

#import necessary packages
import cv2
import numpy as np 
import os

#Weights File Generated after performing Transfer learning  
#yolov3_custom configuration file consists of 2 classes, for each input it produces 21 filters
net = cv2.dnn.readNet("C:/Users/suman/PROJECTS/major_project/SIHProject/weights/yolov3_custom_best_helmet_detection.weights", r"C:/Users/suman/PROJECTS/major_project/SIHProject/configuration_files/yolov3_custom.cfg") 
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(100, 3))

#store paths of violated frames
violation_paths = set()
#@app.route('/helmetdetection') 
def Predict_helmets(output_dirname,imgpath,filename):
    img = cv2.imread(imgpath)
    height, width, _ = img.shape
    classes = ["no Helmet","Helmet"]
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)
    if len(indexes)>0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y+20), font, 1, (255,255,255), 2)
            if(label in ["no Helmet"]):
                violation_paths.add(output_dirname+"/"+filename+"\n")
                   
    img.shape
    print("This is file name ____> ",filename[3:])
    print(" updated file name : ",output_dirname+"/"+filename[4:])
    cv2.imwrite(output_dirname+"/"+filename[4:],img) 