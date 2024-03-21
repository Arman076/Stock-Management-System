from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import datetime
import time
import os
import tempfile


class Billing_Class:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Welcome to Inventory")
        self.root.config(bg="white")
        
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        self.var_search=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_cal_input=StringVar()
        self.cart_list=[]
        self.chk_print=0
        
        
        #===========================================HEADING========================================================================================
        self.icon_title=PhotoImage(file="2.png")
        title=Label(self.root,text="Stock Managemnt System",font=("times new roman",40,"bold"),fg="white",bg="black",anchor="w",padx=400).place(x=0,y=0,relwidth=1,height=70)
        
        #=========================================================LOG_OUT BUTTON====================================================================================
        btn_log_out=Button(self.root,text="log out",command=self.logout,font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2").place(x=1250,y=10,height=50,width=150)
        
        #=============================================================CLOCK========================================================================================
        self.lbl_clock=Label(self.root,text="Welcome Stock Managemnt System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="black",fg="white",anchor="w",padx=500)
        self.lbl_clock.place(x=0,y=80,relwidth=1,height=30)
        
        
        #========================================Product Frame =========================
        
        ProductFrame1=Frame(self.root,bd=3,relief=RIDGE,bg="black")
        ProductFrame1.place(x=10,y=120,width=410,height=550)
        
        
        pTitle=Label(ProductFrame1,text="All Product",font=("goudy old style",20,"bold"),bg="green",fg="white").pack(side=TOP,fill=X)
        
        #============================================PRODUCT EARCH FRAME===================================
        
        ProductFrame2=Frame(ProductFrame1,bd=3,relief=RIDGE,bg="black")
        ProductFrame2.place(x=2,y=42,width=390,height=90)
        
        lbl_search=Label(ProductFrame2,text="Search Product By Name",font=("goudy old style",15,"bold"),bg="black",fg="white").place(x=2,y=5)
        lbl_name=Label(ProductFrame2,text="Product Name",font=("goudy old style",15,"bold"),bg="black",fg="white").place(x=5,y=45)
        
        txt_search =  Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),background="lightyellow",fg="red").place(x=135,y=47,width=150,height=22)
        
        #txt_price =  Entry(ProductFrame2,textvariable=self.var_price,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=210,width=180)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="black",fg="white",activebackground="green",activeforeground="red",cursor="hand2").place(x=290,y=45,width=90,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="black",fg="white",activebackground="green",activeforeground="red",cursor="hand2").place(x=285,y=10,width=100,height=25)

        #=======================Product DETAILS Frame=====================
        
        
        Product_Frame3 = Frame(ProductFrame1,bd=3,relief=RIDGE)
        Product_Frame3.place(x=2,y=140,width=380,height=385)
        
        scrolly=Scrollbar(Product_Frame3,orient=VERTICAL)
        scrollx=Scrollbar(Product_Frame3,orient=HORIZONTAL)
        
        self.ProductTable = ttk.Treeview(Product_Frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("pid",text="PID")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="QTY")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"
        
        self.ProductTable.column("pid",width=50)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=40)
        self.ProductTable.column("status",width=90)
        
        self.ProductTable.pack(expand=1,fill=BOTH)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(Product_Frame3,text="Note Enter 0 QTY to remove the product",font=("goudy old style",15),anchor="w",fg="red").pack(side=BOTTOM,fill=X)
        
        
        #===============================Customer Frame========================================== 
        
        CustomerFrame=Frame(self.root,bd=3,relief=RIDGE,bg="black")
        CustomerFrame.place(x=430,y=120,width=530,height=70)
        
        
        
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray",fg="black").pack(side=TOP,fill=X)
        
        
        lbl_cname=Label(CustomerFrame,text="Name",font=("goudy old style",15,),bg="black",fg="white").place(x=5,y=35)
        lbl_ccontact=Label(CustomerFrame,text="Contact No",font=("goudy old style",15,"bold"),bg="black",fg="white").place(x=270,y=35)
        
        txt_name =  Entry(CustomerFrame,textvariable=self.var_name,font=("times new roman",15),background="lightyellow",fg="red").place(x=80,y=35,width=180)
        txt_contact =  Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",15),background="lightyellow",fg="red").place(x=380,y=35,width=140)
        
        
        #==============================================================MAIN FRAME CALCULATOR AND CART=======================================
        
        Cal_Cart_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="black")
        Cal_Cart_Frame.place(x=430,y=195,width=530,height=370)
        
        #=========================================================CALCULATOR FRAME===========================================================
        
        Cal_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        
        
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,bg="white",font=("arial",15,"bold"),bd=9,width=21,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text='7',font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text='4',font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text='1',font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2",fg="black").grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text='0',font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=20,cursor="hand2",fg="black").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='C',command=self.clear,font=("arial",15,"bold"),bd=5,width=4,pady=20,cursor="hand2",fg="black").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',command=self.perform_cal,font=("arial",15,"bold"),bd=5,width=4,pady=20,cursor="hand2",fg="black").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=20,cursor="hand2",fg="black").grid(row=4,column=3)
        
        
        #============================================================CART FRAME=================================================================
        
        Cart_Frame = Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)
        
        self.cartTitle=Label(Cart_Frame,text="Cart Total Product:\t [0]",font=("goudy old style",15),bg="lightgray",fg="black")
        self.cartTitle.pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        
        self.CartTable = ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        #self.CartTable.heading("status",text="Status")
        self.CartTable["show"]="headings"
        
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        #self.CartTable.column("status",width=90)
        
        self.CartTable.pack(expand=1,fill=BOTH)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
        
        #=========================ADD CART WIDGET BFRAME=============================
        
        
        
        Add_Cart_Widget=Frame(self.root,bd=3,relief=RIDGE,bg="black")
        Add_Cart_Widget.place(x=430,y=560,width=530,height=110)
        
        lbl_p_name=Label(Add_Cart_Widget,text="Product Name",font=("times new roman",15),bg="white",fg="black").place(x=5,y=5)
        txt_p_name=Entry(Add_Cart_Widget,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",fg="blue",state="readonly").place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_Cart_Widget,text="Price Per QTY",font=("times new roman",15),bg="white",fg="black").place(x=230,y=5)
        text_p_price=Entry(Add_Cart_Widget,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",fg="blue",state="readonly").place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_Cart_Widget,text="Quantity",font=("times new roman",15),bg="white",fg="black").place(x=390,y=5)
        txt_p_qty=Entry(Add_Cart_Widget,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow",fg="blue").place(x=390,y=35,width=130,height=22)
        
        
        self.lbl_instock=Label(Add_Cart_Widget,text="In Stock",font=("times new roman",15),bg="white",fg="black")
        self.lbl_instock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_Cart_Widget,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,height=30,width=150)
        btn_add_cart=Button(Add_Cart_Widget,text="Add | Update",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,height=30,width=180)

        
        #txt_p_name=Entry(Add_Cart_Widget,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",fg="blue",state="readonly").place(x=5,y=35,width=190,height=22)
        
        
        
        #==============================================Billing Area===============================================
        
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=963,y=120,width=410,height=410)
        
        
        bTitle=Label(bill_frame,text="Customer Bills",font=("goudy old style",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        
        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        #scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        
        
        #============================================Billing Button===============================================
        
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=963,y=530,width=410,height=140)
        
        
        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n [0]",font=("goudy old style",15,"bold"),background="#3f51b5",fg="white",bd=3)
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(billMenuFrame,text="Bill Discount \n [5%]",font=("goudy old style",15,"bold"),background="#8bc34a",fg="white",bd=3)
        self.lbl_discount.place(x=125,y=5,width=120,height=70)
        
        self.lbl_net_pay=Label(billMenuFrame,text="Bill Net Pay\n [0]",font=("goudy old style",15,"bold"),background="#607d8b",fg="white",bd=3)
        self.lbl_net_pay.place(x=250,y=5,width=150,height=70)
        
         
        btn_print=Button(billMenuFrame,text='Print',command=self.print_bill,font=("arial",15,"bold"),cursor="hand2",bd=5,width=4,pady=20,fg="black",bg="lightgreen")
        btn_print.place(x=2,y=80,width=120,height=50)
       
        btn_clear_all=Button(billMenuFrame,text='Clear All',command=self.clear_all,font=("arial",15,"bold"),cursor="hand2",bd=5,width=4,pady=20,fg="black",bg="gray")
        btn_clear_all.place(x=124,y=80,width=120,height=50)
        
        btn_genrate=Button(billMenuFrame,text='Genrate Save ',command=self.genrate_bill,font=("arial",15,"bold"),cursor="hand2",bd=5,width=4,pady=20,fg="black",bg="#009688")
        btn_genrate.place(x=250,y=80,width=150,height=50)
        
        
        
        self.show()
        #self.bill_top()
        
        self.update_date_time()
        
        
        #===================================ALL function==========================================
        
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))    
        
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
       
        try:
            cur.execute("Select pid,name,price,qty,status from producteds where status='Active'")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
                
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Text Field Are input Required",parent=self.root)
            else:
                cur.execute("Select pid,name,price,qty,status from producteds where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
        
        
    def get_data(self,ev):#first get data method 08-03-2024 all working this
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        
        self.lbl_instock.config(text=f"In stock [{str(row[4])}]")
        self.var_stock.set(row[4])
       
        
    def get_data_cart(self,ev):#second get_data method created by 09-03-2023
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        
        self.lbl_instock.config(text=f"In stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
    
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","plz select product from the list",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Quantity Is Required",parent=self.root)
        # elif int(self.var_qty.get())>int(self.var_stock.get()):its implemented in last time some proble are there
        #     messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
            # price_cal =int(self.var_qty.get())*float(self.var_price.get())
            # price_cal=float(price_cal)
            price_cal=self.var_price.get()
            # cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get()]
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
           
            
        #============================UPDATE CART==============================
            present="no"
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            #print(present,index_)
                
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product Already Present \n Do You Want To Update Or Remove Frome The Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
            
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            # bill_amnt=bill_amnt+float(row[2])
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        
        self.discount=(self.bill_amnt*5)/100
        
        self.net_pay=self.bill_amnt-self.discount
        
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product:[{str(len(self.cart_list))}]")
            
    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
                
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def genrate_bill(self):
        if self.var_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","Customer Details Are Reuired",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Plz Select the Item",parent=self.root)
        else:
            ##======================Bill Top=========================
            self.bill_top()
            #====================Bill Middle=======================
            self.bill_middle()
            #=====================Bill Bottom========================
            self.bill_bottom()
           
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill Has Been Save",parent=self.root)
            self.chk_print=1
        
    def bill_top(self):
        self.invoice=(int(time.strftime("%H%M%S")))+(int(time.strftime("%d%m%Y")))
        bill_top_temp=f'''
\t Welcome To Arman Store
\t Phone:7977933346,Mumbai-400037
{str('='*47)}
Customer Name : {self.var_name.get()}
Phone No:{self.var_contact.get()}
Bill No:{str(self.invoice)}\t\tDate : {str(time.strftime("%d/%m/%Y"))}
{str('='*47)}
Product Name\t\tQTy\tPrice
{str('='*40)} 
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
        
       
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str('='*47)}
Bill Amount\t\t\t\tRs.{self.bill_amnt}
Discount \t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str('='*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
    
    
    def bill_middle(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
        
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=row[3]
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t"+qty+"\tRs."+price)
                
        except Exception as ex:
            messagebox.showerror("Error",f"due to:{str(ex)}",parent=self.root)
    
    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In stock ")
        self.var_stock.set('')
        
        
    
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product:[0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()        
        

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=F"Welcome Stock Managemnt System\t\t Date:{str(date_)}\t\t Time: {str(time_)}",)
        self.lbl_clock.after(200,self.update_date_time)
        
    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","pls wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))  
            os.startfile(new_file,'print') 
        else:
            messagebox.showerror("Error","Plz genrate bill",parent=self.root)     
            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        


if __name__=="__main__":       
    root=Tk()
    obj=Billing_Class(root)
    root.mainloop()