def Hanoi(size,start,to,spare):
	if size==1:
		print 'move disk from '+start+' to '+to
	else:
		Hanoi(size-1,start,spare,to)
		Hanoi(1,start,to,spare)
		Hanoi(size-1,spare,to,start)


if __name__=='__main__':
	Hanoi(3,"start","des","mid")

    	
	