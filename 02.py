from tkinter import *
from tkinter import ttk         #นำเข้าตกแต่ง
from tkinter import messagebox
import time


GUI =Tk()                       #สร้างหน้าต่าง
GUI.title("โปรแกรมบันทึกข้อมูล")    #ชื่อโปรแกรม
GUI.geometry("600x960")         #ขนาด


image = PhotoImage(file="logo.png") #ใส่ภาพ
image = image.subsample(3,3)        #ขนาดภาพ
img1 = ttk.Label(GUI,image=image)       #แสดงผลรูปภาพ
img1.pack()


l1 = ttk.Label(GUI,text="โปรแกรมบันทึกการสอน")       #ใส่ตัวอักษร
l1.config(font=("Verdana", 40))                 #กำหนดฟอนต์และขนาด
l1.pack(ipadx=30,ipady=30)

l2 = ttk.Label(GUI,text="")                         #จะให้เวลาแสดงตรงนี้
l2.config(font=("Verdana", 20))
l2.pack(ipadx=20,ipady=20)

e1 = ttk.Entry(GUI)
e1.pack(ipadx=50,ipady=50)

##############################################################
def update_time_date():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%m/%d/%Y")
    l2.config(text=f"{current_time}\n{current_date}")
    GUI.after(1000, update_time_date)

###############################################################
def save_data():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%m/%d/%Y")    
    save_text = e1.get()
    e1.delete(0,END)
    text = "บันทึกแล้ว"
    print("วันที่ {}  เวลา {}  ข้อความคือ:{}" .format(current_date,current_time,save_text))
    messagebox.showinfo("สถานะ" , text)
    
    
#################################################################    

fb2 =Frame(GUI)                 #กำหนดเฟรม
fb2.pack(ipady=50)         #กำหนดตำแหน่งเฟรม
b2 = ttk.Button(fb2,text="บันทึก",command=save_data)    #กำหนดปุ่มให้อยู่ในเฟรม
b2.pack(ipadx=20,ipady=20)      #กำหนดแพดดิงให้ปุ่ม
#########################################################################



update_time_date()
GUI.mainloop()
