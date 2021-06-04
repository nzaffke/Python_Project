import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
stmt=conn.cursor()
p=int(input("Enter Product ID: "))
stmt.execute ("SELECT * from products where prod_id=%d" %p)
row=stmt.fetchone()
if row==None:
    print ("Sorry no Product found with ID %d" %p)
else:
    print ("Information of the product with ID %d is as follows:" %p)
    print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0], row[1], row[2], row[3]))
    pname=input("Enter new Product Name: ")
    qty=int(input("Enter new Quantity: "))
    price=float(input("Enter new Price: "))
    stmt.execute ("UPDATE products set prod_name='%s', quantity=%d, price=%f where prod_id=%d" %(pname, qty, price,p))
    print("Information of the Product with ID %d is updated." %p)
stmt.close()
conn.commit()
conn.close()


