# a=10
# print(a)
# def aaa():
#     a=12         #def下的变量不运转
#     global a
# aaa()
# print(a)







class  jsj():    #面向对象
    a=None
    b=None
    res=None
    def input(self,a,b):
      self.a=a
      self.b=b
    def sum(self):
        self.res=self.a + self.b
    def div(self):
        self.res=self.a / self.b
    def get_result(self):
         print(self.res)
j=jsj()

j.input(100,200)       #  . 是一个访问符
j.sum()
j.get_result()
j.div()
j.get_result()



# class  jsj():    #面向对象
#     res = None
#     def  __init__(self,a,b): #魔法函数，类实际化的时候调用，又称构造方法
#        self.a =a
#        self.b =b
#     def sum(self):
#         self.res=self.a + self.b
#     def div(self):
#         self.res=self.a / self.b
#     def get_result(self):
#          print(self.res)
# j=jsj(20,56)
#
# # j.input(100,200)       #  . 是一个访问符
# j.sum()
# j.get_result()
# j.div()
# j.get_result()
# class Parent():
#     house=10000
#     money=1000000000
#     def sou_ji(self):
#        print('点石成金')
#
# class Child(Parent):
#     ai_hao='吃吃吃'
#     pass
#
# c=
