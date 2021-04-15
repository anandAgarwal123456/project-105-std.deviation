import pandas as pd
import csv
import math

with open('data.csv', newline='') as f:
    data_a = csv.reader(f)
    data = list(data_a)

totalMarks = 0
totalEntries = len(data_a)

for marks in marksData:
    totalMarks = totalMarks + float(marks[1])

mean = totalMarks/totalEntries
print(mean)

square=[]

for marks in marksData:
    num = float(marks[1])
    num = num**2
    square.append(num)

sum_of_numbers = 0

for marks in square:
    sum_of_numbers = sum_of_numbers + 1

number = sum_of_numbers/(totalEntries-1)

deviation = math.sqrt(number)

print(deviation)