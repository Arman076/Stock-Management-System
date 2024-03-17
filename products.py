from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Welcome to Stock")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #variable
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        print(type(self.var_status))
        print(type(self.var_qty))
        
        
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)
        
        #title
        
        lbl_title =  Label(product_frame,text="Product Details",font=("times new roman",20),relief=RIDGE,bd=2,background="blue",fg="red").pack(side=TOP,fill=X)
        #====================================column 1============================
        lbl_category =  Label(product_frame,text="Category",font=("times new roman",15),background="white").place(x=30,y=60)
        lbl_supplier =  Label(product_frame,text="Supplier",font=("times new roman",15),background="white",fg="red").place(x=30,y=110)
        lbl_product_name =  Label(product_frame,text="Name",font=("times new roman",15),background="white",fg="red").place(x=30,y=160)
        lbl_price =  Label(product_frame,text="Price",font=("times new roman",15),background="white",fg="red").place(x=30,y=210)
        lbl_quantity =  Label(product_frame,text="Quantity",font=("times new roman",15),background="white",fg="red").place(x=30,y=260)
        lbl_status =  Label(product_frame,text="Status",font=("times new roman",15),background="white",fg="red").place(x=30,y=310)
        
        #======================================ComboBox Column 2=================================================
        
        cmb_category=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_category.place(x=150,y=60,width=180)
        cmb_category.current(0)
        
        cmb_supplier=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_supplier.place(x=150,y=110,width=180)
        cmb_supplier.current(0)
        
        txt_product_name =  Entry(product_frame,textvariable=self.var_name,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=160,width=180)
        
        txt_price =  Entry(product_frame,textvariable=self.var_price,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=210,width=180)
        
        txt_quantity =  Entry(product_frame,textvariable=self.var_qty,font=("times new roman",15),background="lightyellow",fg="red").place(x=150,y=260,width=180)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Select","Active","InActive"),state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_status.place(x=150,y=310,width=180)
        cmb_status.current(0)
        
        #==========================BUTTON==============================
        
        btn_add= Button(product_frame,text="Add",command=self.add,font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update= Button(product_frame,text="Update",command=self.update,font=("Times new roman",20,"bold"),bg="orange",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete= Button(product_frame,text="Delete",command=self.delete,font=("Times new roman",20,"bold"),bg="red",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear= Button(product_frame,text="Clear",command=self.clear,font=("Times new roman",20,"bold"),bg="gray",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
        
        #===================================================Search Frame=========================================================================
        lbl_Search_Frame=LabelFrame(self.root,text="Search Product",font=("times new roman",15),relief=RIDGE,bd=2,background="white",fg="red")
        lbl_Search_Frame.place(x=480,y=10,height=80,width=600)
        
        
        cmb_search=ttk.Combobox(lbl_Search_Frame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(lbl_Search_Frame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=10)
        
        btn_Search= Button(lbl_Search_Frame,text="Search",command=self.search,font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2")
        btn_Search.place(x=410,y=10,width=150,height=30)
        
        #==========================================Tree View=====================================================
        
        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.product_Table = ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        
        self.product_Table.heading("pid",text="P_id")
        self.product_Table.heading("Category",text="Category")
        self.product_Table.heading("Supplier",text="Supplier")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Qty")
        self.product_Table.heading("status",text="Status")
        
        
        self.product_Table["show"]="headings"
        
        self.product_Table.column("pid",width=90)
        self.product_Table.column("Category",width=100)
        self.product_Table.column("Supplier",width=100)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
      
        
        self.product_Table.pack(expand=1,fill=BOTH)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_cat_sup()
        
      #=======================Functions  
    
    def fetch_cat_sup(self):  
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                cur.execute("Select name from category")
                cat=cur.fetchall()
                self.cat_list.append("Empty")
                #print(cat)
                
                #cat_list=[]
                if len(cat)>0:
                    del self.cat_list[:]
                    self.cat_list.append("Select")
                
                for i in cat:
                    self.cat_list.append(i[0])
                #print(cat_list)
                
                cur.execute("Select name from supplier")
                sup=cur.fetchall()
                
                if len(sup)>0:
                    del self.sup_list[:]
                    self.sup_list.append("Select")
                
                for i in sup:
                    self.sup_list.append(i[0])
                
                #print(sup)
                
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All Field Are Required",parent=self.root)
            else:
                cur.execute("Select * from producted where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This product Already Available",parent=self.root)
                else:
                    cur.execute("Insert into producted (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                                                self.var_cat.get(),
                                                                self.var_sup.get(),
                                                                self.var_name.get(),
                                                                self.var_price.get(),
                                                                self.var_qty.get(),
                                                                self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Successfully","products Data Has Been Added Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
          
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from producted")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","product Id Select In The List ",parent=self.root)
            else:
                cur.execute("Select * from producted where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID",parent=self.root)
                else:
                    cur.execute("Update producted set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                                                self.var_cat.get(),
                                                                self.var_sup.get(),
                                                                self.var_name.get(),
                                                                self.var_price.get(),
                                                                self.var_qty.get(),
                                                                self.var_status.get(),
                                                                self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Successfully","product Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","product Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from producted where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from producted where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","product Data Deleted successfully",parent=self.root)
                        #self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Select")
        self.var_pid.set("")
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
                cur.execute("Select * from producted where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
        
if __name__=="__main__":       
    root=Tk()
    obj=productClass(root)
    root.mainloop()