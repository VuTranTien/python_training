# import xlwt,xlrd,openpyxl
# from xlutils import copy
# from xlutils.margins import number_of_good_rows
# username="vanC"
# filePath=r"F:\Source code\python _PR\QuanLyThuVien_vs1\Data\receipt\receipt_vanC.xls"
# rb=xlrd.open_workbook(filePath)
# view_sheet=rb.sheet_by_index(0)
# print(view_sheet.cell_value(0,3))
# wb=copy.copy(rb)
# sheet=wb.get_sheet(0)
# print("Hello")
# # sheet.write(0,1,'Hello!')
# wb.save(filePath)

import pandas as pd
temp=pd.read(r'C:\Users\MyPC\Desktop\Self-study Schedule.xls')
print(temp)