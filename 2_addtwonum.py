import numpy


def addtwonum(l1,l2) :
	result = [0 for i in range (len(l1))]
	flag = 0
	for i in range(len(l1)) :
		
		if flag == 0 :
			result[i]=l1[i]+l2[i]
		else :
			result[i]=l1[i]+l2[i]+1
			
		if result[i] >= 10 :
			flag = 1
			result[i]= result[i] % 10
		else :
			flag = 0
		
	return result
		
	
	
	
	
	
	

if __name__=="__main__" :
	final_result = addtwonum([2,8,1],[1,3,7])
	print(final_result)
