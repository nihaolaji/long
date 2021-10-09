'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：猜3次就睡眠 time.sleep(10)
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
import time
jinbi=5000
guess=15
an=3
randint = random.randint(1, 30)  # 随机产生的数字
while True:
    print(randint)
    num=input("请输入一个数字")
    if jinbi==0:
        break
    if guess==0:
        break
    if an==0:
        time.sleep(10)
    if num.isdigit():
        num=int(num)
        if num == randint:
            jinbi+=3000
            an-=1
            print("恭喜猜对了，获得3000金币，还有",jinbi,"金币")
            continue
        elif num >randint:
            jinbi -= 500
            guess-=1
            an-=1
            print("猜大了，扣除500金币，还有",jinbi,"金币",'还剩'+str(guess-0)+'的次数')
            continue
        elif num <randint:
            jinbi -= 500
            guess-=1
            an-=1
            print("猜小了，扣除500金币，还有",jinbi,"金币",'还剩'+str(guess-0)+'的次数')
            continue
    else:
        jinbi -= 500
        guess-=1
        an-=1
        print("别瞎输入,扣除500金币，还有",jinbi,"金币",'还剩'+str(guess-0)+'的次数')




