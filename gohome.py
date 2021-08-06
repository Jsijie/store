luxian={"1":{"龙跃苑":"020","流星小区":"303"},"2":{"通天苑":"111"}}

name=input("请输入地铁线路:")
if name=="1":
    name1=input("请输入小区名：")
    if name1=="龙跃苑":
        name2=input("请输入门牌号")
        if name2=="020":
            print("您已到家")
        else:
            print("输入错误")
    elif name1=="流星小区":
        name2=input("请输入门牌号")
        if name2=="流星小区":
            print("您已到家")
        else:
            print("输入错误")
    else:
        print("输入错误")
elif name=="2":
    name1 = input("请输入小区名：")
    if name1=="通天苑":
        name2=input("请输入门牌号")
        if name2=="020":
            print("您已到家")
        else:
            print("输入错误")
    else:
        print("输入错误")
else:
    print("输入错误")
