#program to write date in excelsheet

import xlsxwriter as xl

w = xl.Workbook("C:\\Users\\Desktop\\all_xl_file\\gamilAndnumber.xlsx")
w1 = w.add_worksheet('gmailpnumber')
w1.write("A1","Resume name")
w1.write("B1","Gmail Id")
w1.write("C1", "Mobile Number")
allresume = ['aa','bb','cc']
allgmail = ['aa@com','bb@com','cc@com']
allnumber = ['22','33','44']

for i in range(1,len(allgmail)+1):
    w1.write(i, 0, allresume[i-1])
    w1.write(i, 1, allgmail[i-1])
    w1.write(i, 2, allnumber[i-1])
w.close()
