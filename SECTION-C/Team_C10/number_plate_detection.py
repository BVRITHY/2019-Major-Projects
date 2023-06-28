#from main import app

#import necessary packages
import cv2
import numpy as np


#Weights File Generated after performing Transfer learning  
#yolov3_custom2 configuration file consists of 1 class, for each input it produces 18 filters 
yolov3_net = cv2.dnn.readNet(r"C:\Users\suman\PROJECTS\major_project\SIHProject\weights\yolov3_custom2_best.weights",r"C:\Users\suman\PROJECTS\major_project\SIHProject\yolov3_custom2.cfg")
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(100, 3))

#@app.route('/numberplate')
def Predict(output_dirname,imgpath,filename):
    try:
      img = cv2.imread(imgpath)
      height, width, _ = img.shape
      classes = ["Lisence Plate"]
      blob = cv2.dnn.blobFromImage(img, 1/255, (608, 608), (0,0,0), swapRB=True, crop=False)
      yolov3_net.setInput(blob)
      output_layers_names = yolov3_net.getUnconnectedOutLayersNames()
      layerOutputs = yolov3_net.forward(output_layers_names)

      boxes = []
      confidences = []
      class_ids = []
      for output in layerOutputs:
          for detection in output:
              scores = detection[5:]
              class_id = np.argmax(scores)
              confidence = scores[class_id]
              if confidence > 0.1:
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
              cv2.putText(img, label + " " + confidence, (x+20, y+60), font, 1, (255,255,255), 2)    
      img.shape 
      cv2.imwrite(output_dirname+"/"+filename,img)   
      return x,y,w,h  
    except UnboundLocalError:
         pass



# #from main import app

# #import necessary packages
# import cv2
# import numpy as np


# #Weights File Generated after performing Transfer learning  
# #yolov3_custom2 configuration file consists of 1 class, for each input it produces 18 filters 
# yolov3_net = cv2.dnn.readNet(r"C:\Users\SRINIVAS\Desktop\PROJECTS\major_project\SIHProject\weights\yolov3_custom2_best.weights",r"C:\Users\SRINIVAS\Desktop\PROJECTS\major_project\SIHProject\yolov3_custom2.cfg")
# font = cv2.FONT_HERSHEY_PLAIN
# colors = np.random.uniform(0, 255, size=(100, 3))

# #@app.route('/numberplate')
# def Predict(output_dirname,imgpath,filename):

#     img = cv2.imread(imgpath)
#     height, width, _ = img.shape
#     classes = ["Lisence Plate"]
#     blob = cv2.dnn.blobFromImage(img, 1/255, (608, 608), (0,0,0), swapRB=True, crop=False)
#     yolov3_net.setInput(blob)
#     output_layers_names = yolov3_net.getUnconnectedOutLayersNames()
#     layerOutputs = yolov3_net.forward(output_layers_names)

#     boxes = []
#     confidences = []
#     class_ids = []
#     for output in layerOutputs:
#         for detection in output:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.1:
#                 center_x = int(detection[0]*width)
#                 center_y = int(detection[1]*height)
#                 w = int(detection[2]*width)
#                 h = int(detection[3]*height)

#                 x = int(center_x - w/2)
#                 y = int(center_y - h/2)

#                 boxes.append([x, y, w, h])
#                 confidences.append((float(confidence)))
#                 class_ids.append(class_id)

#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)
#     if len(indexes)>0:
#         for i in indexes.flatten():
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             confidence = str(round(confidences[i],2))
#             color = colors[i]
#             cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
#             cv2.putText(img, label + " " + confidence, (x+20, y+60), font, 1, (255,255,255), 2)    
#     img.shape 
#     cv2.imwrite(output_dirname+"/"+filename,img)   
#     return x,y,w,h  
