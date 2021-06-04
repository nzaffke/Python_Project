import sys
import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
stmt=conn.cursor()
try:
#   stmt.execute ("""
#   drop table products
#   """)
    stmt.execute ("""
    create table products (prod_id smallint NOT NULL,
    prod_name char(50),
    quantity smallint,
    price float)
    """)
except MySQLdb.Error:
    print ("Error in creating products table")
    sys.exit(1)    
stmt.close()
conn.close()
