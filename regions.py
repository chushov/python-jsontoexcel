import openpyxl
import json


with open('json/regions.json') as file:
    data = json.load(file)

book = openpyxl.Workbook()
sheet = book.active

sheet['A1'] = 'OKTMO'
sheet['B1'] = 'NAME'

row = 2
for activity in data:
    sheet[row][0].value = activity['oktmo']
    sheet[row][1].value = activity['name']
    row += 1

book.save("xlsx/regions_jsontoexcel.xlsx")
book.close()