# Image Aneurysm_Detection-SS2019

An on-going Project for SS2019.

Below is my apprach towards solving the task.The learning is slow and indicates underfitting for now, I am yet to figure out the reason.

Introduction-
The input data is real patient brain scans images of the shape (220,256,256) and masks of (220,256,256)
I have used UNET model for Aneursym_Detection with Pytorch based implementation.

Not all the data provided is of the same shape hence and it had to be pre-processed before training.
1. DataPreprocessing-charul-final.ipynb 
   - Images are converted into the format 200*256*256
   - Each DCIOM file is split into the slices 220 times. The result are jpeg images of the form 
        Slice0_0..... Slice0_119 for (Patient-0)

1. image_to_npy.ipynb
   - Jpeg files are converted to numpy for training Process
 
1. model.py
   - Basic UNET model for Aneursym_Detection

1. unet-charul.ipynb
   - DataLoader and training
  


 
