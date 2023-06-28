print("Starting..")
from flask import Flask,render_template,request,json,jsonify,session,redirect,send_file,url_for,flash
import os
from werkzeug.utils import secure_filename


import cv2
import numpy as np
from PIL import Image
import systemcheck

# import the necessary packages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow.keras.models import load_model
import numpy as np
import cv2

IMAGE_SIZE = (224, 224, 3)

CATEGORIES = ['Corktown,_Toronto', 'Lviv', 'Catedral_San_Sebastin,_Cochabamba', 'Skopje_Fortress', 'Eiffel_Tower', 'Nieuwe_Waterweg', 'Grand_Canyon', 'Media_contributed_by_the_ETH-Bibliothek', 'Masada', 'Edinburgh_Castle', 'Hayravank_monastery', 'Genoese_fortress_(Sudak)', 'St._Lawrence,_Toronto', 'Madrid_Ro', 'Mathura_Museum', 'Haleakal_National_Park', 'Niagara_Falls', 'Salve', 'Kecharis', 'Feroz_Shah_Kotla', 'Sofiyivsky_Park', 'Peter', 'Golden_Gate_Bridge', 'Qutb_Minar_and_its_monuments,_Delhi', 'Pakistan_Monument_Islamabad', 'Museum_of_Folk_Architecture_and_Ethnography_in_Pyrohiv', 'Matka_Canyon', 'Akkerman_fortress', 'Noraduz_Cemetery', 'Khotyn_Fortress']


