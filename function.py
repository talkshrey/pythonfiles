#function definition
def multi(a,b):
	print("your function multiplies two numbers given by you:")
	print(a * b)

def mod(x,y):
	print("returns remainder of 2 numbers:")
	return x%y

multi(78,43)
print(mod(100,3))

def nature():
	"""
	Function docstring
	-------------------
	returns the type of value the user has entered
	"""
	a = type(input("enter anything:\t"))
	return a

print("the type of value you entered is: ",nature())

help(nature)