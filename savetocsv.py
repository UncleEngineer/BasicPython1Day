import csv

def savetocsv(data=['Coffee','Drink',50]):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

d = ['Milk','Drink',60]

savetocsv(d)
