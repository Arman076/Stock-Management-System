from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import ttk,messagebox
import sqlite3

class SupplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Welcome to Stock")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
    #============================================ALL VARIABLE==============================
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
    
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
        
        
        
        
        
        
    #===================================================Search Frame=========================================================================
        #=Label(self.root,text="Search supplier",font=("times new roman",15),relief=RIDGE,bd=2,background="white",fg="red")
        #self.root.place(x=200,y=10,height=80,width=600)
    
    
      
    
    #===========================================options=================================================================================
        lbl_search=Label(self.root,text="Invoice No",font=("goudy old style",15,"bold"))
        lbl_search.place(x=700,y=80)
       

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=800,y=80,width=150)
        
        btn_Search= Button(self.root,text="Search",command=self.search,font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2")
        btn_Search.place(x=960,y=79,width=100,height=30)
        
        
     #=====================================================title========================================================================
     
        lbl_title =  Label(self.root,text="Supplier Details",font=("times new roman",15),relief=RIDGE,bd=2,background="aqua",fg="white").place(x=50,y=10,width=1000,height=40)
        
        #=============================================content=========================================
        #row 1
        lbl_supplier_invoice =  Label(self.root,text="Invoice No",font=("times new roman",15),background="white",fg="red").place(x=50,y=80)
        txt_supplier_invoice =  Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15),background="lightyellow",fg="red").place(x=180,y=80,width=180)
        
        #row 2
    
        lbl_name =  Label(self.root,text="Name",font=("times new roman",15),background="white",fg="red").place(x=50,y=120)
        txt_name =  Entry(self.root,textvariable=self.var_name,font=("times new roman",15),background="lightyellow",fg="red").place(x=180,y=120,width=180)
        
        #row 3
        
        lbl_contact =  Label(self.root,text="Contact",font=("times new roman",15),background="white",fg="red").place(x=50,y=160)
        txt_contact =  Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),background="lightyellow",fg="red").place(x=180,y=160,width=180)
      
       #row 4 
      
        lbl_description =  Label(self.root,text="Description",font=("times new roman",15),background="white",fg="red").place(x=50,y=200)
        
        self.txt_description =  Text(self.root,font=("times new roman",15),background="lightyellow",fg="red")
        self.txt_description.place(x=180,y=200,width=470,height=120)
        
        
        
        #==============button
        
        
        btn_add= Button(self.root,text="Add",command=self.add,font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update= Button(self.root,text="Update",command=self.update,font=("Times new roman",20,"bold"),bg="orange",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete= Button(self.root,text="Delete",command=self.delete,font=("Times new roman",20,"bold"),bg="red",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear= Button(self.root,text="Clear",command=self.clear,font=("Times new roman",20,"bold"),bg="gray",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)
        
        #================================supplier Details=================================
        
        supplier_frame = Frame(self.root,bd=3,relief=RIDGE)
        supplier_frame.place(x=700,y=120,width=380,height=350)
        
        scrolly=Scrollbar(supplier_frame,orient=VERTICAL)
        scrollx=Scrollbar(supplier_frame,orient=HORIZONTAL)
        
        self.SupplierTable = ttk.Treeview(supplier_frame,columns=("invoice","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("invoice",text="Invoice No")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("description",text="Description")
        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("description",width=100)
        self.SupplierTable.pack(expand=1,fill=BOTH)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        #self.show()

#==============================FUNCTION STARTED HERE==========================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice  Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from suppliers where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Inoice No Already Assigned",parent=self.root)
                else:
                    cur.execute("Insert into suppliers(invoice,name,contact,description) values(?,?,?,?)",(
                                                                self.var_sup_invoice.get(),
                                                                self.var_name.get(),
                                                                self.var_contact.get(),
                                                                self.txt_description.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Successfully","supplier Data Has Been Added Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
            
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from suppliers")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
                
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])
        
        
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from suppliers where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)
                else:
                    cur.execute("Update suppliers set name=?,contact=?,description=? where invoice=?",(
                                                                self.var_name.get(),
                                                                self.var_contact.get(),
                                                                self.txt_description.get('1.0',END),
                                                                self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Successfully","supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoce No Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from suppliers where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from suppliers where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success","supplier Data Deleted successfully",parent=self.root)
                        #self.show()
                        self.clear()
                
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_description.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No Required",parent=self.root)
            else:
                cur.execute("Select * from suppliers where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchall()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in row:
                        self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
                
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
        
            

if __name__=="__main__":       
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()