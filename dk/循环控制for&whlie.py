#for 循环变量 in 可迭代对象
     #循环体
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)    #重复循环变量中的代码
k=['牛奶','可乐','果汁']
for i in k:
 if (i=='面包'):
    print(i)




for i in range (0,100,20):  #递增
   print(i)
for i in range (100,0,-10):   #递减
    print(i)
# range(第一个参数,第二个参数,第三个参数)
# 第一个参数：迭代起始的数据，默认值0
# 第二个参数：迭代截止的数据，开区间
# 第三个参数：增量，可正可负，默认为1
#while条件：
  #循环体
flag=True
b=59
while flag:
    a=int(input('请输入数字'))  #int是将字符串转换成数字
    if b > a:
        print('小了')
    elif b<a:
        print('大了')
    else:
        print('猜对了')
        flag= False