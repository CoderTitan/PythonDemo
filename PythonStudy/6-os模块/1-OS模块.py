
'''
os: 包含了普遍的操作系统的功能

使用前先导入os模块
'''

import os

'''获取操作系统的类型
nt -> windows
posix -> Linux/Unix
OS -> Mac(内核是Linux)
'''
print(os.name)
# 输出: posix

# 输出操作系统详细的信息
print(os.uname())
# 输出:
# posix.uname_result(sysname='Darwin', nodename='quanjunt.local', release='17.5.0', version='Darwin Kernel Version 17.5.0: Mon Mar  5 22:24:32 PST 2018; root:xnu-4570.51.1~1/RELEASE_X86_64', machine='x86_64')

# 获取操作系统中的环境变量
print(os.environ)
'''输出
environ({'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/usr/local/apache-tomcat-7.0.85/bin', 'PYTHONPATH': '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend:/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy', 'SHELL': '/bin/bash', 'PYTHONIOENCODING': 'UTF-8', 'GOPATH': '/Users/quanjunt/mygo', 'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'USER': 'quanjunt', 'TMPDIR': '/var/folders/ty/804897ld2zg4pfcgx2p4wqh80000gn/T/', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.R99MHbJeNK/Listeners', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', 'VERSIONER_PYTHON_VERSION': '2.7', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.mC6UXsr9Qz/Render', 'LOGNAME': 'quanjunt', 'LC_CTYPE': 'zh_CN.UTF-8', 'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.29160', 'PWD': '/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块', 'PYCHARM_HOSTED': '1', 'HOME': '/Users/quanjunt', 'PYCHARM_MATPLOTLIB_PORT': '53280', '__PYVENV_LAUNCHER__': '/usr/local/bin/python3.6'})
'''

# 获取指定环境变量
print('指定环境变量: ', os.environ.get('PYTHONPATH'))
'''输出:
 /Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend:/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy
'''

# 获取当前目录
print('当前目录: ', os.curdir)
'''输出:
.
'''

# 获取当前工作目录, 即当前python脚本所在的目录
print('当前工作目录:', os.getcwd())
'''输出:
/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块

'''

# 返回指定目录下的所有的文件, 列表形式
print(os.listdir(r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/4-装饰器和文件读写'))
'''输出:
['1-装饰器.py', "2-通用装饰器'.py", '3-偏函数.py', '4-变量的作用域.py', '5-读文件.py', 'text.txt', 'text1.txt']
'''

# 在当前目录下创建文件
# os.mkdir(r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块/titan.txt')
# os.mkdir('jun')

# 删除目录
# os.rmdir('jun')
# os.rmdir('titan.txt')


# 获取文件属性
print('文件属性:', os.stat('titan'))
'''输出:
文件属性: os.stat_result(st_mode=16877, st_ino=10797606, st_dev=16777224, st_nlink=2, st_uid=501, st_gid=20, st_size=68, st_atime=1527059854, st_mtime=1527058920, st_ctime=1527058920)
'''

# 重命名
# os.rename('jun', 'titan')

# 删除普通文件
# os.remove(r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块/jun.txt')

# 运行shell命名
os.system('notepad')
'''
notepad: shell命令
white: 记事本
mspaint: 画板
'''

# 拼接路径
p1 = '/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy'
p2 = '6-os模块/jun.txt'
print(os.path.join(p1, p2))
# /Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块/jun.txt


# 拆分路径
path2 = r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块/jun.txt'
print('拆分路径:', os.path.split(path2))
# 拆分路径: ('/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块', 'jun.txt')

# 获取扩展名'
print('获取扩展名:', os.path.splitext(path2))
# 获取扩展名: ('/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块/jun', '.txt')

# 是否是目录
print('是否是目录:', os.path.isdir(path2))
# 是否是目录: False

# 判断文件是否存在
print('文件是否存在:', os.path.isfile(path2))
# 文件是否存在: False


# 判断目录是否存在
path3 = r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/6-os模块'
print('判断目录是否存在:', os.path.exists(path3))

# 获取文件大小(字节)
print('文件大小:', os.path.getsize(path3))

# 获取文件名
# print('文件名:', os.path.dirname(path2))
print('文件名:', os.path.basename(path2))

