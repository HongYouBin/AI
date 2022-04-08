#B735539 홍유빈

from tokenize import Double
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
testData = iris.data    #iris 데이터를 저장하는 리스트
trueClass =  iris.target    #iris의 종류중 무엇인지 그 결과값을 저장하는 리스트
targetName = iris.target_names  #iris target의 결과값을 통해 이름을 알게해주는 target name을 저장하는 리스트

class knn:  
    def __init__(self, k, index):
        self.k = k #몇 개의 값과 비교할지 설정하는 k
        self.index = index*15+14 #index는 14, 29, ... 149까지 15씩 증가하도록 한다
        self.inpData = testData[self.index] #해당 인덱스의 iris 데이터를 저장한다
        self.outData = [] #계산 결과값을 저장할 list
    def calDist(self):
        for i in range(150): 
            if (i+1)%15!=0: #150개의 데이터중 14, 29, ... , 149까지의 데이터를 제외한 총 130개의 데이터로 비교한다
                res = float(0) #sepal length, sepal width, petal length, petal width 총 4가지 데이터를 비교하여 차이값을 계산한다
                for t in range(4):
                    res += (float(testData[i][t])-float(self.inpData[t]))**2
                res = res**(1/2) #차이값 계산 후 저장한다
                lst = [res, trueClass[i]] #차이값과, 해당 i번째 데이터의 참 결과값을(i번째 iris가 무슨 종류인지 알려주는 값) 같이 리스트에 넣어 저장
                self.outData.append(lst) 
    def obtainVote(self):
        self.outData.sort(key=lambda x:x[0]) #차이값을 기준으로 오른차순으로 정렬한다. 차이값이 가장 작을 수록 리스트의 앞에 오도록 정렬한다
        res = [0, 0, 0] #결과값을 받는 list
        for i in range(self.k):
            res[self.outData[i][1]]+=1 #차이값이 가장 작은 k개의 참 결과값을 인덱스로하여 res에 값을 추가한다
        maxKey = 0
        for i in range(1,3):
            if res[maxKey]<res[i]: 
                maxKey = i #가장 많이 나온 iris의 인덱스를 max key로 저장
        return targetName[maxKey] #최종 결과를 출력한다