SOLUTIONS = {
'Corktown,_Toronto':"""Corktown is an older residential neighbourhood in downtown Toronto, Ontario, Canada. The neighbourhood is south of Shuter Street, north of the Gardiner Expressway, east of Parliament Street, and west of Don River to the east.

""", 
'Lviv':"""
Lviv is a city in western Ukraine, around 70 kilometers from the border with Poland. Traces of its Polish and Austro-Hungarian heritage are evident in its architecture, which blends Central and Eastern European styles with those of Italy and Germany. In High Castle Park, the mountaintop ruins of a 14th-century castle provide panoramic views of the city’s green-domed churches and the surrounding hills.
""", 
'Catedral_San_Sebastin,_Cochabamba':"""
The Metropolitan Cathedral of Saint Sebastian is the cathedral of the Roman Catholic Church in the Archdiocese of Cochabamba. It is located in the Plaza 14 de Septiembre in Cochabamba, Bolivia.
""", 
'Skopje_Fortress':"""
The Skopje Fortress, commonly referred to as Kale, is a historic fortress located in the old town of Skopje, the capital of North Macedonia. It is located in Centar municipality and situated on the highest point in the city overlooking the Vardar River.
""", 
'Eiffel_Tower':"""
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower. Locally nicknamed "La dame de fer", it was constructed from 1887 to 1889 as the centerpiece of the 1889 World's Fair.
""", 
'Nieuwe_Waterweg':"""
The Nieuwe Waterweg is a ship canal in the Netherlands from het Scheur west of the town of Maassluis to the North Sea at Hook of Holland: the Maasmond, where the Nieuwe Waterweg connects to the Maasgeul. It is the artificial mouth of the river Rhine. 
""", 
'Grand_Canyon':"""
Grand Canyon National Park, in Northern Arizona, encompasses 278 miles (447 km) of the Colorado River and adjacent uplands. Located on ancestral homeland of 11 Associated Tribes, Grand Canyon is one of the most spectacular examples of erosion anywhere in the world—unmatched in the incomparable vistas it offers visitors from the rim. South Rim is open. North Rim closed for winter.
""", 
'Media_contributed_by_the_ETH-Bibliothek':"""
ETH-Bibliothek's photographic and audio-visual documents are curated by the Image Archive. Its collection of more than 3 million visual sources include ETH Zurich's Portrait and View Collection, images included in various personal papers and major image collections, among them pictures by the photographic agency Comet Photo AG, aerial photographs of the Luftbild Schweiz Archive or the Swissair Photo Archive. Initiated by a partnership project with Wikimedia CH, public-domain and CC BY-SA-licensed content in the Image Archive are being uploaded to Wikimedia Commons since 2016.
""", 
'Masada':"""
Masada is an ancient fortress in southern Israel’s Judean Desert. It's on a massive plateau overlooking the Dead Sea. A cable car and a long, winding path climb up to the fortifications, built around 30 B.C. Among the ruins are King Herod's Palace, which sprawls over 3 rock terraces, and a Roman-style bathhouse with mosaic floors. The Masada Museum has archaeological exhibits and recreations of historical scenes. 
""", 
'Edinburgh_Castle':"""
Edinburgh Castle is a historic castle in Edinburgh, Scotland. It stands on Castle Rock, which has been occupied by humans since at least the Iron Age, although the nature of the early settlement is unclear.
""", 
'Hayravank_monastery':"""
Noravank is a 13th-century Armenian monastery, located 122 km from Yerevan in a narrow gorge made by the Amaghu River, near the town of Yeghegnadzor in Armenia. The gorge is known for its tall, sheer, brick-red cliffs, directly across from the monastery.
""", 
'Genoese_fortress_(Sudak)':"""
Scenic medieval fortress complex sprawling 30 hectares over a mountain overlooking the sea.
""", 
'St._Lawrence,_Toronto':"""
Set in a historic industrial section where Georgian mansions mingle with 1970s buildings, this family friendly neighbourhood attracts plenty of visitors to the more than 200 food stalls of the St. Lawrence Market. Hip crowds head to the vibrant restaurants, bars and cafes on Front Street East. The St. Lawrence Centre for the Arts and the Sony Centre for the Performing Arts offer live theatre and cultural events.
""", 
'Madrid_Ro':"""
Madrid Río is an urban park in the Spanish capital Madrid, built along an urban stretch of the Manzanares River 
""", 
'Mathura_Museum':"""
Government Museum, Mathura, commonly referred to as Mathura museum, is an archaeological museum in Mathura city of Uttar Pradesh state in India. The museum was founded by then collector of the Mathura district, Sir F. S. Growse in 1874. 
""", 
'Haleakal_National_Park':"""
Haleakalā National Park is on the Hawaiian island of Maui. It’s home to the dormant Haleakalā Volcano and endangered Hawaiian geese. The Leleiwi and Kalahaku overlooks on the steep Crater Road have views across the West Maui Mountains. Rugged trails in the Summit District pass cinder cones and lava flows. In the coastal area of Kīpahulu are the Pools of Ohe’o, freshwater pools and waterfalls set amid bamboo forest.
""", 
'Niagara_Falls':"""
The Chitrakote Falls is a natural waterfall on the Indravati River, located approximately 38 kilometres to the west of Jagdalpur, in Bastar district in the Indian state of Chhattisgarh. The height of the falls is about 29 metres
""", 
'Salve':"""

""", 
'Kecharis':"""
Kecharis Monastery (Armenian: Կեչառիսի վանքային համալիր), is a medieval Armenian monastic complex
""", 
'Feroz_Shah_Kotla':"""
The Feroz Shah Kotla or Kotla was a fortress built circa 1354 by Feroz Shah Tughlaq to house his version of Delhi city called Firozabad.
""", 
'Sofiyivsky_Park':"""
Maybe the best mall in Sofia. Lots of shops, food courts and entertainment. There is Cinema City with 4Dx. Nice gym with big swimming pool on the roof.
""", 
'Peter':"""
Saint Peter, also known as Peter the Apostle, Peter the Rock, Simon Peter, Simeon, Simon, or Cephas, was one of the Twelve Apostles of Jesus Christ and one of the first leaders of the early Christian Church. According to Christian tradition, Peter was crucified in Rome under Emperor Nero. 
""", 
'Golden_Gate_Bridge':"""
The Golden Gate Bridge is a suspension bridge spanning the Golden Gate, the one-mile-wide strait connecting San Francisco Bay and the Pacific Ocean. 
""", 
'Qutb_Minar_and_its_monuments,_Delhi':"""
The Qutb Minar, also spelled Qutub Minar and Qutab Minar, is a minaret and "victory tower" that forms part of the Qutb complex, which lies at the site of Delhi’s oldest fortified city, Lal Kot, founded by the Tomar Rajputs. It is a UNESCO World Heritage Site in the Mehrauli area of South Delhi, India.
""", 
'Pakistan_Monument_Islamabad':"""
The Pakistan Monument is a national monument and heritage museum located on the western Shakarparian Hills in Islamabad, Pakistan. The monument was constructed to symbolize the unity of the Pakistani people. It is dedicated to the people of Pakistan who sacrificed their "today" for a better "tomorrow".
""", 
'Museum_of_Folk_Architecture_and_Ethnography_in_Pyrohiv':"""
Museum of Folk Architecture and Ethnography in Pyrohiv. open-air museum in Kyiv, Ukraine. Museum of Folk Architecture and Folkways of Ukraine.
""", 
'Matka_Canyon':"""
Matka is a canyon located west of central Skopje, North Macedonia. Covering roughly 5,000 hectares, Matka is one of the most popular outdoor destinations in North Macedonia and is home to several medieval monasteries. The Matka Lake within the Matka Canyon is the oldest artificial lake in the country. 
""", 
'Akkerman_fortress':"""
Bilhorod-Dnistrovskyi fortress is a historical and architectural monument of the 13th-14th centuries. It is located in Bilhorod-Dnistrovskyi in the Odessa region of southwestern Ukraine, the historical Budjak.
""", 
'Noraduz_Cemetery':"""
Noratus cemetery, also spelled Noraduz, is a medieval cemetery with many early khachkars located in the village of Noratus, Gegharkunik Province near Gavar and Lake Sevan, 90 km north of Yerevan. The cemetery has the largest cluster of khachkars in Armenia.
""", 
'Khotyn_Fortress':"""
The Khotyn Fortress is a fortification complex located on the right bank of the Dniester River in Khotyn, Chernivtsi Oblast of western Ukraine. It is situated on a territory of the historical northern Bessarabia region which was split in 1940 between Ukraine and Moldova.
""", 

}


model = load_model("./resnet_101_v2_model.h5")

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

    img_rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img_rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
    img_rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img_flip_ver = cv2.flip(img, 0)
    img_flip_hor = cv2.flip(img, 1)

    images = []
    images.append(img)
    images.append(img_rotated_90)
    images.append(img_rotated_180)
    images.append(img_rotated_270)
    images.append(img_flip_ver)
    images.append(img_flip_hor)

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
            solution = SOLUTIONS[op]
            return render_template("data_page.html",
                           filename=filename, result = op, solution = solution.split("\n"))
        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif')
            return redirect(request.url)

    else:
        return render_template("form_page.html")


@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

app.run(debug=True, host="0.0.0.0", port=5001)

