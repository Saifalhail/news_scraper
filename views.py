from flask import Blueprint, g, render_template, request, session, redirect, url_for, abort
from datetime import datetime
from scraper import scraper

pull_date = datetime.now().strftime('%d-%b-%Y')

views = Blueprint(__name__, "views")

class User:
    def __init__ (self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


users = []
users.append(User(id = 1, username='bhrd', password='BH@123456'))   


@views.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@views.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('views.home'))

        return redirect(url_for('views.login'))

    return render_template('login.html')


@views.route("/home")
def home():
    if not g.user:
        return redirect(url_for('views.login'))
    return render_template("homepage.html")


@views.route("/result", methods=['POST'])
def result():
    list_of_urls_mena = []
    list_of_urls_int = []
    list_of_urls_proc = []
    for i in request.form.getlist('mena-url'):
        list_of_urls_mena.append(i)
    for i in request.form.getlist('int-url'):
        list_of_urls_int.append(i)
    for i in request.form.getlist('proc-url'):
        list_of_urls_proc.append(i)    
    extracted1, extracted2, extracted3 = scraper(list_of_urls_mena, list_of_urls_int, list_of_urls_proc)
    return render_template("index.html", date=pull_date, articles_mena=extracted1, articles_int=extracted2, articles_proc=extracted3)

