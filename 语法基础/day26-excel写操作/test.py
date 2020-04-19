import xlsxwriter
import xlrd

workbook = xlrd.open_workbook('./语法基础/res/excel/班级卡片数据.xlsx')
sheet1 = workbook.sheet_by_index(0)
list = sheet1.col_values(1)
print(len(list))