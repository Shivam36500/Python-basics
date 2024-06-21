integer=[]
n=int(input("How many integers you want to enter: "))

def logic(integer):
    sum=0
    for x in integer:
        if x%2==0:
            sum=sum+x
        else:
            return 0
    return sum


for x in range(1,n+1):
    print("enter integer ",x)
    integer.append(int(input()))    #taking input from user in a list.
print(logic(integer))               #calling function for calculation.