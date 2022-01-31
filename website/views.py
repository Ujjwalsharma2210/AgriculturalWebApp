from flask import Blueprint, render_template, request, flash
import dbHelper

views = Blueprint('views', __name__)

@views.route('/')
def homePage():
    return render_template("home.html")

@views.route('/search', methods=['GET', 'POST'])
def searchPage():
    data = request.form.get('plantname')
    print(dbHelper.getInfoExcel(data))

    return render_template("search.html", plantsInfo=dbHelper.getInfoExcel(data))

@views.route('/about_us')
def madeByPage():
    return render_template("about_us.html")
