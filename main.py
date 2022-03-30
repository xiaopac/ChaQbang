import os
import tkinter as tk
from tkinter import *

CQBVersion = "ChaQbang v1.0.0"
color = "#ffd46c"
window = tk.Tk()

def FoundQQpy():
    import time
    import requests
    from future.moves import sys

    status = "RUNNING"

    def stop(status=status):
        if status == "RUNNING":
            status = "STOP"
        print("")
        print("ChaQbang made by xiaopac")
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
            print("ChaQbang made by xiaopac    ")
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



def FoundQQUIpy():
    import os.path
    import time
    from tkinter import ttk
    import requests
    import tkinter as tk
    from tkinter import filedialog, messagebox
    from PIL import ImageTk, Image
    import json

    window = tk.Tk()
    fontPath = "./font/simhei.ttf"
    s = requests.Session()

    def getUserInfo():
        global QQ
        QQ = QQS.get()
        if os.path.exists("./QQconfig/photo/" + QQ + ".jpg") is True:
            UserImg = ImageTk.PhotoImage(file="./QQconfig/photo/" + QQ + ".jpg")
            User = tk.Label(window, image=UserImg, bd=0, width=640, height=640)
            User.place(x=0, y=0)
            getQQtoALL()
            # window.mainloop()
            # getQQtoALL()
        else:
            downloadQQuserimage()
        # window.mainloop()
        # 头像粘贴

    def discoverfile():
        # 检查文件夹
        if os.path.exists("./QQconfig/photo") is False:
            os.makedirs("./QQconfig/photo")
        if os.path.exists("./QQconfig/font") is False:
            os.makedirs("./QQconfig/font")
        if os.path.exists("./QQconfig/font/simhei.ttf") is False:
            with open("C:/Windows/Fonts/simhei.ttf", "rb") as f:
                image = f.read()
            with open("./QQconfig/font/simhei.ttf", "wb") as f:
                f.write(image)
        if os.path.exists("./QQconfig/photo/bg.jpg") is False:
            bgurl = "https://img.alicdn.com/imgextra/i3/262595263/O1CN01pZ4Q8N1okV5FUSJ3O_!!262595263.jpg"
            resource = s.get(bgurl)
            with open("./QQconfig/photo/bg.jpg", "wb") as f:
                f.write(resource.content)

    def downloadQQuserimage():
        # 声明 这个变量等于刚刚输入的
        QQuserlogo = QQ
        # 下载图片地址
        QQuserimg = ('https://q.qlogo.cn/headimg_dl?dst_uin=' + QQ + '&spec=640&img_type=jpg')
        # 获取图片
        response = s.get(QQuserimg)
        # 打包图片为text
        # getQQimg = response.text
        # 写入图片到photo文件夹
        with open("./QQconfig/photo/" + QQuserlogo + ".jpg", "wb") as f:
            f.write(response.content)

    def UserGETinfoSETTING():
        global QQS

        color = '#ffd46c'

        QQS = tk.Entry(window, font=("./QQconfig/font/simhei.ttf", 15))
        ok = tk.Button(window, text='OJBK', bg=color, font=(fontPath, 13), command=getUserInfo)  # command=getUserimg()
        EnterID = tk.Label(window, text="QQ", bg=color, font=(fontPath, 13))

        QQS.place(x=700, y=90)
        EnterID.place(x=670, y=90)
        ok.place(x=870, y=90)

    def getQQtoALL():
        QQtoPhone = QQ
        color = "#ffd46c"

        urlstatus = "https://tenapi.cn/qqzx/?qq=" + QQtoPhone
        urlPhone = "https://zy.xywlapi.cc/qqapi?qq=" + QQtoPhone
        urlname = "https://tenapi.cn/qqname/?qq=" + QQtoPhone

        # 昵称，空间等
        response_name = s.post(urlname)
        QQinfoName = response_name.json()
        # 手机号等
        response_phone = s.post(urlPhone)
        QQinfotoPhone = response_phone.json()
        # QQ状态
        response_Status = s.post(urlstatus)
        QQinfotoStatus = response_Status.json()

        bgImg = ImageTk.PhotoImage(file="./QQconfig/photo/bg.jpg")
        bg = tk.Label(window, width=1370, height=913, image=bgImg)
        bg.place(x=0, y=0)

        UserGETinfoSETTING()

        # getUserInfo()
        if QQinfoName["code"] == 202:
            QQNamenofound = tk.Label(window, text="致命错误:无法查找此QQ", bg=color, font=(fontPath, 14))
            QQNamenofound.place(x=670, y=120)
        else:
            QQtoName = tk.Label(window, text="昵称: " + QQinfoName["name"], bg=color, font=(fontPath, 14))
            QQtoName.place(x=670, y=120)

            QQstatus = tk.Label(window, text="QQ状态: " + QQinfotoStatus["msg"], bg=color, font=(fontPath, 14))
            QQstatus.place(x=670, y=150)

        if QQinfotoPhone["status"] == 200:
            QQtoALLstatus = tk.Label(window, text="    详细信息" + QQinfotoPhone["message"], bg=color, font=(fontPath, 14))
            QQtoALLstatus.place(x=700, y=180)

            QQtoPhonenumber = tk.Label(window, text="手机号: " + QQinfotoPhone["phone"], bg=color, font=(fontPath, 14))
            QQtoPhonenumber.place(x=670, y=210)

            QQplace = tk.Label(window, text="注册地址: " + QQinfotoPhone["phonediqu"], bg=color, font=(fontPath, 14))
            QQplace.place(x=670, y=240)

            QQmail = tk.Label(window, text="QQmail: " + QQ + "@qq.com", bg=color, font=(fontPath, 14))
            QQmail.place(x=670, y=270)

            urlwatchPhone = "https://tenapi.cn/tel/?tel=" + QQinfotoPhone["phone"]
            response_blog = s.post(urlwatchPhone)
            PhoneInfo = response_blog.json()

            urlblog = "https://zy.xywlapi.cc/wbphone?phone=" + QQinfotoPhone["phone"]
            response_blog = s.post(urlblog)
            WEIBOID = response_blog.json()
            if QQinfotoPhone["status"] == 200:
                if WEIBOID["status"] == 500:
                    WEIBOIDFOUND = tk.Label(window, text="    微博id: " + WEIBOID["message"], bg=color,
                                            font=(fontPath, 14))
                    WEIBOIDFOUND.place(x=670, y=300)
                else:
                    WEIBOIDnofound = tk.Label(window, text="    微博id: " + WEIBOID["id"], bg=color, font=(fontPath, 14))
                    WEIBOIDnofound.place(x=670, y=300)
            else:
                WEIBOIDFOUND = tk.Label(window, text="    微博id: " + WEIBOID["message"], bg=color, font=(fontPath, 14))
                WEIBOIDFOUND.place(x=670, y=300)

            if QQinfotoPhone["status"] == 200:
                phonelocal = tk.Label(window, text="手机号" + PhoneInfo["local"], bg=color, font=(fontPath, 14))
                phonelocal.place(x=670, y=330)

                phonetype = tk.Label(window, text="手机" + PhoneInfo["type"], bg=color, font=(fontPath, 14))
                phonetype.place(x=670, y=360)

                phoneyys = tk.Label(window, text="手机" + PhoneInfo["yys"], bg=color, font=(fontPath, 14))
                phoneyys.place(x=670, y=360)

                phonebz = tk.Label(window, text=PhoneInfo["bz"], bg=color, font=(fontPath, 14))
                phonebz.place(x=670, y=360)
            else:
                phonenotfound = tk.Label(window, text="无此类信息", bg=color, font=(fontPath, 14))
                phonenotfound.place(x=670, y=330)
        else:

            QQtoALLstatus = tk.Label(window, text="    详细信息" + QQinfotoPhone["message"], bg=color, font=(fontPath, 14))
            QQtoALLstatus.place(x=700, y=180)

        UserImg = ImageTk.PhotoImage(file="./QQconfig/photo/" + QQ + ".jpg")
        User = tk.Label(window, image=UserImg, bd=0, width=640, height=640)
        User.place(x=0, y=0)
        # getUserInfo()
        window.mainloop()

    # UI窗口
    def UIwindows():
        discoverfile()
        window.geometry("1050x640")
        window.resizable(0, 0)
        window.title('QQ信息查询        ' + CQBVersion)
        bgImg = ImageTk.PhotoImage(file="./QQconfig/photo/bg.jpg")
        bg = tk.Label(window, width=1370, height=913, image=bgImg)
        bg.place(x=0, y=0)

        UserGETinfoSETTING()

        window.mainloop()

    # 主函数，运行
    def runmain():
        # if os.path.exists("./Desktop" + CQBVersion + ".exe") or os.path.exists("./Desktop/" + CQBVersion + ".exe") is True:
        UIwindows()

    # elif os.path.exists("./Desktop" + CQBVersion + ".exe") or os.path.exists("./Desktop/" + CQBVersion + ".exe") is False:
    #    messagebox.showwarning(title='请注意', message='请勿在桌面运训此程序，否则会带来不可挽回的错误')
    runmain()


def windowconfig():
    #设置窗口大小
    window.geometry("300x150")
    #设置窗口不可移
    window.resizable(0, 0)
    #设置标题
    window.title(CQBVersion)
    choose()
    window.mainloop()

def dontrunonUI():
    window.destroy()
    FoundQQpy()

def runUI():
    window.destroy()
    FoundQQUIpy()

def choose():
    chooserun = tk.Label(window, text="选择一个")
    chooserun.place(x=125,y=5)

    UseUI = Button(window, text='使用UI运行', command=runUI)
    UseUI.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.2)

    DontUseUI = Button(window, text="不使用UI运行", command=dontrunonUI)
    DontUseUI.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.2)

    window.mainloop()

def runmain():
    windowconfig()

runmain()

