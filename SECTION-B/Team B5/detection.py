import base64
import tensorflow as tf
import cv2
import time
import label_map_util 
import visualization_utils as viz_utils
import numpy as np
import pybase64


PATH_TO_LABELS = 'label_map.pbtxt'
MIN_CONF_THRESH = float(0.20)
PATH_TO_SAVED_MODEL = "saved_model"
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                        use_display_name=True)

def mobilenet(image):
    image_expanded = np.expand_dims(image, axis=0)

    
    input_tensor = tf.convert_to_tensor(image)
    
    input_tensor = input_tensor[tf.newaxis, ...]

    
    detections = detect_fn(input_tensor)

    
    num_detections = int(detections.pop('num_detections'))
    

    detections = {key: value[0, :num_detections].numpy()
                   for key, value in detections.items()}
    detections['num_detections'] = num_detections

    
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    image_with_detections = image.copy()

    
    x=viz_utils.visualize_boxes_and_labels_on_image_array(image_with_detections,
                                                        detections['detection_boxes'],
                                                        detections['detection_classes'],
                                                        detections['detection_scores'],
                                                        category_index,
                                                        use_normalized_coordinates=True,
                                                        max_boxes_to_draw=200,
                                                        min_score_thresh=0.6,
                                                        agnostic_mode=False)
    
    
    cv2.imwrite('static/output.jpg', image_with_detections)
    
    with open("static/output.jpg", "rb") as img_file:
        my_string = base64.b64encode(img_file.read()).decode("utf-8")
        
    
    return my_string, x


def Decode(image):
    imgdata = pybase64.b64decode(image)
    image1 = np.asarray(bytearray(imgdata), dtype="uint8")
    image1 = cv2.imdecode(image1, cv2.IMREAD_COLOR)
    return image1

