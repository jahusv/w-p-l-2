from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route("/")
@lab2.route("/index")
def start():
    return redirect ("/menu", code=302)

@lab2.route("/menu")
def menu():
    return ''' 
    <!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h1>
            <a href="/lab1">Лабораторная работа 1</a><br>
            <a href="/lab2">Лабораторная работа 2</a>
        </h1>
        <footer>
            &copy; Панчук Анастасия Андреевна, ФБИ-13, Курс 3, 2023
        </footer>
    </body>
</html>
    '''


   
@lab2.route('/lab2/example')
def example():
    name = 'Анастасия Панчук'
    numCour = '3'
    group = 'ФБИ-13'
    labNum = '2'
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120}, 
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321}
        ]
        
    books = [
        {'authorName' : 'Ф.М. Достоевский', 'bookName' : 'Преступление и наказание', 'kind': 'Роман', 'pages': 500},
        {'authorName' : 'Джером Д. Сэлинджер', 'bookName' : 'Над пропастью во ржи', 'kind': 'Роман', 'pages': 257},
        {'authorName' : 'Джейн Остин', 'bookName' : 'Гордость и предубеждение', 'kind': 'Роман', 'pages': 387},
        {'authorName' : 'Ф. Фицжеральд', 'bookName' : 'Великий Гэтсби', 'kind': 'Роман', 'pages':367 },
        {'authorName' : 'М. Булгаков', 'bookName' : 'Мастер и Маргарита', 'kind': 'Роман', 'pages': 623},
        {'authorName' : 'М.Ю. Лермонтов', 'bookName' : 'Герой нашего времени', 'kind': 'Роман', 'pages': 267},
        {'authorName' : 'А.С. Пушкин', 'bookName' : 'Капитанская дочка', 'kind': 'Роман', 'pages':144 },
        {'authorName' : 'В.В. Набоков', 'bookName' : 'Лолита', 'kind': 'Роман', 'pages': 367},
        {'authorName' : 'Л.Н. Толстой', 'bookName' : 'Война и мир', 'kind': 'Роман', 'pages': 1000},
        {'authorName' : 'Н.В. Гоголь', 'bookName' : 'Вечера на хуторе близ диканьки', 'kind': 'Роман', 'pages': 627}
    ]

    return render_template ('temppates/example.html', name = name, 
            numCour = numCour, group = group, labNum = labNum, fruits = fruits, books = books)

@lab2.route('/lab2/')
def lab():
    return render_template('tempates/lab2.html')

@lab2.route('/lab2/puppys/')
def puppys():
    return render_template('templates/puppys.html')
