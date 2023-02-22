#Write a python program to read specific columns of a given CSV file and print thr contents of the column.
"""import pandas as p
stdfile=p.read_csv("studentdetails.csv",usecols=["Name","address"])
print("Student name and address:")
print(stdfile)"""
import pandas as p
stdfile=p.read_csv("studentdetails.csv")
spec_cols=stdfile[["Name","address"]]
print("Student name and address:")
print(spec_cols)