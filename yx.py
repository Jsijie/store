import random
hero=["普通","稀有","传奇"]
hp=10
heroname=hero[random.randint(0,len(hero)-1)]
print(heroname)
if heroname == "稀有":
   hp=30
while hp<100:
   i=0
   alist=[]
   while i<3:
      i=i+1
      a=random.randint(3,8)
      alist.append(a)
   hp1=alist[random.randint(0,len(alist)-1)]
   if heroname== "普通" or heroname =="稀有":
      hplist = [hp - hp1, hp + hp1]
      hp=hplist[random.randint(0,len(hplist)-1)]
   else:
      hp=hp+hp1
   if hp <=0:
      print("任务失败，您的分数为:",hp)
      break
   else:
      print("当前分数:",hp)
if hp>0:
   print("任务成功，分数为：",hp,"请进入下一关")

