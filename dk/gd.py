# #a=1,2,3,4,5
#     print(a)
#     a,b,d,r=[1,2,3,4]
#     print(a)
#     print(b)
#     print(d)
#     print(r)
#     a,b,*s=(1,2,3,4,5)
#     print(a)
#     print(b)
#     print(s)
#     k="小明"
#     a,b=k#
#     print(a)
#     print(b)
#
#
# q=30
# w=40
# e=80
# print(e/w)
# a=2
# b=3
# c=4
# print(a**(b*c))
# z=4454552
# print(z % 10)
# z//=10
#
# ##print(z % 10)
# ##k=["土豆","辣椒","白菜","番茄"]
# ##if ("胡萝卜"in k)
#
#
# cj_1=[60,80,25,46,18,62]
# for cj in cj_1:
#     if(cj<60):
#        print('不及格')
#     if (60<=cj<=70):
#        print('及格')
#     if(71<=cj<=80):
#         print('良好')
#     if(81<=cj<=100):
#         print('优秀')
# u=1
# for o in range (10,1,-1):
#     u*=o
#     print(u
# flag = True
# b=36
# while flag:
#     a=int(input('请输入数字'))
#     if b > a:
#         print('小了')
#     elif b<a:
#         print('大了')
#     else:
#         print('猜对了')
#         flag= False
#一百以内不能被3整除的数
#100以内能被3整除的数
# for i in range(1,100):
#     if (i % 3 )!=0:
#         continue
#     print(i)
#100以内不能被3整除的数
# for i in range(0, 100):
#         if (i % 3) ==0:
#             continue
#         print(i)
#ding
# def cd (a,b):
#     print('商：',a//b ,',余数：',a % b )
# cd(72,30)
# cd(63,30)


# def cd (a,b):
#     if(b==0):
#         return None
#     else:
#         return (a//b, a%b )
# g=cd(60,5)#位置入参数
# g=cd(a=60,b=5)#按关键字入参数
# if g is None:
#     print('参数错误')
# else:
#     print('商为：',g[0],'余数为：',g[1])

# def cd (a,b):
#     if(b==0):
#      print('除数不为0')
#     else:
#         print('商：',a//b ,',余数：',a % b )
# cd(60,20)
# cd(67,32)
# def sm(a,b=3):
#     return a+b
# print (sm(2,3))




k=1,2,3,4,5,6,7,8,9
a,*b=[1,2,3,4,5,6,7,8,9]
print(*b)
print(a)
def suml(*args):
    s=0
    for i in args:
        s+=i
    return s
print(suml(1,5,9,6,3,12,54,976,79,4,5,6,))
while k(0,100,3):
    print(k)