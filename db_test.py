import sqlite3
database_location=r'D:\Dashboard\DASH_V2\d3\sample\home_dashboard2.db'
conn=sqlite3.connect(database_location)

def update_db():
    c=conn.cursor()
    #tmp_output=c.execute('select * from transaction_table')
    #print(tmp_output)
    #c.execute('insert into transaction_table  (product_id,start_date,end_date,QUANTITY) values (?,?,?,?)',(1,'2021-07-21','2021-07-22',1000))
    #c.execute('delete from transaction_table WHERE product_id=11')
    #c.execute('delete from transaction_table WHERE SERIAL_ID >18')
    #c.execute('delete from transaction_table_u ')
    #conn.commit()
    #tmp_rows=c.execute('select * from transaction_table where start_date="2021-07-21" ')
    #for i in tmp_rows:
    #    print(i)
    #a='2021-07-24'
    #b=1
    #ct='2021-07-21'
    #c.execute('update transaction_table set end_date =? where product_id=? and start_date=?',(a,b,ct))
    #conn.commit()
    #c.close()
    #c.execute('INSERT INTO PRODUCTS_DEMO (PRODUCT_NAME,PRODUCT_QUANTITY) VALUES (?,?)',('RICE',2500))
    #c.execute('INSERT INTO PRODUCTS_DEMO (PRODUCT_NAME,PRODUCT_QUANTITY) VALUES (?,?)',('DAL',1000,))
    #c.execute('INSERT INTO PRODUCTS_DEMO (PRODUCT_NAME,PRODUCT_QUANTITY) VALUES (?,?)',('OIL',1000,))
    #conn.commit()
    #t=c.execute('select * from transaction_table where serial_id in (1,2)')
    t=c.execute('select * from transaction_table_u ')
    #t=c.execute('select product_name,julianday(end_date) - julianday(start_date) from transaction_table where end_date is not null group by product_name')
    #t=c.execute('select * from products')
    #c.execute('update transaction_table_demo set end_date="2021-07-28" where product_id="1" and start_date="2021-07-27" ')
    #c.execute(
    conn.commit()
    

    
    for i in t:
        print(i)
    
    c.close()
    
    
    
t1=update_db()

