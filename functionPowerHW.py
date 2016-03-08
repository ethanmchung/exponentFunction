def power(base, exponent):
	
	newNumber = base
	#one is subtracted from the exponent variable, so when the user uses positive exponent '1', the output is not the base * the base
	#in other words, you have to account for the fact that 2^2 is not 2*2*2 but 2*2;
	#the same applies for a negative exponent but in this case one is added to the negative exponent variable
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
		newNumber = 1
		
	return(newNumber)


base = int(input("Give me a base "))
exponent = int(input("Give me an exponent ")) 
	
print(power(base,exponent))