from flask import Flask
app = Flask (__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
    <!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h1>
            <a href="/lab1">Лабораторная работа 1</a>
        </h1>
        <footer>
            &copy; Панчук Анастасия Андреевна, ФБИ-13, Курс 3, 2023
        </footer>
    </body>
</html>
    """

@app.route("/lab1")
def lab1():
    return """
    <!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Панчук Анастасия Андреевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>
            web-сервер на flask
        </h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <footer>
            &copy; Панчук Анастасия Андреевна, ФБИ-13, Курс 3, 2023
        </footer>
    </body>
</html>
    """