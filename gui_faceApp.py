import cv2  as cv
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import filedialog as fd 
from PIL import Image,ImageTk
import time
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        self.configure(bg='#f7f8e7')
        self.s=""
        menu=Menu(self.master)
        self.master.config(menu=menu)
        filemenu=Menu(menu)
        menu.add_cascade(label="File",menu=filemenu)
        editMenu=Menu(menu)
        timeMenu=Menu(menu)
        menu.add_cascade(label="edit",menu=editMenu)
        filemenu.add_command(label="Item")
        filemenu.add_command(label="exit",command=self.clickExitButton)
        editMenu.add_command(label="undo")
        editMenu.add_command(label="redo")
        self.pack(fill=BOTH, expand=1)
        self.heading=Label(self,text="Image Processor",fg="#FCF5F5",bg="#FB4343",width=50,height=2,font=("Helvetica",25)).pack(fill=X,pady=0)
        self.la=Label(self,text="time",fg="black",font=("Times new roman",9))
        self.heading=Label(self,text="By Sudhanshu Mishra",fg="black",font=("Helvetica",8)).pack(side=BOTTOM,pady=0)
        self.la.pack(side=BOTTOM)
        self.var1=StringVar()
        self.bttn=Button(self,text="select image",bg="green",fg="white",font=("Arial",15),width=50,command=self.askFile).pack(padx=40,pady=10)
        self.heading=Label(self,text="select operation on image",fg="#000000",height=2,font=("Helvetica",12)).pack(padx=50,pady=0)
        self.bttn=Button(self,text="Convert to black and white",width=25,bg="#0EABBC",fg="#fff",command=self.convert_BnW).pack(padx=50,pady=2)
        self.bttn=Button(self,text="Resize image",bg="#0EABBC",fg="#fff",width=25,command=self.print_var).pack(padx=50,pady=2)
        self.bttn=Button(self,text="Recognize face",bg="#0EABBC",fg="#fff",width=25,command=self.face_recog).pack(padx=50,pady=2)
        self.bttn=Button(self,text="Display edges in images",bg="#0EABBC",fg="#fff",width=25,command=self.convert_edge).pack(padx=50,pady=2)
        #uncomment next 2 line to place a label on the entry 
        #self.top=Label(self,text="text area").pack(padx=45,pady=100)
        #self.e=Entry(self,bd=5,font=("Arial",25),textvariable=self.var1).pack(fill=X,pady=0)
        #self.bttn=Button(self,text="enter",command=self.print_var).pack(fill=X,pady=0)
        #self.e2=Entry(self, show='*', font=('Arial', 14)).pack(fill=X,pady=0)#for pwd endtry
        self.update_Clock()
    def print_var(self):
        value = str(self.var1.get())   
        #self.var1.set(value)  
        print(value)
        self.top.config(text="dd")
    def place_output(self,img):
        self.heading=Label(self,text="Output image",fg="#000000",height=2,font=("Helvetica",8)).pack(padx=100,pady=0)
        img=img.resize((500,300))
        img1=ImageTk.PhotoImage(img)
        imgq=Label(self,image=img1)
        imgq.image=img1
        imgq.pack(side=RIGHT)
    
    def convert_BnW(self):
        img3=cv.imread(self.s,0)
        img=Image.fromarray(img3)
        self.place_output(img)

    def convert_edge(self):
        img3=cv.imread(self.s,1)
        edges = cv.Canny(img3,100,200)
        img=Image.fromarray(edges)
        self.place_output(img)    

    def askFile(self):
        self.s=fd.askopenfilename(title="select file",filetypes=(("jpeg files","*.jpg"),("all files",".*")))
        img3=cv.imread(self.s,1)
        img=Image.fromarray(img3)
        img=img.resize((350,350))
        img1=ImageTk.PhotoImage(img)
        imgq=Label(self,image=img1)
        imgq.image=img1
        imgq.pack(side=LEFT,padx=90)
    def face_recog(self):
        a=cv.imread(self.s,1)
        cascade_face = cv.CascadeClassifier('C:\\Users\\abc\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
        faces=cascade_face.detectMultiScale(a,scaleFactor=1.05,minNeighbors=5)
        for x,y,w,h in faces:
            a=cv.rectangle(a,(x,y),(x+w,y+h),(0,255,0),3)
        img=Image.fromarray(a)
        self.place_output(img)    
    def clickExitButton(self):
        lbl=Label(self,text="hello world")
        lbl.grid(column=12,row=0)
    def update_Clock(self):
        t=time.strftime("%H:%M:%S")
        self.la.configure(text=t)
        self.after(1000,self.update_Clock)

       
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("520x520")
root.mainloop()
