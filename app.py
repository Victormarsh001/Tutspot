from copy import deepcopy
import sqlite3
import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
if not app.secret_key:
    app.secret_key = secrets.token_urlsafe(32)

if not os.path.exists('tutspotData.db'):
   conn = sqlite3.connect('tutspotData.db')
   cursor = conn.cursor()
   cursor.execute("Create Table Data(name TEXT, country TEXT, email TEXT, password TEXT)")
   cursor.execute("Insert into Data Values('Heung', 'China', 'seongheungshim@gmail.com', 'heung4k')")
#Android Table  
   cursor.execute("CREATE Table Android(email TEXT)")
   cursor.execute("INSERT INTO Android(email) VALUES('androidTutspot@gmail.com')")
#Reviews Table
   cursor.execute("CREATE Table Reviews(name TEXT, review TEXT)")
   conn.commit()
   conn.close()

intro = {'Frontend Web Development': [['Introduction to HTML', 'HTML Basic Structure', 'HTML Headings', 'HTML Paragraphs', 'HTML Links', 'Images/Videos in HTML', 'HTML Lists', 'HTML Tables','HTML Forms','Semantic HTML'], 
                              ['HTML Code Editor','You must signup or login to access this free course', 'Any prior knowledge on programming will be an icing on the cake']
], 'Machine Learning':[['Introduction to Machine Learning', 'Linear Regression', 'Logistic Regression', 'Decision Trees', 'Random Forest', 'Neural Networks', 'K-Nearest Neighbors', 'Support Vector Machines', 'Clustering', 'Dimensionality Reduction', 'ML Practice'], 
                              ['Python IDE or Code Editor','You must login and pay a token to access this course', 'Any prior knowledge on Basic Mathematics, Statistics and Python Programming Language is relevant']
], 'SQL Database': [[ 'Introduction to SQL', 'SQL Basics', 'SQL Queries', 'SQL Joins', 'SQL Aggregates', 'SQL Functions', 'SQL Practice'], ['Python IDE or Code Editor', 'You must login and pay a token to access this course', 'Any prior knowledge on Python Programming Language will be relevant']], 'Data Science': [[ 'Introduction to Data Science', 'Data Visualization', 'Data Analysis', 'Data Preprocessing', 'Data Cleaning', 'Data Modeling', 'Data Wrangling'], ['Python IDE or Code Editor', 'You must login and pay a token to access this course', 'Any prior knowledge on SQL Database and Python Programming Language will be relevant']]}

