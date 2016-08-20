def insertionSort(alist):
	for index in range(1,len(alist)):
		currentValue = alist[index] # 2 4 6 1 3
		position = index # 1 2 3 4 5

		while position > 0 and alist[position-1] > currentValue:
			alist[position] = alist [position-1]
			position = position -1
		alist[position] = currentValue

alist = [5,2,4,6,1,3]
insertionSort(alist)
print alist

#insertionSort(a[0...n-1])
# for i <--- 1 to n-1 do
        #v <--- a[i]
        #j <-- i - 1
        #while j>= 0 and a[j]>v:
        	#a[j+1]=a[j]
        	#j = j - 1
        #a[j+1] = v
        
