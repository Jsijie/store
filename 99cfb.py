i=int(input("请输入一个数字："))
for a in range(i+1):
    cfb=""
    for n in  range(a):
      n+=1
      cfb=cfb+str(n)+"*"+str(a)+"="+str(n*a)+"|"
    print(cfb)