from flask import Flask
app = Flask (__name__)

@app.route("/")
def start():
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
        <footer>
            &copy; Панчук Анастасия Андреевна, ФБИ-13, Курс 3, 2023
        </footer>
    </body>
</html>
    """
