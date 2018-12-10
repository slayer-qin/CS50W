from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv
import os


# Set up database
engine = create_engine('postgresql://project1:qinjidong@localhost:5432/project-1')
db = scoped_session(sessionmaker(bind=engine))

f = open('./project1/books.csv', 'r')
reader = csv.reader(f)
for isbn, title, auther, year in reader:
    db.execute("INSERT INTO books (isbn, title, auther, year) VALUES (:isbn, :title, :auther, :year)",
     {'isbn':isbn, 'title':title, 'auther':auther, 'year':year})
    print(f"Added book ISBN: {isbn}, TITLE: {title}, AUTHER: {auther}, YEAR: {year}.")
db.commit()
