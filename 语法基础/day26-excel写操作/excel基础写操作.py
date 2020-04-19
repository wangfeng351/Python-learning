"""
excel基础写操作
@Date 2020.04.19
"""
import xlsxwriter

# 1. 创建一个excel文件并作为当前工作波
workbook = xlsxwriter.Workbook('./语法基础/res/excel/demo.xlsx')
# 2. 添加一个工作波，默认名称是Sheet1,Sheet2等，可以指定名称
# 默认名称: Sheet1
worksheet1 = workbook.add_worksheet()
# 指定名称： Date
worksheet2 = workbook.add_worksheet('Data')
# 3、 写数据
# 向workshhet1 指定单元格写入内容
bg_format = workbook.add_format({'bold': True, 'font_name': u'微软雅黑', 'bg_color': '#217346',
                                    'align': 'center', 'valign': 'vcenter', 'font_color': '#282c34',
                                    'font_size': 11, 'border': 1})
worksheet1.write('A1', 'Hello world', bg_format)
# 向worksheet2写入一组数据并用公式求和
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50]
)
# 行和列的索引初值都为0
row = 0
col = 0
# 遍历数据并逐行写入
for item, cost in (expenses):
    worksheet2.write(row, col, item, bg_format)
    worksheet2.write(row, col+1, cost)
    row += 1
# 写一个公式，计算出综合
worksheet2.write(row, 0, 'Total')
worksheet2.write(row, 1, '=SUM(B1:B4)')

workbook.close()