
import matplotlib.pyplot as plt
import glob
import SimpleITK as sitk
import numpy as np
import os
import skimage
from skimage.io import imread_collection
import numpy as np
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras import backend as keras
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.metrics import precision_score
from sklearn.metrics import jaccard_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from numpy import load
from keras import backend as K
import tensorflow as tf


## Please load the trained model for testing in line 158
## Please load the preprocessed test dataset 'data_test_final.npz' in line 165
## Please change the corresponding model while running a segnet (get_segnet) or a unet (get_unet) in line 144 



#UNET ARCHITECTURE
# Input: 48X48 size patch
# Output: 48x48 size patch


def conv2d_block(input_tensor,n_filters,kernel_size,batchnorm=True):
    # first layer
    x = Conv2D(filters=n_filters, kernel_size=(kernel_size, kernel_size), kernel_initializer="he_normal",
               padding="same")(input_tensor)
    if batchnorm:
        x = BatchNormalization()(x)
    x = Activation("sigmoid")(x)
    # second layer
    x = Conv2D(filters=n_filters, kernel_size=(kernel_size, kernel_size), kernel_initializer="he_normal",
               padding="same")(x)
    if batchnorm:
        x = BatchNormalization()(x)
    x = Activation("sigmoid")(x)
    return x


def get_unet(input_img, n_filters=16, dropout=0.5, batchnorm=True):
    # contracting path
    c1 = conv2d_block(input_img, n_filters=n_filters*1, kernel_size=3, batchnorm=batchnorm)
    p1 = MaxPooling2D((2,2)) (c1)
    p1 = Dropout(dropout*0.5)(p1)

    c2 = conv2d_block(p1, n_filters=n_filters*2, kernel_size=3, batchnorm=batchnorm)
    p2 = MaxPooling2D((2,2)) (c2)
    p2 = Dropout(dropout)(p2)

    c3 = conv2d_block(p2, n_filters=n_filters*4, kernel_size=3, batchnorm=batchnorm)
    p3 = MaxPooling2D((2, 2)) (c3)
    p3 = Dropout(dropout)(p3)

    c4 = conv2d_block(p3, n_filters=n_filters*8, kernel_size=3, batchnorm=batchnorm)
    p4 = MaxPooling2D(pool_size=(2, 2)) (c4)
    p4 = Dropout(dropout)(p4)

    c5 = conv2d_block(p4, n_filters=n_filters*16, kernel_size=3, batchnorm=batchnorm)

    # expansive path
    u6 = Conv2DTranspose(n_filters*8, (3, 3), strides=(2, 2), padding='same') (c5)
    u6 = concatenate([u6, c4])
    u6 = Dropout(dropout)(u6)
    c6 = conv2d_block(u6, n_filters=n_filters*8, kernel_size=3, batchnorm=batchnorm)

    u7 = Conv2DTranspose(n_filters*4, (3, 3), strides=(2, 2), padding='same') (c6)
    u7 = concatenate([u7, c3])
    u7 = Dropout(dropout)(u7)
    c7 = conv2d_block(u7, n_filters=n_filters*4, kernel_size=3, batchnorm=batchnorm)

    u8 = Conv2DTranspose(n_filters*2, (3, 3), strides=(2,2), padding='same') (c7)
    u8 = concatenate([u8, c2])
    u8 = Dropout(dropout)(u8)
    c8 = conv2d_block(u8, n_filters=n_filters*2, kernel_size=3, batchnorm=batchnorm)

    u9 = Conv2DTranspose(n_filters*1, (3,3), strides=(2,2), padding='same') (c8)
    u9 = concatenate([u9, c1], axis=3)
    u9 = Dropout(dropout)(u9)
    c9 = conv2d_block(u9, n_filters=n_filters*1, kernel_size=3, batchnorm=batchnorm)

    outputs = Conv2D(1, (1, 1), activation='sigmoid') (c9)
    model = Model(inputs=[input_img], outputs=[outputs])
    return model


## Seg-Net Architecture
# Input: 48X48 size patch
# Output: 48x48 size patch

