#Program to find out mean median and mode of the given array
import numpy as np
from scipy import stats

size = int(input())
#Used list map and split methods here
numbers = list(map(int, input().split()))
#used mean method
print(np.mean(numbers))
#used median method
print(np.median(numbers))
#Used mode method which is in stats module
print(int(stats.mode(numbers)[0]))
