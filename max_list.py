integer=[]
n=int(input("How many integers you want to enter: "))

def max(integer):
    max=0
    for x in integer:
        if x>max:
            max=x
    return max


for x in range(1,n+1):
    print("enter integer ",x)
    integer.append(int(input()))    #taking input from user in a list.
print(max(integer))                 #calling function for calculation.
