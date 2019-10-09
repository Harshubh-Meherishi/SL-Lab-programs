list1 = [12,24,35,70,88,120,155,261]
newlist=list()
newlist = [i for i in list1 if (i%2 != 0)]
print(newlist)
for i in newlist:
	if( i%5 == 0):
		print("element ",i," is divisible by 5")
	elif( i%7 == 0):
		print("element ",i," is divisible by 5")
	else:
		print("element ",i," is not divisible by 5 or 7")
	
