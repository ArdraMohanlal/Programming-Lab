#17. Sort dictionary in ascending and descending order.
dic = {"Bob":23,"Charlie":36,"Alice":72,"Eric":18,"David":9}
s=sorted(dic.items())
print("Ascending order is:",s)
s1=sorted(dic.items(),reverse=True)
print("Descending order is:",s1)