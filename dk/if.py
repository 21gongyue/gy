age=56  #单条件（if   条件：  print输出   else：print输出相对的）
if age<18:
    print ('未成年')
else:
    print('成年')             #if 于 elif 一样 后面可以加else 也可以不加

if age<18:#多条件（if  条件：  p输出  elif  条件：  p输出。。。。else：print输出相对的）
    print('未成年')
elif (age in range(18,30)):
   print('成年')
elif (age in range(30,60)):
    print('中年')
else:
    print('老年')
cj=48
if (cj>0 and cj<60):
    print('不及格')
elif (cj > 60 and cj < 70):
        print('及格')
elif (cj > 70 and cj < 80):
         print('良好')
elif (cj > 80 and cj < 90):
        print('好')
elif (cj > 90 and cj < 100):
        print('优秀')
#在if控制语句中，如果条件满足 才会执行if下方的代码块，
# 所有条件都不满足，才会去执行else下方的代码块；
# 如果if语句中有任何一个代码块中代码被执行,其他代码块中的代码都会被跳过；