frontend =[
{'title':'Introduction to HTML', 'description':'Brief overview of HTML', 'content':['HTML is short for Hyper Text Markup Language. It is the standard language for building and structuring web pages.', 'HTML was developed by Mr. Tim Berners Lee who was obsessed with building a media through which scientists from colleges and universities could access and share documents, and that obsession led to the development of the World Wide Web(WWW), Hyper Text Transfer Protocol(the rules that guides the transfer of data on the WWW) and HTML(the language of the web) in 1990 by him.', 'This course is the Frontend Web Developer course that will teach you how to build the frontend of a web site or web app using HTML and CSS. Frontend is the part of the web site or app that interacts with the users.','You may be asking, why would anyone need to learn HTML especially in the world of today where AIs have made everything easier. Yes AIs have automated everything but when using AIs to build your own website, you WILL surely need to make customized changes to the codes that the AI will generate for you and if you know nothing about HTML or programming as a whole, you will not know where or what to change or edit. That\'s the fact.', 'For this course, you\'ll need to download a HTML code editor(a software for writing codes).', 'For the PC users, I strongly recommend VS Code so go ahead and download VS Code and create a file that has the extension \'.html\'. Once that is done, open the file and thats where we\'ll be writing our HTML codes', 'For the Android/iOS users, simply head to the Google Playstore or the App Store, search and download HTML code editor', 'Summary', 'Once you\'ve setup the code the code editor, grab a pen, a notebook and get ready to become the latest Frontend Web Developer.']},

{'title':'Basics of HTML', 'description':'Foundational concepts of HTML including tags, elements, attributes.', 'content':['HTML is not a Programming language, it is a Markup language that describes the structure of web pages using markup.', 'HTML elements are the building blocks of HTML pages. HTML tags are the codes that describes the appearance of a web page in a browser. They are enclosed in angle brackets, and most come in pairs: an opening tag and a closing tag.', 'Examples of Common Tags:', '- `<h1>` to `<h6>`: Heading tags, with `<h1>` being the largest and `<h6>` the smallest.', '`<p>`: Paragraph tag, used to define blocks of text.', '`<a>`: Anchor tag, used to create hyperlinks.','- `<img>`: Image tag, used to embed images in a page.','- `<ul>`, `<ol>`, `<li>`: List tags, used for creating unordered and ordered lists.', 'HTML elements are the building blocks of HTML. An element is defined by a start tag, some contents, and an end tag.','Example:  <p>This is a paragraph.</p>','In the example above, `<p>` is the start tag, and `</p>` is the end tag. The text  "This is a paragraph." is the content of the `<p>` element.']},
{'title':'Basics of HTML', 'description':'Foundational concepts of HTML including tags, elements, attributes.', 'content':['A basic HTML document has a well-defined structure. It consists of several key parts:', '1. `<!DOCTYPE html>` This declaration defines the document type and version of HTML. It helps the browser render the page correctly.', '2. `<html>` This element is the root element of an HTML page. It contains all other elements in the document.', '3. `<head>` This element contains meta-information about the document, such as its title, character set, and links to stylesheets or scripts.', '4. `<title>`: This sets the title of the web page (as shown in your browser tab `Tutspot`).', '5. `<meta>`: Provides metadata, such as character set and keywords for search engines.', '6. `<link>`: It is used to setup links or connections to external resources like stylesheets, etc.',' 7. `<style>`: Contains internal CSS styles(we will get to that later in the course).', '8.  `<body>`: The `<body>` element contains the actual content of the web page, such as text, images, links, and other media.', '9. Headings (`<h1>` to `<h6>`): Define headings(we`ll see its use later).', '10. Paragraphs (`<p>`): As you\'ve seen, it defines text paragraphs.', 'Summary','There are many others but these are the commonly used elements.Having said all that, if you don\'t understand anything, just keep going it will all make sense once you see them in use. For now just take note of the different elements and tags and their uses.']},

{'title':'Basics of HTML', 'description':'Foundational concepts of HTML including tags, elements, attributes.', 'content':['<!DOCTYPE html>','<html lang="en">','    <head>', '        <meta charset="UTF-8">', '        <meta name="viewport" content="width=device-width, initial-scale=1.0">', '        <title>My First Web Page</title>', '    </head>', '    <body>', '        <h1> Welcome to My Website</h1>','        <p>This is a paragraph of text.</p>', '        <a href="https://www.google.com">Visit Us</a>','    </body>','</html>','Summary','The code above contains the basics of a HTML document. Copy the code above and run it on your html editor. Take your time to observe the outcome of the code, arrangements and the indentations in certain places. Each tags, attributes and elements will be explained in the next slide.','Understanding the basic structure and elements of HTML is crucial for web development. By mastering HTML tags and the document structure, you can create well-structured and accessible web page.']},

{'title':'Basics of HTML', 'description':'Foundational concepts of HTML including tags, elements, attributes.', 'content':['Try to understand this analogy:', 'The `!Doctype html` tag tells the browser that the document type is a HTML document, but even if you don`t add the tag, there won`t be an issue.','The `<html></html>` element is seen as a mother ship that contains other parts of the HTML documents, you have to include this part.','The `<meta>` tag is a self closing tag i.e. you don`t need to add a closing tag to it if you observed. This tag holds some peripheral informations about your site it has attributes like, name, content, author etc. Feel free to browse more and understand them. They all have effects when the site is hosted or viewed from a web browser.','The `link` tag is used to create a connection to external resources such as CSS files, bootstrap(a css framework, we will talk about them later), etc.','The `title` tag is used to indicate the title of the site as in our case its `Tutspot` as you can see on your browser tab above.','The `head` element is like a sub-mothership that holds informations of how the site should be rendered on the browser. The meta, link and title tags are all in the head element.','Next is the `body` element that holds all the contents that will be displayed on the webpage. They could be the paragrapgh tags, heading tags, image tag, anchor tag,etc.','Take a look at the Anchor tag in the code, it is used to create a commectiin to another webpage or another website entirely. It has an attribute called `href` (Hyperlink Reference)which takes the url of the webpage or website that you want to connect to. Click the `Visit Us` link and see what happens.','Summary','Go through the code more often and understand the HTML structure.We will talk more about tags in the next slide.']},

{'title':'Headings in HTML', 'description':'Meaning, Types and Uses of Headings in HTML.', 'content':['Headings are used in formatting a webpage to enhance easy navigation and understanding by the user. Headings in HTML ranges from <h1> being the highest to <h6> being the lowest.', 'Correct use of Headings:','- `<h1>`: Typically used for the main title of the page. There should usually be only one `<h1>` tag per page.','- `<h2>`: Used for main section titles.','- `<h3>`: Used for subsection titles.','- `<h4>` to `<h6>`: Used for further subdivision of content as needed.', 'Code Examples: ', '<h1> Heading </h1>', '<h2> Heading </h2>', '<h3> Heading </h3>', '<h4> Heading </h4>', '<h5> Heading </h5>', '<h6> Heading </h6>', 'Summary','Copy the above code and paste in the body element of your own code and see the outcome. Understand the correct use of the types of Headings in HTML.']},

{'title':'Paragraphs in HTML', 'description':'Handling texts and paragraphs in HTML.', 'content':['Paragraphs are used to group blocks of text together, making it easier to read and understand. The `<p>` tag defines a paragraph in HTML.', 'Code Example: <p> This is a simple paragraph. </p>', 'Best Practices for Paragraphs','- Use paragraphs to break up text into manageable chunks.','- Keep paragraphs short and focused on a single idea.','- Avoid using multiple `<br>` tags for spacing; use paragraphs instead.','Text Formatting Elements','HTML provides various tags to format text, allowing you to emphasize or style contents as needed.','Common Text Formatting Tags:','- `<b>`: Makes text bold.','- `<strong>`: Also makes text bold, but with semantic importance.','- `<i>`: Italicizes text.','- `<em>`: Italicizes text with emphasis.','- `<u>`: Underlines text.','- `<mark>`: Highlights text.','- `<small>`: Makes text smaller.','- `<del>`: Strikethrough text (indicates deletion).','- `<ins>`: Underlines text (indicates insertion).','- `<sub>`: Subscript text.','- `<sup>`: Superscript text.', 'Summary','Keep going, you are doing great!'
]},
{'title':'Paragraphs in HTML', 'description':'Handling texts and paragraphs in HTML.', 'content':['Code Example:','<p>This is a <strong>bold</strong> text and this is an <em>emphasized</em> text.</p>','<p>Here is some <mark>highlighted text</mark> and a <del>deleted text</del>.</p>', '<p>Use <sub>subscript</sub> and <sup>superscript</sup> for chemical formulas like H<sub>2</sub>O and mathematical expressions like x<sup>2</sup>.</p>', 'Paste the above into your code. Run it and see the outcome.', 'Best Practices for Text Formatting','- Use formatting sparingly to avoid overwhelming the reader.', '- Prefer semantic tags (`<strong>`, `<em>`) over purely stylistic ones (`<b>`, `<i>`) for better accessibility and SEO.', '- Use `<mark>` for highlighting important information.', 'Summary', 'Understanding how to use headings, paragraphs, and text formatting elements is essential for creating well-structured and accessible web content. Proper use of these elements not only enhances the readability of your content but also improves the overall user experience.']},
{'title': 'Mastering Links and Hyperlinks in HTML', 'description': 'How to create and manage links in HTML, including the use of anchor tags and URLs.','content':['Hyperlinks are the backbone of the web, allowing users to navigate between pages and websites. In HTML, hyperlinks are created using the `<a>` (anchor) tag.','The basic syntax for creating a link is:','<a href="URL">Link Text</a>', '- `href`: The `href` attribute specifies the destination URL. It can be an absolute URL (full web address) or a relative URL (path relative to the current page).','- `Link Text`: The clickable text that users see.','Best Practices:','- Use absolute URLs for external links to avoid confusion.', '- Use relative URLs for internal links to make the website easier to maintain and more flexible.','Code Examples:', '<a href="https://www.google.com"> Go to Google </a>', 'Summary','Mastering the use of links and hyperlinks in HTML is crucial for creating an interconnected and user-friendly website. Properly implemented links not only improve navigation and accessibility but also contribute to better SEO performance.'
]},
{'title': 'Working with Images and Media in HTML', 'description': 'Understand how to integrate images, videos, and other media into your HTML pages.', 'content':['Media elements such as images, videos, and audio are essential for creating engaging and visually appealing web pages. HTML provides various tags and attributes to incorporate and manage these elements efficiently.','The `<img>` tag is used to embed images in an HTML document. It is a self-closing tag that requires at least the `src` and `alt` attributes.', 'Code Examples:','<img src="image.jpg" alt="Description of the image">','- `src`: Short for Source, specifies the path to the image file. This can be a relative or absolute URL.','- `alt`: Provides alternative text for the image (if at all the image could not be displayed) which is important for accessibility and SEO.','Choosing the Right Format:','- Use JPEG for photographs and complex images.','- Use PNG for images requiring transparency or high-quality graphics.','- Use GIF for simple animations.','- Use SVG for vector graphics that need to scale without losing quality.','How to set:','In your computer or phone, upload an image to the same folder that has your current `.html` file, get the name of the image and the folder name and use them as in the code example below.','<img src="folder_name_here/image_name_here" alt="Alternative Display">', 'You could go online, search and click on an image. Copy the image link and paste it in the `src` attribute on your code. When you run the code, it will open the image online(remember you have to establish internet connection).', 'Summary','Keep going, you are doing great'
]},
{'title': 'Working with Images and Media in HTML', 'description': 'Understand how to integrate images, videos, and other media into your HTML pages.','content':['The `<video>`  and `<audio>` tags allows you to embed videos and audio content in HTML. They support multiple file formats and provides attributes for controlling playback.', 'Code Example:','<video controls>','    <source src="online_url_to_video_or_videoName.mp4" type="video/mp4">','</video>','<audio controls>','    <source src="url_to_audio.mp3" type="audio/mpeg">','</audio>','- `controls`: Adds video and audio controls like play, pause, and volume.','- `source`: Specifies the video/audio file and format.', 'Summary','Incorporating images effectively in your HTML documents enhances user experience and engagement. Understanding the various tags and techniques for handling images will help you create more dynamic and accessible web pages.']},

{'title':'HTML Lists', 'description':'Structuring contents using Lists', 'content':['Lists are ideal for presenting items in a sequential or bullet format.','Unordered Lists','Unordered lists display items in a bullet-point format. The `<ul>` tag is used to create an unordered list, with each item enclosed in an `<li>` tag.', 'Code Example: ','<ul>','    <li>Item 1</li>','    <li>Item 2</li>','    <li>Item 3</li>','</ul>', 'Ordered Lists','Ordered lists display items in a numbered format. The `<ol>` tag is used, with each item enclosed in an `<li>` tag.','Code Example: ','<ol>','    <li>Step 1</li>','    <li>Step 2</li>','    <li>Step 3</li>','</ol>', 'Nested Lists','Lists can be nested inside each other to create multi-level lists. This is useful for representing hierarchical data.','Code Example: ','<ul>','    <li>Programming Languages','    <ul>','        <li>JavaScript</li>','       <li>Python</li>','        <li>Java</li>','    </ul>','        </li>','        <li>Web Development','    <ul>','        <li>HTML</li>','        <li>CSS</li>','        <li>JavaScript</li>','    </ul>','    </li>','</ul>','Summary','Lists are very important especially when organizing contents on a webpage. Go through the codes above, run them on your editor and study the outcome.']},
{'title':'HTML Tables', 'description':'Structuring contents using Tables', 'content':['A Table is a  fundamental element in HTML that is used to structure and display data in rows and columns.The `<table>` tag is used to create a table. A basic table includes the `<tr>` (table row), `<th>` (table header), and `<td>` (table data) elements.', 'Code Example: ','<table>','    <tr>','        <th>Course</th>','        <th>Duration</th>','    </tr>','    <tr>','        <td>HTML Basics</td>','        <td>3 hours</td>','    </tr>','    <tr>','        <td>CSS Fundamentals</td>','        <td>4 hours</td>','    </tr>','</table>','Summary','Tables are used to structure data in rows and columns, take note of the tags(`tr`, `th`, `td`) within the `<table>` elements.','Now this is quite a milestone. why don`t you take a break and practice all we had discussed earlier and don`t forget to send us a review of your experience with Tutspot so far.']},{'title':'HTML Forms', 'description':'Handling Forms and User Inputs in HTML','content':['Forms collect user inputs and are created using the `<form>` tag, with various input types like `<input>`, `<textarea>`, and `<select>`.','Code Example: ','<form action="/submit" method="post">','    <label>Name:</label>','    <input placeholder="Write username here"type="text" id="name" name="name">','    <input type="submit" value="Submit">','</form>','The <form> tag in the code above contains two attributes(action and method) which are used when working on the backend of your web app. When you purchase and start learning our Backend Development Course, you\'ll see the action and method attributes in use but for now lets continue in the Frontend Course.','The <label> tag provides descriptions to the <input> telling the user the type of data to input.','The <input> tag provides the space for a user to input the data.It is a self-closing tag as you\'ve noticed, it does not need a closing tag like this `</input>`. It has many attributes(feel free to lookup)','Common attributes of the <input> tag: ','\'type\' : This attributes defines the type of data to input. Its values could be \'text\'(for mere texts), \'email\'(for email address), \'password\'(for paswords)\', \'integer/number\'(for numbers)\' or \'submit\' (this particular values changes the input space to a button as you see in the second <input> tag in the code above).','\'id\' : This attribute is used to set a specific identifier for a particular tag(we\'ll make use of it in the Backend Course). Its value could be anything you want to give to it','\'placeholder\' : This is used to give further description to an input.', 'Summary', 'I don\'t wanna be a spoiler but I want you to copy the code above and put it in your work and study each of the <input> tag attributes and understand their effects on your code output.There are many more attributes of the <input> tag out there, do yourself the favour to look them up and practice them. It is very important to practice and fully understand HTML forms before moving on to the next concept. Practicing is the only way to become a better programmer.']},

{'title':'HTML Containers', 'description':'Working with divs', 'content':['HTML provides tags to enable the developer to organise contents in divisions on the webpage. For the this course, we\'ll only talk about the <div> tag. The <div> tag is used in organizing content of the webpage in divisions.','Code Example: ', '<div>','    <h3> The first div </h3>','    <p> This is the first div </p>', '</div>','<div>','    <h3> The second div </h3>','    <p> This is the second div </p>', '</div>', 'Best use of divs', 'Divs are used to organise contents on the web page.', 'Use divs to create a visually appealing webpage.','Summary','Divs organizes contents into partitions on the webpage. Do not forget to continue practicing.']}

]