def get_segnet(input_img, n_filters=16*2, dropout=0.5, batchnorm=True):
    
    # contracting path
    c1 = conv2d_block(input_img, n_filters=n_filters*1, kernel_size=3, batchnorm=batchnorm)
    p1 = MaxPooling2D((2,2)) (c1)
    p1 = Dropout(dropout*0.5)(p1)

    c2 = conv2d_block(p1, n_filters=n_filters*2, kernel_size=3, batchnorm=batchnorm)
    p2 = MaxPooling2D((2,2)) (c2)
    p2 = Dropout(dropout)(p2)


    # expansive path

    u8 = Conv2DTranspose(n_filters*2, (3, 3), strides=(2,2), padding='same') (p2)
    u8 = Dropout(dropout)(u8)
    c8 = conv2d_block(u8, n_filters=n_filters*2, kernel_size=3, batchnorm=batchnorm)

    u9 = Conv2DTranspose(n_filters*1, (3,3), strides=(2,2), padding='same') (c8)
    u9 = Dropout(dropout)(u9)
    c9 = conv2d_block(u9, n_filters=n_filters*1, kernel_size=3, batchnorm=batchnorm)

    outputs = Conv2D(1, (1, 1), activation='sigmoid') (c9)
    model = Model(inputs=[input_img], outputs=[outputs])
    return model


### Loss function
# Focal Loss function
def focal_loss(gamma=2., alpha=.25):
    def focal_loss_fixed(y_true, y_pred):
        pt_1 = tf.where(tf.equal(y_true, 1), y_pred, tf.ones_like(y_pred))
        pt_0 = tf.where(tf.equal(y_true, 0), y_pred, tf.zeros_like(y_pred))
        return -K.sum(alpha * K.pow(1. - pt_1, gamma) * K.log(pt_1))-K.sum((1-alpha) * K.pow( pt_0, gamma) * K.log(1. - pt_0)) 
    return focal_loss_fixed



# Initialising image height and width as 48, 48
im_width = 48
im_height = 48
input_img = Input((im_width, im_height,1), name='img')


model = get_segnet(input_img, n_filters=32, dropout=0.6, batchnorm=True)                         ## Incase of U-net please change the number of filters to 16. For SegNet, keep the filters as 16*2
model.compile(optimizer=Adam(),loss=[focal_loss(alpha=.5, gamma=2)], metrics=["accuracy"])
model.summary()



callbacks = [
    EarlyStopping(patience=10, verbose=1),
    ReduceLROnPlateau(factor=0.1, patience=3, min_lr=0.01, verbose=1),
    ModelCheckpoint('model-tgs-salt.h5', verbose=1, save_best_only=True, save_weights_only=True)
]


#### Loading the trained model.
#import os

#model.load_weights(os.path.abspath('seg_epoch10.h5'))

model.load_weights('C://Users//LENOVO//Documents//Harsha//14.12.22//retina-segmentation-CNN-//trained_models//seg_epoch10.h5')              ## In case of Seg-net, please load 'segnet_epoch10.h5' file. In case of U-net, please load 'unet_epoch10.h5'

#C:\Users\LENOVO\Documents\Harsha\14.12.22\retina-segmentation-CNN-\trained_models\seg_epoch10.h5

### Loading test dataset

data = load('C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/code/data_test_final.npz')                ## Pre-processed dataset obtained from preprocess.py. Please load the data file 'data_test_final.npz'
test_list=data["test_list"]
test_ground_truth_list=data["test_ground_truth_list"]
test_mask_list=data["test_mask_list"]


## Generates ordered patches

def get_test(test_img, mask_img,test_groundTruth, patch_h, patch_w):
 
    print (test_img.shape)
    test_array = construct_border(test_img,patch_h,patch_w)


    test_norm= test_array/np.max(test_array)

    mask_array = construct_border(mask_img,patch_h,patch_w)
    mask_norm= mask_array/np.max(mask_array)
    ground_array = construct_border(test_groundTruth,patch_h,patch_w)
    ground_norm= ground_array/np.max(ground_array)
    patches_imgs_test=None
    patches_masks_test=None
    patches_ground_test= None
    patches_imgs_test = ordered_patches(test_norm,patch_h,patch_w)
    patches_masks_test = ordered_patches(mask_norm,patch_h,patch_w)
    patches_ground_test = ordered_patches(ground_norm,patch_h,patch_w)
    return patches_imgs_test, patches_masks_test,patches_ground_test


def get_shape_of_image(image):
    h = image.shape[0]
    w = image.shape[1]
    return h,w

