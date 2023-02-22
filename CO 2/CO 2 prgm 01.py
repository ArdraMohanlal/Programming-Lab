"""# programme to find factorial of a number
num=int(input("Enter the number"))
factorial=1
if num<0:
    print("Given number is negative and hence no factorial exist")
elif num==0:
    print("No factorial")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("The factorial of",num,"is",factorial)"""

# ANOTHER METHOD
def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x * calc_factorial(x-1))
num=int(input("Enter the number"))
print("The factorial of the",num,"is",calc_factorial(num))