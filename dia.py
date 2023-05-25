import threading
import imageio
from PIL import ImageTk,Image
import PIL.Image
# from tkinter import *
import tkinter

root = tkinter.Tk()
root.title('my window')
root.geometry('600x800+300+110')
# root.resizable(False,False)
pic=tkinter.Label(root,text='test',width=400,height=600)
im=Image.open('C:\\Users\\Administrator\\Pictures\\pic\\kj.jpg')
image=ImageTk.PhotoImage(im)
pic['image']=image
pic.image=image
def changeSize(event):
    image=ImageTk.PhotoImage(im.resize((event.width,event.height),Image.ANTIALIAS))
    pic['image']=image
    pic.image=image
pic.bind('<Configure>',changeSize) #绑定
pic.pack(fill=tkinter.BOTH,expand=tkinter.YES)
# background_image = ImageTk.PhotoImage(file = 'C:\\Users\Administrator\Pictures\Saved Pictures\lih.jpg')
# background_button=tkinter.Label(root, image = background_image)
# background_button.pack()
from tkinter import *
def mm():
    video_name = "C:/Users/Administrator/Videos/S.mp4"  # This is your video file path
    video = imageio.get_reader(video_name)
    def stream(label):
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(PIL.Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
    so = Toplevel()
    so.geometry('660x580+600+200')
    so.title('JCY-1 转动源')
    my_label = Label(so)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    def m():
        mm()
        so.destroy()
    Button(so, text='再次播放视频',bg='PINK', command=m).pack(fill='x',side=BOTTOM,before=my_label)
#root---界面（需要放在那个界面），textvariable----显示文本变量
#bg----背景   font----字体格式，大小    width----宽度   height----高度

l = Label(root, text='do', bg='yellow')
l.pack(side=TOP,before=pic)
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1


#menubar----菜单
menubar = Menu(root) #菜单加入root界面
filemenu = Menu(menubar, tearoff=0) #filemenu加入菜单栏menubar下（tearoff=0 不可分割）
#filemenu菜单加入标签和相应执行命令
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator() #添加分割线
filemenu.add_command(label='Exit', command=root.quit)
#submenu加入菜单filemenu下（tearoff=0 不可分割）
submenu = Menu(filemenu)
#filemenu菜单加入标签和相应执行命令
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)


editmenu = Menu(menubar, tearoff=0)#editmenu加入菜单menubar下（tearoff=0 不可分割）
#editmenu菜单加入标签和相应执行命令
menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label='Cut',image='img',compound='left',command=do_job) #添加图标
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='View',menu=viewmenu)
viewmenu.add_command(label='type',command=do_job)
viewmenu.add_command(label='info',command=do_job)
viewmenu.add_command(label='recent',command=do_job)
viewmenu.add_command(label='active',command=do_job)
vubmenu=Menu(viewmenu)
viewmenu.add_cascade(label='Appearance',menu=vubmenu)
vubmenu.add_command(label='Mode',command=do_job)
vubmenu.add_command(label='Bar',command=do_job)
vubmenu.add_command(label='Tree',command=do_job)
vmenu=Menu(vubmenu)
vubmenu.add_cascade(label='status',menu=vmenu)
vmenu.add_command(label='JSON',command=do_job)
vmenu.add_separator()
vmenu.add_command(label='Python',command=mm)

#配置菜单栏
root.config(menu=menubar)
root.mainloop()