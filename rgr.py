from flask import Blueprint, flash, render_template,request, redirect, session, Flask, abort, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash 
import psycopg2
from psycopg2 import sql
rgr = Blueprint('rgr', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = 'knowledge_base',
        user = 'panchuk_anastasia_knowledge_base',
        password='123'
    )

    return conn; 
def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@rgr.route('/initiatives/')
def user():
    visibleUser = session.get ('username','Anon')
    userID = session.get('id')
    articles = []

    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, title, arcticle_text FROM articles")
    articles = cur.fetchall()

    dbClose(cur, conn)
    return render_template('rgr/main.html', username = visibleUser, articles=articles)    

@rgr.route('/registration/api/', methods=['GET', 'POST'])
def registerPage():
    
    errors = []   
    if request.method == 'GET':
        return render_template('rgr/registration.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):  
        errors.append('Заполните все поля')
        print(errors)
        return render_template('rgr/registration.html', errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()
    
    #проверка
    cur.execute("SELECT username FROM users WHERE username = %s;", (username,))
    
    if cur.fetchone() is not None:
        errors.append('Пользователь с данным именем уже существует')
       
        conn.close()
        cur.close()

        return render_template('rgr/registration.html', errors=errors)

    #вставка нового пользователя
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))
    conn.commit()  
    conn.close()
    cur.close()

    return redirect ('/login/api/')


@rgr.route('/login/api/', methods = ['GET', 'POST'])
def loginPage():
    errors = [];
    
    if request.method == 'GET':
        return render_template('rgr/login.html', errors=errors)
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors.append('Заполните все поля')
        return render_template('rgr/login.html', errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append('Неправильный логин')
        dbClose(cur, conn)
        return render_template('rgr/login.html', errors = errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password) or hashPassword == password:
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect ('/main/')
    else: 
        errors.append('Неправильный логин или пароль')
        return render_template('rgr/login.html', errors=errors)
    

@rgr.route('/offer_initiative/api/', methods=['GET', 'POST'])
def add_new():
    errors = []
    userID = session.get('id')

    if userID is not None:
        if request.method == 'GET':
            return render_template('rgr/new_initiative.html')

        if request.method == 'POST':
            text = request.form.get('text')  
            title = request.form.get('title_article')

            if text is None:
                errors.append('Заполните поле')
                return render_template('rgr/new_initiative.html', errors=errors)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles (user_ID, title, arcticle_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, text))
           
            conn.commit()
            conn.close()
            cur.close()
        return render_template('rgr/main.html')
    abort (403) 


@rgr.route('/my_initiatives/api/')
def my_initiatives():
    user_id = session.get('id')

    if user_id is not None:
        conn = dbConnect()
        cur = conn.cursor()

        # Проверка, является ли пользователь администратором
        is_admin = session.get('id') == 38

        if is_admin:
            cur.execute("SELECT id, title, arcticle_text FROM articles")
        else:
            cur.execute(f"SELECT id, title, arcticle_text FROM articles WHERE user_id = {user_id}")

        articles = cur.fetchall()

        dbClose(cur, conn)
        return render_template('rgr/my_initiatives.html', articles=articles)

    abort(404)   


@rgr.route('/delete_article/<int:article_id>/', methods=['DELETE'])
def delete_article(article_id):
    user_id = session.get('id')

    if user_id is not None:
        conn = dbConnect()
        cur = conn.cursor()

        # Проверка, является ли пользователь администратором
        is_admin = session.get('id') == 38

        if is_admin:
            cur.execute("DELETE FROM articles WHERE id = %s", (article_id,))
        else:
            cur.execute("DELETE FROM articles WHERE id = %s AND user_id = %s", (article_id, user_id))

        conn.commit()
        conn.close()
        return render_template('rgr/my_initiatives.html')
    abort (404)
       

@rgr.route('/logout/api/')
def logout():
    # Clear the entire session
    session.clear()
    return redirect('/login/api/')