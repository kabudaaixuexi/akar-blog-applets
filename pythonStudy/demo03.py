#coding=utf-8

name = 123
num = name*1234
print(id(name),name)
print(id(num),num)
print(num == name,end='')
print('''
   亲爱的： 祖国
      我爱你
      
          -- 周鹏
''',end='')
name = input('please enter your name')
myname = 'jack'
print('hello %s i`m %s' % (name,myname))

list = ['jack','pick','lick','keke']
list.append('coke')
list.insert(0,'mack')
print(list)
list.pop(2)
print(list)

