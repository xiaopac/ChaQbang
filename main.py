import os
import tkinter as tk
from tkinter import *

CQBVersion = "CHAQBANG-v1.2.4"
color = "#ffd46c"
window = tk.Tk()

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
    os.system("python ./FoundQQ.py")

def runUI():
    window.destroy()
    os.system("python ./FoundQQUI.py")

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

