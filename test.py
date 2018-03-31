# class Node:
#
#     def __init__(self,x=[]):
#         self.x=x
#
#
# node = []
# for i in range(3):
#     node.append(Node())
#
# for i in range(3):
#     node[0].x.append(1)
#
# for i in node:
#     print(i.x)

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# filepath='data.xls'
# df = pd.read_excel(filepath , usecols="A")

# print("Column headings:")
# print(df.head().__len__())

def readExel(exelname):
    import xlrd

    ExcelFileName= exelname
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name("Data")

    num_rows = worksheet.nrows  #Number of Rows
    num_cols = worksheet.ncols  #Number of Columns

    result_data =[]
    for curr_row in range(2,num_rows): # read except header
        row_data = []

        for curr_col in range(1, num_cols): # read except ID
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            # print(data)
            row_data.append(data)

        result_data.append(row_data)
    print("read done")
    # print(result_data[0].__len__())
    return result_data

def preprocess():
    return

data=readExel('Data.xls')
ans=[]

for i in data :
    ans.append(int(i.pop(i.__len__()-1)))

lmax=max(data)
lmin=min(data)

print(lmax)
print(lmin)