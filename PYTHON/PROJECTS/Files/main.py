import csv

file = open('python/projects/files/csv.csv', 'r')
b = csv.reader(file)
print(b)
a = list(b)
print(a[1])
