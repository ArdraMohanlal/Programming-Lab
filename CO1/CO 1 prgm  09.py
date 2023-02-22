"""9. Create a string from given string where first and last characters exchanged. [eg: python -
> nythop]"""
str1=str(input("Enter the string:"))
print("The output is:",str1[-1:] + str1[1:-1] + str1[:1])

