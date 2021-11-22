from main import *
from image_to_data import image_to_data
from images import images_processing

images_processing('input.png')
data = image_to_data('./image')
CKPT_2='ckpt/lenet-3_2187.ckpt'
infer(data, CKPT_2)
