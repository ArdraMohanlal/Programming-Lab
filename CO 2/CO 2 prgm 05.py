#5.display the given pyramid with step number acccepted from user
n=int(input("Enter the limit"))
for i in range (1, n+1):
    for j in range(1,i+1):
        a=i*j
        if a==0:
            continue
        else:
            print(a,end=" ")
    print("\n")