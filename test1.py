# -*- coding: utf-8 -*-



import time


print "欢迎来到Miss Python的秘密日记"
print '''
选择：
a.写给今天
b.回味过往
c.创造未来
'''

prompt = '>>>'
choice = raw_input(prompt)

if choice == "a":
    diary == raw_input('>>>')
    diaryFile.write('\n' + time.strftime('%Y/%m/%d')+ ' ' +diary)
    
                                               
elif choice == "b":                         
    diaryFile == open('diary.txt')
     == diaryFile.read()
    print(diary)

elif choice == "c":
    diaryFile.close()
                                         
else:
    print "您逗我呢？"
    
    write='y'
    while write=='y':
        diaryFile.write('\n' + time.strftime('%Y/%m/%d')+ ' ' +diary)

                             
diaryFile.close()
