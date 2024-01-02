import numpy as np
import matplotlib.pyplot as plt

from skimage.metrics import mean_squared_error
import matplotlib.image as imgplt

avg_norm = np.zeros(200)
for k in range(64,65):
    print(k)
    for j in range(200):
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/train_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 1
        test_range_r = 240
        for i in range(test_range_l,test_range_r+1):
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            mse = mean_squared_error(img_real[:,:,0], img_fake[:,:,0]) 
            a_1 = a_1 +mse
        avg_norm[j] = a_1/(test_range_r+1-test_range_l)
        print (5+5*j,avg_norm[j])

    epochs = np.arange(5,1001,5)
    L2_change = plt.plot(epochs,avg_norm)
    plt.ylabel('L2_norm')
    plt.xlabel('epochs')
    plt.savefig(r'00'+str(k)+'_train_L2_layer0.jpg')
    plt.show()
    plt.close()

    for j in range(200):
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/train_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 1
        test_range_r = 240
        for i in range(test_range_l,test_range_r+1):
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            mse = mean_squared_error(img_real[:,:,1], img_fake[:,:,1]) 
            a_1 = a_1 +mse
        avg_norm[j] = a_1/(test_range_r+1-test_range_l)
        print (5+5*j,avg_norm[j])

    epochs = np.arange(5,1001,5)
    L2_change = plt.plot(epochs,avg_norm)
    plt.ylabel('L2_norm')
    plt.xlabel('epochs')
    plt.savefig(r'00'+str(k)+'_train_L2_layer1.jpg')
    plt.show()
    plt.close()

    for j in range(200):
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/train_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 1
        test_range_r = 240
        for i in range(test_range_l,test_range_r+1):
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            mse = mean_squared_error(img_real[:,:,2], img_fake[:,:,2]) 
            a_1 = a_1 +mse
        avg_norm[j] = a_1/(test_range_r+1-test_range_l)
        print (5+5*j,avg_norm[j])

    epochs = np.arange(5,1001,5)
    L2_change = plt.plot(epochs,avg_norm)
    plt.ylabel('L2_norm')
    plt.xlabel('epochs')
    plt.savefig(r'00'+str(k)+'_train_L2_layer2.jpg')
    plt.show()
    plt.close()


    print(k)
    for j in range(200):
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/test_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 271
        test_range_r = 300
        for i in range(test_range_l,test_range_r+1):
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            mse = mean_squared_error(img_real[:,:,0], img_fake[:,:,0]) 
            a_1 = a_1 +mse
        avg_norm[j] = a_1/(test_range_r+1-test_range_l)
        print (5+5*j,avg_norm[j])

    epochs = np.arange(5,1001,5)
    L2_change = plt.plot(epochs,avg_norm)
    plt.ylabel('L2_norm')
    plt.xlabel('epochs')
    plt.savefig(r'00'+str(k)+'_test_L2_layer0.jpg')
    plt.show()
    plt.close()

    for j in range(200):
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/test_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 271
        test_range_r = 300
        for i in range(test_range_l,test_range_r+1):
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            mse = mean_squared_error(img_real[:,:,1], img_fake[:,:,1]) 
            a_1 = a_1 +mse
        avg_norm[j] = a_1/(test_range_r+1-test_range_l)
        print (5+5*j,avg_norm[j])

    epochs = np.arange(5,1001,5)
    L2_change = plt.plot(epochs,avg_norm)
    plt.ylabel('L2_norm')
    plt.xlabel('epochs')
    plt.savefig(r'00'+str(k)+'_test_L2_layer1.jpg')
    plt.show()
    plt.close()

    for j in range(200):
        PATH = r'/N/project/polycrystalGAN/polycrystal/pytorch-CycleGAN-and-pix2pix/results/00'+str(k)+'/test_'+str(j*5+5)+'/images/'
        print(PATH)
        a_1 = 0
        test_range_l = 271
        test_range_r = 300
        for i in range(test_range_l,test_range_r+1):
            img_fake = imgplt.imread(PATH+str(i)+'_fake_B.png')
        #     print (img_fake)
            img_real = imgplt.imread(PATH+str(i)+'_real_B.png')
            mse = mean_squared_error(img_real[:,:,2], img_fake[:,:,2]) 
            a_1 = a_1 +mse
        avg_norm[j] = a_1/(test_range_r+1-test_range_l)
        print (5+5*j,avg_norm[j])

    epochs = np.arange(5,1001,5)
    L2_change = plt.plot(epochs,avg_norm)
    plt.ylabel('L2_norm')
    plt.xlabel('epochs')
    plt.savefig(r'00'+str(k)+'_test_L2_layer2.jpg')
    plt.show()
    plt.close()