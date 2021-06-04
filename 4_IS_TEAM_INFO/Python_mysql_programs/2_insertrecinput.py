import sys
import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
stmt=conn.cursor()
k="YES"
while k.upper()=="YES" :
    pid=int(input("Enter Product ID: ")) # 100, 200
    pname=input("Enter Product Name: ")  # nuts, bolts
    qty=int(input("Enter Quantity: "))   # 200, 300
    price=float(input("Enter Price: "))  # 10.48 14.13
    try:
        stmt.execute("""
        INSERT INTO products (prod_id, prod_name, quantity, price)
        VALUES (%d, '%s', %d, %f)
        """  %(pid, pname, qty, price))
        conn.commit()
        k=input("Want to insert more products, yes/no: ") # YeS,yes,YEs,NO,nO,no
    except:
        conn.rollback()
        sys.exit(1)
stmt.close()
conn.close()
