import random
print("====================================")
print("|-------中国工商银行账户管理系统-------|")
print("|-------1、开户              -------|")
print("|-------2、存钱              -------|")
print("|-------3、取钱              -------|")
print("|-------4、转账              -------|")
print("|-------5、查询              -------|")
print("|-------6、退出              -------|")
print("====================================")
bank={}
bank_name="中国工商银行"
def bank_adduser(account,username,password,contury,province,street,door):
    if len(bank)>100:
        return 3
    if username in bank:
        return 2
    bank[username]={
        "acount":account,
        "password":password,
        "coutury":contury,
        "province":province,
        "streed":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1

def adduser():
    username=input("请输入您的用户名")
    password=input("请输入密码")
    print("请输入详细信息")
    contury=input("请输入您的国家")
    province=input("请输入所在省份")
    street=input("请输入所在街道")
    door=input("请输入门牌号")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,contury,province,street,door)
    if status==3:
        print("对不起，该银行账户已满，请到其他行进行办理")
    if status==2:
        print("对不起，该账户已开")
    if status==1:
        print("恭喜你正常开户，一下是您的信息")
        info="""
           -----------个人信息----------
           用户名：%s
           账号：%s
           密码：******
           国籍：%s
           省份：%s
           街道：%s
           门牌号：%s
           余额：%s
           开户行名称：%s
        """
        print(info%(username,account, contury, province, street, door, bank[username]["money"], bank_name))
def AccVali(i=0):
    off=0
    Iacc = int(input("请输入账号："))
    for i in range(len(username1)+1):
        if i == len(username1):
            print("此账号不存在，请重新输入")
            AccVali()
        if Iacc == bank[username1[i]]['acount']:
            off = 1
            break
    while off == 1:
        Ipass = input("请输入密码")
        if Ipass in bank[username1[i]]['password']:
            print("密码正确")
            return i
            break
        else:
            while True:
                fn = input("密码错误，是否继续输入")
                if fn == "是":
                    print()
                    break
                elif fn == "否":
                    print("退出存款")
                    return -1
                    #break
                else:
                    print("请输入正确的选项")

def addmoney(i):
    while True:
        deposit=int(input("请输入存款金额："))
        if deposit>0:
            print("1"+str(i))
            bank[username1[i]]['money']+=deposit
            print("当前余额："+str(bank[username1[i]]['money']))
            break
        elif deposit==0:
            print("")
            break
        else:
            print("请输入正确的金额")
    print("成功存入")


def delmoney(i):
    while True:
        deposit=int(input("请输入取款金额："))
        if deposit>0:
            if bank[username1[i]]['money']-deposit>=0:
                bank[username1[i]]['money']-=deposit
                print("当前余额："+str(bank[username1[i]]['money']))
                break
            else:
                print("卡内余额不足")
        elif deposit==0:
            print("")
            break
        else:
            print("请输入正确的金额")
    print("取款成功")

def updmoney(i):
    i2=0
    while True:
        trants=int(input("请输入转账账号："))
        for i2 in range(len(username1) + 1):
            print(len(username1),i2)
            if i2 == len(username1):
                print("此账号不存在，请重新输入")
                updmoney(i)
            if trants == bank[username1[i2]]['acount']:
                off = 1
                break
        while off == 1:
            if trants != bank[username1[i]]:
                deposit=int(input("请输入转账金额："))
                if deposit>0:
                    if bank[username1[i]]['money']-deposit>=0:
                        bank[username1[i]]['money']-=deposit
                        bank[username1[i2]]['money']+=deposit
                        print(username1[i]+"当前余额："+str(bank[username1[i]]['money']))
                        print(username1[i2] + "当前余额：" + str(bank[username1[i2]]['money']))
                        print("转账成功")
                        break
                    else:
                        print("卡内余额不足")
                elif deposit==0:
                    print("")
                    break
                else:
                    print("请输入正确的金额")
            else:
                print("不能对本卡进行转账")


while True:
    num=input("请输入您要办的业务：")
    if num=="1":
        adduser()
        print(bank)
    elif num=="2":
        i=0
        username1=list(bank.keys())
        print(len(username1))
        print(bank[username1[0]])
        print(bank[username1[1]])
        i=AccVali()
        if i == -1:
             print("取消存款操作")
        else :
            addmoney(i)
            print(bank)
    elif num=="3":
        i=0
        username1 = list(bank.keys())
        print(len(username1))
        print(bank[username1[0]])
        print(bank[username1[1]])
        i = AccVali()
        if i == -1:
            print("取消取款操作")
        else:
            updmoney(i)
    elif num=="4":
        i = 0
        username1 = list(bank.keys())
        print(len(username1))
        print(bank[username1[0]])
        print(bank[username1[1]])
        i = AccVali()
        if i == -1:
            print("取消取款操作")
        else:
            updmoney(i)
    elif num=="5":
        i = 0
        bank = {'j': {'acount': 48429962, 'password': '145698', 'coutury': 'cn', 'province': 'xj', 'streed': '145',
                      'door': '365', 'money': 300, 'bank_name': '中国工商银行'},
                'd': {'acount': 14789632, 'password': '145698', 'coutury': 'cn', 'province': 'xj', 'streed': '145',
                      'door': '365', 'money': 300, 'bank_name': '中国工商银行'}}
        username1 = list(bank.keys())
        print(len(username1))
        print(bank[username1[0]])
        print(bank[username1[1]])
        i = AccVali()
        if i == -1:
            print("取消查询")
        else:
            info = """
                       -----------个人信息----------
                       用户名：%s
                       账号：%s
                       密码：******
                       国籍：%s
                       省份：%s
                       街道：%s
                       门牌号：%s
                       余额：%s
                       开户行名称：%s
                    """
            print(info % (username1[i], bank[username1[i]]['acount'], bank[username1[i]]['coutury'], bank[username1[i]]['province'],
                          bank[username1[i]]['streed'], bank[username1[i]]['door'], bank[username1[i]]["money"], bank_name))
    elif num=="6":
        print("退出系统")
        break
    else:
        print("输入错误")
        break
    print()