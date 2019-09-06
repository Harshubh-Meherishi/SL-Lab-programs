#demo: classes in python
#notice the use of "self". It is the first argument passed to any function

class Person:
	def __init__(self,name,age):
		self.name = name;
		self.age = age;

p1 = Person("Suppandi", 14)
p2 = Person("Ramu", 12)

print("\nName of person #1 is ",p1.name)
print("\nAge of person #1 is ",p1.age)

print("\nName of person #2 is ",p2.name)
print("\nAge of person #2 is ",p2.age)

p2.age=10

print("\nThe Modified Age of person #2 is ",p2.age)
