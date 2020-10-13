from flask import Flask  # render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'library_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
# mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

cursor.execute('''
INSERT INTO Book (name, author) VALUES ("Clean Code", "Robert   
       C. Martin");
INSERT INTO Book (name, author) VALUES ("Agile Principles,    
       Patterns and Practices in C#", "Robert C. Martin");
INSERT INTO Book (name, author) VALUES ("Clean Architecture",     
       "Robert C. Martin");
INSERT INTO Book (name, author) VALUES ("The Pragmatic    
       Programmer",  "Andrew Hunt");
INSERT INTO Book (name, author) VALUES ("Practices of 
       an Agile Developer", "Andrew Hunt");
''')

conn.commit()
