from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def picture_tow_valued(image):
    # 把图片转为numpy类型
    image_np=np.array(image)
    # 计算图片离散度
    discretization=image_np.mean()-image_np.std()
    discretization=int(discretization)
    discretization=120
    # 循环图片上每一个点
    for i in range(image_np.shape[0]):
        for j in range(image_np.shape[1]):
            # 把大于离散度的数值变为0,小于的变为1,图片就变成了只有两个数值的黑白图片
            if image_np[i,j]>discretization:
                image_np[i,j]=0
            else:
                image_np[i,j]=1
 
    '''
    有些图片有瑕疵,边缘没有处理会影响切图,吧边缘数字全部变为0(黑色)
    '''
    for i in range(image_np.shape[0]):
        for j in range(image_np.shape[1]):
            if i == 0 or i == (image_np.shape[0]-1):
                image_np[i,j]=0
                continue
            if j == 0 or j == (image_np.shape[1]-1):
                image_np[i,j]=0
                continue
    print(image_np)
    return image_np

def cut_picture_rank(image):
    image0=[]
    image1=[]
    #  按照图片的列切
    for i in range(image.shape[1]):
        # 如果行全部是0就证明这一行没有数字
        if any(image[:,i]):
            image1.append(image[:,i])
        else:
            # 检测到数字的末尾
            if any(image[:,i-1]) and len(image1)>8:
                image0.append(image1)
                image1=[]
    # list转numpy类型
    for i,j in enumerate(image0):
        image0[i]=np.array(j).T
    return image0

def cut_picture_row(image):
    image0=[]
    image1=[]
    for z in image:
        #  按照图片的行切
        for i in range(z.shape[0]):
            # 如果行全部是0就证明这一行没有数字
            if any(z[i,:]):
                image1.append(z[i,:])
            else:
                # 检测到数字的末尾 并且高度要大于8 筛选出去一些躁点
                if any(z[i-1,:]) and len(image1)>8:
                    image0.append(image1)
                    image1=[]
    for i,j in enumerate(image0):
        image0[i]=np.array(j)
    return image0

def save_picture(image):
    j=0
    print(np.shape(image))
    for i in image:
        plt.imsave("./image/%s.png" % (str(j)), i, cmap='gray')
        i=Image.open("./image/%s.png" % (str(j)))
        i.thumbnail((32,32),Image.ANTIALIAS)
        i.convert('L').save("./image/%s.png" % (str(j)))
        j += 1

def make_picture_square(image):
    n=np.shape(image)
    print(n[0])
    list=[]
    for i in range(n[0]):
        shape=np.shape(image[i])
        print(shape)
        if image[i].ndim == 2 and shape[1]>10 and shape[0]>10:
            if shape[0]>shape[1]:
                add_h = int((shape[0]-shape[1])/2)+64
                add_h_np = np.zeros((shape[0],add_h),dtype=int)
                add_v_np = np.zeros((64,shape[1]+2*add_h),dtype=int)
                image[i] = np.hstack((add_h_np,image[i],add_h_np))
                image[i] = np.vstack((add_v_np,image[i],add_v_np))
            elif shape[1]>shape[0]:
                add_v = int((shape[1]-shape[0])/2)+64
                add_v_np = np.zeros((add_v,shape[1]),dtype=int)
                add_h_np = np.zeros((shape[0]+2*add_v,64),dtype=int)
                image[i] = np.vstack((add_v_np,image[i],add_v_np))
                image[i] = np.hstack((add_h_np,image[i],add_h_np))
            else:
                continue
        else:
            list.append(i)
    image = np.delete(image, list, axis=0)
    return image


def images_processing(image_name='test.png'):
    img=Image.open(image_name)
    image=img.convert("L")
    # plt.imshow(image)
    image_np = picture_tow_valued(image)
    image_rank = cut_picture_rank(image_np)
    image_row = cut_picture_row(image_rank)
    image_square = make_picture_square(image_row)
    save_picture(image_square)

if __name__ == '__main__':
    images_processing('input17.png')