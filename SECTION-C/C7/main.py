print("Starting..")
from flask import Flask,render_template,request,json,jsonify,session,redirect,send_file,url_for,flash
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model

import cv2
import numpy as np
from PIL import Image
#import systemcheck

# import the necessary packages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
import cv2

IMAGE_SIZE = (224, 224, 3)
CATEGORIES = {0:'Normal',1:'mild',2:'moderate',3:'severe',4:'Proliferative Diabetic Retinopathy'}





model = load_model("diabetic_retinopathy_resnet_50v2_model.h5")

def model_warmup():
    dummy_image = []
    for i in range(224):
        dummy_image.append([[0]*3]*224)
    image = np.array(dummy_image)
    # print(image.shape)
    image = np.expand_dims(image, axis=0)
    pred = model.predict(image)
    # print(pred)



def predict_disease(imgpath):
    img = cv2.imread(imgpath)
    img = cv2.resize(img, (IMAGE_SIZE[0], IMAGE_SIZE[1]))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(img.shape)

    img_rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img_rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
    # img_rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # img_flip_ver = cv2.flip(img, 0)
    # img_flip_hor = cv2.flip(img, 1)

    images = []
    images.append(img)
    images.append(img_rotated_90)
    images.append(img_rotated_180)
    # images.append(img_rotated_270)
    # images.append(img_flip_ver)
    # images.append(img_flip_hor)

    images = np.array(images)
    images = images.astype(np.float32)
    images /= 255

    op = []
    # make predictions on the input image
    for im in images:
        image = np.array(im)
        image = np.expand_dims(image, axis=0)
        pred = model.predict(image)
        pred = pred.argmax(axis=1)[0]
        op.append(pred)
        print("Pred:", pred, CATEGORIES[pred])

    op = np.array(op)
    print("Final Output:", CATEGORIES[np.bincount(op).argmax()])
    return CATEGORIES[np.bincount(op).argmax()]


model_warmup()



app=Flask(__name__)
app.secret_key="secure"
app.config['UPLOAD_FOLDER'] = str(os.getcwd())+'/static/uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=["post","get"])
def first_page():
    if request.method=="POST":
        global image_name,image_data

        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            op = predict_disease('static/uploads/'+filename)
            # solution = SOLUTIONS[op]
            return render_template("data_page.html",
                           filename=filename, result = op)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif')
            return redirect(request.url)

    else:
        return render_template("form_page.html")


@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

app.run(debug=True, host="0.0.0.0")
