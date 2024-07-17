

import sqlite3
import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
if not app.secret_key:
    app.secret_key = secrets.token_urlsafe(32)

if not os.path.exists('tutspotUserData.db'):
   conn = sqlite3.connect('tutspotUserData.db')
   cursor = conn.cursor()
   cursor.execute("Create Table Data(name TEXT, country TEXT, email TEXT, password TEXT)")
   cursor.execute("Insert into Data Values('Heung', 'China', 'seongheungshim@gmail.com', 'heung4k')")
   conn.commit()
   conn.close()
            


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
   if "username" in session:
      active_user = session["username"]
   else:
      active_user = False
   return render_template('index.html', courses=courses, active_user=active_user)

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

@app.route('/signupDetail', methods=["GET", "POST"])
def signupDetail():
   if request.method == "POST":
      name = request.form['username']
      country = request.form['country']
      email = request.form['email']
      password = request.form['password']
      conn = sqlite3.connect('tutspotUserData.db')
      cursor = conn.cursor()
      cursor.execute("Select * from Data Where email = :email", {'email': email})
      user = cursor.fetchone()
      if user and email in user:
         conn.close()
         return "Email already exists. Check your email for your password.", 404
      else:
         session["username"] = name
         session["country"] = country
         session["email"] = email
         cursor.execute("Insert into Data(name, country, email, password) Values(:name, :country, :email, :password)", {'name':name, 'country':country, 'email':email, 'password':password})
         conn.commit()
         conn.close()
         return redirect(url_for('index'))
   else:
      return render_template('signup.html')



@app.route('/loginDetail', methods=["GET", "POST"])
def loginDetail():
   if request.method == "POST":
      email = request.form['email']
      password = request.form['password']
      conn = sqlite3.connect('tutspotUserData.db')
      cursor = conn.cursor()
      cursor.execute("Select * from Data Where email = :email", {'email': email})
      user = cursor.fetchone()
      if user and email in user:
         if password == user[3]:
            session["username"] = user[0]
            session["country"] = user[1]
            session["password"] = password
            return redirect(url_for('index'))
         else:
            return "Incorrect Password", 404
      else:
         return "Email does not exist", 404
   else:
      return render_template('login.html')
         


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)