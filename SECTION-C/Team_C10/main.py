#import necessary packages
from flask import Flask,render_template,request,redirect,url_for,send_from_directory
import os
import urllib.request
from werkzeug.utils import secure_filename
from object_detection import *
from helmet_detection import *
import time
from number_plate_detection import *
from super_resolution import *
#import pytesseract

UPLOAD_FOLDER = 'static/uploads/'
videofile = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/"
Frames_Folder_path = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Frames_Folder"
Output_Folder_path = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Output_Frames"
Helmet_Folder_path = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Helmet_Folder"

slash = "/"
Total_time_taken_by_object_detection = 0 
Total_time_taken_by_Helmet_detection = 0
Total_time_taken_by_NumberPlate_detection = 0
app = Flask(__name__) 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024 



@app.route("/") 
def main():
    return render_template("upload.html")

def get_image_paths(folder_path):
    image_paths = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_paths.append(os.path.join(folder_path, filename))
    return image_paths

@app.route("/",methods=['POST']) 
def upload_video():
    file = request.files['file']
    if file.filename == "":
      print("No image is selected") 
      return redirect(request.url)
    else:
      filename = secure_filename(file.filename) 
      print("type of file -----> ",type(filename))
      print("filename : ",filename)
      global videofile
      if videofile[:4] != ".mp4":
          videofile += filename 
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print('Video successfully uploaded and displayed below')
      return render_template('upload.html', filename=filename)

@app.route('/display/<filename>')
def display_video(filename):
    print('display_video filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/frames')
def generate():  
    global videofile
    videofile = os.path.join(app.config['UPLOAD_FOLDER'], videofile)
    print("This is the video file path: ", videofile)
    status = Capture_frames(videofile, Frames_Folder_path)
    if status:
        image_filenames = os.listdir(Frames_Folder_path)
        return render_template("frames.html", image_filenames=image_filenames)
    else:
        return "Error capturing frames from the video."
   #print("this is a video file ---> ",videofile)
   #status = Capture_frames(videofile,Frames_Folder_path) 
   #print(Frames_Folder_path)
   #return render_template("frames.html",Frames_Folder_path=Frames_Folder_path)

@app.route('/detectobjects')
def detect_object():
  classes = object_classes()
  i = 0
  global Total_time_taken_by_object_detection
  for files in os.listdir(Frames_Folder_path):

    #to measure the detection time taken by the above function 
    start_time = time.time()
    Predict_objects(Frames_Folder_path+slash+files,Output_Folder_path,files,Frames_Folder_path,classes)
    end_time = time.time()
    Total_time_taken_by_object_detection += end_time-start_time
    i += 1
    print(i)
    if(i==len(os.listdir(Frames_Folder_path))):
        break;
  print("exited()") 
  image_paths = Store_paths_inside_textfile()
  print("--------------------------------------IMAGE PATHS-------------------------------")
  print(image_paths)
  print("--------------------------------------------------------------------------------")
  #return render_template('display.html',image_names=image_paths)
  # Get the image filenames from the output folder
  image_filenames = get_image_paths(Output_Folder_path)
  print(image_filenames)
  #modify the structure of image file names"
  image_filenames2 = []
  for p in image_filenames:
      image_filenames2.append(p[88:]) 
  return render_template("display.html", image_filenames=image_filenames2,message=Total_time_taken_by_object_detection)
  
  #return render_template("display.html",Output_Folder_path=Output_Folder_path,message=Total_time_taken_by_object_detection)

#@app.route('/<filename>')
#def send_image(filename):
#  print(filename,"filename is ----------------------------------------------------")
#  return send_from_directory(directory="C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/Output_Frames",filename=filename[1:])

@app.route('/detectobjects')
#store the paths in a text file
# writing to file
def Store_paths_inside_textfile():
  print("-----------------------")
  print("The Frames which contain Two wheelers are : ",two_wheeler_frame_path)
  text_filepath = "C:/Users/suman/PROJECTS/major_project/SIHProject/configuration_files/helmet_path_files"
  file1 = open(text_filepath, 'w')
  file1.writelines(two_wheeler_frame_path)
  file1.close() 
  # remove newlines  
  image_paths = []
  for f in two_wheeler_frame_path:
    image_paths.append(f[69:-1])
  return image_paths

