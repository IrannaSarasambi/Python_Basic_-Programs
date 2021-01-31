#program to read doc file and exract gmail id and  mobile number.

import docx2txt
import re

mytxt = docx2txt.process("iranna.docx")

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",mytxt)

mobnum = re.findall(r"\d\d\d\d\d\d\d\d\d\d",mytxt)
print("gmail id of person:")

for mail in emails:
    print(mail)
    
print("mobile number of person is :")

for num in mobnum:
    print(num)
