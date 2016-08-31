def squareRootBi(x,epsilon):

	assert x >= 0, "x must be positive, not"+str(x)
	assert epsilon >0, "epsilon must be positive, not"+str(epsilon)

	low = 0
	high = max(x,1)
	guess = (low+high)/2.0
	ctr = 1

	while abs(guess**2-x) > epsilon and ctr <= 100:
		
		if guess**2 < x:
			low = guess
		else:
			high = guess
		guess = (low+high)/2.0
		ctr += 1
	string = "Bi method "+"iteration:"+str(ctr)+" answer:"+str(guess)
	print(string)
	return guess

if __name__=='__main__':
	squareRootBi(4,0.0001)
	squareRootBi(9,0.0001)
	squareRootBi(2,0.0001)
	squareRootBi(0.25,0.0001)