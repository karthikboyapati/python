#Weighted mean summation code in python

n = int(input())
#used split and map methods to get the required array from input of keyboard
x = list(map(int,input().split()))
w = list(map(int,input().split()))
#Actual code
num =0
for i in range(n):
    num = (x[i]*w[i]) + num

den = sum(w)

#Rounded off to value 1
print(round((num/den),1))


#Code with numpy library
import numpy as np

num = input()
x = list(map(int,input().split()))
w = list(map(int,input().split()))
#method for weighted mean "np.average"
xw = np.average(x,weights=w)
#rounded off the value to 1
print(round(xw,1))
