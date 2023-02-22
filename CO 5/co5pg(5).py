"""Write a python program to write a python dictionary to a scv file.
After writing the  CSV file read the CSV file and display the content"""
import csv
cars=[{'No':1,'Company':'Ferrari','Model':'F128GC'},{'No':2,'Company':'Suzuki','Model':'F444GD'},{'No':3,'Company':'TATA','Model':'F3456BGC'}]
csvfile=open("Names.csv",'w')
field_names=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(cars)
csvfile.close()
csv_file=open("Names.csv",'r')
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print(line,end="")
csv_file.close()
