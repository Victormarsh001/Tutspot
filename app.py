from copy import deepcopy
import sqlite3
from os import environ, path
from secrets import token_urlsafe
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Course

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY")

if not app.secret_key:
    app.secret_key = token_urlsafe(32)

if not path.exists('data.db'):
   conn = sqlite3.connect('data.db')
   cursor = conn.cursor()
   cursor.execute("Create Table Data(name TEXT, country TEXT, email TEXT, password TEXT)")
   cursor.execute("Insert into Data Values('Heung', 'China', 'seongheungshim@gmail.com', 'heung4k')")
#Android Table  
   cursor.execute("CREATE Table Android(email TEXT)")
   cursor.execute("INSERT INTO Android(email) VALUES('androidTutspot@gmail.com')")
   
#Comments Table
   cursor.execute("CREATE Table Comments(id Integer, name TEXT, comment TEXT, date TEXT)")
   conn.commit()
   conn.close()

if not path.exists('post.db'):
   conn = sqlite3.connect('post.db')
   cursor = conn.cursor()
   cursor.execute("CREATE Table Post(id Integer, name TEXT, post TEXT, date TEXT)")
   conn.commit()
   conn.close()
if not path.exists('jobs.db'):
   conn = sqlite3.connect('jobs.db')
   cursor = conn.cursor()
   cursor.execute("Create Table Job(email Text, name Text, role Text, description Text, date Text)")
   cursor.execute("Insert Into Job Values('hack@gmail.com','Tesh','Flutter Developer','Build Flutter Apps','23/08/2024')")
   conn.commit()
   conn.close()
if not path.exists('review.db'):
   conn = sqlite3.connect('review.db')
   cursor = conn.cursor()
   cursor.execute("CREATE Table Rating(name TEXT, rate TEXT, date TEXT)")
   cursor.execute("Insert Into Rating VALUES('Louis', 'Great and Simple UI!', '19/08/2024')")
   conn.commit()
   conn.close()
   


