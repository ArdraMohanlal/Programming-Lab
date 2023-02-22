#4. Generate a list of four digit numbers in a given range with all their numbers even and the number is a perfect square.
from math import sqrt
x=int(input("Enter a limit"))
y=int(input("Enter the limit"))
for i in range(x,y):
    if sqrt(i)==int(sqrt(i)) and i%2==0:
        print(i)