@app.route('/helmetdetection') 
def detect_helmet():
  global Total_time_taken_by_Helmet_detection
  #open file having paths of helmet frames
  with open("C:/Users/suman/PROJECTS/major_project/SIHProject/configuration_files/helmet_path_files") as f:
      lines = [line.rstrip() for line in f]
    
  '''l[48:-4] gives name of file in path ex - o/p :  Frame_43,Frame_44,Frame_46,Frame_51,Frame_52,Frame_53,Frame_82,Frame_84,Frame_87 '''   
  for filepath in lines:
      start_time1 = time.time()
      print(filepath[84:],"it is filepath 84")
      Predict_helmets(Helmet_Folder_path,filepath,filepath[84:])
      end_time1 = time.time()
      Total_time_taken_by_Helmet_detection += end_time1-start_time1
  Store_paths_inside_textfile2()
  image_filenames = get_image_paths(Helmet_Folder_path)
  #modify the structure of image file names"
  image_filenames2 = []
  for p in image_filenames:
      image_filenames2.append(p[88:]) 
  print("------------------------>",image_filenames)
  return render_template("helmets.html", image_filenames=image_filenames2,message=Total_time_taken_by_Helmet_detection)    
  #return render_template("helmets.html",Output_Folder_path=Helmet_Folder_path,message=Total_time_taken_by_Helmet_detection)

@app.route('/helmetdetection') 
def Store_paths_inside_textfile2():
  #print the paths and store them in a text file
  print(violation_paths)
  #store the paths in a text file
  # writing to file
  text_filepath2 = "C:/Users/suman/PROJECTS/major_project/SIHProject/configuration_files/violation_path_files"
  file2 = open(text_filepath2, 'w')
  file2.writelines(violation_paths)
  file2.close()     


@app.route('/numberplate')
def detect_numberplates():
  output_dir = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Lisence_Plates_Folder"
  number_plate_detections = {}
  global Total_time_taken_by_NumberPlate_detection
  for files in os.listdir(output_dir):
      filepath = output_dir+slash+files
      try:
          start_time1 = time.time()
          left_x,top_y,width,height = Predict(output_dir,filepath,files[:3]+"-output.jpg")
          image = cv2.imread(output_dir+"/"+files[:3]+"-output.jpg")
          cropped_img = image[top_y:(top_y+height), left_x:(left_x+width)]
          cv2.imwrite(output_dir+"/"+files[:3]+"-output_plate.jpg",cropped_img)
          #extractedInfo = pytesseract.image_to_string(cropped_img)
          #print(extractedInfo)
          end_time1 = time.time()
          Total_time_taken_by_NumberPlate_detection += end_time1-start_time1
          number_plate_detections[files[:3]+"-output.jpg"] = [left_x,top_y,width,height]
      except TypeError:
          continue 
      #fetch number plate results paths 
      numberplate_image_paths = get_image_paths(output_dir) 
      numberplate_image_paths2 = []
      for p in numberplate_image_paths:
        numberplate_image_paths2.append(p[96:])  
      #print("-->number plate path : ",numberplate_image_paths2[0])
  return render_template('numberplate.html',image_filenames=numberplate_image_paths2,Output_Folder_path=output_dir,message=Total_time_taken_by_NumberPlate_detection)  

@app.route('/superresolution')
def super_resolution():
  image_paths_2 = get_image_paths("C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Lisence_Plates_Folder") 
  new_image_paths_2 = []
  for p in image_paths_2:
    print(p)
    if(p[-9::] == "plate.jpg"):
      new_image_paths_2.append(p) 
  print("the number plates are : ",new_image_paths_2)  
  for p in new_image_paths_2:  
    superresolution(p)
  modified_path = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Lisence_Plates"  
  image_filenames_path = get_image_paths(modified_path)
  #modify the structure of image file names"
  image_filenames_path2 = []
  for p in image_filenames_path:
      image_filenames_path2.append(p[89:]) 
  print("------------------------>",image_filenames_path2)
  return render_template('superresolution.html',image_filenames=image_filenames_path2)

app.static_folder = 'static'
if __name__ == "__main__":
    app.run(debug=True) 