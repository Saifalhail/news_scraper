from flask import Blueprint, render_template
from datetime import datetime
from scraper import extracted1, extracted2, extracted3


pull_date = datetime.now().strftime('%d-%b-%Y')

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", date=pull_date, articles_mena=extracted1, articles_int=extracted2, articles_proc=extracted3)