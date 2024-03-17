import sqlite3

#createng a data base
def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,password text,utype text,address text,salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    #"pid","Category","Supplier","name","price","qty","status",
    
    cur.execute("CREATE TABLE IF NOT EXISTS producted(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,qty text,status text)")
    con.commit()
    
   
    
    
create_db()