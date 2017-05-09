import numpy as np


def twosum(nums, target):
	for i in nums  :
		#print i
		k = target - i
		#print k
		for j in nums :
			#print j
			if (j == k & j != i)  :
				result = [i,j]
				return  result

if __name__ == "__main__":
	result = twosum([2,5,6,7,8],8)
	print result
