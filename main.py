import csv
from tokenize import String

from Model.Database_Column import Database_Column
from Model.Database_Row import Database_Row

def add_row(row):
    data_columns = row.columns
    data_array = []
    for column in data_columns:
        data_array.append(column.column_name)
    table.append(data_array)

def table_header(columns):
    row_header = Database_Row(rows_count, columns)
    add_row(row_header)

def create_row(i, column_count):
    i = str(i)
    row_columns = []
    for j in range(column_count):
        if columns[j].column_type == "Int":
            column = Database_Column(i, "Int")
        else:
            column = Database_Column(columns[j].column_name+"_"+i , "String")
        row_columns.append(column)
    row = Database_Row(rows_count, row_columns)
    add_row(row)

def create_columns(column_count):
    for i in range(column_count):
        column_name = input("Column Name: ")
        column_type = input("Column Type:\n1. String  \n2. Integer\n:")
        if column_type == 1:
            column_type = "String"
        elif column_type == 2:
            column_type = "Int"
        else:
            column_type = "String"

        column = Database_Column(column_name, column_type)
        columns.append(column)
    table_header(columns)

table = []
rows_count = 0
columns = []

column_count = int(input("How many columns are in the table? "))
create_columns(column_count)

row_count = int(input("How many rows are in the table? "))
for i in range(row_count):
    rows_count += 1
    create_row(rows_count, column_count)

filename = "table.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(table)

print("Excel file created")