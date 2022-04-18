import numpy as np
import matplotlib.pylab as plt

#계단 함수
def step_function(x):
    if x>0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

def step_function3(x):
    return np.array(x>0, dtype=np.int)

#시그모이드 함수
def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

#소프트맥스 함수
def softMaxFunction(x):
    return np.exp(x)/np.sum(np.exp(x))
    