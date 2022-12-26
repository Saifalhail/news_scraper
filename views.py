from flask import Blueprint, render_template, request
from datetime import datetime
from scraper import scraper


pull_date = datetime.now().strftime('%d-%b-%Y')

views = Blueprint(__name__, "views")





@views.route("/")
def home():
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


