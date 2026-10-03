while True:
	num1 = float(input("first number: "))

	operator = input("Enter operator: ")
	num2 = float(input("Second number: "))

	if operator == "+":
		result = num1 + num2
	elif operator == "-":
		result = num1 - num2
	elif operator == "*":
		result = num1 * num2
	elif operator == "/":
		result = num1 / num2
	else:
		print("Invalid operator")
	print("result:",result)
	y_n = input("Do you want to continue? (y/n): ").lower()
	if y_n != "y":
		break