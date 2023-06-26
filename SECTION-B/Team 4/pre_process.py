
import matplotlib.pyplot as plt
import glob
import SimpleITK as sitk
import numpy as np
import os
import skimage
from skimage.io import imread_collection
import numpy as np


## For Training:
## Please download the images from DRIVE dataset link which I have given as a firsrt reference in this code
## Please change the ground reference, mask and actual image directory to the corresponding location

ground_dir= "C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/training/1st_manual/*.gif"
img_dir="C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/training/images/*.tif"
mask_dir= "C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/training/mask/*.gif"

train_image_set= imread_collection(img_dir)
#print("-------------------------------", train_image_set)

ground_truth_set= imread_collection(ground_dir)
mask_set=imread_collection(mask_dir)

train_image_list=list(train_image_set)
ground_truth_list=list(ground_truth_set)
mask_list= list(mask_set)


## Preprocessing steps- normalising and taking only the green channel
train_list=[]
for i in range(len(train_image_set)):
    image= sitk.GetImageFromArray(train_image_list[i])
    normalised_image= sitk.NormalizeImageFilter()
    normalised_image=normalised_image.Execute(image)
    normalised_image=sitk.GetArrayFromImage(normalised_image)
    green_image= normalised_image[:,:,1]
    train_list.append(green_image)

#Preprocessing I tried: Please uncomment this part.
## Steps tried: Normalisation, Intensity shift, Gaussian Noise and Adaptive Histogram Equalisation

# for i in range(len(train_set)):
#     normalised_image= sitk.NormalizeImageFilter()
#     normalised_image=normalised_image.Execute(train_image_set[i])
#     normalised_image=sitk.GetArrayFromImage(normalised_image)
#     green_img=normalised_image[:,:,1]
#     green_img=sitk.GetImageFromArray(green_img)
#     #bright_img=sitk.ShiftScaleImageFilter()
#     #bright_img.SetShift(0)
#     #bright_img.SetScale(2)
#     #bright_img=bright_img.Execute(green_img)
#      noise_img=sitk.AdditiveGaussianNoiseImageFilter()
#      noise_img.SetMean(0)

#     noise_img.SetStandardDeviation(0.5)
#     noise_img=noise_img.Execute(bright_img)

#     #hist= sitk.AdaptiveHistogramEqualizationImageFilter()
#     #hist.SetAlpha(0.3)
#     #hist.SetBeta(0.3)
#     #hist.SetRadius(2)
#     #y=hist.Execute(noise_img)
#    # y2= sitk.GetArrayFromImage(_img)
#     train_list.append(y2)

print ('train_data')
np.savez('data_train_final.npz',mask_set=mask_set,ground_truth_list=ground_truth_list,train_list=train_list)
print ('saved')

## For test Images:
## Please change the DRIVE data location
ground_test_dir= "C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/test/1st_manual/*.gif"
img_test_dir="C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/test/images/*.tif"
mask_test_dir= "C:/Users/LENOVO/Documents/Harsha/14.12.22/retina-segmentation-CNN-/test/mask/*.gif"

test_image_set= imread_collection(img_test_dir)
ground_truth_set= imread_collection(ground_test_dir)
test_mask_set=imread_collection(mask_test_dir)

test_image_list=list(test_image_set)
test_ground_truth_list=list(ground_truth_set)
test_mask_list= list(test_mask_set)
test_mask_list=np.asarray(test_mask_list)

test_list=[]
for i in range(len(test_image_set)):
    image= sitk.GetImageFromArray(test_image_list[i])
    normalised_image= sitk.NormalizeImageFilter()
    normalised_image=normalised_image.Execute(image)
    normalised_image=sitk.GetArrayFromImage(normalised_image)
    green_image= normalised_image[:,:,1]
    test_list.append(green_image)

test_list=np.asarray(test_list)
test_ground_truth_list=np.asarray(test_ground_truth_list)
test_mask_list=np.asarray(test_mask_list)

print ('test_data')
np.savez('data_test_final.npz',test_list=test_list,test_ground_truth_list=test_ground_truth_list,test_mask_list=test_mask_list)

print ('saved')


## References:
# [1] www.isi.uu.nl/Research/Databases/DRIVE/
# [2] simpleitk.readthedocs.io/en/master/


