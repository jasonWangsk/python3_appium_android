"""

---
- python3 函数

    函数是程序实现模块话的基本单元、实现某一功能的集合
    函数名：程序代码集合的名称
    参数：函数运算时需要参与运算的值
    函数体：程序的某个功能，进行一系列的逻辑运算

    return返回值： 函数的运行结果或状态

- 函数的作用
    可复用
    提供应用的模块行和代码的重复利用率
- 语法
 def 函数名(参数)：
    函数体
    return 返回值内容



"""
'''
--定义函数语法
def printinfo():
    print("hello world")
    return
'''

# 调用函数

def printifo():
    print("hello world")
    return     # 默认函数值返回内容

# printifo()
# 查看函数返回值
print(printifo())


def printinfo1():
    print("return 有返回值")
    return [111+222]
printinfo1()
print(printinfo1()) # 查看函数返回值

'''
函数参数
    必须参数
    关键字参数
    默认参数
    可变参数（*args，**kwargs）：
    
'''
# 必须参数

def pa_11(name,age):
    print(name,age)
    return
pa_11("jason",22)
#  关键字参数

def pa_12(name,age,hh):
    # print(name,age,hh)
     return name,age,hh

print(pa_12(name='jason',age=22,hh="how are you"))