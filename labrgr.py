from flask import Blueprint, render_template,request, redirect
labgrg = Blueprint('labgrg', __name__)


@labgrg.route('/rgr/')
def lab():
    return render_template('rgr.html')
