# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# Create a function named `home` which uses template file named `index.html` given under `templates` folder,
# send your name as template variable, and assign route of no path ('/')
@app.route('/')
def home():
    return render_template('index.html', name='Zylina')

# Write a function named `greet` which uses template file named `greet.html` given under `templates` folder
# and assign to the static route of ('/<greet>')
@app.route('/<greet>', methods=['GET'])
def greet(name):
    if 'user' in request.args:
        usr=request.args['user']
        return render_template('greet.html', user=usr)
    else:
        return render_template('greet.html', user='Send your username with "user" param in query string')

# Write a function named `login` which uses `GET` and `POST` methods,
# and template files named `login.html` and `secure.html` given under `templates` folder
# and assign to the static route of ('login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name=request.form['username']
        return render_template('secure.html', user=user_name)
    else:
        return render_template('login.html')

# Add a statement to run the Flask application which can be reached from any host on port 80.

if __name__ == '__main__':
    #app.run(debug=True)
    app.run('0.0.0.0', port=80)
    ````
#Write an application with database implementation using MySQL and save the complete code as app-with-mysql.py under hands-on/flask-03-handling-forms-and-sql-on-ec2-linux2 folder.
```python
# Import Flask modules

# Create an object named app

# Configure sqlite database

# Create users table within MySQL db and populate with sample data
# Execute the code below only once.
# Write sql code for initializing users table..

# Write a function named `find_emails` which find emails using keyword from the user table in the db,
# and returns result as tuples `(name, email)`.

# Write a function named `insert_email` which adds new email to users table the db.
    # if user input are None (null) give warning
    # if there is no same user name in the db, then insert the new one
    # if there is user with same name, then give warning

# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')

# Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')

# Add a statement to run the Flask application which can be reached from any host on port 80.