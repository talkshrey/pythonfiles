age = int(input("enter your age"))
print("your age is",age)

#normal elif format
if age >= 21 :
	print("you can vote and drink")
elif age >= 18 :
    print("you can vote but cannot drink")
elif age <= 18 :
    print("you cannot vote and drink")
else :
    print("you cannot drink nor vote")

s = 0
#ifelse standard format
if s==0:
    r = True
else:
    r = False

#ifelse one liner
r = True if(s==0) else False


