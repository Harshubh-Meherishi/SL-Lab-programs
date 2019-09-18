list1 = list()
list2 = list()
def CeltoFar(celsius):
	fahrenheit = (celsius * 1.8) + 32
	print(fahrenheit," degree fahrenheit ")
	list1.append((float(celsius), fahrenheit))
	
def FartoCel(fahrenheit):
	celsius = (fahrenheit - 32) / 1.8
	print(celsius, "degree celsius")
	list2.append((float(fahrenheit), celsius))
	
while True:
	print("************************WELCOME TO THE TEMPERATURE CONVERTER***********************")
	print("Enter your choice\n")
	print("1) Celsius to Fahrenheit")
	print("2) Fahrenheit to Celsius")
	print("3) View all conversions done of (1)")
	print("4) View all conversions done of (2)")
	print("Enter N to exit")
	ch = input("(1 / 2 /3 / 4): ")
	if (ch.isalpha()):
		break
	if(ch == 1):
		num = input("Enter the Celsius value: ")
		CeltoFar(num)
	if(ch == 2):
		num = input("Enter the Fahrenheit value: ")
		FartoCel(num)
	if(ch == 3):
		print(list1)
	if(ch == 4):
		print(list2)
	en = input("Do you wish to continue?(Y/N)")
	if(en ==("Y")):
		continue
	else:
		break

