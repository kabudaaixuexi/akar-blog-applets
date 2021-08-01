from wsgiref.simple_server import make_server  
from jinja2 import Template  
  
  
def index(url):  
    # 读取HTML文件内容  
    with open("index2.html", "r", encoding="utf8") as f:  
        data = f.read()  
        template = Template(data)   # 生成模板文件  
        ret = template.render({'name': 'alex', 'hobby_list': ['抽烟', '喝酒', '烫头']})   # 把数据填充到模板中  
    return bytes(ret, encoding="utf8")  
  
  
def home(url):
    with open("home.html", "r", encoding="utf8") as f:
        s = f.read()
    return bytes(s, encoding="utf8")


# 定义一个url和实际要执行的函数的对应关系  
list1 = [  
    ("/index/", index),  
]
  
  
def run_server(environ, start_response):  
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ])  # 设置HTTP响应的状态码和头信息  
    url = environ['PATH_INFO']  # 取到用户输入的url  
    func = None  
    for i in list1:  
        if i[0] == url:  
            func = i[1]  
            break  
    if func:  
        response = func(url)  
    else:  
        response = b"404 not found!"  
    return [response, ]  
  
  
if __name__ == '__main__':  
    httpd = make_server('127.0.0.1', 8090, run_server)  
    print("我在8090等你哦...")  
    httpd.serve_forever() 