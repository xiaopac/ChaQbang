from tkinter import *
from tkinter.simpledialog import *



def choosefile():
      import tkinter.filedialog
      root = Tk()
      lb = Label(root, text='')
      lb.pack()
      btn = Button(root, text='弹出文件选择对话框', command=xz)
      btn.pack()
      root.mainloop()
      def xz():
            filename=tkinter.filedialog.askopenfilename()
            if filename != '':
                  lb.config(text='您选择的文件是'+filename)
            else:
                  lb.config(text='您没有选择任何文件')

def colorchoose():
      import tkinter.colorchooser
      def xz():
            color = tkinter.colorchooser.askcolor()
            colorstr = str(color)
            print('打印字符串%s 切掉后=%s' % (colorstr, colorstr[-9:-2]))
            lb.config(text=colorstr[-9:-2], background=colorstr[-9:-2])
      root = Tk()
      lb = Label(root, text='请关注颜色的变化')
      lb.pack()
      btn = Button(root, text='弹出颜色选择对话框', command= xz)
      btn.pack()
      root.mainloop()

def carmra():
      import cv2
      from PIL import Image, ImageTk

      def take_snapshot():
            print("有人给你点赞啦！")

      def video_loop():
            success, img = camera.read()  # 从摄像头读取照片
            if success:
                  cv2.waitKey(100)
                  cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
                  current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
                  imgtk = ImageTk.PhotoImage(image=current_image)
                  panel.imgtk1 = imgtk
                  panel.config(image=imgtk)
                  root.after(1, video_loop)

      camera = cv2.VideoCapture(0)  # 摄像头

      root = Tk()
      root.title("opencv + tkinter")
      # root.protocol('WM_DELETE_WINDOW', detector)

      panel = Label(root)  # initialize image panel
      panel.pack(padx=10, pady=10)
      # root.config(cursor="arrow")
      btn = Button(root, text="点赞!", command=take_snapshot)
      btn.pack(fill="both", expand=True, padx=10, pady=10)

      video_loop()

      root.mainloop()
      # 当一切都完成后，关闭摄像头并释放所占资源
      camera.release()
      cv2.destroyAllWindows()

def talkenterbox():

      #from tkinter.simpledialog import *
      root = Tk()
      lb = Label(root, text='')
      lb.pack()

      def xz():
            s = askstring('请输入', '请输入一串文字')
            lb.config(text=s)

      btn = Button(root, text='弹出输入对话框', command=xz)
      btn.pack()
      root.mainloop()

def choosemessagebox():
      #from tkinter import *
      import tkinter.messagebox

      def xz():
            answer = tkinter.messagebox.askokcancel('请选择', '请选择确定或取消')
            if answer:
                  lb.config(text='已确认')
            else:
                  lb.config(text='已取消')

      root = Tk()

      lb = Label(root, text='')
      lb.pack()
      btn = Button(root, text='弹出对话框', command=xz)
      btn.pack()
      root.mainloop()

def subzonewindow():
      def newwind():
            winNew = Toplevel(root)
            winNew.geometry('320x240')
            winNew.title('新窗体')
            lb2 = Label(winNew, text='我在新窗体上')
            lb2.place(relx=0.2, rely=0.2)
            btClose = Button(winNew, text='关闭', command=winNew.destroy)
            btClose.place(relx=0.7, rely=0.5)

      root = Tk()
      root.title('新建窗体实验')
      root.geometry('320x240')

      lb1 = Label(root, text='主窗体', font=('黑体', 32, 'bold'))
      lb1.place(relx=0.2, rely=0.2)

      mainmenu = Menu(root)
      menuFile = Menu(mainmenu)
      mainmenu.add_cascade(label='菜单', menu=menuFile)
      menuFile.add_command(label='新窗体', command=newwind)
      menuFile.add_separator()
      menuFile.add_command(label='退出', command=root.destroy)

      root.config(menu=mainmenu)
      root.mainloop()

def menuofthewindow():

      def new():
            s = '新建'
            lb1.config(text=s)

      def ope():
            s = '打开'
            lb1.config(text=s)

      def sav():
            s = '保存'
            lb1.config(text=s)

      def cut():
            s = '剪切'
            lb1.config(text=s)

      def cop():
            s = '复制'
            lb1.config(text=s)

      def pas():
            s = '粘贴'
            lb1.config(text=s)

      def popupmenu(event):
            mainmenu.post(event.x_root, event.y_root)

      root = Tk()
      root.title('菜单实验')
      root.geometry('320x240')

      lb1 = Label(root, text='显示信息', font=('黑体', 32, 'bold'))
      lb1.place(relx=0.2, rely=0.2)

      mainmenu = Menu(root)
      menuFile = Menu(mainmenu)  # 菜单分组 menuFile
      mainmenu.add_cascade(label="文件", menu=menuFile)
      menuFile.add_command(label="新建", command=new)
      menuFile.add_command(label="打开", command=ope)
      menuFile.add_command(label="保存", command=sav)
      menuFile.add_separator()  # 分割线
      menuFile.add_command(label="退出", command=root.destroy)

      menuEdit = Menu(mainmenu)  # 菜单分组 menuEdit
      mainmenu.add_cascade(label="编辑", menu=menuEdit)
      menuEdit.add_command(label="剪切", command=cut)
      menuEdit.add_command(label="复制", command=cop())
      menuEdit.add_command(label="粘贴", command=pas())

      root.config(menu=mainmenu)
      root.bind('Button-3', popupmenu)  # 根窗体绑定鼠标右击响应事件
      root.mainloop()
