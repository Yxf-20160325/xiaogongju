import tkinter as tk
import subprocess
import os
import time
import messagebox
# 变量区
小彩蛋 = False
# 函数区
def jisuan():
    subprocess.Popen('calc.exe')

time1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# tk结构
root = tk.Tk()
root.geometry('500x500')
root.title('小工具')
label1 = tk.Label(root,text="目前时间:")
label1.pack()
label = tk.Label(root,text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
label.pack()
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
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    

root.mainloop()
