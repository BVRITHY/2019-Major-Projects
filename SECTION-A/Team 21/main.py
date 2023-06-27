import streamlit as st
import streamlit.components.v1 as components
import playsound as ps
import os
from werkzeug.utils import secure_filename
from keras.models import load_model
import numpy as np
from PIL import Image
from gtts import gTTS


components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        .jumbotron{
            background: lightcoral;
        }
        .display-4{
            display: flex;
            justify-content: center;
            color: black;
            font-weight: bold;
        }
        p{
            display: flex;
            justify-content: center;
        }
    </style>
    <div class="jumbotron">
        <h2 class="display-4">Traffic Sign Board Recognition</h2>
        <p class="lead">Upload The Image</p>
        <hr class="my-4">
        <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
        <p class="lead">
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
        </p>
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """,
    height=200,
)

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Vehicle > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing vehicle > 3.5 tons' }

def image_processing(img):
    model = load_model('model.h5')
    data=[]
    image = Image.open(img)
    image = image.resize((60, 60))
    data.append(np.array(image))
    X_test = np.array(data)
    Y_pred = model.predict(X_test)
    classes = np.argmax(Y_pred, axis=1)
    return classes

def upload():
        st.subheader("Image")

        image_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
        print("IMAGE ", image_file)
        if image_file is not None:
            # To See details
            file_details = {"filename": image_file.name, "filetype": image_file.type,
                            "filesize": image_file.size}
            st.write(file_details)
            print(file_details)
            image = Image.open(image_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
        return image_file

def recognize(image_file):
        prediction = image_processing(image_file)

        s = [str(i) for i in prediction]
        a = int("".join(s))
        result = "Predicted Traffic Sign is: " + classes[a]
        st.write(result)

        output = gTTS(text=result, lang='en', slow=False)
        output.save("voice_alert.mp3")
        # os.system("start voice_alert.mp3")
        ps.playsound('voice_alert.mp3')
        # os.remove('voice_alert.mp3')

st.subheader("Upload an image")
image_file = st.file_uploader("", type=['jpg', 'jpeg', 'png'])
if image_file is not None:
    image = Image.open(image_file)
    st.image(image, use_column_width=True)

    if st.button("PREDICT"):
        recognize(image_file)
