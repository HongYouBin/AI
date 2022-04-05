#perceptron
import numpy as np

#AND 
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    a = np.sum(w*x)+b
    if a>=0:
        return 1
    else:
        return 0

#NAND
def NAND(x1, x2):
    #return not AND(x1, x2)
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    a = np.sum(w*x)+b
    if a>=0:
        return 1
    else:
        return 0
   

#OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    a = np.sum(w*x)+b
    if a>=0:
        return 1
    else:
        return 0

#XOR
def XOR(x1, x2):
    y1 = NAND(x1, x2)
    y2 = OR(x1, x2)
    return AND(y1, y2)

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))