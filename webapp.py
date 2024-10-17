from flask import Flask, render_template,request,redirect,url_for,flash
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def creation():
    return render_template("creation.html")

@app.route('/favourites')
def favourites():
    return render_template("favourites.html")

if __name__ == '__main__':
    app.run(debug=True,port=6298)