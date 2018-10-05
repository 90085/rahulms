import random
print("remember 1 s stone")
print("remember 2 s paper")
print("remember 3 s sizer")
c1=0
c2=0
#user input
def useinp():
	r=random.randint(1,3)
	return r
	

while True:
	r=useinp()
	x=int(input("what do u wanna throw"))
	if(x==1 and r==2):
		print("u loose bec stone win against paper")
		c1=c1+1
		print("computer win ",c1,"times")
	elif(x==2 and r==1):
		print("u win bec paper aginst stones")
		c2=c2+1
		print("u win ",c2," times")
	elif(x==1 and r==3):
		print("u win bec stone against sizer")
		c2=c2+1
		print("u win ",c2," times")
	elif(x==2 and r==3):
		print("u loose bec paper against sizer")
		c1=c1+1
		print("computer win ",c1," times")
	elif(x==3 and r==1):
		print("u loose bec sizer against stone")
		c1=c1+1
		print("computer win ",c1," times")
	elif(x==3 and r==2):
		print("u win bec sizer against paper")
		c2=c2+1
		print("u win ",c2," times")
	else:
		print("u and computer put same value so draw")
	if c1==3:
		print("computer won against u")
	if c2==3:
		print("u won against computer,have a great day")
		break
      
	
	
