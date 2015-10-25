# -*- coding: utf-8 -*-

print "欢迎来到Miss Python的秘密日记"
psw = 1234
guess = int(raw_input('暗号：'))

if guess == psw:
    print 'Welcome'
else:
    print '不是的，再想想'


from datetime import date
now = date.today()
now.strftime("%Y-%m-%d")

print "写给今天的我："
print now
prompt = ">>>"
diary = raw_input()

print now , diary

'''
def ecrire():
    now + diary

print ecrire
'''
