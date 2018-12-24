import json


'''
    将python对象编码成json字符串
'''
data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
print(type(data))
jsons = json.dumps(data)
print(type(jsons))

# 注意这里必须是双引号
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
print(type(jsonData))
text = json.loads(jsonData)
print(type(text))

# 再次尝试push，做了更改哦
