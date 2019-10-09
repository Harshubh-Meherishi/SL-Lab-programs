def func(string):
	count1 = 0
	count2 = 0
	for i in string:
		if(i.islower()):
			count1 = count1+1
		if(i.isupper()):
			count2 = count2 +1
	print("\nThe Number of lowercase characters are: ",count1)
	print("\nThe Number of uppercase caharacters are: ",count2)
	print("\nThe reversed string is: ", string[ ::-1])
	print("\nThe length of the string is", len(string))
	
st1 = input("Enter the string")
func(st1)
