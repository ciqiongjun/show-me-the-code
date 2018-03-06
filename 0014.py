#-*- coding:utf-8 -*-
import xlwt
import json


def student_xls(txt):
    with open(txt) as f:
        content = f.read().decode('GBK')
    wb = xlwt.Workbook()
    table = wb.add_sheet('student')
    js = json.loads(content)
    i = 0
    for con in js:
        values = js.get(con)
        table.write(i,0,con)
        j = 1
        for value in values:
            table.write(i,j,value)
            j += 1
        i += 1
    wb.save('stu.xls')


if __name__ == '__main__':
    student_xls(r'd:\gakki\student.txt')