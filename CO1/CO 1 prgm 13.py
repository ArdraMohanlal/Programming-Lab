"""13. Create a list of colors from comma-separated color names entered by user. Display 
 first and last colors."""
colors=str(input("Please enter the color names"))
str=colors.split(",")
print("The list of required colors are:",(str[0:1]+str[-1:]))