# encoding: utf-8

#By Nelson Vieira

from tkinter import *
  
class Application:

#layout

    
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.titulo = Label(master, text="DayTime 2.0", width=15)
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()

        self.R1 = Radiobutton(master, text="Hemisfério Norte",variable=var, value=1,command=self.command)
        self.R1["font"] = ("Arial", "10", "bold")
        self.R1.pack( anchor = W)

        self.R2 = Radiobutton(master, text="Hemisfério Sul", variable=var, value=2,command=self.command)
        self.R2["font"] = ("Arial", "10", "bold")
        self.R2.pack( anchor = W )

        self.lb1 = Label(master, text="Dia" , font="Arial",width=20)
        self.lb1["font"]=("Arial", "10", "bold")
        self.lb1.pack()

        self.w1 = Scale(master, from_=1, to=31, orient=HORIZONTAL, width=20) 
        self.w1.pack(fill=X, padx=10)

        self.lb2 = Label(master, text="Mês" , font="Arial",width=20)
        self.lb2["font"]=("Arial", "10", "bold")
        self.lb2.pack()

        self.w2 = Scale(master, from_=1, to=12, orient=HORIZONTAL, width=20) 
        self.w2.pack(fill=X, padx=10)

        self.lb3 = Label(master, text="Verão", bg='light blue', font="Arial",width=20)
        self.lb3["font"]=("Arial", "20", "bold")
        self.lb3.pack()

        self.b1 = Button(master, text = 'OK', fg ='red',width=20,command=self.command) 
        self.b1["font"] = ("Arial", "20", "bold")
        self.b1.pack(anchor=CENTER) 


    def command(self):

        if(var.get()==1):
            lis=lisN
        elif(var.get()==2):
            lis=lisS

        print("Teste"+str(var.get()))

#system

#programa receba o dia e mês e retorna estação do ano!


        D=self.w1.get()
        M=self.w2.get()

         
        if( M in (1,2)):
            self.lb3["text"]=lis[0]
        elif(M==3):
            if(D<21):
                self.lb3["text"]=lis[0]
            else:
                self.lb3["text"]=lis[1]               
        elif( M in (4,5)):
            self.lb3["text"]=lis[1]
        elif(M==6):
            if(D<21):
                self.lb3["text"]=lis[1]
            else:
                self.lb3["text"]=lis[2]
        elif( M in (7,8)):
            self.lb3["text"]=lis[2]
        elif(M==9):
             if(D<21):
                self.lb3["text"]=lis[2]
             else:
                self.lb3["text"]=lis[3]
        elif( M in (10,11)):
            self.lb3["text"]=lis[3]
        elif(M==12):
            if(D<21):
                self.lb3["text"]=lis[3]
            else:
                self.lb3["text"]=lis[3]

        if(self.lb3["text"]== "Verão"):
            self.lb3["bg"]='orange'

        elif(self.lb3["text"]== "Outono"):
            self.lb3["bg"]='light yellow'

        elif(self.lb3["text"]== "Primavera"):
            self.lb3["bg"]='light yellow'

        elif(self.lb3["text"]== "Inverno"):
            self.lb3["bg"]='light blue'

#definições
lis=[]
lisN=["Verão","Outono","Inverno","Primavera"]
lisS=["Inverno","Primavera","Verão","Outono"]
lis=lisS


x1=0
x2=0
root = Tk()
var = IntVar()
Application(root)
root.title("Simple Prog")
root.mainloop()
root.geometry("500x300+50+50")

