# #冒泡
# l=[13,15,123,64,2,36,98,12,65,154,321,1,36,45,65,801]
#
# length = len(l)
# for i in range(length-1,0,-1):
#         for j in range(i):
#          if(l[j]>l[j+1]):
#           l[j],l[j+1]=l[j+1],l[j]
# print(l)



# #九九乘法表
# for i in range(1,10):
#     for d in range(1,i+1):
#         print(i, 'x', d, '=', i*d, end='\t')
#     print()


#面向对象
# class jsj():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#       self.a=a
#       self.b=b
#     def sum(self):
#        self.res=self.a+self.b
#     def div(self):
#        self.res=self.a/self.b
#     def get_result(self):
#        print(self.res )

# j =jsj()
# j.input(12,60)
# j.sum()
# j.get_result()
# j.div()
# j.get_result()


# class jsj():   #具体参数的方式
#     res=None
#     def __init__(self,a,b):
#       self.a=a
#       self.b=b
#     def sum(self):
#        self.res=self.a+self.b
#     def div(self):
#        self.res=self.a/self.b
#     def get_result(self):
#        print(self.res )
#
# j =jsj(60,17)
# j.sum()
# j.get_result()
# j.div()
# j.get_result()
#


#找出100以内可以被3整除的数字
# for i in range(1,100):
#     if (i % 3 != 0):
#         continue
#     print(i)


# 成绩评定： 0-59分 不及格 60-70 及格 71-80 良好 81-100 优秀
# 编写程序实现下列需求，给定任意成绩，程序运行之后输出该成绩的级别
# 例如：59分，程序打印出"不及格"
# score_l = [40,70,90,20,87,38,29,30,68,98] # 可迭代对象
# for score in score_l:
#     if(score > 0 and score < 60):
#         print("不及格")
#     elif(score >= 60 and score <= 70):
#         print("及格")
#     elif(score >= 71 and score <= 80):
#         print("良好")
#     elif(score >= 81 and score <= 100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")

# 100以内数的和 不算100
# 求出10*9*8.。。*1 的结果 10的阶乘  10!
# m=1
# for i in range(10,0,-1):
#     m*=i
# print(m)

# break 终止循环
# continue 跳过本次循环
#集合、字符串、数字、列表、字典解包
#变量类型   存储单个值/储存多个值    类型 例子
#变量类型
#八种    存储单个值(字符串，none，数字，布尔，）   储存多个值（元组，列表，字典，集合）
# 例子
# a=[1,2,3,4,5,6]
# b=[1]
# c=(1,2,3,4,5)
# d=(1,)
# e={1,2,4}
# f={1,1,2,2,3,3}
# #s=set()
# k={'名字：''切换','年龄:''18'}
# print()


# 猜数字
# import random
# a=random.randint(0,100)

# while True:
#     b = int(input("请输入数字"))
#     if b > a :
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         break

# a=50
# while True:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("大了")
#     elif (b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         break
#
# import random
# a=32
#
# while True:
#     b = random.randint(0,100)
#     if b > a :
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         break


# 打开模式：r读取   w清空  a 追加写入    b二进制模式
# f=open('hk.txt','w')
# # f.write('我真不懂')
# f.writelines(['ddad\n','dadd\n','ffff\n'])
# # f.write("jhhjk\jdfhk\jfhgkd\n")
# print(f.writable())
# f.close()


#可迭代对象基本操作
#有序对象
#字符串
#拼接
# a='41654'
# b='65474'
# print(a+b)
# # 截取
# a='zxcvbnmkljhgf'
# print(a[-1])   #去最后一个数
# print(a[0])     #取第一个数
# print(a[::-1])  #倒叙
# print(a[:-1])   #倒数第二个开始
# print(a[-1:0:-1]) #倒数去除第一数
# print(a[2:])    #第三个开始
# print(a[2:-2])  #去除前后两个数
# print(a[1:-2:2])  #去除前一个后两个，每隔两个取一个数
# 语法格式 变量名[参数一:参数二:参数三]
# 类比range函数
# 第一个参数:截取字符串的起始下标，默认为0
# 第二个参数：截取字符串的结束下标，开区间
# 第三个参数：步长，默认为1
#遍历？？？？？
# 字符串格式化
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} x {} = {}'.format(j,i,i*j),end = '\t')
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d x %d = %d'%(j,i,i*j),end = '\t')
#     print()
# 列表
#拼接/截取/基本是和字符串一样的
# 批量修改
# p=[1,23,56,112,54585,62,]
# p[5]=23
# print(p)
# p[1:5]=30,20,40,50
# print(p)

#l=[]
#l.append(126)    ##添加一个
#l.extend({'123','545','5465'})   ##添加多个
#l.extend([123,524,546])
#l.insert(1,21)
# print(l.pop(2))  ##下表删数值
#l.remove(123)  ##根据具体数值删
#l.clear()    ##清表
#print(l)

#排序
# w=[1,3,65,74,9,65,45,2,1,63,14,21,30,9]
# w.sort(reverse=True)
# w.sort(reverse=False)
# print(w)

#无序对象
#字典   #最好不要删除或新增
        #为什么？
# m={'name':'果芽','addr':'上海浦东','age':'18'}
# # # for k in m:
# # m.update({'name':'果芽','addr':'上海浦东','age':'18'})
# # print(m)
# #print(m.copy('age'))
# s={}
# for k in m:
#     if k.startswith('n'):
#         continue
#     s[k]=m[k]
# print(s)
#元集

# 报错
# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:  #ZeroDivisionError报错类型，不同类型显示的不同，也只是显示此类型的报错。
#         print(e)   #
# print(div(31,0))     #
#
# print(10/0)
#else补写

# class Cu(Exception):
#     def __init__(self,v='值不为0'):
#         self.v=v
#     def  __str__(self):
#         return self.v
# a=0
# try:
#     if a==0:
#         print('a={}，触发异常'.format(a))
#         raise Cu
#     print('a={}为触发异常'.format(a))
# except Cu as e:
#     pr






