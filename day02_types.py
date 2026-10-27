# 动态类型及基本数据类型
## 类型跟着值走 不跟着变量走 同一个变量可以先后绑定不同类型
# **type()函数可以查看变量类型**
age = 18
print(type(age))      # <class 'int'>

age = "十八"
print(type(age))      # <class 'str'>  

## 基本数据类型
### int float str bool none

## 类型转换 num = int ("123") 字符串->整数
## 算数运算 7//2 = 3(整除) 2 ** 3 = 8(幂运算)
## 字符常用操作 
    #* 字符串拼接: "hello" + "world" = "helloworld"
    #* 字符串重复: "hello" * 3 = "hellohellohello"
    #* 字符串索引: "hello"[0] = "h"  "hello"[-1] = "o"
    #*字符串取长度: len("hello") = 5
## f-string 格式化

name = "James Sun"
age = 18
height = 1.85
if_student = True
none_value = None

type(name)      # <class 'str'>
type(age)       # <class 'int'>
type(height)    # <class 'float'>
type(if_student) # <class 'bool'>
type(none_value) # <class 'NoneType'>

age = str(age)  
print(type(age))      # <class 'str'>

"变量没有类型,指向的对象有类型"

print(f"我的名字是{name},年龄是{age},身高是{height},是否是学生:{if_student},空值:{none_value}")