courses = [{'course':"Frontend Web Development", 'language': "HTML • CSS • JS", 'price':5},
           {'course':"Machine Learning", 'language': "Python • Numpy • Pandas", 'price':12},
           {'course':"SQL Database", 'language': "Python • SQL", 'price':4},
           {'course':"Data Science", 'language': "Python", 'price':15},
           {'course':"Backend Development", 'language': "Python • Flask • SQL", 'price':10},
        {'course':"Blockchain Development", 'price':20},
           
        {'course':"Android Development", 'language': "Java • Kotlin • Android Studio", 'price':20},
           {'course':"iOS Development", 'language': "Swift • X-Code • iOS", 'price':20},
          {'course':"Cross-platform Development", 'language': "Dart • Flutter", 'price':15},
           
           {'course':"UI/UX Design", 'price':8}
]

@app.route('/')
def index():
   if "username" in session:
      active_user = session["username"]
   else:
      active_user = False
   return render_template('index.html', courses=courses, active_user=active_user)

@app.route('/course', methods=["GET", "POST"])
def course():
   
   global frontend
   if "pos" not in session:
      session["pos"] = -1

   if request.method == "POST":
      if session["pos"] < len(frontend)-1:
         session["pos"] += 1
      else:
         session["pos"] = 0
      
   return render_template('course.html',course=session["current_course"], frontend=frontend, length=len(frontend), progress=session["pos"]+1)

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
   if course and price:
      session["current_course"] = deepcopy(course)
      session["current_price"] = deepcopy(price)
   else:
      return redirect(url_for("index"))
   name = session["current_course"]
   if name not in intro.keys():
      return "This Course is not Available", 404
   return render_template('intro.html',name=name, intros=intro)



   
@app.route('/dashboard')
def dashboard():
   value = session["email"]
   conn = sqlite3.connect('tutspotData.db')
   cursor = conn.cursor()
   cursor.execute("Select * from Android Where email = :value", {'value':value})
   result = cursor.fetchone()
   conn.commit()
   if result:
      session["android"] = value
   else:
      session["android"] = False

   return render_template('dashboard.html', android=session["android"])
      

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
      conn = sqlite3.connect('tutspotData.db')
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
      conn = sqlite3.connect('tutspotData.db')
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