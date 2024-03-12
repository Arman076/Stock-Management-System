from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Welcome to Inventory")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
    #============================================ALL VARIABLE==============================
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
    
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_emp_id=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        #self.var_address=StringVar()
        self.var_salary=StringVar()
        
        
        
    #===================================================Search Frame=========================================================================
        lbl_Search_Frame=LabelFrame(self.root,text="Search Employee",font=("times new roman",15),relief=RIDGE,bd=2,background="white",fg="red")
        lbl_Search_Frame.place(x=200,y=20,height=70,width=600)
    
    
        # btn_Search= Button(lbl_Search_Frame,text="Search",font=("Times new roman",20,"bold"),bg="green",fg="white",anchor="w")
        # btn_Search.place(x=500,y=20,width=180,height=50)
    
    #===========================================options=================================================================================
        cmb_search=ttk.Combobox(lbl_Search_Frame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(lbl_Search_Frame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=10)
        
        btn_Search= Button(lbl_Search_Frame,text="Search",command=self.search,font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2")
        btn_Search.place(x=410,y=10,width=150,height=30)
        
        
     #=====================================================title========================================================================
     
        lbl_title =  Label(self.root,text="Employee Details",font=("times new roman",15),relief=RIDGE,bd=2,background="blue",fg="red").place(x=50,y=100,width=1000)
        
        #=============================================content=========================================
        #row 1
        lbl_empid =  Label(self.root,text="Emp ID",font=("times new roman",15),background="white",fg="red").place(x=50,y=150)
        lbl_gender =  Label(self.root,text="Gender",font=("times new roman",15),background="white",fg="red").place(x=350,y=150)
        lbl_contact =  Label(self.root,text="Contact",font=("times new roman",15),background="white",fg="red").place(x=750,y=150)
        
        txt_empid =  Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=150,width=180)
        #txt_gender =  Entry(self.root,textvariable=self.var_gender,font=("times new roman",15),background="white",fg="red").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Transgender"),state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact =  Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),background="lightyellow",fg="red").place(x=850,y=150,width=180)
        
        #row 2
        
        lbl_name =  Label(self.root,text="Name",font=("times new roman",15),background="white",fg="red").place(x=50,y=190)
        lbl_dob =  Label(self.root,text="D.O.B",font=("times new roman",15),background="white",fg="red").place(x=350,y=190)
        lbl_doj =  Label(self.root,text="D.O.J",font=("times new roman",15),background="white",fg="red").place(x=750,y=190)
        
        txt_name =  Entry(self.root,textvariable=self.var_name,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=190,width=180)
        txt_dob =  Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),background="white",fg="red").place(x=500,y=190,width=180)
        txt_doj =  Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),background="lightyellow",fg="red").place(x=850,y=190,width=180)
        
        
        #===row 3
        
        lbl_email =  Label(self.root,text="Email",font=("times new roman",15),background="white",fg="red").place(x=50,y=230)
        lbl_password =  Label(self.root,text="Password",font=("times new roman",15),background="white",fg="red").place(x=350,y=230)
        lbl_utype =  Label(self.root,text="User Type",font=("times new roman",15),background="white",fg="red").place(x=750,y=230)
        
        txt_email =  Entry(self.root,textvariable=self.var_email,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=230,width=180)
        txt_password =  Entry(self.root,textvariable=self.var_password,font=("times new roman",15),background="white",fg="red").place(x=500,y=230,width=180)
        #txt_utype =  Entry(self.root,textvariable=self.var_utype,font=("times new roman",15),background="lightyellow",fg="red").place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        
        #===row 4
        
        lbl_address =  Label(self.root,text="Address",font=("times new roman",15),background="white",fg="red").place(x=50,y=270)
        lbl_salary =  Label(self.root,text="Salary",font=("times new roman",15),background="white",fg="red").place(x=500,y=270)
        
        self.txt_address =  Text(self.root,font=("times new roman",15),background="lightyellow",fg="red")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary =  Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),background="white",fg="red").place(x=600,y=270,width=180)
        
        
        #==============button
        
        
        btn_add= Button(self.root,text="Add",command=self.add,font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=30)
        btn_update= Button(self.root,text="Update",command=self.update,font=("Times new roman",20,"bold"),bg="orange",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=30)
        btn_delete= Button(self.root,text="Delete",command=self.delete,font=("Times new roman",20,"bold"),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=30)
        btn_clear= Button(self.root,text="Clear",command=self.clear,font=("Times new roman",20,"bold"),bg="gray",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=30)
        
        #================================Employee Details=================================
        
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable = ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("password",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(expand=1,fill=BOTH)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()

#==============================FUNCTION STARTED HERE==========================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee Id Already Assigned",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,password,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                                self.var_emp_id.get(),
                                                                self.var_name.get(),
                                                                self.var_email.get(),
                                                                self.var_gender.get(),
                                                                self.var_contact.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.var_password.get(),
                                                                self.var_utype.get(),
                                                                self.txt_address.get('1.0',END),
                                                                self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Successfully","Employee Data Has Been Added Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
            
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
                
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        
        self.var_password.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,utype=?,address=?,salary=? where eid=?",(
                                                                self.var_name.get(),
                                                                self.var_email.get(),
                                                                self.var_gender.get(),
                                                                self.var_contact.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.var_password.get(),
                                                                self.var_utype.get(),
                                                                self.txt_address.get('1.0',END),
                                                                self.var_salary.get(),
                                                                self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Successfully","Employee Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Data Deleted successfully",parent=self.root)
                        #self.show()
                        self.clear()
                
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        
        self.var_dob.set("")
        self.var_doj.set("")
        
        self.var_password.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Text Field Are input Required",parent=self.root)
            else:
                cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
                
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
        
            

if __name__=="__main__":       
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()