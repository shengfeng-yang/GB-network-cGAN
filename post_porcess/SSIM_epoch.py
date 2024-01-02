import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
import matplotlib.image as imgplt

SSIM = np.zeros(200)
for k in range(89,90):
    print(k)
    for j in range(200):
        # result direction of pix2pix model
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/train_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 1 # id of sample's left side
        test_range_r = 240 # id of sample's right side
        num = test_range_r+1-test_range_l
        for i in range(test_range_l,test_range_r+1):
        #     try:
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
            img_fake = 20*img_fake[:,:,:]
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            img_real = 20*img_real[:,:,:]
            ssim_const = ssim(img_real[:,:,0:2], img_fake[:,:,0:2],data_range=20,multichannel=True)
            # ssim_const = ssim(img_real, img_fake,data_range=img_fake.max() - img_fake.min(),multichannel=True)
    #         print (ssim_const)
            a_1 += ssim_const
        print (j*5+5,'avg =',a_1/(test_range_r+1-test_range_l)) 
        SSIM[j] = a_1/(test_range_r+1-test_range_l)

    epochs = np.arange(5,1001,5)
    plt.plot(epochs,SSIM)
    plt.ylabel('SSIM')
    plt.xlabel('epochs')
    plt.savefig('00'+str(k)+'trainSSIM.jpg')
    plt.show()
    plt.close()


    print(k)
    for j in range(200):
        # result direction of pix2pix model
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/test_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 271 # id of sample's left side
        test_range_r = 300 # id of sample's right side
        num = test_range_r+1-test_range_l
        for i in range(test_range_l,test_range_r+1):
        #     try:
            img_fake = 20*imgplt.imread(PATH+str(i)+'_fake_B.png')
            img_fake = img_fake[:,:,:]
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            img_real = 20*img_real[:,:,:]
            # ssim_const = ssim(img_real, img_fake,data_range=img_fake.max() - img_fake.min(),multichannel=True)
            ssim_const = ssim(img_real[:,:,0:2], img_fake[:,:,0:2],data_range=20,multichannel=True)
    #         print (ssim_const)
            a_1 += ssim_const
        print (j*5+5,'avg =',a_1/(test_range_r+1-test_range_l)) 
        SSIM[j] = a_1/(test_range_r+1-test_range_l)

    epochs = np.arange(5,1001,5)
    plt.plot(epochs,SSIM)
    plt.ylabel('SSIM')
    plt.xlabel('epochs')
    plt.savefig('00'+str(k)+'testSSIM.jpg')
    plt.show()
    plt.close()