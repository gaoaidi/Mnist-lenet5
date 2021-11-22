import os
from PIL import Image
import numpy as np
from array import *
image_path='./image'
def image_to_data(image_path='./image'):
    FileList = []
    # for dirname in os.listdir(image_path)[1:]: # [1:] Excludes .DS_Store from Mac OS
    #     path = os.path.join(image_path,dirname)
    filenames = os.listdir(image_path)
    if '.DS_Store' in filenames:
        filenames.remove('.DS_Store')
    filenames.sort(key = lambda x:int(x[:-4]))
    print(filenames)
    for filename in filenames:
        if filename.endswith(".png"):
            FileList.append(os.path.join(image_path,filename))

    image_datas=[]
    for filename in FileList:
        image_data=[]
        Im = Image.open(filename)
        pixel = Im.load()
        width, height = Im.size
        for x in range(0,width):
            image_data_rank=[]
            for y in range(0,height):
                image_data_rank.append(pixel[y,x]/78.56550044-0.42421293)
            image_data.append(image_data_rank)
        image_datas.append([image_data])
    image_data_np=np.array(image_datas)
    print(np.shape(image_data_np))
    return image_data_np

	
