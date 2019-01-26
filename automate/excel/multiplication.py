import openpyxl
import os

wb=openpyxl.Workbook()
ws=wb.create_sheet('table')

for i in range (1,7):
    for j in range(1,7):
        if j==1:
            ws.cell(row=i,column=j).value=i*j
            ws.cell(row=i,column=j).font=Font(bold=True)
        ws.cell(row=i+1,column=j+1).value=i*j

wb.save('multiplication.xlsx')