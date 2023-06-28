from flask import Flask,render_template,request,jsonify
from flask_cors import cross_origin
from detection import mobilenet, Decode
import cv2
from PIL import Image
import paddleocr 
import base64
import numpy as np
from io import BytesIO
from paddleocr import PaddleOCR, draw_ocr
import re 
from flask import Flask, request, jsonify
ocr = PaddleOCR()
app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
@cross_origin()
def result():
    if request.method == 'POST':
        image_data = request.json['image']
        
        decoded_data = base64.b64decode(image_data)
        img_file = open('./num_image.jpeg', 'wb')
        img_file.write(decoded_data)
        img_file.close()
        result = ocr.ocr("./num_image.jpeg")
        for idx in range(len(result)):
            res = result[idx]
            
            
            data = []
            for line in res:
                
                x = " ".join(re.split(r'[A-Z]{2}[0-9]{2}|[A-Z]{2}[0-9]{2}',(line[1][0]).strip()))
                y = " ".join(re.split(r'([A-Z]{2} [0-9]{4}|[0-9]{4})',(line[1][0]).strip()))
                if x!=None or y!=None:
                    data.append(x)
                    data.append(y)
                
       
        img = Decode(image_data).copy()
        img = cv2.resize(img, (480, 320),interpolation=cv2.INTER_NEAREST)
        
       
       
        print("result numberplate :",data)
        new_data=[]
        for string in data:
            new_string= string.replace(" ","")
            new_data.append(new_string)
        print ("new_string=====>",new_string)
                                                                                                       
        pattern1 = r'[A-Z]{2}[0-9]{2}[-][A-Z]{1,2}[0-9]{3,4}|[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{3,4}|[A-Z]{2}[0-9]{2}[A-Z]{1,2}|[AP]{2}[0-9]{2}|[TS]{2}[0-9]{2}|[A-Z]{2}[0-9]{2}[A-Z]{2} [0-9]{4}|[A-Z]{2}[0-9]{2}[A-Z]{1,2}'#AP09CP 4854#|[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}
        pattern2 =r'[0-9]{4}|[A-Z]{1,2}[0-9]{4}|[A-Z]{1,2}[0-9]{4}'
        aaa=[]
        aa=""
        bb=""
        for item in new_data:
            match = re.search(pattern1, item)
            matchx = re.search(pattern2, item)
            if match:
                aa=match.group(0)
                aa=aa.replace("-"," ").replace("CP4854","")
                print("AAA",aa)

            if matchx:
                bb=matchx.group(0)
                print("BB", bb)
            aaa=[aa + bb]


        
        imgdata=mobilenet(img)
        datax = str(imgdata[1])
        
        return jsonify({"image":str(imgdata[0]),"Number":aaa,"datax":str(imgdata[1][1])})
        
    
    return render_template('index.html')



if __name__=="__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)


