from copy import deepcopy
import sqlite3
from os import environ, path
from secrets import token_urlsafe
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session

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
   cursor.execute("Create Table Job(id Integer, name Text, role Text, description Text, date Text)")
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
], 'SQL Database': [[ 'Introduction to SQL', 'SQL Basics', 'SQL Queries', 'SQL Joins', 'SQL Aggregates', 'SQL Functions', 'SQL Practice'], ['Python IDE or Code Editor', 'You must login and pay a token to access this course', 'Any prior knowledge on Python Programming Language will be relevant']], 'Backend Development': [[ 'Introduction to Data Science', 'Data Visualization', 'Data Analysis', 'Data Preprocessing', 'Data Cleaning', 'Data Modeling', 'Data Wrangling'], ['Python IDE or Code Editor', 'You must login and pay a token to access this course', 'Any prior knowledge on SQL Database and Python Programming Language will be relevant']],
'Swift':[[ 'Introduction to Swift', 'Swift Basics', 'Swift Control Flow', 'Swift Collections', 'Swift Functions', 'Swift Practice'], ['Swift IDE or Code Editor', 'You have to  login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'Dart':[[ 'Introduction to Dart', 'Dart Basics', 'Dart Control Flow', 'Dart Collections', 'Dart Functions', 'Dart Practice'],[ 'Dart IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'UI/UX Design Principles':[[ 'Introduction to UI/UX Design', 'UI/UX Design Principles', 'UI/UX Design Tools', 'UI/UX Design Practice'], ['UI/UX Design IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'Kotlin':[[ 'Introduction to Kotlin', 'Kotlin Basics', 'Kotlin Control Flow', 'Kotlin Collections', 'Kotlin Functions', 'Kotlin Practice'],[ 'Kotlin IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'Java':[[ 'Introduction to Java', 'Java Basics', 'Java Control Flow', 'Java Collections', 'Java Functions', 'Java Practice'], [ 'Java IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'Mongo Database':[['Introduction to MongoDB', 'MongoDB Basics', 'MongoDB Queries', 'MongoDB Aggregates'],[ 'MongoDB IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']], 'Digital Marketing':[[ 'Introduction to Digital Marketing', 'Digital Marketing Basics', 'Digital Marketing Tools', 'Digital Marketing Practice'],[ 'Digital Marketing IDE or Code Editor', 'You have to login and make payment to access this course', 'Prior knowledge of any Object-Oriented Programming Language will be an advantage']]
}
python = [
{'title':'Introduction to Python', 'description':'Brief overview of Python', 'content':['Python is a fun and easy programming language developed by Guido Van Rossum in the year 1990. It is widely used in the development of AIs and Backend.','Python is very versatile in the sense that it can be used for AI/ML Development, Backend Web Development(check out the Backend course), Automation, App/Game Development, etc.','For this course, you\'ll need a Python code editor or an IDE(softwares for writing python codes).','We suggest you download the Pycharm IDE on your computer or download the Pydroid3 app on Playstore for the Android users, install, setup and create a file that has a \'.py\' extension and start writing Python codes.']},{'title':'Python Basics', 'description':'Outputs and Comments', 'content':['Here, we will start seeing some codes in action so grab a pen, grab a notebook fasten your seat belts and lets begin.','Output in Python', 'In Python, output refers to displaying information to the user. The most common way to output data in Python by using the `print()` function. ','The `print()` function can take various data types such as strings, numbers, and more.','Code Examples :', 'print("Hello, World!")','print(42)', 'print(3.14)','Copy the code above, paste it on your IDE or code editor and you will see the following outputs: ','Hello, World!','42','3.14', 'The first output is a String because it is enclosed in quotaion marks. You may be asking, why didn\'t I put the numeric values too in a quotation mark. That is because, python knows numbers so if you put numbers in quotaion marks, python will automatically treat them as strings.','You can also use the `print()` function to output multiple items separated by a comma.','Code Example:','print("The answer is", 42)','The Output is: The answer is 42','Comments','Comments are used to describe a line or block of codes. It is denoted by a \'#\' sign.','Code Example: ','print("Hello World")','#prints Hello','When you run the code above, you realize that the comment which is the line of code gets ignored by the interpreter and is not executed. The purpose of comments is to describe codes for easy understanding of other developers and yourself in the future. Its a good practice to always use comments in your codes.',
            'Summary','It is very important to understand outputs in python because the main reason for writing codes is to see a desired output when the code is executed. In programming the best way to become better is to practice so go ahead and practice what you\'ve learnt in this lesson before going to the next.']},{'title':'Basic Syntax','description':'Variables', 'content':['A variable in Python is a way to store information that you want to reuse or manipulate later. It is a named location in memory for storing data',
           'Think of a variable as a labeled box where you can store your data.Just like you might have a box labeled "Toys" to store toys, you can have a variable labeled `message` to store a string.',
            'Code Example:',
           
            'message = "Hello, Python!" ',
            'number = 10',
            'pi = 3.14159',
            'print(message)',
            'print(number)',
            'print(pi)',
            
            'The Outputs are:','Hello, Python!','10','3.14159',
            'To declare a variable, you need a variable name, an equal sign and a value to the variable, as simple as that.',
            'Variables can store different types of data such as integers, floats, strings, and more. ',
            'Here are a few code examples:',
            'Integer variable',
            'age = 25',
            'Float variable',
            'height = 5.9',
            'String variable',
            'name = "Alice"',
        
            'Boolean variable',
            'is_student = True',
         
            'Summary',
            'In this lesson, you learned how to create variables to store data. We will talk about the different datatypes in the next page. Be sure to practice and don\'t forget all you need to declare a variable is a name, an equal sign and a value.',
           'We covered the basics of outputting strings, numbers, and multiple items, as well as how to create and use variables of different data types. Understanding these fundamentals is crucial as you move forward with learning Python. Keep practicing, and you\'ll become more comfortable with these concepts in no time!']},

{'title':'Basic Syntax', 'description':'Data types in Python', 'content':['Data types in Python specify what kind of value a variable holds. Understanding data types is crucial because it helps you know what operations can be performed on a particular piece of data. Examples of Data Types in Python are: ',
            'Integers: Whole numbers, positive or negative, without decimals.',
            'Code Example',
            'age = 25',
            'year = 2023',
      
            'Floats: Numbers with decimals.',
            'Code Examples: ',
            'height = 5.9',
            'price = 19.99',
          
            'Strings: Sequences of characters, enclosed in single or double quotes.'
            'Code Examples: ',
            'name = "Alice"',
            'message = \'Hello, World!\'',
            
            'Booleans : They can only have two values \'True\' and \'False\' which do not need to enclosed in quotation marks because python also recognizes them too. If you don\'t understand them, just keep going it will all make sense later.',
            'Code Examples: ',
            'is_student = True',
            'has_license = False',
            'Summary','If things do not add up for you, just keep going forward, you will understand better once you see them in some code action.']},
           
{'title':'Basic Syntax', 'description':'Operators in Python', 'content':['Operators in Python are used to perform operations on variables and values. They are categorized based on the operations they perform.'
            '1. Arithmetic Operators: Used to perform basic arithmetic operations like addition, subtraction, multiplication, etc.',
            'Code Examples: ',
            
            'sum = 10 + 5  # sum is 15',
            'difference = 10 - 5  # difference is 5',
            'product = 10 * 5  # product is 50',
            'quotient = 10 / 5  # quotient is 2.0',
            'floor_div = 10 // 3  # floor_div is 3',
            'remainder = 10 % 3  # remainder is 1',
            'power = 2 ** 3  # power is 8','All other operators are quite familiar except the Modulo(%) and the Floor Div(//) operators. The Modulo operator is used to return the remainder of a division operation i.e 10%5 will be 0 because they will be no remainder and 7%6 will be 1 because the remainder after dividing 7 by 6 will be 1.','The Floor Div(//) Operator can be seen as the opposite of the modulo operator which returns the number of times a number divides another, not minding the remainder i.e 10//3 will be 3 because thats the number of times 3 can divide 10 and we don\'t mind the remainder. So you can simply say its just normal division but not minding any remainders.','If it doesn\'t make sense, read again and try to understand things because they\'re quite technical.',
            
            '2. Comparison Operators: They are used to compare two values and they return Boolean values. They make use of greater than(>), less than(<), greater than or equal to(>=), less than or equal to(<=), equal-equal to(==) and not equal to(!=).',
            'Code Examples: ',
            'x = 10',
            'y = 5',
            'print(x == y)  #Compares if the two values are exactly equal. False',
            'print(x != y)  # Checks if the two values are not equal. True',
            'print(x > y)  # Checks if x is greater than y. True',
            'print(x < y)  # Checks is x is less than y. False',
            'print(x >= y)  # Checks is x greater or equal to y. True beacuse x is greater',
            'print(x <= y)  # Checks if x is less than or equal to y. False',
      
            '3. Logical Operators: Used to combine conditional statements.You will see its use later in the course.',
            'Code Examples: ',
            'a = True',
            'b = False',
            'print(a and b)  # False',
            'print(a or b)  # True',
            'print(not a)  # False',
            'Summary'
            'In this lesson, you learned about different operators, including arithmetic, comparison, and logical operators. ',
            'These fundamental building blocks will allow you to perform a wide range of operations in your Python programs. Keep practicing, and you\'ll get comfortable with using these operators!']},
{'title':'Basic Syntax','description':'Control Flow: If Statements', 'content':['Control flow statements in Python allows you to execute different blocks of code based on certain conditions. This is essential for making decisions in your programs.','If Statements','The `if` statement allows you to execute blocks of code only if a specified condition is true. Here\'s a basic example:','age = 18','if age >= 18:','    print("You are an adult.")','In this example, the message "You are an adult." will be printed only if the variable `age` is greater than or equal to 18. Also observe the indentation given in the print() function, it is very important to show that if a condition is met, the block of code beneath it will be executed. The indentation could be 2 to 4 blank spaces.',  'Else Statements','The `else` statement can be used to execute a block of code if the condition in the `if` statement is false. Here\'s how it works:','age = 16','if age >= 18:','    print("You are an adult.")','else:','    print("You are not an adult.")',
            'In this case, the message "You are not an adult." will be printed because the variable `age` is less than 18 and so the `else` block will be executed.',
            'Elif Statements',
            'The `elif` statement stands for "else if" and can be used to check multiple conditions. If the first condition is false, the `elif` statement checks the next condition, and so on:','age = 17','if age >= 18:','    print("You are an adult.")','elif age >= 13:','    print("You are a teenager.")','else:','    print("You are a child.")',  'In this example, the message "You are a teenager." will be printed because the variable `age` is greater than or equal to 13 but less than 18. Observe the inde tations.',
            'Summary',
            'In this lesson, you learned about control flow in Python using `if`, `else`, and `elif` statements. These statements allow you to make decisions in your code based on conditions. ',
            'By using `if` statements, you can execute code only when certain conditions are met. The `else` statement provides an alternative block of code when the `if` condition is not met, and `elif` statements allow for multiple conditions to be checked sequentially.',
            'These control flow tools are fundamental for creating dynamic and responsive programs. Keep practicing, and you\'ll become proficient in using them in no time!']}                  

]

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



courses = [{'course':"Frontend Web Development", 'language': "HTML • CSS • Bootstrap", 'price':0, "content":frontend},
           {'course':"Python Programming Language", 'language': "Python", 'price':5, "content":python},          {'course':"Backend Development", 'language': "Python • Flask • SQL", 'price':10,"content":python}, {'course':"SQL Database", 'language': "Python • SQL", 'price':2,"content":python}, {'course':"Mongo Database", 'language': "Mongo • Python", 'price':5,"content":python}, {'course':"Digital Marketing ", 'price':5,"content":python},  {'course':"Java Programming Language", 'language': "Java", 'price':5,"content":python}, {'course':'Kotlin Programming Language', 'language': "Kotlin", 'price':5,"content":python}, {'course':"Dart Programming Language", 'language': 'Dart', 'price':5,"content":python}, {'course':'Swift Programming Language', 'language':'Swift', 'price':5,"content":python},         {'course':"UI/UX Design Principles", 'price':2,"content":python}]


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
   conn.close()
   return render_template('jobView.html', jobs=jobs)
   
@app.route('/job')
def job():
   data = []
   Id = request.args.get("id")
   
   if Id:
      session['jobId'] = Id
   else:
      return redirect(url_for("jobView"))
   conn = sqlite3.connect('jobs.db')
   cursor = conn.cursor()
   cursor.execute("Select * From Job Where id = :id", {'id':session["jobId"]})
   data = cursor.fetchall()
   conn.close()
   return render_template("job.html", jobs=data)

@app.route('/discussion')
def discussion():
   conn = sqlite3.connect('post.db')
   cursor = conn.cursor()
   cursor.execute("Select * from Post")
   discussions = cursor.fetchall()
   conn.close()
   return render_template('discussion.html', discussions=discussions)

@app.route('/commentView')
def commentView():
   Id = request.args.get("id")
   Author = request.args.get('author')
   if Id or Author:
      session['discussionId'] = Id
      session['discussionAuthor'] = Author
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
   if request.method == "POST":
      time = datetime.now()
      name = session["username"]
      pub = request.form["pub"]
      date = time.strftime("%d/%m/%Y")
      conn = sqlite3.connect('post.db')
      cursor = conn.cursor()
      cursor.execute("Select * from Post")
      size = len(cursor.fetchall()) + 1
      cursor.execute("INSERT INTO Post(id, name, post, date) VALUES (:id, :name, :post, :date)", {'id':size, 'name':name, 'post':pub, 'date':date})
      conn.commit()
      conn.close()
      print("Added to Post table")
      return render_template('discussion.html')
   

   return render_template('publisher.html')

@app.route('/course', methods=["GET", "POST"])
def course():
   
   
   if "pos" not in session:
      session["pos"] = -1

   if request.method == "POST":
      if session["pos"] < len(session["content"])-1:
         session["pos"] += 1
      else:
         session["pos"] = 0
      
   return render_template('course.html',course=session["current_course"], content=session["content"], length=len(session["content"]), progress=session["pos"]+1)

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
   conn = sqlite3.connect('data.db')
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