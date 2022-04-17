import sys, os
sys.path.append(os.pardir)
from random import *
import numpy as np
from dataset.mnist import load_mnist

from PIL import Image

(x_train, t_train), (x_test, t_test) =load_mnist(flatten=True, normalize=False)


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


class myKnnClass:  
    def __init__(self, k, index):
        self.k = k 
        self.index = index
        self.outData = [] 
    def calDist(self):
        for i in range(100):
            res = float(0)
            for k in range(100):
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

# knn1 = knn(100, 1)
# knn1.calDist()
# print(knn1.obtainVote())
# print(t_test[1])



# size = 10
# sample = np.random.randint(0, t_test.shape[0], size)

# accuracy = float(size)
# lst = []
# for i in sample:
#     tmp = knnClass(100, i)
#     tmp.calDist()
#     output = f"{i}th data result {tmp.obtainVote()} label {t_test[i]}"
#     print(output)
#     if tmp.obtainVote() != t_test[i]:
#         accuracy-=1

# accuracy /= size

# print("accuracy = "+str(accuracy))