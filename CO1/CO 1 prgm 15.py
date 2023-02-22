#15. Print out all colors from color-list1 not contained in color-list2.
colorlist1 = ["WHITE","PURPLE","BLACK","RED","BLUE",]
colorlist2 = ["RED","YELLOW","GREEN","LAVENDER"]
list=[x for x in colorlist1 if x not in colorlist2]
print("The colours are:",list)

 