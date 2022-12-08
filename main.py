import openpyxl
import json


with open('/json/activities.json') as file:
    data = json.load(file)

book = openpyxl.Workbook()
sheet = book.active

sheet['A1'] = 'ID'
sheet['B1'] = 'CITY'
sheet['C1'] = 'NUM'

row = 2
for ssssssample in data['activities']:
    sheet[row][0].value = ssssssample['id']
    sheet[row][1].value = ssssssample['city']
    sheet[row][2].value = ssssssample['num']
    # sheet[row][3].value = ' '.join(ssssssample['num'])
    # etc
    row += 1

book.save("/xlsx/jsontoexcelexport.xlsx")
book.close()
