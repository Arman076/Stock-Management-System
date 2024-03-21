from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass 
import smtplib
import time

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login System")
        self.root.config(bg="#fafafa")
        
        self.otp=''
        
        self.var_employee_id=StringVar()
        self.var_pass=StringVar()
        
        
        self.phone_image=ImageTk.PhotoImage(file="menu.webp")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=80,width=400,height=300)
        
        
        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        
        title = Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="red").place(x=0,y=30,relwidth=1)       
        
        lbl_user=Label(login_frame,text="Enployee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100) 
        txt_user=Entry(login_frame,textvariable=self.var_employee_id,font=("times new roman",12),bg="lightyellow",fg="green").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200) 
        txt_pass=Entry(login_frame,textvariable=self.var_pass,font=("times new roman",12),bg="lightyellow",fg="green").place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("times new roman",15),bg="gold",fg="red",activebackground="green").place(x=50,y=300,width=250,height=35)
        btn_forget=Button(login_frame,text="forget password",command=self.forget_window,font=("times new roman",13),bg="white",fg="red",bd=0,activebackground="green",activeforeground="pink").place(x=100,y=390)
        
        
        hr_lbl=Label(login_frame,text="",bg="gray").place(x=50,y=370,width=250,height=2)
        or_lbl=Label(login_frame,text="OR",font=("times new roman",15),bg="white",fg="red").place(x=150,y=355)
        
        
        
        
        
        register_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=Label(register_frame,text="Don't Have An Account ?",font=("times new roman",15),bg="gold",fg="red").place(x=40,y=20)
        btn_sign_up=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="red",bd=0,activebackground="green",activeforeground="orange").place(x=246,y=17)
        
        
        self.im1=ImageTk.PhotoImage(file="2.png")
        self.im2=ImageTk.PhotoImage(file="category.png")
        self.im3=ImageTk.PhotoImage(file="category2.jpg")
        
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=200,y=80,width=400,height=300)
        
        self.animate()
        #self.send_email('xyz')
        
    #====================================ALL FUNCTION================================
     
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
        
    def login(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_employee_id.get()=="" or self.var_pass.get()=="":
                messagebox.showerror("Error","All field are required",parent=self.root)
            else:
                cur.execute("select utype from employees where eid=? AND password=?",(self.var_employee_id.get(),self.var_pass.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python Dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                    
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
    def forget_window(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee Id Must Be Required")
            
            else:
                cur.execute("select email from employees where eid=? ",(self.var_employee_id.get(),))
                email=cur.fetchone()
                
                if email==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root)
                else:
                    
                    #====================varibale forget win=============
                    
                    
                    #=============forget window=============
                   self.var_otp=StringVar()
                   self.var_new_pass=StringVar()
                   self.var_conf_pass=StringVar()
                   
                   #call send email function======================
                   
                   chk=self.send_email(email[0])
                   
                   if chk=='f':
                       messagebox.showerror("Error","Connection Error Try Again",parent=self.root)
                   else:
                       

                   
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title("RESET PASSWORD")
                    self.forget_win.geometry("400x350+500+100")
                    self.forget_win.focus_force()
                    
                    title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="blue",fg="green").pack(side=TOP,fill=X)
                    
                    lbl_reset=Label(self.forget_win,text="Enter OTP sent on registered email",font=("goudy old style",15,"bold")).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                    
                    self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("goudy old style",15,"bold"),bg="lightblue",fg="green")
                    self.btn_reset.place(x=280,y=100,width=100,height=30)
                    
                    lbl_new_pass=Label(self.forget_win,text="New Password",font=("goudy old style",15,"bold")).place(x=20,y=160)
                    new_pass_txt=Entry(self.forget_win,textvariable=self.var_new_pass,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                    
                    conf_pass=Label(self.forget_win,text="Confirm Password",font=("goudy old style",15,"bold")).place(x=20,y=225)
                    conf_pass_txt=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                    
                    self.btn_update=Button(self.forget_win,text="UPDATE",command=self.update_password,state=DISABLED,font=("goudy old style",15,"bold"),bg="lightblue",fg="green")
                    self.btn_update.place(x=150,y=300,width=100,height=30)
                   
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
            
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_conf_pass.get():            
             messagebox.showerror("Error","Password Must Be Same",parent=self.forget_win)
        
        else:
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            
            try:
                cur.execute("Update employees SET password=? where eid=?",(self.var_new_pass.get(),self.var_employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                self.forget_win.destroy()
                
            except Exception as ex:
                messagebox.showerror("Error",f"due to :{str(ex)}")
                
            
        
        
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP",parent=self.forget_win)
            
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_ =email_pass.email_
        pass_ = email_pass.pass_
        
        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        #print(self.otp)
        
        subj='IMS-RESET PASSWORD OTP'
        msg=f"Dear Sir Madam \n\n Your Reset Otp Is {str(self.otp)}.\n\nWith Regards, \n IMS Team"
        msg="Subject {}\\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)#1st para from second parameter to third parameter what msg you send
        chk=s.ehlo()
        
        if chk[0]==250:
            return 's'
        else:
            return 'f'
        
        
    
            
        
if __name__=="__main__":       
    root=Tk()
    obj=Login(root)
    root.mainloop()