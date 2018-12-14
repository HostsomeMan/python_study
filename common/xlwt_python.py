import xlwt
import datetime

# 初始化一个excel
excel = xlwt.Workbook(encoding='utf-8')
# 新建一个sheet
sheet = excel.add_sheet('xlwt_sheet1')
# 设置样式
style = xlwt.XFStyle()  # 初始化样式
style1 = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 创建字体
font.name = u'微软雅黑'  # 字体类型
font.colour_index = 3  # 字体颜色
font.underline = True  # 下划线
font.italic = True  # 斜体
font.height = 400  # 字体大小   200等于excel字体大小中的10
style.font = font  # 设定样式

# sheet.write(0, 0, 'test')  # 写入不带字体样式的内容
# sheet.write(1, 0, 'test', style)  # 写入带字体样式的内容
# style1.num_format_str = 'M/D/YY'
# sheet.write(2, 0, datetime.datetime.now(), style1)
# 合并单元格
sheet.write_merge(0,2,0,0,'ceshi')
sheet.write_merge(0,0,1,2,'yixia')
excel.save('E:/test_xlwt1.xls')