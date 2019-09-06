#demo: classes in python
#notice the use of "self". It is the first argument passed to any function

class Person:
	def __init__(self,name,age):
		self.name = name;
		self.age = age;

p1 = Person("Suppandi", 14)


print("\nName of person  is ",p1.name)
print("\nAge of person  is ",p1.age)

print("\n**** Printing after deleteing age attribute ***")
del p1.age
print("\nName of person  is ",p1.name)


del p1
#print("\nName of person  is ",p1.name)

