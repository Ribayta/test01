from flask import Flask, render_template
import psycopg2
from config import config 

app = Flask(__name__)

def get_db_connection():
    # conn = psycopg2.connect(config.DATABASE_URL)
    conn = psycopg2.connect("host=localhost dbname=school user=postgres password=Supanat7410")
    return conn

def soul(num1):
    if num1 >=80 and num1<=100:
        return("Your grade is A")
    if num1 >=70 and num1<=79:
        return("Your grade is B")
    if num1 >=60 and num1<=69:
        return("Your grade is C")
    if num1 >=50 and num1<=59:
        return("Your grade is D")
    if num1 >=0 and num1<=49:
        return("Your grade is F")
        

@app.route("/")
def hello_world():
    return "<p>Hell, World!</p>"

@app.route("/home")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('select * from students')
    students = cursor.fetchall()
    conn.close()
    for index, item in enumerate(students):
        grade = soul(item[3])
        students[index] = item + (grade,)
        
    return render_template('home.html',students=students)