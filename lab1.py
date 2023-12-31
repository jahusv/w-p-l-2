from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)


@lab1.route("/menu")
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
            <a href="/lab2">Лабораторная работа 2</a><br>
            <a href="/lab3">Лабораторная работа 3</a><br>
            <a href="/lab4">Лабораторная работа 4</a><br>
            <a href="/lab5">Лабораторная работа 5</a><br>
            <a href="/lab6">Лабораторная работа 6</a><br>
            <a href="/lab7">Лабораторная работа 7</a><br>
            <a href="/lab8">Лабораторная работа 8</a><br>
            <a href="/lab9">Лабораторная работа 9</a><br>
            <a href="/initiatives/">РГР</a><br>
        </h1>
        <footer>
            &copy; Панчук Анастасия Андреевна, ФБИ-13, Курс 3, 2023
        </footer>
    </body>
</html>
    '''

@lab1.route("/lab1")
def lab():
    return '''
    <!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Панчук Анастасия Андреевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>
            web-сервер на flask
        </h1>
        <p>
            Flask — Фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
            <div><a href="/menu">Меню</a></div>
            <h2>Реализованные роуты</h2>
            <div><a href="/lab1/oak">/lab1/oak - дуб</a></div>
            <div><a href="/lab1/student">/lab1/student - студент</a></div>
            <div><a href="/lab1/python">/lab1/python - python </a></div>
            <div><a href="/lab1/pear">/lab1/pear - грушевый штрудель </a></div>
        <footer>
            &copy; Панчук Анастасия Андреевна, ФБИ-13, Курс 3, 2023
        </footer>
    </body>
</html>
    '''

@lab1.route('/lab1/oak')
def oak ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1> Дуб </h1>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
        </body>
    </html>
    '''

@lab1.route('/lab1/student')
def student ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1> Панчук Анастасия Андреевна </h1>
            <img src="''' + url_for('static', filename='nstu.jpg') + '''">
        </body>
    </html>
    '''


@lab1.route('/lab1/python')
def python ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <div>Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах. Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки. </div>
            <div>Специалисты по работе с данными используют библиотеки Python ML для моделей машинного обучения и создания классификаторов, которые точно классифицируют данные. Классификаторы на основе Python используются в различных областях и применяются для выполнения таких задач, как классификация изображений, текста и сетевого трафика, распознавание речи и распознавание лиц. Специалисты по работе с данными также используют Python для глубокого обучения — передовой техники машинного обучения. </div>
            <img src="''' + url_for('static', filename='python.jpg') + '''">
        </body>
    </html>
    '''


@lab1.route ('/lab1/pear')
def pear ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
        <div> Венгерский рулет ретеш и правда похож на венский штрудель, однако, точно не<br> 
            известно, как ретеш появился в Вене. Большинство исследователей сходится во мнении,<br>
            что штрудель пришел в Австрию именно из этой страны и распространился по Европе в период<br> 
            правления Габсбургов. Первый известный рецепт венского штруделя датируется 1696 годом.<br> 
            Он был найден в рукописной поваренной книге, сохранившейся в библиотеке Венской ратуши.<br> 
            Это рецепт так называемого молочно-сливочного штруделя с творожной начинкой Millirahmstrudel.<br>
            Мильрахмштрудель и сейчас присутствует в меню австрийских кофеен, а подают его прямо в сковороде,<br>
            щедро политым сливочным соусом.</div>
        <div>За пределами австро-венгерской империи о штруделе стало широко известно после Венского конгресса,<br>
        проходившего с сентября 1814 по июнь 1815 года. Переговоры европейских монархов и дипломатов по переделу<br> 
        территории наполеоновской Франции сопровождались многочисленными банкетами, где и дебютировала выпечка из<br> 
        слоеного теста с воздушными взбитыми сливками. Легкий десерт очень понравился сильным мира сего, и его рецепт <br>
        быстро распространился по всей Европе.</div>
        <img src="''' + url_for('static', filename='pear.jpg') + '''">
        </body>
    </html>
    '''