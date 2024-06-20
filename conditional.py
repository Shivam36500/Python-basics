#age = int(input("Enter age:"))
#if age>=18:
 #   print("Eligible to vote")
#else:
 #   print("Not Eligible")
a = int(input("Enter first value: "))
b = int(input("Enter Second value: "))
c = int(input("Enter third value: "))

if (a>b and a>c):
    print(a,"is big")
elif(b>a and b>c):
    print(b,"is big")
else:
    print(c,"is big")         