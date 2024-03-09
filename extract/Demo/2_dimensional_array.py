row_num = int(input("Input row number: "))
column_number = int(input("Input column number: "))
multi_list = [[0 for col in range(column_number)] for row in range(row_num)]

for row in range(row_num):
    for col in range(column_number):
        multi_list[row][col] = row * col


print(multi_list)