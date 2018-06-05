'readTextFile.oy -- read and display text file'
#get filename
fname = input("enter filename: ")
print()

#open file or reading
try:
    f = open(fname, 'r')
except IOError as e:     #定义异常实例(except IOError as e)
    print("***file open error:" + e)
else:
    for eachLine in f:
        print(eachLine,end="")     #python2: print eachline,(尾部","去掉换行 )
    f.close()



"""python2: except IOError, e:
attributeError 调用不存在的方法引发的异常
EOFError    遇到文件末尾引发的异常
ImportError 导入模块出错引发的异常
IndexError    列表越界引发的异常
IOError    I/O操作引发的异常，如打开文件出错等
KeyError  使用字典中不存在的关键字引发的异常
NameError 使用不存在的变量名引发的异常
TabError 语句块缩进不正确引发的异常
ValueError 搜索列表中不存在的值引发的异常
ZeroDivisionError   除数为零引发的异常"""