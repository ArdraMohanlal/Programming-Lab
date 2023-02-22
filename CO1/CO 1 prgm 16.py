"""16. Create a single string separated with space from two strings by swapping the 
 character at position1."""
a=str(input("Enter the first string"))
b=str(input("Enter the second string"))
print("Output is",b[0:1]+a[1:-1]+a[-1] , a[0:1]+b[1:-1]+b[-1])
