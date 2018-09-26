#what do u want 
i=int(input("enter the value of i"))
j=int(input("enter the value fo j"))
o=input("what do u want? +,-,*,/:")
def add():
	return i+j
def sub():
	return i-j
def mult():
	return i*j
def div():
	return i/j


if(o=="+"):
	print(add())
elif(o=="-"):
	print(sub())
elif(o=="*"):
	print(mult())
elif(o=="/"):
	print(div())
else:
	print("give only +,-,*,/ ")