def ordered_patches(test_imgs, patch_h, patch_w):
    img_h,img_w = get_shape_of_image(test_imgs)
    N_patches_h = int(np.floor(img_h/patch_h))
    N_patches_w = int(np.floor(img_w/patch_w) )
    total_patch = N_patches_h*N_patches_w
    patches = np.empty((total_patch,patch_h,patch_w))
    
    count = 0
    for h  in range(N_patches_h):
        for w in range(N_patches_w):
            patch = test_imgs[ h*patch_h:(h*patch_h)+patch_h  , w*patch_w:(w*patch_w)+patch_w ]
            patches[count]=patch
            count = count + 1   
    return patches


def image_structuring(preds_test):
    new_image=np.reshape(preds_test,(preds_test.shape[0],preds_test.shape[3],preds_test.shape[1],preds_test.shape[2]))
    return new_image


def construct_border(data,patch_h,patch_w):

    img_h,img_w = get_shape_of_image(data) 
    new_img_h = 0
    new_img_w = 0
    
    if (img_h%patch_h)==0:
        new_img_h = img_h
    else:
        new_img_h = (int(img_h/patch_h)+1)*patch_h
    if (img_w%patch_w)==0:
        new_img_w = img_w
    else:
        new_img_w = (int(img_w/patch_w)+1)*patch_w
    new_data = np.zeros((new_img_h,new_img_w))
    new_data[0:img_h,0:img_w] = data[:,:]

    
    return new_data


def constructed(data,N_h,N_w):
    num_patchs = N_w*N_h
    total_imgs = int(data.shape[0]/num_patchs)
    patch_h = data.shape[2]
    patch_w = data.shape[3]
    full_recomp = np.empty((total_imgs,data.shape[1],N_h*patch_h,N_w*patch_w))
    tot= 0 
    small=0
   
    while (small<data.shape[0]):
        #recompone one:
        single_recon = np.empty((data.shape[1],N_h*patch_h,N_w*patch_w))
        for h in range(N_h):
            for w in range(N_w):
                single_recon[:,h*patch_h:(h*patch_h)+patch_h,w*patch_w:(w*patch_w)+patch_w]=data[small]
                small=small+1
        
        full_recomp[tot]=single_recon
        tot=tot+1
    return full_recomp


def inside_FOV_DRIVE(i, x, y, test_mask_list ):
    test_mask_list=np.reshape(test_mask_list,(test_mask_list.shape[0],1,test_mask_list.shape[1],test_mask_list.shape[2]))
    assert (len(test_mask_list.shape)==4)
    assert (test_mask_list.shape[1]==1)  
    if (x >= test_mask_list.shape[3] or y >= test_mask_list.shape[2]):
        return False

    if (test_mask_list[i,0,y,x]>0):
 
        return True
    else:
        return False

def resize(data, original_imgs_border_masks):

    height = data.shape[2]
    width = data.shape[3]
    for i in range(data.shape[0]):  
        for x in range(width):
            for y in range(height):
                if inside_FOV_DRIVE(i,x,y,original_imgs_border_masks)==False:
                    data[i,:,y,x]=0

def pred_only_FOV(data_imgs,data_masks,orig_imgs):
    height = data_imgs.shape[1]
    width = data_imgs.shape[2]
    new_pred_imgs = []
    new_pred_masks = []
    for i in range(data_imgs.shape[0]):
        for x in range(width):
            for y in range(height):
                if inside_FOV_DRIVE(i,x,y,orig_imgs)==True:
                    new_pred_imgs.append(data_imgs[i,y,x])
                    new_pred_masks.append(data_masks[i,y,x])
    new_pred_imgs = np.asarray(new_pred_imgs)
    new_pred_masks = np.asarray(new_pred_masks)
    return new_pred_imgs, new_pred_masks

def is_patch_valid(x,y,img_w,img_h,patch_h):
    
    x_modified = x - int(img_w/2)
    y_modified = y - int(img_h/2)
    R_inside = 270 - int(patch_h * np.sqrt(2.0) / 2.0)
    
    radius = np.sqrt( np.power(x_modified,2) + np.power(y_modified,2) )
    is_inside = True
    
    if radius > R_inside:
        is_inside = False
    
    return is_inside


