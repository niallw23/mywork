# Lab Work from Week 11
# Looked at the module pandas
# Already helpful for some project work

import pandas as pd

listdata = [
    ['John', 'Math', 23],
    ['John', 'Programming', 66],
    ['Mary', 'Math', 45],
    ['Mary', 'Programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'Programming', 70],
    ['Mark', 'Math', 73],
    ['John', 'Programming', 61]
]

df = pd.DataFrame(listdata, columns = ['Name', 'Subject', 'Grade'])
print (df.head(3))

print(df.describe())
print(type(df.describe()))

path = r'C:\Users\nwynn\Documents\pands\mywork\Week 11'
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)

excelFilename = path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='Data')





