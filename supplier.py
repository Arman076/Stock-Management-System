from tkinter import*
from PIL import Image,ImageTk

class SupplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Welcome to Inventory")
        self.root.config(bg="white")
        
        
        #==========================================Title===========================================
        lbl_title=Label(self.root,text="Manage Supplier Deatils",justify=CENTER,anchor="w",font=("times new roman",15,"bold"),bg="blue",fg="gold").place(x=0,y=10,height=50,width=1000)
        
        lbl_Invoice = Label(self.root,text="Invoice No",font=("times new roman",15),fg="black",bg="white").place(x=10,y=90)
        lbl_Invoice_Txt = Entry(self.root,fg="gold",bg="lightyellow").place(x=150,y=90,width=200)
        
        lbl_supplier = Label(self.root,text="Supplier Name",font=("times new roman",15),fg="black",bg="white").place(x=10,y=140)
        lbl_supplier = Entry(self.root,fg="gold",bg="lightyellow").place(x=150,y=150,width=200)
        
        lbl_contact = Label(self.root,text="Contact No",font=("times new roman",15),fg="black",bg="white").place(x=10,y=190)
        lbl_contact_Txt = Entry(self.root,fg="gold",bg="lightyellow").place(x=150,y=190,width=200)
        
        lbl_Description = Label(self.root,text="Description",font=("times new roman",15),fg="black",bg="white").place(x=10,y=240)
        lbl_Description_Txt = Entry(self.root,fg="gold",bg="lightyellow").place(x=150,y=240,width=400,height=100)
        
        
        #=========================================BUTTON=====================================================
        
          
        
        
        btn_add= Button(self.root,text="Save",font=("Times new roman",20,"bold"),bg="green",fg="white",cursor="hand2").place(x=150,y=360,width=110,height=30)
        btn_update= Button(self.root,text="Update",font=("Times new roman",20,"bold"),bg="orange",fg="white",cursor="hand2").place(x=280,y=360,width=110,height=30)
        btn_delete= Button(self.root,text="Delete",ont=("Times new roman",20,"bold"),bg="red",fg="white",cursor="hand2").place(x=410,y=360,width=110,height=30)
        btn_clear= Button(self.root,text="Clear",font=("Times new roman",20,"bold"),bg="gray",fg="white",cursor="hand2").place(x=550,y=360,width=110,height=30)
        
        
        
if __name__=="__main__":       
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()