from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://project1:qinjidong@localhost:5432/project-1') # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives，也可以直接填写数据库地址
db = scoped_session(sessionmaker(bind=engine))    # create a 'scoped session' that ensures different users' interactions with the
                                                    # database are kept separate
name="qin"
result = db.execute("SELECT * FROM users WHERE name=:name", {"name":name}).fetchall()# execute this SQL command and return all of the results
print(result)