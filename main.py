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
    label4 = tk.Label(root2, text="选择关机方式:")
    label4.pack()
    button6 = tk.Button(root2, text="关机(10秒后)", command=lambda: subprocess.Popen("shutdown /s /t 10 /f", shell=True))
    button6.pack()
    button7 = tk.Button(root2, text="重启(10秒后)", command=lambda: subprocess.Popen("shutdown /r /t 10 /f", shell=True))
    button7.pack()
    button8 = tk.Button(root2, text="取消关机", command=lambda: subprocess.Popen("shutdown /a", shell=True))
    button8.pack()
    button9 = tk.Button(root2, text="关闭窗口", command=lambda: root2.destroy())
    button9.pack()
    button10 = tk.Button(root2, text="debug", command=lambda:open_root3())
    button10.pack()

    def open_root3():
        root3 = tk.Tk()
        root3.geometry("500x500")
        root3.title("debug")
        label5 = tk.Label(root3, text="debug:print(time.time())")
        label5.pack()
        button11 = tk.Button(root3, text="print", command=lambda: print(time.time()))
        button11.pack()
        label6 = tk.Label(root3, text="debug:使用自动刷新时间")
        label6.pack()
        button12 = tk.Button(root3, text="使用", command=lambda: auto_update_time(root))
        button12.pack()

    root2.mainloop()

def auto_update_time(root):
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 每隔1000毫秒（即1秒）调用一次 auto_update_time 函数
    root.after(1000, lambda: auto_update_time(root))

time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
def kill_python():
    subprocess.Popen("taskkill /im python.exe /f",shell=True)
# tk结构
root = tk.Tk()
root.geometry('500x500')
root.title('小工具')
label1 = tk.Label(root, text="目前时间:")
label1.pack()
label = tk.Label(root, text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
label.pack()
button9 = tk.Button(root, text="关闭", command=lambda:root.destroy())
button9.pack()
button13 = tk.Button(root,text="关闭此工具的所有弹窗",command=lambda:kill_python())
button13.pack()
if 小彩蛋 == True:
    label3 = tk.Label(root, text="未转换时间:" + str(time.time()))
button = tk.Button(root, text="打开explorer.exe", command=lambda: subprocess.Popen('explorer.exe'))
button.pack()
button2 = tk.Button(root, text="打开cmd.exe", command=lambda: subprocess.Popen('cmd.exe'))
button2.pack()
button3 = tk.Button(root, text="打开计算机", command=jisuan)
button3.pack()
button4 = tk.Button(root, text="更新时间", command=lambda: update_time())
button4.pack()
button5 = tk.Button(root, text="关机", command=shutdown)
button5.pack()

def update_time():
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

root.mainloop()
