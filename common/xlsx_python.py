import xlrd

# 打开excel文件读取数据
exce = xlrd.open_workbook('D:\PycharmProjects\python_study\excel_test.xlsx')

# 获取excel中对应的sheet
print('所有sheet名称：',exce.sheet_names())
# 获取所有sheets
sheets = exce.sheets()
# sheet = exce.sheets()[0]        # 也可以通过下标去访问某个具体的sheet
sheet1 = exce.sheet_by_name('Sheet1')       # 通过sheet名称获取
# sheet2 = exce.sheet_by_index(1)              # 通过下标获取某个sheet

# 获取sheet中行数和列数
nrows = sheet1.nrows
ncols = sheet1.ncols
print('对应sheet中行数：%d行，列数：%d列'% (nrows, ncols))

# 获取sheet中整行或整列的数据（数组）
row1 = sheet1.row_values(2)             # 通过下标获取某一行的数据
col1 = sheet1.col_values(0)             # 通过下标获取某一列的数据
print('第三行的数据：', row1)
print('第一列的数据：', col1)

# 获取sheet中某个单元格的数据
cell_C1 = sheet1.cell(2, 0).value       # 第三行第一列
cell_B2 = sheet1.cell(1,1).value        # 第二行第二列
cell_A3 = sheet1.cell(0,2).value        # 第一行第三列
print('第三行第一列', cell_C1)
print('第二行第二列', cell_B2)
print('第一行第三列', cell_A3)

# 获取单元格数据类型     --type：0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
cell_A1 = sheet1.cell(0,0).ctype
print(cell_A1)
print(sheet1.merged_cells)
merge = []
for row, row_range, col, col_range in sheet1.merged_cells:
    print(row, row_range, col, col_range )
    merge.append([row, col])
for index in merge:
    print("index:", index[0])
    print("测试:",sheet1.cell(index[0],index[1]).value)

'''
    在打印整行数据和整列数据的时候，合并的单元格，只会在合并的第一行或者第一列会有数据，之后打印出来都是空白。另外打印的日期时间也是错误的。
    先看合并单元格，这个没有任何技巧。只能获取合并行单元格读取行的第一个索引，合并列单元格读取列的第一个索引。这样才能读到值，读错了就是空值。
    但是合并单元格可能是读到空值，excel本身也可能就存在空值。要怎么获取单元格所谓的‘第一行或列的索引的’，这需要事先知道哪些单元格是合并的。
'''
# cell_G1 = sheet1.cell(6,0).value
# cell_H1 = sheet1.cell(7,0).value
#
# print(cell_G1)
# print(cell_H1)
# print("输出结束啦")

#处理单元格内容为data格式的数据
print(xlrd.xldate_as_datetime(sheet1.cell(2,2).value,0))    #转换成日期格式
print(xlrd.xldate_as_tuple(sheet1.cell(2,2).value,0))   #返回元组




