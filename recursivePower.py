def power(base, exponent):
	if exponent > 0:
		return(base * power(base, exponent - 1))
	else:
		return 1

def floatFunction():
	x = input("Tell me a number. ")
	try:
		return float(x)
	except ValueError:
		print("WRONG")
		return floatFunction()

def intFunction():
	x = input("Tell me a number. ")
	try:
		return int(x)
	except ValueError:
		print("WRONG")
		return intFunction()	

print("When 5 is the base and 2 is the exponent, the answer is " + str(power(5, 2)))
print("When 0 is the base and 2 is the exponent, the answer is " + str(power(0, 2)))
print("When -2 is the base and 4 is the exponent, the answer is " + str(power(-2, 4)))
print("When 65 is the base and 1 is the exponent, the answer is " + str(power(65, 1)))
print("When -5 is the base and 3 is the exponent, the answer is " + str(power(-5, 3)))
print("When 3 is the base and 3 is the exponent, the answer is " + str(power(3, 3)))
print("When 5 is the base and 0 is the exponent, the answer is " + str(power(5, 0)))
print("When 1 is the base and 0 is the exponent, the answer is " + str(power(1, 0)))
print("When 1 is the base and 13 is the exponent, the answer is " + str(power(1, 13)))

print("When converted to a float, the previously entered number to the power of 4 is " + str(power(floatFunction(), 4)))
print("When converted to a float, the previously entered number to the power of 3 is " + str(power(floatFunction(), 3)))
print("When converted to a float, the previously entered number to the power of 2 is " + str(power(floatFunction(), 2)))

print("When converted to an int, the previously entered number to the power of 4 is " + str(power(intFunction(), 4)))
print("When converted to an int, the previously entered number to the power of 3 is " + str(power(intFunction(), 3)))
print("When converted to an int, the previously entered number to the power of 2 is " + str(power(intFunction(), 2)))