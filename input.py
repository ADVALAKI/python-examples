def add(value1, value2):
	total = value1 + value2
	choise_str = "Addition"
	return total, choise_str

def division(value1, value2):
	total = value1 / value2
	choise_str = "Division"
	return total, choise_str
	
value1 = float(input("Enter first value1: "))
value2 = float(input("Enter first value2: "))
print("1. For Addition \n 2. For Subtraction \n 3. For Multiplication \n 4. For Division")

choise = int(input("Enter your chose:"))

total = 0
choise_str = ''
if choise == 1:
	total, choise_str = add(value1, value2)
elif choise == 2:
	total = value1 - value2
	choise_str = "Subtraction"
elif choise == 3:
	total = value1 * value2
	choise_str = "Multiplication"
elif choise == 4:
	total, choise_str = division(value1, value2)
	
else:
	print("Invalid choise")

print(f"{choise_str} of both value {value1} and {value2} is: {total}")



