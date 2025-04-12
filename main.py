import tkinter as tk
import subprocess
import os
import time

# 变量区
小彩蛋 = False
log_on = False
# 函数区
def jisuan():
    subprocess.Popen('calc.exe')

def open_debug_entry():
    entry0 = tk.Entry(root)
    entry0.pack()
    button0 = tk.Button(root, text="run", command=lambda:subprocess.Popen(entry0.get(),shell=True))
    button0.pack()
    
def shutdown():
    root2 = tk.Tk()
    root2.geometry("500x500")
    root2.title("关机")
    label4 = tk.Label(root2, text="选择关机方式:")
    label4.pack()
    button6 = tk.Button(root2, text="关机(10秒后)", command=lambda:subprocess.Popen("shutdown /s /t 10 /f", shell=True))
    button6.pack()
    button7 = tk.Button(root2, text="重启(10秒后)", command=lambda:subprocess.Popen("shutdown /r /t 10 /f", shell=True))
    button7.pack()
    button8 = tk.Button(root2, text="取消关机", command=lambda:subprocess.Popen("shutdown /a", shell=True))
    button8.pack()
    button9 = tk.Button(root2, text="关闭窗口", command=lambda: root2.destroy())
    button9.pack()
    button10 = tk.Button(root2, text="debug", command=lambda:open_root3())
    button10.pack()
    time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    def print_log():
     import logging
     logging.basicConfig(filename='debug_log',level=logging.DEBUG)
     logging.debug('open_debug_log')
     logging.debug('最开始时间(未转换):' + str(time.time()))
     logging.debug('最开始时间(已转换):' + time1)
    def open_new_window():
        root4 = tk.Tk()
        root4.geometry("500x500")
        root4.title("tk")
    def open_root3():
        root3 = tk.Tk()
        root3.geometry("500x500")
        root3.title("debug")
        label5 = tk.Label(root3, text="debug:print(time.time())")
        label5.pack()
        button11 = tk.Button(root3, text="print", command=lambda:print(time.time()))
        button11.pack()
        label6 = tk.Label(root3, text="debug:使用自动刷新时间")
        label6.pack()
        button12 = tk.Button(root3, text="使用", command=lambda:auto_update_time(root))
        button12.pack()
  
        label7 = tk.Label(root3, text="debug:显示日志 ")
        #label7.pack()
        button14 = tk.Button(root3, text="显示", command=lambda:NameError)
        #button14.pack()

        label8 = tk.Label(root3, text="debug:打开空白窗口")
        label8.pack()
        button18 = tk.Button(root3, text="打开", command=lambda:open_new_window())
        button18.pack()
        label9 = tk.Label(root3, text="debug:输出当前时间")
        label9.pack()
        button19 = tk.Button(root3, text="输出", command=lambda:print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        button19.pack()
        label10 = tk.Label(root3, text="debug:一直输出当前时间")
        label10.pack()
        button21 = tk.Button(root3, text="输出", command=lambda:auto_print_time(root))
        button21.pack()
        label11 = tk.Label(root3, text="debug:print")
        label11.pack()
        entry2 = tk.Entry(root3)
        entry2.pack()
        button22 = tk.Button(root3, text="输出", command=lambda:print_entry2())
        button22.pack()
        label12 = tk.Label(root3, text="debug:输出打开程序的时间")
        label12.pack()
        button20 = tk.Button(root3, text="输出", command=lambda:print(time1))
        button20.pack()
        label13 = tk.Label(root3, text="debug:open_debug_entry")
        label13.pack()
        button22 = tk.Button(root3, text="打开", command=lambda:open_debug_entry())
        button22.pack()
        def print_entry2():
            print(entry2.get())
            
        button15 = tk.Button(root3, text="关闭窗口", command=lambda:root3.destroy())
        button15.pack()
       
    root2.mainloop()

def auto_update_time(root):
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 每隔1000毫秒（即1秒）调用一次 auto_update_time 函数
    root.after(1000, lambda: auto_update_time(root))
def auto_print_time(root):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # 每隔1000毫秒（即1秒）调用一次 auto_update_time 函数
        root.after(1000, lambda:auto_print_time(root))
       
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
button = tk.Button(root, text="打开explorer.exe", command=lambda:subprocess.Popen('explorer.exe'))
button.pack()
button2 = tk.Button(root, text="打开cmd.exe", command=lambda:subprocess.Popen('cmd.exe'))
button2.pack()
button3 = tk.Button(root, text="打开计算机", command=jisuan)
button3.pack()
button4 = tk.Button(root, text="更新时间", command=lambda:update_time())
button4.pack()
button5 = tk.Button(root, text="关机", command=shutdown)
button5.pack()

def update_time():
    import messagebox
    label.config(text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    messagebox.showwarning("警告","建议使用debug下自动刷新时间,将自动打开自动刷新时间")
    auto_update_time(root)
      
root.mainloop()
