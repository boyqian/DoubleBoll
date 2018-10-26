# -* - coding: UTF-8 -* -
import  time
import  random
money = int(input("一张彩票2块钱，请输入您要充值的金额："))
print("您现在的余额为：%d元"%money)
c=0
shuru = 0
while True:
    list1=[]
    list2=[]
    if money<=4:
        print("您的余额即将不足，请及时充值：")
        c = int(input("请问是否要进行充值：【1：充值；0：拒绝】"))
    if money<2:
        print("余额不足，结束游戏！")
        break
    if c==1:
        money1 = int(input("请输入您要充值的金额："))
        money = money + money1
        print("您现在的余额为：%d元" % money)
    if c==0:
        pass
    caipiaoshu =int(input("您要买几张彩票？"))
    while True:
        if caipiaoshu>money//2:
            z = money //2
            print("您没钱买这么多彩票,您还能购买%d张" %z)
            caipiaoshu = int(input("您要买几张彩票？"))
        else:
            break
    print("温馨提示：中奖数据有七位数，红球1-33,蓝球1-16")
    for n in range(caipiaoshu):
        n1 = n+1
        shuru =input("请输入第%s张彩票的数据，红球：" %n1)
        list1=shuru.split()
        shuru2 = input("请输入第%s张彩票的数据，蓝球：" % n1)
        list2.append(shuru2)
    print("游戏即将开始，请稍后....")
    time.sleep(1)
    print("开始产生中将数据....")
    time.sleep(1)
    Num = []
    Bule = []
    n = 0
    while True:
        suiji = random.choice(range(1, 34))
        Num.append(suiji)
        Num = list(set(Num))
        if(len(Num)==6):
            break
    suiji2 = random.choice(range(1, 17))
    Bule.append(suiji2)
    print("数据产生成功！")
    Num1 = [str(i) for i in Num]
    Num2 = " ".join(Num1)
    Num3 = [str(j) for j in Bule]
    Num4 = " ".join(Num3)
    print("红球：", Num2," 蓝球：", Num4)
    for m in range(len(list1)):
        if list1[m] in Num and list2[0] in Bule:
            money = 5000000+money-2
            print("恭喜您中奖，获得500万大奖！，当前余额为：%d"%money)
    money -= 2*caipiaoshu
    print("很遗憾，本次猜不中哦，当前余额为：%d"%money)
    con = input("请问还要继续么？继续请输入 1, 结束请输入 0")
    if con == '1':
        continue
    elif con == '0':
        print("游戏结束")
        break
