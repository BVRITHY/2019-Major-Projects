from main import app

#import necessary packages
import cv2
import numpy as np 
import os

@app.route('/frames') 
def Capture_frames(videopath,path_to_store):
    os.chdir(path_to_store)
    video_obj = cv2.VideoCapture(videopath) 
    c,s = 0,1
    wait = 0
    if video_obj.isOpened() == False:
        print("Error in opening video file")
    while s:
        s,img = video_obj.read() 
        if img is None:
            break
        print(img.shape)
        #cv2.imwrite("frame%d.png" % c, img) 
        key = cv2.waitKey(100)
        wait = wait+100
        print("length of image :",len(img))
        #rotated_image1 = img.rotate(180)
        img = cv2.resize(img, (540, 380), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
        
        '''DEPENDS ON ORIENTATION OF VIDEO SET THIS ABOVE PARAMETER 
        ------>if orientation is landscape, then dont rotate to 180 
        -------> if orientation is potrait, then rotate to 180
        '''
        
        #for potrait
        #image = cv2.rotate(img, cv2.ROTATE_180)
        
        #for landscape 
        image = img
        
        print("width height fps frame_count ",video_obj.get(3),video_obj.get(4),video_obj.get(5),video_obj.get(6))
        if wait == 2000:
            print("wait",image,c)
            filename = 'Frame_'+str(c)+'.jpg'
            cv2.imwrite(filename, image)
            c += 1
            wait = 0
        #cv2.imshow('Frame', image)
    return "Frames are extracted into folder : "+path_to_store

#fetch YOLOV3 - 320 object detection weights file by COCO Dataset 
#yolov3 configuration file consists of 80 classes, for each input it produces 255 filters

yolov3_net2 = cv2.dnn.readNet(r"C:\Users\suman\PROJECTS\major_project\SIHProject\weights\yolov3.weights",r"C:\Users\suman\PROJECTS\major_project\SIHProject\configuration_files\yolov3.cfg")
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(100, 3))

#storing two wheeler paths in a list
two_wheeler_frame_path = set()
Data_information = {}

@app.route('/detectobjects')
def object_classes():
    classes = []
    with open(r"C:\Users\suman\PROJECTS\major_project\SIHProject\coco.names",'r') as file:
        classes = file.read().splitlines() 
    classes[7] = 'auto'
    return classes    

@app.route('/detectobjects') 
def Predict_objects(imgpath,output_dirpath,file_name,Frames_Folder_path,classes) -> list:
    img = cv2.imread(imgpath)
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img,1/255,(320,320),(0,0,0),swapRB=True,crop=False)
    yolov3_net2.setInput(blob)
    output_layers_names = yolov3_net2.getUnconnectedOutLayersNames()
    layerOutputs = yolov3_net2.forward(output_layers_names)

    boxes = [] 
    confs = []
    class_ids = []
    for output in layerOutputs:
        for detect in output:
            scores = detect[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > 0.4:
                center_x = int(detect[0] * width)
                center_y = int(detect[1] * height)
                w = int(detect[2] * width)
                h = int(detect[3] * height)
                x = int(center_x - w/2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    if len(indexes)>0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            
            #if label is person or motorbike or bicycle ,then detect and extract two wheeler frames.
            if(label in ['motorbike','bicycle']):
                two_wheeler_frame_path.add(Frames_Folder_path+"/"+file_name+"\n")
                   
            confidence = str(round(confs[i],2))
            #storing each value in dictionary
            if file_name not in Data_information:
                Data_information[file_name] = [[label,x,y,w,h,confidence]]
            else:
                Data_information[file_name].append([label,x,y,w,h,confidence])
            color = colors[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y+20), font, 1, (255,255,255), 2)
    print(img.shape)
    cv2.imwrite(output_dirpath+"/"+file_name,img)
    