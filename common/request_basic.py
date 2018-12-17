import requests
import json
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

base_url='http://httpbin.org/'

# r=requests.get(base_url+'get')
# print(r.status_code)
#
# r=requests.post(base_url+"post")
# print(r.status_code)
#
# r=requests.put(base_url+'put')
# print(r.status_code)
#
# r=requests.delete(base_url+'delete')
# print(r.status_code)

# 参数传递
# GET请求
# param_data={'user':'zxw','password':'6666'}
# r=requests.get(base_url+'get', params=param_data)
# print(r.url)
# print(r.status_code)

# POST请求
# form_data={'user':'51zxw','password':'8888'}
# r=requests.post(base_url+'post',data=form_data)
# print(r.text)

# 请求头定制
# form_data={'user':'51zxw','password':'8888'}
# header={'user-agent':'Mozilla/5.0'}
# r=requests.post(base_url+'post',data=form_data,headers=header)
# print(r.text)
# print(r.json()) # json格式输出

# 知乎网站有反爬虫机制，若不加请求头，则无法获取其资源
# header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
# r=requests.get('https://www.zhihu.com/explore',headers=header)
# print(r.headers)
# print(r.text)

# Cookie设置
# cookie={'user':'51zxw'}
# r=requests.get(base_url+'cookies',cookies=cookie)
# print(r.text)

# 获取cookie
# r=requests.get('http://www.baidu.com')
# print(r.cookies)
# print(type(r.cookies))
# for key,value in r.cookies.items():
#     print(key+":"+value)

# 超时
# cookie={'user':'51zxw'}
# r=requests.get(base_url+'cookies',cookies=cookie,timeout=3)
# print(r.text)

# 文件上传
# file={'file':open('文件名称','rb')}
# r=requests.post(base_url+'post',files=file)
# print(r.text)

# 设置cookie值
# r=requests.get(base_url+'cookies/set/user/51zxw')
# print(r.text)
# 打印cookie值,结果中是没有cookie值得
# r=requests.get(base_url+'cookies')
# print(r.text)

# session会话对象
# s=requests.session()
# r=s.get(base_url+'cookies/set/user/51zxw')
# print(r.text)
#
# r=s.get(base_url+'cookies')
# print(r.text)

# SSL证书验证
# 12306默认开启证书验证,关闭SSL验证：verify=False
# r=requests.get('https://www.12306.cn')
# print(r.text)

# 代理（proxy）设置（去www.xicidaili.com获取IP端口
# proxies={'http':'http://121.31.195.224:8123'}
# r=requests.get(base_url+'get',proxies=proxies)
# print(r.text)

# 身份认证，BasicAuth和digestAuth
# r=requests.get(base_url+'basic-auth/zxw/8888',auth=HTTPBasicAuth('zxw','88886'))
# print(r.text)
# print(r.status_code)
# r=requests.get(base_url+'digest-auth/auth/zxws/666',auth=HTTPDigestAuth('zxws','6666'))
# print(r.text)
# print(r.status_code)

# 流式请求
# 有一些接口返回值比较特殊，不是单纯返回一个结果，而是多个结果，比如某个查看接口，返回值为排行榜前10的商品信息。
# r=requests.get(base_url+'stream/10',stream=True)
# # 如果响应内容未设置编码，默认设置为utf-8
# if r.encoding is None:
#     r.encoding='utf-8'
#
# # 对响应结果进行处理
# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         data = json.loads(line)
#         print(data['id'])

# 重定向和请求历史
# r = requests.get('http://github.com')
# print("请求地址：", r.url)
# print("状态码：", r.status_code)
# # print("内容：", r.text)
# print("请求头：", r.headers)
# print("历史：", r.history)

# print("==================================================================================================")

# 限制重定向
# r = requests.get('http://github.com', allow_redirects=False)
# print("请求地址：", r.url)
# print("状态码：", r.status_code)
# # print("内容：", r.text)
# print("请求头：", r.headers)
# print("历史：", r.history)
#
# print("==================================================================================================")
#
# 当使用head请求的时候，默认不启用重定向的，其他请求是默认使用重定向的
# r = requests.head('http://github.com')
# print("请求地址：", r.url)
# print("状态码：", r.status_code)
# # print("内容：", r.text)
# print("请求头：", r.headers)
# print("历史：", r.history)
#
# print("==================================================================================================")
#
# r = requests.head('http://github.com', allow_redirects=True)
# print("请求地址：", r.url)
# print("状态码：", r.status_code)
# # print("内容：", r.text)
# print("请求头：", r.headers)
# print("历史：", r.history)

# 文件下载
# 默认情况下，使用requests库在进行请求，响应体是会被立即下载的，所以需要使用stream这个参数覆盖这个行为，
# 然后content来下载这个被推迟的响应体，如果不使用stream参数，是下载不到东西，肯定是空的
# url = 'http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png'
# path = 'E:/test.jpg'
# r = requests.get(url, stream = True)
# print(r.status_code)
# with open(path,'wb') as f:
#     f.write(r.content)

# 会话对象session
# s = requests.session()
# s.auth = ('1136702931@qq.com', 'jiang0827.')
#
# url1 = 'https://api.github.com/user'
# url2 = 'https://api.github.com/user/emails'
#
# r1 = s.get(url1)
# print(r1.status_code)
# print(r1.text)
#
# r2 = s.get(url2)
# print(r2.status_code)
# print(r2.text)

s=requests.Session()
# 设置session对象的auth属性，用来作为请求的默认参数
# s.auth=('user','pass')
# 设置session的headers属性，通过update方法，将其余请求方法中的headers属性合并起来作为最终的请求方法的headers
# s.headers.update({'x-text':'true'})
# 发送请求，这里没有设置auth会默认使用session对象的auth属性，这里的headers属性会与session对象的headers属性合并,如果想取消session的某个参数，可以在传递一个相同key，value为None的dict
# r=s.get('http://httpbin.org/headers',headers={'x-text1':'true'}) #如果设置相同的'x-text'则会覆盖上面设置的header
# print(r.text)


# 会话还可以用作前后文管理器，保证with 区块退出后会话能被关闭
# with requests.Session() as s:
#     s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
