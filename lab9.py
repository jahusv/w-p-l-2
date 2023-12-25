from flask import Blueprint, render_template, request

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods = ['GET'])
def main(): 
    recipient_name = request.args.get('recipient_name')
    gender = request.args.get('gender')
    sender_name = request.args.get('sender_name')
    return render_template ('/lab9/index.html', recipient_name=recipient_name, gender=gender, sender_name=sender_name)


@lab9.app_errorhandler(404)
def not_found(err):
    return render_template ('/lab9/404.html')

@lab9.app_errorhandler(500)
def server_error(err):
    return render_template ('/lab9/500.html')


@lab9.app_errorhandler(403)
def server_error(err):
    return render_template ('/rgr/403.html')

@lab9.route('/lab9/500/')
def no_answer():
    return render_template ('/lab9/500.html')


