import KNN_class as knn
import numpy as np
import sys

sys.stdout = open('output3.txt', 'w')

size = 10
sample = np.random.randint(0, knn.t_test.shape[0], size)

accuracy = float(size)
for i in sample:
    tmp = knn.knnClass(100, i)
    tmp.calDist()
    output = f"{i}th data result {tmp.obtainVote()} label {knn.t_test[i]}"
    print(output)
    if tmp.obtainVote() != knn.t_test[i]:
        accuracy-=1

accuracy /= size

print("accuracy = "+str(accuracy))
print("------------------------------")
accuracy = float(size)
for i in sample:
    tmp = knn.myKnnClass(100, i)
    tmp.calDist()
    output = f"{i}th data result {tmp.obtainVote()} label {knn.t_test[i]}"
    print(output)
    if tmp.obtainVote() != knn.t_test[i]:
        accuracy-=1

accuracy /= size
print("accuracy = "+str(accuracy))

sys.stdout.close()

