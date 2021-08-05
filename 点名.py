
import random
name=["小红","小李","小黄","小白","老王"]
i=0

while i<2:
    i+=1
    chose=input("请输入您的业务(1、点名  2、分发棒棒糖)")
    if chose == "1":
       a=len(name)
       index=random.randint(0,a-1)
       print(name[index])
    elif chose== "2":
        num=random.randint(5,10)
        print ("获得了",num,"个棒棒糖")
    else :
        print("输入错误")
        i=0
        break
if i==0:
    print(" ")
else:
    print(name[index],"获得了",num,"个棒棒糖")

