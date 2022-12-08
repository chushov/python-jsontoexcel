import openpyxl
import json


with open('json/activities_prod.json') as file:
    data = json.load(file)

book = openpyxl.Workbook()
sheet = book.active

sheet['A1'] = 'PARENTID'
sheet['B1'] = 'ID'
sheet['C1'] = 'NAME'
sheet['D1'] = 'ACTIVE'

row = 2
for activity in data:
    sheet[row][0].value = activity['parentId']
    sheet[row][1].value = activity['id']
    sheet[row][2].value = activity['name']
    sheet[row][3].value = activity['active']
    row += 1

book.save("xlsx/activities_jsontoexcel.xlsx")
book.close()