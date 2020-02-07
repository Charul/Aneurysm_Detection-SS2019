# Image Segmentation,Aneurysm_Detection-SS2019

Project for SS2019.


UPDATE: I implemented a new Unet model with Keras and it now predicts the masks for an image with aneurysm.The final code is in the file with the name keras_unet_final.I realized that from the 23k slices for the given dataset of 106 patients only 1750 where with aneurysm. So I trained the network with only aneurysms to see if if it learns to predict the masks and it does so. 

Earlier approach with feeding 70-30 of 23k images, the network learnt to predict black images and not with aneurysm.

----------------------------------------
Below is my approach towards solving the task.The learning is slow and indicates underfitting for now, I am yet to figure out the reason.

Introduction-
The input data is real patient brain scans images of the shape (220,256,256) and masks of (220,256,256)
I have used UNET model for Aneursym_Detection with Pytorch based implementation.

Not all the data provided is of the same shape hence and it had to be pre-processed before training.
1. DataPreprocessing-charul-final.ipynb 
   - Images are converted into the format (220,256,256)
   - Each DCIOM file is split into the slices 220 times. The result are jpeg images of the form 
        Slice0_0..... Slice0_119 for (Patient-0)

1. image_to_npy.ipynb
   - Jpeg files are converted to numpy for training Process
 
1. model.py
   - Basic UNET model for Aneursym_Detection

1. unet-charul.ipynb
   - DataLoader and training
  

