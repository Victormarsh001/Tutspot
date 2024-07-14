

import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
if not os.path.exists('tutspotUserData.db'):
   conn = sqlite3.connect('tutspotUserData.db')
   cursor = conn.cursor()
   cursor.execute("Create Table Data(name TEXT, country TEXT, email TEXT, password TEXT)")
   cursor.execute("Insert into Data Values('Heung', 'China', 'seongheungshim@gmail.com', 'heung4k')")
   conn.commit()
   conn.close()
else:
   print("Database Exists")
            


courses = [{'course':"Frontend Web Development", 'language': "HTML • CSS • JS"},
           {'course':"Machine Learning", 'language': "Python • Numpy • Pandas"},
           {'course':"Database", 'language': "SQL"},
           {'course':"Data Science", 'language': "Python"},
           {'course':"Backend Development", 'language': "Python • Flask • SQL"},
        {'course':"Blockchain Development"},
           
        {'course':"Android Development", 'language': "Java • Kotlin • Android Studio"},
           {'course':"iOS Development", 'language': "Swift • X-Code • iOS"},
          {'course':"Cross-platform Development", 'language': "Dart • Flutter"},
           
           {'course':"UI/UX Design"}
]

@app.route('/')
def index():
  return render_template('index.html', courses=courses, active_user="")

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/reviews')
def reviews():  
   return render_template('review.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')
@app.route('/privacy')
def privacy():
   return render_template('privacy.html')
@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')


@app.route('/terms')
def terms():
   return render_template('terms.html')

@app.route('/signupDetail', methods=["POST"])
def signupDetail():
   name = request.form['username']
   country = request.form['country']
   email = request.form['email']
   password = request.form['password']
   conn = sqlite3.connect('tutspotUserData.db')
   cursor = conn.cursor()
   
   cursor.execute("Insert into Data(name, country, email, password) Values(?,?,?,?)", (name, country, email, password))
   
   cursor.execute("select * from Data")
   user = cursor.fetchall()
   conn.commit()
   print(user)
   conn.close()
   return render_template('index.html', active_user=name)





if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)