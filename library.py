# library.py
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = 'hdk'
app.config['MYSQL_DATABASE_PASSWORD'] = '@hdkCLARKE24'
app.config['MYSQL_DATABASE_DB'] = 'library_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route('/search', methods=['GET', 'POST'])  # endpoint for search
def search():
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cursor.execute("SELECT name, author from Book WHERE name LIKE %s OR author LIKE %s", (book, book))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            cursor.execute("SELECT name, author from Book")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')


@app.route('/insert', methods=['GET', 'POST'])  # end point for inserting data dynamically in the database
def insert():
    if request.method == "POST":
        book = request.form['book']
        author = request.form['author']
        cursor.execute("INSERT INTO Book (name, author) Values (%s, %s)", (book, author))
        conn.commit()
        return redirect("http://localhost:5000/search", code=302)
    return render_template('insert.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
