#-*- coding:utf-8 -*-
import xlwt
import json


def student_xls(txt):
    with open(txt) as f:
        content = f.read()
    wb = xlwt.Workbook()
    table = wb.add_sheet('numbers')
    js = json.loads(content)
    i = 0
    for con in js:
        j = 0
        for item in con:
            table.write(i,j,item)
            j += 1
        i += 1
    wb.save('numbers.xls')


if __name__ == '__main__':
    student_xls(r'd:\gakki\numbers.txt')

    