final_pred_list=[]
for var in range(20):
    patches_imgs_test, patches_masks_test,patches_ground_test = get_test(test_list[var],test_mask_list[var],test_ground_truth_list[var],48,48)
    patches_imgs_test=np.asarray(patches_imgs_test)
    patches_masks_test=np.asarray(patches_masks_test)
    patches_ground_test=np.asarray(patches_ground_test)
    patches_imgs_test=patches_imgs_test.reshape((patches_imgs_test.shape[0],patches_imgs_test.shape[1],patches_imgs_test.shape[2],1))
    patches_ground_test=patches_ground_test.reshape((patches_ground_test.shape[0],patches_ground_test.shape[1],patches_ground_test.shape[2],1))
    patches_masks_test= patches_masks_test.reshape((patches_masks_test.shape[0],patches_masks_test.shape[1],patches_masks_test.shape[2],1))
    preds_test = model.predict(patches_imgs_test, verbose=1)
    predict_reshaped=image_structuring(preds_test)
    pred_imgs = constructed(predict_reshaped,13,12)
    resize(pred_imgs,test_mask_list)
    pred_imgs = pred_imgs[:,:,0:584,0:565]
    pred_imgs=np.reshape(pred_imgs,(pred_imgs.shape[0],pred_imgs.shape[2],pred_imgs.shape[3]))
    pred_imgs=np.squeeze(pred_imgs)
    final_pred_list.append(pred_imgs)

for i in range(len(final_pred_list)):
    plt.imshow(final_pred_list[i],cmap='gray') 
    s = "results_segnet/" + str(i)
    plt.savefig(s)
    plt.show()

grnd_set=test_ground_truth_list

## Evaluation of Metrics

IOU_list=[]
precision_list=[]
for m in range(20):
    grnd_img= np.asarray(grnd_set[m])
    grnd_img=grnd_img/255
    grnd_img[grnd_img>0.3]=1
    pred_img= np.squeeze(final_pred_list[m])
    IOU_score= jaccard_score(np.round(grnd_img),np.round(pred_img),average='weighted')
    #print("After IOC - -------------------------------------")
    precision=precision_score(np.round(grnd_img),np.round(pred_img), average='weighted')
    IOU_list.append(IOU_score)
    precision_list.append(precision)
print (IOU_list)                                                        ## I have included the image wise IOU and Precision score for both the nets in Report. Please check the report for details
print (precision_list)



final_pred_list=np.asarray(final_pred_list)


### Plotting ROC Curve.                                                                         ## I have included the results in my report for visualisation.
y_scores, y_true = pred_only_FOV(final_pred_list,test_ground_truth_list,test_mask_list)
y_true=y_true/255

fpr, tpr, thresholds = roc_curve((y_true), y_scores)


AUC_ROC = roc_auc_score(y_true, y_scores)
print ("\nArea under the ROC curve: " +str(AUC_ROC))
plt.plot(fpr,tpr,'-',label='Area Under the Curve (AUC = %0.4f)' % AUC_ROC)
plt.title('ROC curve')
plt.xlabel("FPR (False Positive Rate)")
plt.ylabel("TPR (True Positive Rate)")
plt.legend(loc="lower right")
plt.savefig("results_segnet/ROC_unet.png")       ## While running U-Net, please save it as ROC_unet.png for visualisation



#References:

#[1] Ronneberger, O., Fischer, P. and Brox, T., 2015, October. U-net: Convolutional networks for biomedical image segmentation. In ​International Conference on Medical image computing and computer-assisted intervention​ (pp. 234-241). Springer, Cham
#[2] Badrinarayanan, Vijay, Alex Kendall, and Roberto Cipolla. "Segnet: A deep convolutional encoder-decoder architecture for image segmentation." ​IEEE transactions on pattern analysis and machine intelligence 39, no. 12 (2017): 2481-2495
#[3] github.com/orobix/retina-unet
#[4] towardsdatascience.com/understanding-semantic-segmentation-with-unet-6be4f42d4b47
#[5] Lin, T.Y., Goyal, P., Girshick, R., He, K. and Dollár, P., 2017. Focal loss for dense object detection. In Proceedings of the IEEE international conference on computer vision​ (pp. 2980-2988)
#[6] www.isi.uu.nl/Research/Databases/DRIVE/

