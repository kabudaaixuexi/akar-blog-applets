# coding=utf-8

# %d digit数字
# %s str字符串
# %f float浮点数
person = '我'
age = '年龄'
say = '爱'
num = 18.71429411
who = '祖国'
print('我'+'%s%s' % (say,who))
print(person + '%.4f' % num)
# format
message = '{}{}'.format(person,num)
print(message)
# input 
print('''
************************************
               捕鱼达人
************************************
''')
username = input('请输入名字：')
password = input('请输入密码：')
print('%s请充值才能加入游戏！' % username)
coins = input('请充值：')
print('%s充值成功，当前游戏币：%s' % (username,coins))