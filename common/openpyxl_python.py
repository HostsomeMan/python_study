#-*-coding:utf-8-*-

'''
· font(字体类)：字号、字体颜色、下划线等

· fill(填充类)：颜色等

· border(边框类)：设置单元格边框

· alignment(位置类)：对齐方式

· number_format(格式类)：数据格式

· protection(保护类)：写保护

'''

from openpyxl import Workbook
from openpyxl import worksheet

import _datetime
import time
import os

# # 创建文件对象
wb = Workbook()

# # 获取第一个sheet
# ws = wb.active
#
# # 写入数字
# ws['A1'] = 43
# ws['A2'] = '测试'
#
# # 写入一个当前时间
# ws['A3'] = _datetime.datetime.now()
# # 写入一个自定义的时间格式
# ws['A4'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# wb.save('E:/EXCEL_TEST.xlsx')

# 写入多个单元格

# 创建sheet
ws1 = wb.create_sheet("Mysheet")        # 创建一个sheet
ws1.title = "New Title"                 # 设定一个sheet的名字
ws2 = wb.create_sheet("Mysheet", 0)     # 设定sheet的插入位置，默认插在后面
ws2.title = u"你好"                       # 设定一个sheet的名字，必须是Unicode

# 获取全部sheet的名字，病例sheet名字
print(wb.sheetnames)
for sheet_name in wb.sheetnames:
    print(sheet_name)

print("*"*5)

for sheet in wb:
    print(sheet.title)

# 复制一个sheet
wb["New Title"]["A1"] = "zeke"
source = wb["New Title"]
target = wb.copy_worksheet(source)

wb.save("e:\\sample.xlsx")
