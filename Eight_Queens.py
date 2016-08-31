#deep search recursively for eight queens

def Queen(num):
	global queens_num,total_ans
	queens_num=num
	row=0
	array=[0]*queens_num
	total_ans=0
	backtrack(row,array)

def backtrack(row,array):
	if row==queens_num:
		global total_ans
		total_ans+=1
		for i in array:
			print i
		print '\n'
	else:
		for j in xrange(1,queens_num+1):
			array[row]=j;
			if place(row,array):
				backtrack(row+1,array)

def place(row,array):
	for i in xrange(0,row):
		if abs(array[row]-array[i])==abs(row-i) or array[row]==array[i]:
			return False
	return True


if __name__=='__main__':
	Queen(8)
	print total_ans

