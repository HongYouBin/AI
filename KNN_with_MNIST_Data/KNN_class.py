import sys, os
sys.path.append(os.pardir)
from random import *
import numpy as np
from dataset.mnist import load_mnist

from PIL import Image

(x_train, t_train), (x_test, t_test) =load_mnist(flatten=True, normalize=False)

# image = x_test[0]
# label = t_test[0]
# def img_show(img):
#     pil_img = Image.fromarray(np.uint8(img))
#     pil_img.show()
# image = image.reshape(28, 28)
# print(image.shape)
# img_show(image)

class knnClass:  
    def __init__(self, k, index):
        self.k = k 
        self.index = index
        self.outData = [] 
    def calDist(self):
        for i in range(10000):
            res = float(0)
            for t in range(784):
                res += (float(x_test[self.index][t])-float(x_train[i][t]))**2
            res = res**(1/2)
            lst = [res, t_train[i]]
            self.outData.append(lst)
    def obtainVote(self):
        self.outData.sort(key=lambda x:x[0]) 
        res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        for i in range(self.k):
            res[self.outData[i][1]]+=1 
        maxKey = 0
        for i in range(10):
            if res[maxKey]<res[i]: 
                maxKey = i 
        return maxKey


# k1= knnClass(100, 0)
# k1.calDist()
# print(k1.obtainVote())

class myKnnClass:  
    def __init__(self, k, index):
        self.k = k 
        self.index = index
        self.outData = [] 
    def calDist(self):
        for i in range(2000):
            res = float(0)
            for k in range(500):
                ran = randrange(0, 784)
                res += (float(x_test[self.index][ran])-float(x_train[i][ran]))**2
            res = res**(1/2)
            lst = [res, t_train[i]]
            self.outData.append(lst)
    def obtainVote(self):
        self.outData.sort(key=lambda x:x[0]) 
        res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        for i in range(self.k):
            res[self.outData[i][1]]+=1 
        maxKey = 0
        for i in range(10):
            if res[maxKey]<res[i]: 
                maxKey = i 
        return maxKey

