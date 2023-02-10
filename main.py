from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master =master
        self.master.title("test login system")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg = "powder blue")
        self.frame = Frame(self.master, bg = "powder blue")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Login System Demo', font=("arial", 50, "bold"), bg = 'powder blue', fg='black')
        self.lblTitle.grid(row =0, column =0, columnspan =2, pady=40)

#================================================================<login frames>=============================================================#

        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600, font=("arial", 20, "bold"), relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600, font=("arial", 20, "bold"), relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

#===============================================================<label & entry>=============================================================#
        
        self.lblUsername=Label(self.LoginFrame1, text = "Username", font=("arial", 20, "bold"), bd =22,bg ='cadet blue', fg = 'cornsilk')
        self.lblUsername.grid(row=0, column =0)
        self.txtUsername=Entry(self.LoginFrame1, font=("arial", 20, "bold"), textvariable = self.Username, bd =22,bg ='cadet blue', fg = 'cornsilk')
        self.txtUsername.grid(row=0, column =1)

        self.lblPassword=Label(self.LoginFrame1, text = "Password", font=("arial", 20, "bold"), bd =22,bg ='cadet blue', fg = 'cornsilk')
        self.lblPassword.grid(row=1, column =0)
        self.txtPassword=Entry(self.LoginFrame1, font=("arial", 20, "bold"), show ='*', textvariable = self.Password, bd =22,bg ='cadet blue', fg = 'cornsilk')
        self.txtPassword.grid(row=1, column =1)


#==================================================================<buttons>=================================================================#
        
        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width =17, font=("arial", 20, "bold"), command = self.Login_system)
        self.btnLogin.grid(row=3, column =0, pady =20, padx=8)
        
        self.btnLogin = Button(self.LoginFrame2, text = 'Reset', width =17, font=("arial", 20, "bold"), command =self.Reset)
        self.btnLogin.grid(row=3, column =1, pady =20, padx=8)

        self.btnLogin = Button(self.LoginFrame2, text = 'Exit', width =17, font=("arial", 20, "bold"), command =self.iExit)
        self.btnLogin.grid(row=3, column =2, pady =20, padx=8)

#===============================================================<login control>==============================================================#

    def Login_system(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u ==str(123) and p ==str(123)):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        
        else:
            tkinter.messagebox.askyesno("Login Systems", "Too Bad, invalid login details. Continue?")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
            
#===============================================================<login control [reset]>======================================================#
            
    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login Systems", "Conf. you wish to exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return    

def new_window(self):
    self.newWindow = Toplevel(self.master)
    self.app = Window2(self.newWindow)
        
class Window2:
    def __init__(self, master):
        self.master =  master
        self.master.title("test management system")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg = "cadet blue")
        self.frame = Frame(self.master, bg = "powder blue")
        self.frame.pack()
        
#===============================================================<what happens when you login>==================================================#
        
        self.LoginFrame3 = LabelFrame(self.frame, width=1350, height=100, font=("arial", 20, "bold"), relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame3.grid(row= 0, column=0)


        self.lblTitle = Label(self.frame, text = 'THANKS FOR LOGGING IN', bg ='cadet blue', font=("arial", 18, "bold"), fg='black')
        self.lblTitle.grid(row = 0, column =0, columnspan =2)




if __name__== '__main__':
    main()
