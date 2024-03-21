from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from suppliers import SupplierClass
from category import category_Class
from products import productClass
from sales import SalesClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Welcome to Stock")
        self.root.config(bg="white")
        
        #===========================================HEADING========================================================================================
        self.icon_title=PhotoImage(file="2.png")
        title=Label(self.root,text="Stock Managemnt System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),fg="#010c48",bg="white",anchor="w",padx=100).place(x=0,y=0,relwidth=1,height=70)
        
        #=========================================================LOG_OUT BUTTON====================================================================================
        btn_log_out=Button(self.root,text="log out",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1250,y=10,height=50,width=150)
        
        #=============================================================CLOCK========================================================================================
        self.lbl_clock=Label(self.root,text="Welcome Stock Managemnt System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="blue",anchor="w",padx=500)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #===================================================LEFT MENU=================================================================================================
        self.MenuLogo = Image.open("menu.webp")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root,bd = 2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)  
        
        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)    
        
        #============================================================================BUTTON===========================================================================  
        self.icon_side=Image.open("side.png")       
        self.icon_side = self.icon_side.resize((50,40),Image.LANCZOS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="green").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employees,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_cateogery=Button(LeftMenu,text="Cateogery",command=self.category,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_products=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        #====================================================================content==================================================================================
        self.lbl_employee = Label(self.root,text="Total Employee\n [0]",bd=2,relief=RIDGE,bg = "black" , fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier = Label(self.root,text="Total Supplier\n [0]",bd=2,relief=RIDGE,bg = "black" , fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category = Label(self.root,text="Total Category\n [0]",bd=2,relief=RIDGE,bg = "black" , fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product = Label(self.root,text="Total Product\n [0]",bd=2,relief=RIDGE,bg = "black" , fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales = Label(self.root,text="Total Sales\n [0]",bd=2,relief=RIDGE,bg = "black" , fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        #=============================================================Footer========================================================================================
        self.footer=Label(self.root,text="IMS-Inventory Mgmt System | Developer By Arman\n Any Technical Issue Contact Me : 7977933346",font=("times new roman",12),bg="#4d636d",fg="blue",anchor="w",padx=500)
        self.footer.pack(side=BOTTOM,fill=X)
        
        self.update_content()
        
    def employees(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=category_Class(self.new_win)
    
    def product(self):
        self.new_obj=Toplevel(self.root)
        self.new_obj=productClass(self.new_obj)
        
    def sales(self):
        self.new_obj=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_obj)
        
    def update_content(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employees")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")
            
            cur.execute("select * from suppliers")
            suppliers=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n[ {str(len(suppliers))} ]")
            
            cur.execute("select * from categorys")
            categorys=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(categorys))} ]")
            
            cur.execute("select * from producteds")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales \n [ {str(bill)}]')
            
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=F"Welcome Stock Managemnt System\t\t Date:{str(date_)}\t\t Time: {str(time_)}",)
            self.lbl_clock.after(200,self.update_content)
            
        except Exception as ex:
            messagebox.showerror("","",parent=self.root)
            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
            
        
if __name__=="__main__":       
    root=Tk()
    obj=IMS(root)
    root.mainloop()