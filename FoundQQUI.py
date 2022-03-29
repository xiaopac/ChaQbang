import os.path
import time
from tkinter import ttk
import requests
import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import ImageTk,Image
from tkinter import *
import json
window = tk.Tk()
fontPath = "./font/simhei.ttf"
s = requests.Session()

def getUserInfo():
    global QQ
    QQ = QQS.get()
    if os.path.exists("./QQconfig/photo/"+QQ+".jpg") is True:
        UserImg = ImageTk.PhotoImage(file="./QQconfig/photo/" + QQ + ".jpg")
        User = tk.Label(window, image=UserImg, bd=0, width=640, height=640)
        User.place(x=0, y=0)
        getQQtoALL()
        #window.mainloop()
        #getQQtoALL()
    else:
        downloadQQuserimage()
    #window.mainloop()
    # 头像粘贴


def discoverfile():
    #检查文件夹
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
    #getQQimg = response.text
    # 写入图片到photo文件夹
    with open("./QQconfig/photo/" + QQuserlogo +".jpg","wb") as f:
        f.write(response.content)

def UserGETinfoSETTING():
    global QQS
    #字体

    color = '#ffd46c'

    QQS = tk.Entry(window, font=("./QQconfig/font/simhei.ttf", 15))
    QQS.place(x=700,y=90)

    EnterID = tk.Label(window, text="QQ", bg=color, font=(fontPath, 13))
    EnterID.place(x=670,y=90)

    ok = tk.Button(window, text='OJBK', bg=color, font=(fontPath, 13),command=getUserInfo) #command=getUserimg()
    ok.place(x=870, y=90)
    checkTime = 0
    #if checkTime >= 1:
    #    getUserInfo()
    #else:
    #    checkTime = checkTime + 1
    #    #getUserInfo()
    #getUserInfo()
    #window.mainloop()

def getQQtoALL():
    QQtoPhone = QQ
    color = "#ffd46c"
    urlstatus = "https://tenapi.cn/qqzx/?qq=" + QQtoPhone
    urlPhone = "https://zy.xywlapi.cc/qqapi?qq=" + QQtoPhone
    urlname = "https://tenapi.cn/qqname/?qq=" + QQtoPhone

    #昵称，空间等
    response_name = s.post(urlname)
    QQinfoName = response_name.json()
    #手机号等
    response_phone = s.post(urlPhone)
    QQinfotoPhone = response_phone.json()
    #QQ状态
    response_Status = s.post(urlstatus)
    QQinfotoStatus = response_Status.json()

    bgImg = ImageTk.PhotoImage(file="./QQconfig/photo/bg.jpg")
    bg = tk.Label(window, width=1370, height=913, image=bgImg)
    bg.place(x=0, y=0)

    UserGETinfoSETTING()


    #getUserInfo()
    if QQinfoName["code"] == 202:
        QQNamenofound = tk.Label(window, text="致命错误:无法查找此QQ", bg=color,font=(fontPath, 14))
        QQNamenofound.place(x=670, y=120)
    else:
        QQtoName = tk.Label(window, text="昵称: "+QQinfoName["name"], bg=color,font=(fontPath, 14))
        QQtoName.place(x=670, y=120)

        QQstatus = tk.Label(window, text="QQ状态: "+ QQinfotoStatus["msg"], bg=color,font=(fontPath,14))
        QQstatus.place(x=670, y=150)



    if QQinfotoPhone["status"] == 200:
        QQtoALLstatus = tk.Label(window, text="    详细信息" + QQinfotoPhone["message"], bg=color,font=(fontPath, 14))
        QQtoALLstatus.place(x=700, y=180)

        QQtoPhonenumber = tk.Label(window, text="手机号: " + QQinfotoPhone["phone"], bg=color, font=(fontPath, 14))
        QQtoPhonenumber.place(x=670, y=210)

        QQplace = tk.Label(window, text="注册地址: " + QQinfotoPhone["phonediqu"], bg=color, font=(fontPath, 14))
        QQplace.place(x=670, y=240)

        QQmail = tk.Label(window, text="QQmail: " + QQ + "@qq.com",bg=color, font=(fontPath, 14 ))
        QQmail.place(x= 670 ,y=270)

        urlwatchPhone = "https://tenapi.cn/tel/?tel=" + QQinfotoPhone["phone"]
        response_blog = s.post(urlwatchPhone)
        PhoneInfo = response_blog.json()

        urlblog = "https://zy.xywlapi.cc/wbphone?phone=" + QQinfotoPhone["phone"]
        response_blog = s.post(urlblog)
        WEIBOID = response_blog.json()
        if QQinfotoPhone["status"] == 200:
            if WEIBOID["status"] == 500:
                WEIBOIDFOUND = tk.Label(window, text="    微博id: " + WEIBOID["message"], bg=color, font=(fontPath, 14))
                WEIBOIDFOUND.place(x=670, y=300)
            else:
                WEIBOIDnofound = tk.Label(window, text="    微博id: " + WEIBOID["id"], bg=color, font=(fontPath, 14))
                WEIBOIDnofound.place(x=670, y=300)
        else:
            WEIBOIDFOUND = tk.Label(window, text="    微博id: " + WEIBOID["message"], bg=color, font=(fontPath, 14))
            WEIBOIDFOUND.place(x=670, y=300)

        if QQinfotoPhone["status"] == 200:
            phonelocal = tk.Label(window, text="手机号"+PhoneInfo["local"], bg=color, font=(fontPath, 14))
            phonelocal.place(x=670, y=330)

            phonetype = tk.Label(window, text="手机"+PhoneInfo["type"], bg=color, font=(fontPath, 14))
            phonetype.place(x=670, y=360)

            phoneyys = tk.Label(window, text="手机" + PhoneInfo["yys"], bg=color, font=(fontPath, 14))
            phoneyys.place(x=670, y=360)

            phonebz = tk.Label(window, text=PhoneInfo["bz"], bg=color, font=(fontPath, 14))
            phonebz.place(x=670, y=360)
        else:
            phonenotfound = tk.Label(window, text="无此类信息", bg=color, font=(fontPath, 14))
            phonenotfound.place(x=670, y=330)
    else:

        QQtoALLstatus = tk.Label(window, text="    详细信息" + QQinfotoPhone["message"], bg=color,font=(fontPath, 14))
        QQtoALLstatus.place(x=700, y=180)

    UserImg = ImageTk.PhotoImage(file="./QQconfig/photo/" + QQ + ".jpg")
    User = tk.Label(window, image=UserImg, bd=0, width=640, height=640)
    User.place(x=0, y=0)
    #getUserInfo()
    window.mainloop()
#UI窗口
def UIwindows():
    discoverfile()
    window.geometry("1050x640")
    window.resizable(0,0)
    window.title('QQ信息查询        '+ CQBVersion)
    bgImg = ImageTk.PhotoImage(file="./QQconfig/photo/bg.jpg")
    bg = tk.Label(window, width=1370, height=913, image=bgImg)
    bg.place(x=0, y=0)

    UserGETinfoSETTING()

    window.mainloop()



CQBVersion = "CHAQBANG-v1.2.4"
#主函数，运行
def runmain():
   # if os.path.exists("./Desktop" + CQBVersion + ".exe") or os.path.exists("./Desktop/" + CQBVersion + ".exe") is True:
    UIwindows()
   # elif os.path.exists("./Desktop" + CQBVersion + ".exe") or os.path.exists("./Desktop/" + CQBVersion + ".exe") is False:
    #    messagebox.showwarning(title='请注意', message='请勿在桌面运训此程序，否则会带来不可挽回的错误')

runmain()
