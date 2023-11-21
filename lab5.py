from flask import Blueprint, render_template,request, redirect
import psycopg2


lab5 = Blueprint('lab5', __name__)

 
@lab5.route('/lab5/users/')
def main():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = 'knowledge_base',
        user = 'panchuk_anastasia_knowledge_base',
        password='123'
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    user_names = [user[1] for user in result]

    return render_template('lab5.html', user_names=user_names)



