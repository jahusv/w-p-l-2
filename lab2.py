from flask import Flask, redirect, url_for, render_template
from lab1 import lab1 

app = Flask (__name__)
app.register_blueprint (lab1)
   
@app.route('/lab2/example')
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

    return render_template ("example.html", name = name, 
            numCour = numCour, group = group, labNum = labNum, fruits = fruits, books = books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/puppys/')
def puppys():
    return render_template('puppys.html')