intro = {'Frontend Web Development': [ ['Introduction to HTML', 'HTML Basic Structure', 'HTML Headings', 'HTML Paragraphs', 'HTML Links', 'Images/Videos in HTML', 'HTML Lists', 'HTML Tables','HTML Forms','HTML Containers','Recap','Practice'], 
                              ['HTML Code Editor','You must signup or login to access this free course', 'Any prior knowledge on programming will be an advantage']
],
'Python Programming Language':[['Introduction to Machine Learning', 'Linear Regression', 'Logistic Regression', 'Decision Trees', 'Random Forest', 'Neural Networks', 'K-Nearest Neighbors', 'Support Vector Machines', 'Clustering', 'Dimensionality Reduction', 'ML Practice'], 
                              ['Python IDE or Code Editor','You have to login and make payments to access this course', 'Any prior knowledge on other Programming Language is an advantage']
], 'SQL Database': [[ 'Introduction to SQL', 'SQL Basics', 'SQL Query', 'Python + SQL', 'Sqlite','Create','Read','Update','Delete','Dynamic Querying', 'SQL Summary', 'SQL Practice'], ['Python IDE or Code Editor','This course is for beginners and experts', 'Any prior knowledge on Python Programming Language will be relevant']], 'Mongo Database':[['Introduction to MongoDB', 'MongoDB Basics', 'MongoDB Queries', 'MongoDB Aggregates'],[ 'MongoDB IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'Ultimate Dropshipping':[[ 'A Model called Dropshipping', 'What is Dropshipping', 'The Crowded space','Setting up your Dropshipping Business', 'Setting your online store','Selecting a Dropshipping Partner','The Winning Product','Lets Talk Pricing', 'Think outside the box and be outstanding', 'Promote your store','All in one','Summary'],[ 'Access to a computer or a phone', 'Access to the internet','2-3 hours of work each day', 'A Determined Mindset!']], 'Affiliate Marketing':[['A Model called Affiliate Marketing', 'Roles in Affiliate Marketing', 'Who you work with is important', 'The Perfect Product','Setting your store','Lets talk pricing', 'The Next Big Thing', 'All in one']]
}




courses = [{'course':"Frontend Web Development", 'language': "HTML • CSS • Bootstrap", 'price':0},
           {'course':"Python Programming Language", 'language': "Python", 'price':5},          {'course':"Backend Development with Flask.py", 'language': "Coming Soon...", 'price':10}, {'course':"SQL Database", 'language': "Python • SQL", 'price':2}, {'course':"Mongo Database", 'language': "Mongo • Python", 'price':5}, {'course':"Ultimate Dropshipping", 'price':10}, {'course':'Cryptocurrency and Blockchain Development', 'language': "Coming Soon...", 'price':5}, {'course':"Mobile Application Development", 'language': 'Coming Soon...', 'price':5},{'course':"Backend Development with Node.js", 'language':"Coming Soon...", 'price':5},{'course':"Affiliate Marketing", 'price':10}]


@app.route('/')
def index():
   if "username" in session:
      active_user = session["username"]
   else:
      active_user = False
   return render_template('index.html', courses=courses, active_user=active_user)


@app.route('/jobView')
def jobView():
   jobs = []
   conn = sqlite3.connect('jobs.db')
   cursor = conn.cursor()
   cursor.execute("Select * from Job")
   jobs = cursor.fetchall()
   print(jobs)
   conn.close()
   return render_template('jobView.html', jobs=jobs)
@app.route('/deleteJob')
def deleteJob():
   value = session["email"]
   conn1 = sqlite3.connect('jobs.db')
   cursor1 = conn1.cursor()
   cursor1.execute("Select * From Job Where email = :value", {'value':value})
   jobs = cursor1.fetchall()
   conn1.close()
   
   conn = sqlite3.connect('data.db')
   cursor = conn.cursor()
   cursor.execute("Select * from Android Where email = :value", {'value':value})
   result = cursor.fetchone()
   conn.commit()
   conn.close()
   if result:
      session["android"] = value
   else:
      session["android"] = False

   
   role = request.args.get('role')
   if not role:
      return redirect(url_for('dashboard'))
   else:
      conn = sqlite3.connect("jobs.db")
      cursor = conn.cursor()
      cursor.execute("Delete From Job Where role = :role", {"role":role})
   return render_template('dashboard.html', jobs=jobs, android=session["android"])
   
@app.route('/editJob', methods=["Get","POST"])
def editJob():
   rol = request.args.get('role')
   if not rol:
      return redirect(url_for('dashboard'))
      
   email = session["email"]
   conn = sqlite3.connect('jobs.db')
   cursor = conn.cursor()
   cursor.execute("Select role, description From Job Where role = :role and email = :email", {'role':rol, 'email': email})
   job = cursor.fetchone()
   conn.close()
   if request.method == "POST":
      role = request.form['role']
      description = request.form["description"]
      conn1 = sqlite3.connect('jobs.db')
      cursor1 = conn1.cursor()
      cursor1.execute("Update Job SET role = :role, description = :description Where role = :rol and email = :email", {'role':role, 'description':description, 'rol':rol, 'email':email})
      conn1.commit()
      conn1.close()
      return redirect(url_for('dashboard'))

   
   return render_template("editJob.html", job=job)

@app.route('/listJob', methods=["GET", "POST"])
def listJob():
   if request.method == "POST":
      time = datetime.now()
      name = session['username']
      email = session["email"]
      des = request.form['description']
      role = request.form['role']
      date = time.strftime("%d/%m/%Y")
      conn = sqlite3.connect('jobs.db')
      cursor = conn.cursor()
      cursor.execute("Insert Into Job(email, name, role, description, date) VALUES(:email, :name, :role, :description, :date)", {'email':email, 'name':name, 'role':role, 'description':des, 'date':date})
      conn.commit()
      conn.close()
      return redirect(url_for('jobView'))
   
   return render_template('listJobs.html')
   
@app.route('/job')
def job():
   role = request.args.get('role')
   email = request.args.get('email')
   data = []
   
   if not role or not email:
      return redirect(url_for("jobView"))
   else:
      conn = sqlite3.connect('jobs.db')
      cursor = conn.cursor()
      cursor.execute("Select * From Job Where role = :role and email = :email", {'role':role, 'email':email})
      data = cursor.fetchall()
      conn.close()
   return render_template("job.html", data=data)

@app.route('/discussion')
def discussion():
   discussion = []
   conn = sqlite3.connect('post.db')
   cursor = conn.cursor()
   cursor.execute("Select * from Post")
   discussion = cursor.fetchall()
   conn.close()
      
   return render_template('discussion.html', discussion=discussion)
   
   
@app.route('/commentView')
def commentView():
   Id = request.args.get("id")
   Author = request.args.get('author')
   if Id or Author:
      session['discussionId'] = deepcopy(Id)
      session['discussionAuthor'] = deepcopy(Author)
   else:
      return redirect(url_for("discussion"))
      
   

   id = session['discussionId']
   author = session['discussionAuthor']
   comments = []
   conn = sqlite3.connect('data.db')
   cursor = conn.cursor()
   cursor.execute("select * from Comments Where id = :id", {'id':id})
   comments = cursor.fetchall()
   conn.close()
   return render_template( 'commentView.html', author=author, comments=comments)

@app.route('/comment', methods=["GET", "POST"])
def comment():
   
   if not session['discussionId'] or not session['discussionAuthor']:
      return redirect(url_for('discussion'))

   if request.method == 'POST':
      
      time = datetime.now()
      id = session['discussionId']
      name = session['username']
      date = time.strftime("%d/%m/%Y")
      comment = request.form["comments"]
      conn = sqlite3.connect('data.db')
      cursor = conn.cursor()
      cursor.execute("Insert into Comments(id, name, comment, date) VALUES (:id, :name, :comment,:date)", {'id':id, 'name':name, 'comment':comment,'date':date})
      conn.commit()
      conn.close()
      return redirect(url_for('commentView'))


      
      
   return render_template('comment.html')


@app.route('/publisher', methods=["GET", "POST"])
def publisher():
   size = 0
   if request.method == "POST":
      time = datetime.now()
      name = session["username"]
      pub = request.form["pub"]
      date = time.strftime("%d/%m/%Y")
      conn = sqlite3.connect('post.db')
      cursor = conn.cursor()
      cursor.execute("Select * from Post")
      size += len(cursor.fetchall()) + 1
      cursor.execute("INSERT INTO Post(id, name, post, date) VALUES (:id, :name, :post, :date)", {'id':size, 'name':name, 'post':pub, 'date':date})
      conn.commit()
      conn.close()
      return redirect(url_for('discussion'))
   

   return render_template('publisher.html')

@app.route('/course', methods=["GET", "POST"])
def course():

   content = []
   if "current_course" not in session:
      return redirect(url_for('index'))
   if session["current_course"] == "Python Programming Language":
      content = Course.python_course()
   elif session["current_course"] == "Frontend Web Development":
      content = Course.html_course()
   elif session["current_course"] == "SQL Database":
      content = Course.sql_course()
   elif session["current_course"] == "Ultimate Dropshipping":
      content = Course.dropship_course()
   elif session["current_course"] == "Affiliate Marketing":
      content = Course.affiliate_course()


   
   if "pos" not in session:
      session["pos"] = -1
   if request.method == "POST" and session["pos"] < len(content)-1:
      session["pos"] += 1
   elif request.method == "POST" and session["pos"] == len(content)-1:
      session["pos"] = 0
     
   return render_template('course.html',course=session["current_course"], content=content, progress=session["pos"]+1, length=len(content))

@app.route('/courseRev', methods=["GET", "POST"])
def courseRev():
   if request.method == "POST":
      if session["pos"] == 0:
         session["pos"] = -1
         return redirect(url_for('introPage'))
      else:
         session["pos"] -= 1
   return redirect(url_for('course'))

@app.route('/courseExit', methods= ["GET", "POST"])
def courseExit():
   if request.method == "POST":
      session.pop("current_course")
      session.pop("pos")
   return redirect(url_for('index'))
    
@app.route('/intro')
def introPage():
   global intro
   course = request.args.get("course_name")
   price = request.args.get("course_price")
   content = request.args.get("course_content")
   if course and price:
      session["current_course"] = deepcopy(course)
      session["current_price"] = deepcopy(price)
      session["content"] = deepcopy(content)
   else:
      return redirect(url_for("index"))
   name = session["current_course"]
   if name not in intro.keys():
      return "This Course is not Available", 404
   return render_template('intro.html',name=name, intros=intro)
 
@app.route('/dashboard')
def dashboard():
   value = session["email"]
   conn1 = sqlite3.connect('jobs.db')
   cursor1 = conn1.cursor()
   cursor1.execute("Select * From Job Where email = :value", {'value':value})
   jobs = cursor1.fetchall()
   conn1.close()
   
   conn = sqlite3.connect('data.db')
   cursor = conn.cursor()
   cursor.execute("Select * from Android Where email = :value", {'value':value})
   result = cursor.fetchone()
   conn.commit()
   if result:
      session["android"] = value
   else:
      session["android"] = False

   return render_template('dashboard.html', android=session["android"], jobs=jobs)
      

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/reviews', methods=["GET", "POST"])
def reviews():
   data = []
   conn = sqlite3.connect('review.db')
   cursor = conn.cursor()
   cursor.execute("Select * From Rating")
   data = cursor.fetchall()
   conn.close()
   
   if request.method == "POST":
      name = request.form["name"]

      review = request.form["review"]
      now = datetime.now()
      date = now.strftime("%d / %m / %Y")
      
      conn = sqlite3.connect('review.db')
      cursor = conn.cursor()
      cursor.execute("INSERT INTO Rating(name, rate, date) VALUES(:name, :rate, :date)", {'name':name, 'rate':review, 'date':date})    
      conn.commit() 
      conn.close()

      
   return render_template('review.html', data=data)

@app.route('/contact')
def contact():
   return render_template('contact.html')
@app.route('/privacy')
def privacy():
   return render_template('privacy.html')
@app.route('/login', methods=["GET", "POST"])
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
      conn = sqlite3.connect('data.db')
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
         sender_email = "officialtutspot@gmail.com"
         sender_password = "nuhu gkud kyud fgae"
         recipient_email = email
         body = f"Hello {name}, welcome to Tuspot. \nDo not reply this email, keep it private. \nYour Tutspot password is {password}"
         subject = 'Welcome to Tutspot'
         message = MIMEMultipart()
         message["From"] = "Tutspot.net"
         message["To"] = recipient_email
         message["Subject"] = subject
         message.attach(MIMEText(body, "plain"))
         try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            server.quit()
            print("Email sent successfully!")
         except Exception as e:
            print(f"Failed to send email: {e}")
         
         return redirect(url_for('index'))
   else:
      return render_template('signup.html')

@app.route('/loginDetail', methods=["GET", "POST"])
def loginDetail():
   if request.method == "POST":
      email = request.form['email']
      password = request.form['password']
      conn = sqlite3.connect('data.db')
      cursor = conn.cursor()
      cursor.execute("Select * from Data Where email = :email", {'email': email})
      user = cursor.fetchone()
      if user and email in user:
         if password == user[3]:
            session["email"] = email
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
         
@app.route('/paymentDetail', methods=["POST"])
def payment():
   return render_template("payment.html")

@app.route('/logout')
def logout():
   for i in list(session.keys()):
      session.pop(i)
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")