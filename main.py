from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
	return redirect('/validate-entry')

@app.route('/validate-entry')
def display_empty_error():
	return render_template('home.html', username_error = '', password_error = '', password_match_error = '', email_error = '')

@app.route('/validate-entry', methods=['POST'])

def validate_entry():
    
	username = request.form['username']
	password = request.form['password']
	verify_pswrd = request.form['verify_password']
	email = request.form['email']
    
	username_error = ''
	password_error = ''
	password_match_error = ''
	email_error = ''

    
	if username == '':
		username_error ='You need to enter something'
	else:
		if len(username) < 3 or len(username) >20 or (' ' in username):
        		username_error = 'Your user name must be between 3 and 20 characters in length and contain no spaces'

	if password == '':
    			password_error = 'You need to enter something'
	else:
    			if len(password) < 3 or len(password) >20 or (' ' in password):
        			password_error = 'Your password must be between 3 and 20 characters in length and contain no spaces'
        			password = ''
    
	if verify_pswrd == '':
    			password_match_error = 'You need to enter something'
	else:
    			if verify_pswrd != password:
      			  	password_match_error = 'Your passwords do not match'
       			 	verify_password = ''
	if (len(email) > 0 and len(email) < 3)\
    	or len(email) > 20 \
    	or (' ' in email) \
    	or email.count("@") != 1 \
    	or email.count(".") != 1:
    			email_error = 'Your email address must be between 3 and 20 characters in length and contain one @ and one period'
    
	if not username_error and not password_error and not password_match_error and not email_error:
    			return redirect('/valid-entry?username={0}'.format(username))
	else:
    			return render_template('home.html', title="validation", username=username, email=email, username_error=username_error, password_error=password_error, password_match_error=password_match_error, email_error=email_error)

@app.route("/valid-entry")
def valid_entry():
	username = request.args.get('username')
	return render_template('welcome.html', username=username)

app.run()
