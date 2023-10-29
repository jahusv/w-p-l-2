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
        else:
            return render_template ('password_success.html', error=error, 
                                        username=username, password=password)    
    return render_template('login.html', error=error)

    
@lab4.route('/lab4/password_success/')
def success():
    return render_template('/lab4/password_success')    
    

@lab4.route('/lab4/refrigerator/', methods=['GET', 'POST'])
def refrigerator():
    message = ''
    temperature = request.form.get('temperature')
    if not temperature:
        message = 'Ошибка: не задана температура'
    else:
            temperature = int(temperature)
            if temperature < -12:
                message = 'Не удалось установить температуру — слишком низкое значение'
            elif -12 <= temperature <= -9:
                message = f'Установлена температура: {temperature}°С\n❄❄❄'
            elif -8 <= temperature <= -5:
                message = f'Установлена температура: {temperature}°С\n❄❄'
            elif -4 <= temperature <= -1:
                message = f'Установлена температура: {temperature}°С\n❄'
            elif temperature > -1:
                message = 'Не удалось установить температуру — слишком высокое значение'
            return render_template('temperature.html', message=message)
    return render_template('refrigerator.html')


@lab4.route('/lab4/temperature/')
def temperature():
    return render_template('temperature.html')


@lab4.route('/lab4/grain/', methods=['GET', 'POST'])
def grain():
    price = 0
    error = ''
    sum = 0
    grain = request.form.get('grain')
    weight = request.form.get('weight')
    
    if grain == 'barley':
        price = 12000            
    elif grain == 'oats':
        price = 8500
    elif grain == 'wheat':
        price = 8700
    else:
         price = 14000
        
    if not weight:
        error = 'Ошибка: не выбран вес'
    else: 
        weight = int(weight)
        if weight > 499:
            error = 'Данного объема нет в наличии'
        elif weight < 499 and weight >= 50:
            sum = price * weight - price*weight/10
        else:
            sum = price*weight
        return render_template('grain_order.html', grain=grain, weight=weight, 
                               error=error,sum=sum )
    return render_template('grain.html')



@lab4.route('/lab4/grain_order/')
def order():
    return render_template('grain_order.html')



    
    
    

   


    
    
   
    



   


