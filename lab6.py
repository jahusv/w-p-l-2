from flask import Blueprint, render_template,request, redirect, session, Flask 
from werkzeug.security import check_password_hash, generate_password_hash 
from Db.models import users, articles
from flask_login import login_user, login_required, current_user
import psycopg2


lab6 = Blueprint('lab6', __name__)


@lab6.route('/lab6/')
def lab():
    visibleUser = session.get ('username','Anon')
    return render_template('general6.html', username=visibleUser)

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



@lab6.route('/lab6/check/')
def main():
    my_users = users.query.all()
    print (my_users)
    return 'result in console!'

@lab6.route('/lab6/checkarticles/')
def actickls():
    articles_check = articles.query.all()
    print(articles_check)
    return 'result in console!'

@lab6.route('/lab6/register/', methods = ['GET', 'POST'])
def register():
    error = []
    if request.method == 'GET':
        return render_template ('register.html')
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    if not username_form:
        error.append('Заполните все поля') 
    elif len(password_form) <5:
        error.append('Длина пароля должна быть более 5 символов')
    
    conn = dbConnect()
    cur = conn.cursor()
    
    #проверка
    cur.execute("SELECT username FROM users WHERE username = %s;", (username_form,))
    
    if cur.fetchone() is not None:
        error.append('Пользователь с данным именем уже существует')
       
        conn.close()
        cur.close()

        return render_template('register.html', errors=error)

    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        return render_template ('register.html')
    
    hashedPswd = generate_password_hash(password_form, method = 'pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect ('/lab6/login6/')


@lab6.route('/lab6/login6/', methods = ['GET', 'POST'])
def login():
    error = []

    if request.method == 'GET':
        return render_template('login6.html')
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    if not (username_form and password_form):
        error.append('Заполните все поля')
        return render_template('login6.html', error=error)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username_form,))

    result = cur.fetchone()

    if result is None:
        error.append('Пользователя не существует')
        dbClose(cur, conn)
        return render_template('login6.html', error = error)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password_form) or hashPassword == password_form:
        session['id'] = userID
        session['username'] = username_form
        dbClose(cur, conn)
        return redirect ('/lab6/')
    else: 
        error.append('Неправильный пароль')
        
    
    my_user = users.query.filter_by(username_form=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect('/lab6/articles/')
    return render_template('login6.html', error=error)


@lab6.route('/lab6/articles/')
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template('list_articles.html', articles=my_articles)


@lab6.route('/lab6/articles/<int:article_id>')  
def state(article_id):
    userID = session.get('id')  
        
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
            
        cur.execute("SELECT title, arcticle_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))
        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return 'Not found!'
                
            
        text = articleBody[1].splitlines()

        return render_template('articleN.html', arcticle_text=text, article_title=articleBody[0],
                            username=session.get('username'))
    
    abort (403)


@lab6.route('/lab6/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/lab6')