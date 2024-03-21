import sqlite3

#createng a data base
def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY,name text,email text,gender text,contact text,dob text,doj text,password text,utype text,address text,salary text)")
    # con.commit()
    
    # cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY,name text,contact text,description text)")
    # con.commit()
    
    # cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY,name text)")
    # con.commit()
    # #"pid","Category","Supplier","name","price","qty","status",
    
    # cur.execute("CREATE TABLE IF NOT EXISTS producted(pid INTEGER PRIMARY KEY,Category text,Supplier text,name text,price text,qty text,status text)")
    # con.commit()
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS employees(eid INTEGER PRIMARY KEY,name text,email text,gender text,contact text,dob text,doj text,password text,utype text,address text,salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS suppliers(invoice INTEGER PRIMARY KEY,name text,contact text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS categorys(cid INTEGER PRIMARY KEY,name text)")
    con.commit()
    #"pid","Category","Supplier","name","price","qty","status",
    
    cur.execute("CREATE TABLE IF NOT EXISTS producteds(pid INTEGER PRIMARY KEY,Category text,Supplier text,name text,price text,qty text,status text)")
    con.commit()
    
   
    
    
create_db()