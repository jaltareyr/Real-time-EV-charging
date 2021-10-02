import json
import pandas as pd
import xlsxwriter

file = open('ev_data.json')
data = json.load(file)

workbook = xlsxwriter.Workbook('ev_data.xlsx')
worksheet = workbook.add_worksheet('sheet')
row=1
worksheet.write(0,0,'connectionTime')
worksheet.write(0,1,'disconnectTime')
worksheet.write(0,2,'doneChargingTime')
worksheet.write(0,3,'kWhDelivered')
worksheet.write(0,4,'userID')
for item in data['_items']:

    worksheet.write(row,  0 , item['connectionTime'])
    worksheet.write(row , 1 , item['disconnectTime'])
    worksheet.write(row , 2 , item['doneChargingTime'])
    worksheet.write(row , 3 , item['kWhDelivered'])
    worksheet.write(row , 4 , item['userID'])

    row+=1
workbook.close()





