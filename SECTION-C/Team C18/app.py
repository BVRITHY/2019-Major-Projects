from __future__ import division, print_function
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from flask import make_response
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import cv2
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import sqlite3



app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads/'

static_path = 'static'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


model_path2 = keras.models.load_model('resnet50.h5')


CTS = model_path2
    
@app.route("/")
#@cache.cached(timeout=50)
def home():
    return render_template("home.html")

@app.route('/logon')
#@cache.cached(timeout=50)
def logon():
    return render_template('signup.html')

@app.route('/login')
#@cache.cached(timeout=50)
def login():
    return render_template('signin.html')

@app.route("/signup")
##@cache.cached(timeout=50)
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
#@cache.cached(timeout=50)
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("index.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/index')
#@cache.cached(timeout=50)
def index():
    return render_template('index.html')

@app.route('/predict2',methods=['GET','POST'])
def predict2():
    #pred = []
    print("Entered")
    
    print("Entered here")
    file = request.files['files'] # fet input
    filename = file.filename        
    print("@@ Input posted = ", filename)
        
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)


 

    class_labels = ['No Brain tumor', 'Brain Tumor']

    
    img = cv2.imread(file_path)
    img = cv2.resize(img, (224, 224))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)

    # Get model prediction
    prediction = CTS.predict(img)

    print(prediction)

    # Get class label with highest probability
    label = class_labels[np.argmax(prediction)]

# Print prediction result
    print('Prediction: {} ({:.2f}%)'.format(label, prediction.max()*100))



    
    
    return render_template('result.html', pred_output = label, img_src=UPLOAD_FOLDER + file.filename)

@app.route('/notebook')
#@cache.cached(timeout=50)
def notebook():
    return render_template('Notebook.html')

@app.route('/graph')
#@cache.cached(timeout=50)
def about():
    return render_template('graph.html')
   
if __name__ == '__main__':
    app.run(debug=False)