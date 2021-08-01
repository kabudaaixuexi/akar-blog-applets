import socket

sk = socket.socket()

sk.bind(('127.0.0.1',8000))

sk.listen()


class container():
    def __init__(self):
        self.h = '您好，'
        self.t = '欢迎访问'
    def welIndex(self,url):
        return ('%s %s %s' % (self.h,self.t,url))
    def welList(self,url):
        return 
    def welTest(self,url):
        return ('%s %s %s' % (self.h,self.t,url))
    def welReal(self,url):
        return ('%s %s %s' % (self.h,self.t,url))
    def home_H(self,url):
        with open('./index.html','r',encoding='utf-8') as f:
            ret = f.read()
            return ret
    def acvy_H(self,url):
        with open('./index.html','r',encoding='utf-8') as f:
            ret = f.read()
            return ret.replace('@@name@@','acvytest')

C = container()
list = [
    ('/',C.welIndex),
    ('/test', C.welTest),
    ('/list', C.welList),
    ('/real', C.welReal),
    ('/home', C.home_H),
    ('/acvy', C.acvy_H),
]
while True:

    conn,addr = sk.accept()  # 建立链接
    # 接收数据
    data = conn.recv(2048).decode('utf-8')
    url = data.split()[1]
    print(url)
    # 返回数据
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
    func = None
    for i in list:
        if url == i[0]:
            func = i[1]
            break;
    if func:
        # 路径匹配
        ret = func(url)
    else:
        ret = '404 not found'
    conn.send(ret.encode('utf-8'))
    # 断开连接
    conn.close()