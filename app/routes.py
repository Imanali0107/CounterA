from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    data='Welcome username'
    dictionary={'Россия':'Москва', 'Казахстан':'Нур-Султан', 'Италия':'Рим'}
    return render_template('index.html', dictionary=dictionary, title=data)