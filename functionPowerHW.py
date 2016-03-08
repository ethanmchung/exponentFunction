def power():
	base = int(input("Give me a base "))
	exponent = int(input("Give me an exponent ")) 
	#one was subtracted from the exponent variable before, so when the user uses exponent '1', the output is not the base * the base
	#in other words, you have to account for the fact that 2^2 is not 2*2*2 but 2*2
	
	newNumber = base
	if exponent < 0:
		exponent = exponent + 1
		while exponent < 0:
			newNumber = base * newNumber
			exponent = exponent + 1
		newNumber = 1/newNumber
		
	elif exponent > 0:
		exponent = exponent - 1
		while exponent > 0: #this loop ensures that the base undergoes the exponential operation for as many times as the exponent dictates
			newNumber = base * newNumber
			exponent = exponent - 1
		
	elif exponent == 0:
		exponent = exponent - 1
		newNumber = 1
		
	print(newNumber)

power()