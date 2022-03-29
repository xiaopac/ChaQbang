import time
import requests
from future.moves import sys

status = "RUNNING"

def stop(status=status):
    if status == "RUNNING":
        status = "STOP"
    print("")
    print("CHAQBANG made by xiaopac")
    print("两秒后关闭程序")
    time.sleep(2)
    sys.exit()

def getLOLtoQQ():
    LOLtoQQ = input("('0'表示退出)  请输入查询的LOL昵称》》》")
    if LOLtoQQ == "2730497420":
        print("")
        print("制作人QQ不可查")
        print("")
    elif LOLtoQQ == "0":
        stop()
    else:
        url = "https://zy.xywlapi.cc/lolname?name=" + LOLtoQQ
        response = requests.post(url)
        LOLinfotoQQ = response.json()
        if LOLinfotoQQ["status"] == 200:
            print("")
            print(LOLinfotoQQ["message"])
            print("QQ: " + LOLinfotoQQ["qq"])
            print("QQ绑定的手机号: 仅仅在v2.1启用")
            print("账号名字: " + LOLinfotoQQ["name"])
            print("大区: " + LOLinfotoQQ["daqu"])
            print("")
        else:
            print("")
            print(LOLinfotoQQ["message"])
            print("")

def getQQtoLOL():
    QQtoLOL = input("('0'表示退出)  请输入查询QQ的号》》》")
    if QQtoLOL == "2730497420":
        print("")
        print("制作人QQ不可查")
        print("")
    elif QQtoLOL == "0":
        stop()
    else:
        url = "https://zy.xywlapi.cc/qqlol?qq=" + QQtoLOL
        response = requests.post(url)
        QQinfotoLOL = response.json()
        if QQinfotoLOL["status"] == 200:
            print("QQ>>>LOL信息")
            print(QQinfotoLOL["message"])
            print("QQ: " + QQinfotoLOL["qq"])
            print("账号名字: " + QQinfotoLOL["name"])
            print("大区: " + QQinfotoLOL["daqu"])
            print("")
        else:
            print("")
            print(QQinfotoLOL["message"])
            print("")

def getQQtoPhone():
    QQtoPhone = input("('0'表示退出)  请输入查询QQ的号》》》")
    if QQtoPhone == "2730497420":
        print("")
        print("制作人QQ不可查")
        print("")
    elif QQtoPhone == "0":
        stop()
    else:
        url = "https://zy.xywlapi.cc/qqapi?qq=" + QQtoPhone
        response = requests.post(url)
        QQinfotoPhone = response.json()
        if QQinfotoPhone["status"] == 200:
            print("")
            print("QQ>>>手机号")
            print(QQinfotoPhone["message"])
            print("QQ: " + QQinfotoPhone["qq"])
            print("注册手机号: " + QQinfotoPhone["phone"])
            print("注册地址: " + QQinfotoPhone["phonediqu"])
            print("")
        else:
            print("")
            print(QQinfotoPhone["message"])
            print("")

def getQQtoPSW():
    QQtoPSW = input("('0'表示退出)  请输入查询QQ的手机号码》》》")
    if QQtoPSW == "2730497420":
        print("")
        print("制作人QQ不可查")
        print("")
    elif QQtoPSW == "0":
        stop()
    else:
        url = "https://zy.xywlapi.cc/qqlm?qq=" + QQtoPSW
        response = requests.post(url)
        QQinfotoPSW = response.json()
        if QQinfotoPSW["status"] == 200:
            print("")
            print("QQ>>>密码")
            print(QQinfotoPSW["message"])
            print("QQ: " + QQinfotoPSW["qq"])
            print("QQ密码: " + QQinfotoPSW["qqlm"])
            print("若能查到，就说明您的密码已泄露，请尽快修改密码")
            print("")
        else:
            print("")
            print(QQinfotoPSW["message"])
            print("")

def getPhonetoQQ():
    PhonetoQQ = input("('0'表示退出)  请输入查询QQ的手机号码》》》")
    if PhonetoQQ == "2730497420":
        print("")
        print("制作人QQ不可查")
        print("")
    elif PhonetoQQ == "0":
        stop()
    else:
        url = "https://zy.xywlapi.cc/qqphone?phone=" + PhonetoQQ
        response = requests.post(url)
        PhoneinfotoQQ = response.json()
        if PhoneinfotoQQ["status"] == 200:
            print("")
            print("手机号>>>QQ")
            print(PhoneinfotoQQ["message"])
            print("QQ: " + PhoneinfotoQQ["qq"])
            print("注册手机号: " + PhoneinfotoQQ[""])
            print("注册地址: " + PhoneinfotoQQ["phonediqu"])
            print("")
        else:
            print("")
            print(PhoneinfotoQQ["message"])
            print("")

def run():
    if status == "RUNNING":
        print("star to running....")
        print("")
        print("CHAQBANG made by xiaopac    ")
        print("==========请输入您要查询的信息===========")
        print("！！！！输入0退出！！！！")
        print(" QQ号查询绑定手机: 1")
        print(" 手机号查询绑定QQ: 2")
        print(" QQ号查询LOL信息: 3")
        print(" LOL昵称查询QQ信息: 4")
        print(" QQ号查询QQ密码: 5")
        print("=============Version 2.0=============")
        choose = input("请输入查询方式》》》")
        while True:
            if choose == "1":
                getQQtoPhone()
            elif choose == "2":
                getPhonetoQQ()
            elif choose == "3":
                getQQtoLOL()
            elif choose == "4":
                getLOLtoQQ()
            elif choose == "5":
                getQQtoPSW()
            else:
                stop()
    else:
        stop()
run()











