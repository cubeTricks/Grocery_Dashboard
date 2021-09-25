from flask import Flask, session, redirect, url_for, request,render_template
from datetime import datetime,timedelta
import db_functions
import socket

#to get local machine ip address 
get_current_ip=socket.gethostbyname(socket.gethostname())


app = Flask(__name__, static_folder='static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#1. User Login and Landing Page
# Page 1
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


#Page 2
@app.route('/login',methods=['GET','POST'])
def user_login():
    
    if request.method == 'POST':
        session['username'] = request.form['username']
        if session['username'] in ['1234','1235','1236']:
            c_user=session['username']
            return redirect(url_for('landing_page'))
    return render_template('login.html')
    
#Page 3    
@app.route('/landing_page',methods=['GET','POST'])
def landing_page():
    return render_template('landing_page.html',current_user=session['username'])    
    



@app.route('/refill', methods=['GET','POST'])
def refill():
    
    #current_date=datetime.now()+timedelta(days)
    current_date=datetime.now()
    dates_list=[]
    selected_product=[]
    selected_quantity=[]
    selected_item_id=[]
    selected_date=[]
    products_info=[]
    products_map=[]
    current_date=current_date.strftime('%Y-%m-%d')
    selected_date1=current_date
    selected_date2=current_date
    selected_date3=current_date
    
    
    products_info=db_functions.display_products()
    current_date_for_html={'c_date':current_date}
    products_map=db_functions.products_name_id_map()
    print(products_map)
    



    #selected_date1=request.form.get('process_date1')
    selected_product.append(request.form.getlist('product_name'))
    selected_quantity.append(request.form.getlist('quantity'))
    selected_date.append(request.form.getlist('date'))
    selected_item_id.append(request.form.getlist('item_id'))
    #selected_product.append(request.form.getlist('product_name_2'))
    #selected_product.append(request.form.getlist('product_name_3'))
    print(selected_product)
    print(selected_quantity)
    print(selected_date)
    #print(len(selected_product[0]))
    #print(selected_span)
    if len(selected_product[0])>0:
        
        
    #if selected_date1!=current_date:
    #    print('Hello')
    #    #db_functions.multiple_update_db(dates_list)
    #    #db_functions.show_current_values()
        
    #else:
    #    #db_functions.show_current_values()
    #    print('bye')
        print('hello')
        t=[]
        for i in selected_product[0]:
        #print(i)
            for j in products_map:
                if j[1]==i:
            #print(j[0])
                    t.append(str(j[0]))
        items_pos_to_update=[]
        for i in t:
            for j in selected_item_id[0]:
                if i==j:
                    #print(i,j)
                    items_pos_to_update.append(int(j)-1)
        print(items_pos_to_update)
        #print(items_to_update) 
        items_to_update=[]
        #db_functions.update_db(items_to_update)
        for i in items_pos_to_update:
            tmp_row=[]
            tmp_row.append(products_map[i][0])
            tmp_row.append(products_map[i][1])
            tmp_row.append(selected_quantity[0][i])
            tmp_row.append(selected_date[0][i])
            #changing here
            tmp_row.append(session['username'])
            #print(type(c_user))
            items_to_update.append(tmp_row)
        print(items_to_update)
        db_functions.update_db(items_to_update)
    
    
    else:
        print('bye')
    return render_template('refill.html',current_date_for_html=current_date_for_html,products_info=products_info)
    

@app.route('/existing_list', methods=['GET','POST'])   
def existing_list():
    
    products_list=db_functions.exist_display_products(session['username'])
    return render_template('existing_list.html',products_list=products_list)
        

@app.route('/consumption', methods=['GET','POST'])   
def consumption():
    
    products_list=db_functions.consumption(session['username'])
    return render_template('consumption.html',products_list=products_list)        

        
if __name__ == "__main__":    
    
    app.run(host=get_current_ip,port=9090,debug=True,threaded=True)
    #app.run()
   
