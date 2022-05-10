#!/usr/bin/env python
# coding: utf-8

# In[94]:


#Encode each mask image feature with unique number and save the images 
'''
TASKS BY THIS PIECE OF CODE
Takes the location of all facial masks whose names are saved in the format of CelebAHQMask dataset

Functions of the class splitImages:

BlackToWhite : Transposes the masks such that black pixels become white and viceversa, picks up file 
               from maskPath and save in MaskFilepath

RemoveUnwantedFeatures : Function to control number of features to be used for creating training dataset

move: Uses dictionary to copy all face maks pertaining to one image from MaskFilepath to one folder per 
      image into TargetFolders

process : Reads image masks from each folder, encodes each mask of the facial feature with unique number, 
          combines all the mask images into one uint8 RGB image and saves them as uint8 Black and white 
          image and saves them in the given SavePath with the name same as the original image as per 
          CelebAHQMask dataset.
'''
import os
import sys
import numpy as np
import cv2
import shutil
from PIL import Image 

class splitImages:
    def __init__(self, maskPath, TargetFolders, SavePath):
        self.maskPath = maskPath
        #self.MaskFilepath = MaskFilepath
        self.TargetFolders = TargetFolders
        self.SavePath = SavePath
    
    #To convert black images to white   
    def BlackToWhite(self, MaskFilepath):
        for filename in os.listdir(maskPath):
            img =cv2.imread(self.maskPath+"/"+filename)
            img = 255-img
            cv2.imwrite(MaskFilepath+"/"+filename, img) 
    
    def RemoveUnwantedFeatures(self):
        for filename in os.listdir(self.maskPath):
            #desc=" ".join(filename.split(".png")[0].split("_")[1:])
            desc1=" ".join(filename.split(".png")[0].split("_")[2:])
            if desc1 == 'g':
                os.remove(self.maskPath+"/"+filename)
                #print(file)  
    
    def move(self):
        d={}
        for filename in os.listdir(self.maskPath):
            desc = filename
            id=int(filename.split("_")[0])
            if(id in list(d.keys())):
                d[id].append(desc)
            else:
                d[id]=list([desc])
        for i in d:
            os.mkdir(self.TargetFolders+"/"+str(i))
            for j in range(len(d[i])):
                #print(d[i][j])
                shutil.copyfile(self.maskPath+"/"+d[i][j],self.TargetFolders+"/"+str(i)+"/"+d[i][j])
    def process(self, savetype):
        img =[]
        lst = os.listdir(self.TargetFolders)
        lst.sort()
        for folders in lst:
            #print(folders)
            for filename in os.listdir(self.TargetFolders+'/'+folders+'/'):
                desc=" ".join(filename.split(".png")[0].split("_")[1:]) #to pick up image name
                desc1=" ".join(filename.split(".png")[0].split("_")[2:]) #to pick up image name at third position
                #print(filename)
                if desc == 'hair' or desc == 'hat':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    hair=np.copy(original_image)
                    white=np.where((hair[:,:,0]==255) & (hair[:,:,1]==255) & (hair[:,:,2]==255))
                    hair[white]=(10,10,10)
                elif desc == 'l brow':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    l_brow=np.copy(original_image)
                    white=np.where((l_brow[:,:,0]==255) & (l_brow[:,:,1]==255) & (l_brow[:,:,2]==255))
                    l_brow[white]=(2,2,2)
                elif desc == 'l eye':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    l_EYE=np.copy(original_image)
                    white=np.where((l_EYE[:,:,0]==255) & (l_EYE[:,:,1]==255) & (l_EYE[:,:,2]==255))
                    l_EYE[white]=(4,4,4)
                elif desc == 'r brow':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    r_brow=np.copy(original_image)
                    white=np.where((r_brow[:,:,0]==255) & (r_brow[:,:,1]==255) & (r_brow[:,:,2]==255))
                    r_brow[white]=(1,1,1)
                elif desc == 'r eye':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    r_EYE=np.copy(original_image)
                    white=np.where((r_EYE[:,:,0]==255) & (r_EYE[:,:,1]==255) & (r_EYE[:,:,2]==255))
                    r_EYE[white]=(3,3,3)
                elif desc == 'nose':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    nose=np.copy(original_image)
                    white=np.where((nose[:,:,0]==255) & (nose[:,:,1]==255) & (nose[:,:,2]==255))
                    nose[white]=(5,5,5)
                elif desc == 'skin':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    skin=np.copy(original_image)
                    white=np.where((skin[:,:,0]==255) & (skin[:,:,1]==255) & (skin[:,:,2]==255))
                    skin[white]=(1,1,1)
                elif desc == 'u lip':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    u_lip=np.copy(original_image)
                    white=np.where((u_lip[:,:,0]==255) & (u_lip[:,:,1]==255) & (u_lip[:,:,2]==255))
                    u_lip[white]=(6,6,6)
                elif desc== 'mouth':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    mouth=np.copy(original_image)
                    white=np.where((mouth[:,:,0]==255) & (mouth[:,:,1]==255) & (mouth[:,:,2]==255))
                    mouth[white]=(7,7,7)
                elif desc == 'l lip':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    l_lip=np.copy(original_image)
                    white=np.where((l_lip[:,:,0]==255) & (l_lip[:,:,1]==255) & (l_lip[:,:,2]==255))
                    l_lip[white]=(8,8,8)
                elif desc == 'neck' or desc == 'cloth':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    neckCloth=np.copy(original_image)
                    white=np.where((neckCloth[:,:,0]==255) & (neckCloth[:,:,1]==255) & (neckCloth[:,:,2]==255))
                    neckCloth[white]=(0,0,0)
                elif desc == 'ear' or desc1 == 'ear':
                    original_image=cv2.imread(self.TargetFolders+'/'+folders+'/'+filename)
                    ear=np.copy(original_image)
                    white=np.where((ear[:,:,0]==255) & (ear[:,:,1]==255) & (ear[:,:,2]==255))
                    ear[white]=(10,10,10)
                    
            '''Add all the features except hair, ear, mouth, neckCloth as these features(ear, mouth, neckCloth)
               are not available in all the images and there can poosibly be only one just overlap of mouth, 
               l_lip and u_lip'''
            
            im = skin+l_brow+l_EYE+r_brow+r_EYE+nose+u_lip+l_lip
            
            '''Using try catch block to verify if neckCloth and mouth masks exist in the given folder and then 
            deleting the variables to make sure they do not get included in the mask of next image'''
            try:
                im = im + neckCloth
                del neckCloth
            except NameError:
                pass
            
            try:
                im = im + mouth
                del mouth
            except NameError:
                pass
            
            #Remove all pixels above 9 and replace them with 8 which is the pixel value for mouth
            HValues=np.where((im[:,:,0]>9) & (im[:,:,1]>9) & (im[:,:,2]>9))
            im[HValues]=(8,8,8)  
            
            '''Placing the try-catch block for ear below as its pixel value is 10'''
            try:
                im = im + ear
                del ear
            except NameError:
                pass
            
            #Adding whole face and hair
            #Since hair can sometimes come over all the other facial features, Highest priority is given to hair
            im = hair + im
            HValues=np.where((im[:,:,0]>10) & (im[:,:,1]>10) & (im[:,:,2]>10))
            im[HValues]=(10,10,10)
            
            img.append(im)
            image_file=Image.fromarray(im.astype('uint8'), 'RGB')
            image_file = image_file.convert(savetype) # convert image to black and white or color depending on 
            #the value of savetype
            image_file.save(self.SavePath+folders+".png")
        return(img)
    

Target = "/projects/panday/Mask_Guided_Portrait_Editing/datasets/smallanno/xyz/"
SavePath = "/projects/panday/Mask_Guided_Portrait_Editing/datasets/smallanno/train_label/"
maskPath = "/projects/panday/Mask_Guided_Portrait_Editing/datasets/CelebAMask-HQ/CelebAMask-HQ-mask-anno/2"

sol = splitImages(maskPath, Target, SavePath)
sol.move()
img=sol.process('L')
print('Process completed')
#sol.RemoveUnwantedFeatures()