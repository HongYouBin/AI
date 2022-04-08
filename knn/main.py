#B735539 홍유빈
import knnClass 

lst = []
k = int(input("input k : ")) #총 몇개의 데이터와 비교할지 input으로 받아야 한다
for i in range(10): #index는 0부터 9까지 9개를 할당한다
    lst.append(knnClass.knn(k, i))
    lst[i].calDist()

print("Sample output")

accuracy = int(0) #정확도를 알려주는 변수를 설정

for i in range(10):
    tmp = f"Test Data Index: {i}, " + f"Computed class: {lst[i].obtainVote()}, "
    tmp += f"True class : {knnClass.targetName[knnClass.trueClass[i*15+14]]}"
    print(tmp)
    if lst[i].obtainVote() == knnClass.targetName[knnClass.trueClass[i*15+14]]:
        accuracy+=10 #총 10개의 데이터를 넣기 때문에 일치할 때마다 10%씩 증가한다

print("accuracy : "+str(accuracy)+"%") #결과값 도출
