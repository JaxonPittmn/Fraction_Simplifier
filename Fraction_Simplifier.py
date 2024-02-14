frac_In = str(input("Input: "))
def Challenge():
	done = False
	is_zero = False
	is_undef = False
	fracs = frac_In.split("/")
	
	numer = int(fracs[0])
	denom = int(fracs[1])
	wholeNum = -1
	
	while not done:
		if denom == 0:
			is_undef = True
			done=True
			
		elif numer == 0:
			is_zero = True
			done=True
			
		elif numer > denom:
			if numer/denom % 2 > 0:
				wholeNum = int(round(numer/denom, 0))
				numer = numer%denom
				
				
			else:
				wholeNum = int(numer/denom)
				numer = -1
				denom = -1
				done = True
				
		elif numer < denom:
			denom = int(denom/numer)
			numer = int(numer/numer)
	
			done=True

	
		elif numer == denom:
			done = True
			print("1")

	
	if wholeNum == -1:
		if is_zero:
			print("0")
		elif is_undef:
			print("undefined")
		else:
			print(f"{numer}/{denom}")
			
	elif numer == -1 or denom == -1:
		print(wholeNum)
	else:
		print(f"{wholeNum} {numer}/{denom}")
	
Challenge()