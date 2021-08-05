import random
import time
i=random.randint(0,10)
n=0
while n<6:
    if n!=5:
      m=int(input("请输入一个数字"))
    else :
      m = int(input("请输入一个数字"))
      time.sleep(10)
    if i!=m :
        print ("你猜错了")
    else :
        print ("你猜对了")
        break
    n+=1
print(i)



