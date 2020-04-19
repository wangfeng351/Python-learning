"""
excel格式化写操作
@Date 2020.04.19
"""
from datetime import datetime
import xlsxwriter
import xlrd

def set_format():
    workbook = xlsxwriter.Workbook('./语法基础/res/excel/demo.xlsx')
    worksheet = workbook.add_worksheet()
    # 基础格式
    fmt = workbook.add_format(
        {"font_name": u"微软雅黑", 'font_size': 10})
    # 背景格式： 定义字体、对齐方式，背景前景色等
    # # 金额格式
    # money_format = workbook.add_format({'num_format': '$#,##0'})
    # # 日期格式
    # date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
    # # 设置行高，从第0行开始，行高为20， 格式为fmt
    # worksheet.set_row(0, 20, fmt)
    # # 设置列宽，从A列到c列，列宽为20，格式为fmt
    # worksheet.set_column('A:C', 20, fmt)
    # # 用指定背景格式写入表头
    # worksheet.write('A1', 'Item', bg_format)
    # worksheet.write('B1', 'Date', bg_format)
    # worksheet.write('C1', 'Cost', bg_format)
    
    row = 1
    col = 0
    workbook1 = xlrd.open_workbook('./语法基础/res/excel/班级卡片数据.xlsx')
    # 读取第一个sheet
    sheet1 = workbook1.sheet_by_index(0)
    list = sheet1.row_values(0)
    # 填写表头
    for ls in list:
        worksheet.write(0, col, ls)
        col+=1
    col = 0
    # 获取行长度
    len1 = len(sheet1.col_values(1))
    while(row < len1):
        expenses = sheet1.row_values(row)
        bg_format = workbook.add_format({'bold': True, 'font_name': u'微软雅黑', 'bg_color': expenses[14],
                                    'align': 'center', 'valign': 'vcenter', 'font_color': '#282c34',
                                    'font_size': 11, 'border': 1})
        # 遍历数据，用不同格式写入
        for item in expenses:
            worksheet.write(row, col, item, bg_format)
            col += 1
            # date = datetime.strptime(data_str, '%Y-%m-%d')
            # worksheet.write_string(row, col, item)
            # worksheet.write_datetime(row, col + 1, date, date_format)
            # worksheet.write_number(row, col + 2, cost, money_format)
        row += 1
        col = 0
    workbook.close()

if __name__ == '__main__':
    set_format()
