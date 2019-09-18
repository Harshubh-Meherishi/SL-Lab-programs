#Create a python program that holds all the numbers and removes duplicates.
l1 = list()
def removedup(numbers):
	newlist=[]
	for number in numbers:
		if number not in newlist:
			newlist.append(int(number))

	print(newlist);	
	print("\n\nReversing the list")
	Reverse(newlist)

def Reverse(numbers):
	newlist=[]
	
	newlist = numbers[ ::-1]
	print(newlist)
	print("\n")
	numbers.reverse()
	print(numbers)
	
	
while True:
	x = input("Enter the list of numbers ( Enter any alphabet to stop )")
	if x.isalpha():
		break
	else:
		l1.append(int(x))
	
removedup(l1)



