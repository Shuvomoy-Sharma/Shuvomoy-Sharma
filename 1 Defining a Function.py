#Defining a Function
#we use funtion for reuseable our code and better performence for
#applications or saving our time
# at first we creat a function
#Example without argument
def printmsg():
	print("hello world")

printmsg()
#output: hello world

#Example with arguments
def printname(name):
	print("My name is " + name)

printname("Pritam")
#output: My name isPritam
printname("Victor")

#Example with 2 arguments
def nameHobby(name, hobby):
	print("my name is "+name + "and my hobby is " +hobby)

nameHobby("Pritam","Gyming")
#my name is Pritamand my hobby isGyming
nameHobby("Victor","reading")
#my name is Victorand my hobby isreading

def add(v1,v2):
	print(v1+v2)
add(10,12)
#output:22
add(22,44)
#output:66