
#-*- coding:utf-8 -*-
import xlwt
import json


def student_xls(txt):
    with open(txt) as f:
        content = f.read().decode('GBK')
    wb = xlwt.Workbook()
    table = wb.add_sheet('city')
    js = json.loads(content)
    i = 0
    for con in js:
        table.write(i, 0, con)
        table.write(i, 1, js.get(con))
        i += 1
    wb.save('city.xls')


if __name__ == '__main__':
    student_xls(r'd:\gakki\city.txt')

    
