import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template
from flask import request

from flask import url_for, redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine('postgresql://project1:qinjidong@localhost:5432/project-1')
db = scoped_session(sessionmaker(bind=engine))

# login usename
user_logged = None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login(info=None):
    global user_logged
    if request.method == 'GET':
        return render_template('login.html', info=info)
    elif request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        result = db.execute("SELECT * FROM users WHERE (name=:name) and (password=:password);", {"name":name, "password":password}).fetchall()
        if result != []:
            #重定向到user界面 redirect()
            session['username'] = name
            return redirect(url_for('user', username=name))
        else:
            #仍然在本页面，加上提示信息
            return render_template('login.html', info="Your username or password is not correct.")

@app.route("/registration", methods=['GET', 'POST'])
def registration(info=None):
    global user_logged
    if request.method == 'GET':
        return render_template('registration.html', info="getttttt")
    else:
        name = request.form.get('username')
        password_1 = request.form.get('password1')
        password_2 = request.form.get('password2')
        if db.execute("SELECT * FROM users WHERE name=:name", {"name": name}).fetchall() != []:
            return render_template('registration.html', info="username already exists.")
        if password_1 != password_2:
            return render_template('registration.html', info="two passwords do not match.")
        db.execute("INSERT INTO users (name, password) VALUES(:name, :password)", {"name": name, "password": password_1})
        db.commit()
        return redirect(url_for('user', username=name))


@app.route("/user/<username>", methods=['GET', 'POST'])
def user(username):
    if request.method == 'GET':
        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template('user.html', name=username)
    else:
        field = request.form.get('field')
        keyword = request.form.get('keyword')
        if field=="isbn":
            book_list = db.execute("SELECT isbn, title, auther, year FROM books WHERE (isbn=:keyword);", {"keyword":keyword}).fetchall()
        elif field == "title":
            book_list = db.execute("SELECT isbn, title, auther, year FROM books WHERE (title=:keyword);", {"keyword":keyword}).fetchall()
        elif field == 'auther':
            book_list = db.execute("SELECT isbn, title, auther, year FROM books WHERE (auther=:keyword);", {"keyword":keyword}).fetchall()
        return render_template('user.html', username=session['username'], result=book_list)

@app.route("/logout", methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/<book_isbn>")
def book(book_isbn):
    if 'username' not in session:
        return redirect(url_for('login'))
    name = session['username']
    book = db.execute("SELECT isbn, title, auther, year FROM books WHERE (isbn=:keyword);", {"keyword":book_isbn}).fetchone()
    book_reviews = db.execute("SELECT username, rate, review FROM reviews WHERE book_title=:isbn", {'isbn': book_isbn}).fetchall()
    return render_template('book.html', name=name, bookinfo=book, bookreview = book_reviews)

@app.route("/comment/<book_isbn>", methods=['POST'])
def comment(book_isbn):
    name = session['username']
    rate = int(request.form.get('rate'))
    review = request.form.get('review')
    if db.execute("SELECT * FROM reviews WHERE (username=:name) AND (book_title=:isbn);", {"name": name, "isbn": book_isbn}).fetchall() == []:
        db.execute("INSERT INTO reviews (username, book_title, rate, review) VALUES (:name, :isbn, :rate, :review)", {"name": name, "isbn": book_isbn, 'rate': rate, 'review': review})
        db.commit()
    return redirect(url_for('book', book_isbn=book_isbn))
    




