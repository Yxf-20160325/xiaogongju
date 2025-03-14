import tkinter as tk
import subprocess
import os
import time
# 变量区
小彩蛋 = False
# 函数区
def jisuan():
    subprocess.Popen('calc.exe')
def shutdown():
    root2 = tk.Tk()
    root2.geometry("500x500")
    root2.title("关机")
    label4 = tk.Label(root2,text="选择关机方式:")
    label4.pack()
    button6 = tk.Button(root2,text="关机(10秒后)",command=lambda:subprocess.Popen("shutdown /s /t 10 /f",shell=True))
    button6.pack()
    button7 = tk.Button(root2,text="重启(10秒后)",command=lambda:subprocess.Popen("shutdown /r /t 10 /f",shell=True))
    button7.pack()
    button8 = tk.Button(root2,text="取消关机",command=lambda:subprocess.Popen("shutdown /a",shell=True))
    button8.pack()
    button9 = tk.Button(root2,text="关闭窗口",command=lambda:root2.destroy())
    button9.pack()
time1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# tk结构
root = tk.Tk()
root.geometry('500x500')
root.title('小工具')
label1 = tk.Label(root,text="目前时间:")
label1.pack()
label = tk.Label(root,text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
label.pack()
button9 = tk.Button(root,text="关闭",command=lambda:root.destroy())
button9.pack()

if 小彩蛋 == True:
    label3 = tk.Label(root,text="未转换时间:" + time.time())
button = tk.Button(root,text="打开explorer.exe",command=lambda:subprocess.Popen('explorer.exe'))
button.pack()
button2 = tk.Button(root,text="打开cmd.exe",command=lambda:subprocess.Popen('cmd.exe'))
button2.pack()
button3 = tk.Button(root,text="打开计算机",command=jisuan)  
button3.pack()
button4 = tk.Button(root,text="更新时间",command=lambda:update_time())
button4.pack()
button5 = tk.Button(root,text="关机",command=shutdown)
button5.pack()
def update_time():
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    

root.mainloop()
