def calculate_sum(numList):
	sum = 0
	for number in numList:
		sum += number
	return sum

numList = [10,40,60,90]

#call the methos for sum
result = calculate_sum(numList)

print("The sum of all the elements is: " + str(result))