# -*- coding: utf-8 -*-
#!/usr/bin/python
# Filename : check.py

print "欢迎来到Miss Python的秘密日记"
import getpass
password = getpass.getpass('创建一个暗号: ')

# pwd check
import password
import sys
def main():
    print '\n你已进入密码管控区\n'
    user_input = raw_input('输入密码: ')
    if user_input != password:
	sys.exit('密码错误，Adios! \n')
    print 'Welcome!\n'
	
if __name__ == "__main__":
	main()


