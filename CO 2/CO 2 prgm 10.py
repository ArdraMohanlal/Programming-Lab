#10. Generate all factors of a number.
n=int(input("Enter a number"))
print("factors of n")
for i in range (1,n+1):
    if n%i==0:
        print(i)    