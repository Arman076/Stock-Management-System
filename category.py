from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class category_Class:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Welcome to Inventory")
        self.root.config(bg="white")
        
        #==================variables================
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
    #==============================title===============
    
        lbl_title = Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name = Label(self.root,text="Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
        
        btn_add = Button(self.root,text="ADD",command=self.add,font=("goudy old style",18),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,height=30,width=150)
        btn_delete = Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",18),bg="red",fg="white",cursor="hand2").place(x=520,y=170,height=30,width=150)

        #btn_name = Button(self.root,text="ADD",font=("goudy old style",18),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,height=30,width=150)
        
        
    #=================TREE VIEW========================
    
        cat_frame = Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.Category_Table = ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Category_Table.xview)
        scrolly.config(command=self.Category_Table.yview)
        
        self.Category_Table.heading("cid",text="C ID")
        self.Category_Table.heading("name",text="Name")
        
        self.Category_Table["show"]="headings"
        
        self.Category_Table.column("cid",width=90)
        self.Category_Table.column("name",width=100)
        
        self.Category_Table.pack(expand=1,fill=BOTH)
        self.Category_Table.bind("<ButtonRelease-1>",self.get_data)

    #========================Imgaes
    
        self.im1=Image.open("category.png")
        self.im1=self.im1.resize((500,250),Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=10,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        
        self.im2=Image.open("category2.jpg")
        self.im2=self.im2.resize((500,250),Image.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2=Label(self.root,image=self.im2,bd=10,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        
        self.show()
        
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name Required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category Already There",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Successfully","category Data Has Been Added Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"due to :{str(ex)}")
            
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.Category_Table.delete(*self.Category_Table.get_children())
            for row in rows:
                self.Category_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.Category_Table.focus()
        content=(self.Category_Table.item(f))
        row=content['values']
        #print(row)
        
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","please select category from the list",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Try Again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","category Data Deleted successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
                       
      
        

if __name__=="__main__":       
    root=Tk()
    obj=category_Class(root)
    root.mainloop()