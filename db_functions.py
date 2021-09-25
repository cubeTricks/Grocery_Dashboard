import sqlite3
database_location=r'D:\Dashboard\DASH_V2\d3\sample\home_dashboard2.db'


def update1_db(new_date):
    conn=sqlite3.connect(database_location)
    c=conn.cursor()
    tmp_output=c.execute('select * from transaction_table')
    #print(tmp_output)
    #c.execute('insert into transaction_table  (product_id,start_date,end_date,QUANTITY) values (?,?,?,?)',(1,'2021-07-21','2021-07-22',1000))
    #c.execute('drop table transaction_table')
    conn.commit()
    tmp_rows=c.execute('select * from transaction_table where start_date="2021-07-21" ')
    for i in tmp_rows:
        print(i)
    a=new_date
    b=1
    ct='2021-07-21'
    c.execute('update transaction_table set end_date =? where product_id=? and start_date=?',(a,b,ct))
    conn.commit()
    c.close()


def show_current_values():
    conn=sqlite3.connect(database_location)
    c=conn.cursor()
    tmp_output=c.execute('select * from transaction_table')
    for i in tmp_output:
        print(i)
    
    c.close()
    
def multiple_update_db(new_date_list):
    conn=sqlite3.connect(database_location)
    c=conn.cursor()
    tmp_output=c.execute('select * from transaction_table')
    #print(tmp_output)
    #c.execute('insert into transaction_table  (product_id,start_date,end_date,QUANTITY) values (?,?,?,?)',(1,'2021-07-21','2021-07-22',1000))
    #c.execute('drop table transaction_table')
    conn.commit()
    tmp_rows=c.execute('select * from transaction_table where start_date="2021-07-21" ')
    for i in tmp_rows:
        print(i)
    for i in new_date_list:
        a=i
        b=1
        ct='2021-07-21'
        c.execute('update transaction_table set end_date =? where product_id=? and start_date=?',(a,b,ct))
        conn.commit()
    c.close()
    
def display_products():
   conn=sqlite3.connect(database_location)
   c=conn.cursor()
   tmp_display_products=c.execute('select * from products')
   tmp_display_products_array=[]
   for tmp_rows in tmp_display_products:
       #print(tmp_rows)
       tmp_row_html={'product_id':tmp_rows[0],'product_name':tmp_rows[1],'quantity':tmp_rows[2]}
       #for i in tmp_rows:
            #print(i)
       tmp_display_products_array.append(tmp_row_html)
       #tmp_selected_country_data_for_html_row={'Date':i[0],'Country_Name':i[2],'New_Cases':f'{i[4]:,}','Cummulative_Cases':f'{i[5]:,}','New_Deaths':f'{i[6]:,}','Cummulative_Deaths':f'{i[7]:,}'}
       #selected_country_data_for_html.append(tmp_selected_country_data_for_html_row)
   #print(tmp_display_products_array)
   return tmp_display_products_array     
#x=display_products()
#print(x[0])


def exist_display_products(c_user):
   conn=sqlite3.connect(database_location)
   c=conn.cursor()
   c_user_list=[]
   c_user_list.append(c_user)
   print(c_user_list[0])
   tmp_display_products=c.execute('select product_id,product_name,quantity,start_date from TRANSACTION_TABLE_u where end_date is null and user_id=?',(c_user_list[0],))
   tmp_display_products_array=[]
   for tmp_rows in tmp_display_products:
       #print(tmp_rows)
       tmp_row_html={'product_id':tmp_rows[0],'product_name':tmp_rows[1],'quantity':tmp_rows[2],'start_date':tmp_rows[3]}
       #for i in tmp_rows:
            #print(i)
       tmp_display_products_array.append(tmp_row_html)
       #tmp_selected_country_data_for_html_row={'Date':i[0],'Country_Name':i[2],'New_Cases':f'{i[4]:,}','Cummulative_Cases':f'{i[5]:,}','New_Deaths':f'{i[6]:,}','Cummulative_Deaths':f'{i[7]:,}'}
       #selected_country_data_for_html.append(tmp_selected_country_data_for_html_row)
   #print(tmp_display_products_array)
   return tmp_display_products_array     
   
   
   
def consumption(c_user):
   conn=sqlite3.connect(database_location)
   c=conn.cursor()
   c_user_list=[]
   c_user_list.append(c_user)
   print(c_user_list[0])
   #tmp_display_products=c.execute('select product_id,product_name,quantity,start_date from TRANSACTION_TABLE where end_date is null')
   #tmp_display_products=c.execute('select product_id,product_name,julianday(end_date) - julianday(start_date) from transaction_table where end_date is not null')
   tmp_display_products=c.execute('select product_id,product_name,round(sum(julianday(end_date) - julianday(start_date))/count(*),0),date(julianday("now") + round(sum(julianday(end_date) - julianday(start_date))/count(*),0)) from transaction_table_u where end_date is not null and user_id=? group by product_name',[c_user])
   tmp_display_products_array=[]
   for tmp_rows in tmp_display_products:
       #print(tmp_rows)
       tmp_row_html={'product_id':tmp_rows[0],'product_name':tmp_rows[1],'consumption':tmp_rows[2],'next_buy_date':tmp_rows[3]}
       #for i in tmp_rows:
            #print(i)
       tmp_display_products_array.append(tmp_row_html)
    
   return tmp_display_products_array     
   
   
def products_name_id_map():
   conn=sqlite3.connect(database_location)
   c=conn.cursor()
   tmp_display_products=c.execute('select product_id,product_name from products')
   tmp_products_name_id_map=[]
   for tmp_rows in tmp_display_products:
       tmp_row_html=[tmp_rows[0],tmp_rows[1]]
       tmp_products_name_id_map.append(tmp_row_html)
   conn.close()
   return tmp_products_name_id_map 
    



def update_db(products_list):
    conn=sqlite3.connect(database_location)
    c=conn.cursor()
    tmp_output=c.execute('select * from transaction_table')
    #print(tmp_output)
    
    try:
    
        for items in products_list:
            c.execute('update transaction_table_u set end_date=? where product_id=? and product_name=? and end_date is null',(items[3],items[0],items[1]))
            c.execute('insert into TRANSACTION_TABLE_U  (USER_ID,PRODUCT_ID,PRODUCT_NAME,QUANTITY,START_DATE) values (?,?,?,?,?)',(int(items[4]),items[0],items[1],items[2],items[3]))
            conn.commit()
        
    except Exception as e:
        print(e)
        conn.commit()
        conn.close()
        
        
'''        

    try:
       
        for items in products_list:
            print(items,'here in update')
            c.execute('update transaction_table_u set end_date=? where product_id=? and product_name=? and end_date is null',(items[3],items[0],items[1]))
            c.execute('insert into TRANSACTION_TABLE_U  (USER_ID,PRODUCT_ID,PRODUCT_NAME,QUANTITY,START_DATE) values (?,?,?,?,?)',(int(items[4]),items[0],items[1],items[2],items[3]))
            print('hi')
            conn.commit()
        #c.execute('drop table transaction_table')
    except:
        conn.commit()
        c.close()
        '''
    
    