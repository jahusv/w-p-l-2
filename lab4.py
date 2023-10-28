from flask import Blueprint, render_template,request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login/', methods = ['GET', 'POST'])
def login():
    error = ''   
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username:        
        error = ''
    else: 
        if not username:        
            error = 'Введите логин'
        elif username != 'alex' and password != '123':
            error = 'Неверный логин и/или пароль' 
        elif username != 'alex' and password == '123':
            error = 'Неверный логин'
        elif password != '123' and username == 'alex':
            error = 'Неверный пароль'
        elif not password:
            error = 'Введите пароль'
        elif not username and not password:
            error = 'Введите пароль и логин'
        elif username == 'alex' and password == '123':
            return render_template ('password_success.html', error=error, 
                                        username=username, password=password)    
    return render_template('login.html', error=error)

    
@lab4.route('/lab4/password_success/')
def success():
    return render_template('/lab4/password_success')    
    





    
    
    

   


    
    
   
    



   


