def BubbleSort(array):
	for j in range(len(array)):
		for i in range(len(array)-1-j):
			if array[i] > array[i+1]:
				temp=array[i+1]
				array[i+1]=array[i]
				array[i]=temp
		print array
	return array

def SelectionSort(array):
	for j in range(len(array)):
		minval=j;
		for i in range(j,len(array)):
			if array[i] < array[minval]:
				minval = i
		temp=array[j]
		array[j]=array[minval]
		array[minval]=temp
		print array
	return array

def Merge(left,right):
	i=0
	j=0
	result=[]
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	while i < len(left):
		result.append(left[i])
		i+=1
	while j < len(right):
		result.append(right[j])
		j+=1
	print result
	return result
		


def MergeSort(array):
	if len(array) == 1:
		return array[:]
	else:
		mid = len(array)/2
		left = MergeSort(array[:mid])
		right = MergeSort(array[mid:])

	together = Merge(left,right)
	return together

		


array=[2,3,6,1,5,4,2,8]

#print BubbleSort(array)
#print SelectionSort(array)
#print MergeSort(array)