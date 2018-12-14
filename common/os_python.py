import os
import time
# file_path = os.getcwd()                 # 获取文件当前路径
# print("当前文件路径：",file_path)
# print('返回文件名：',os.path.basename(file_path))  # 返回文件名
# print("返回目录路径：",os.path.dirname(file_path))  # 返回目录路径
# print("分割文件名与路径：",os.path.split(file_path))  # 分割文件名与路径
# print("将目录和文件名合成一个路径：",os.path.join('root', 'test', 'runoob.txt'))  # 将目录和文件名合成一个路径
# print("返回指定目录下的所有文件：",os.listdir())

# all_log_path = os.path.join(os.path.dirname(os.getcwd()), 'Logs/All_Logs.log')
# error_log_path = os.path.join(os.path.dirname(os.getcwd()), 'Error/Error_Logs.log')
# if os.path.exists(all_log_path):
#     print(all_log_path)
#     print("文件存在")
# else:
#     print(all_log_path)
#     # os.makedirs(all_log_path)                     # 创建多级目录
#     print("创建完成")

# print(os.path.getatime(file_path))  # 输出最近访问时间
# print(os.path.getctime(file_path))  # 输出文件创建时间
# print(os.path.getmtime(file_path))  # 输出最近修改时间
# print(time.gmtime(os.path.getmtime(file_path)))  # 以struct_time形式输出最近修改时间
# print(os.path.getsize(file_path))  # 输出文件大小（字节为单位）
# print(os.path.abspath(file_path))  # 输出绝对路径
# print(os.path.normpath(file_path))  # 规范path字符串形式

# print(os.environ)
# print(os.path.abspath('.'))         # 输出文件绝对路径
# print(os.getcwd())
# print(os.listdir('.'))
#
# for x in  os.listdir('.'):
#     print(os.path.splitext(x))
#
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# def detect_walk(path,failename):
# 	for root ,dirs,files in os.walk(path):
# 		for a in files:
# 			if failename in a :
# 				print(root,a)
# detect_walk('E:/个人文件','test' )
# print(os.walk('E:/个人文件'))

# def fand_file(path,failname):
# 	for x in os.listdir(path):
# 		a = os.path.join(path,x)
# 		if os.path.isfile(a) and failname in x:
# 			print(a)
# 		if os.path.isdir(a):
# 			fand_file(a,failname)
# fand_file('E:\\个人文件','test')
# for root, dirs, files in os.walk("E:\\个人文件"):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))
print(os.path.split(os.path.abspath('.'))[0])
print(os.path.join(os.path.split(os.path.abspath('.'))[0], 'report\\report_test1.html'))