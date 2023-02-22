#Generate Fibonacci series of N term
n=int(input("enter a number "))
i=0
j=1
print(i)
print(j)
for x in range(2,n):
    sum=i+j
    i=j
    j=sum
    print(sum)