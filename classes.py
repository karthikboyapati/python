#create a class
class Student():
	pass

#create objects
karthik = Student()
pavan = Student()
#create attributes for the class
karthik.Name = 'Karthik'
karthik.ID = 420
pavan.Name = 'Pavan'
pavan.ID = 421
print("Hi there!! Find the details of the Students entered here. Enter the number: ")
a = int(input())
b = input()
#print them here
if ( a == 1):
	print(karthik.Name)
	print(karthik.ID)

if (a == 2):
	print(pavan.Name)
	print(pavan.ID)
else:
	print("Entered number is wrong!! Please try again")
