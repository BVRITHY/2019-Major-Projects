import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import cv2
os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

# Declaring Constants
IMAGE_PATH = ""
SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"

def preprocess_image(image_path):
  """ Loads image from path and preprocesses to make it model ready
      Args:
        image_path: Path to the image file
  """
  hr_image = tf.image.decode_image(tf.io.read_file(image_path))
  # If PNG, remove the alpha channel. The model only supports
  # images with 3 color channels.
  if hr_image.shape[-1] == 4:
    hr_image = hr_image[...,:-1]
  hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
  hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
  hr_image = tf.cast(hr_image, tf.float32)
  return tf.expand_dims(hr_image, 0)

def save_image(image, filename):
  """
    Saves unscaled Tensor Images.
    Args:
      image: 3D image tensor. [height, width, channels]
      filename: Name of the file to save.
  """
  if not isinstance(image, Image.Image):
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
  image.save("%s.jpg" % filename)
  print("Saved as %s.jpg" % filename)

    
def plot_image(image, title=""):
  """
    Plots images from image tensors.
    Args:
      image: 3D image tensor. [height, width, channels].
      title: Title to display in the plot.
  """
  image = np.asarray(image)
  image = tf.clip_by_value(image, 0, 255)
  image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
  plt.imshow(image)
  plt.axis("off")
  plt.title(title)

def superresolution(imgpath):
    global IMAGE_PATH 
    IMAGE_PATH = imgpath
    hr_image = preprocess_image(IMAGE_PATH)
    # Plotting Original Resolution image
    plot_image(tf.squeeze(hr_image), title="Original Image")
    save_image(tf.squeeze(hr_image), filename="Original Image")
    model = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")

    start = time.time()
    fake_image = model(hr_image)
    fake_image = tf.squeeze(fake_image)
    print("Time Taken: %f" % (time.time() - start))

    # Plotting Super Resolution Image
    plot_image(tf.squeeze(fake_image), title="Super Resolution")
    save_image(tf.squeeze(fake_image), filename="Super Resolution")
    dddd = "C:/Users/suman/PROJECTS/major_project/SIHProject/Flask_API/static/uploads/Lisence_Plates"
    img_orig = cv2.imread(imgpath) 
    cv2.imwrite(dddd+"/"+imgpath[96:],img_orig)    
    cv2.imwrite(dddd+"/"+imgpath[96:]+"-Super_Resolution.jpg",tf.squeeze(fake_image).numpy())  
    print("super resolution :", imgpath,dddd) 
