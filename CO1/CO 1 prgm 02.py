#2. Display future leap years from current year to a final year entered by user.
y=int(input("Enter the year"))
x=int(2022)
for i in range(x,y):
    if i%4==0 and i%100!=0:
        print(i)