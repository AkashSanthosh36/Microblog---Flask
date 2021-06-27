from flask import render_template,flash,redirect,get_flashed_messages,url_for,request
from app import app,db
from app.forms import LoginForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Post
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
	user={'username':'Akash'}
	post=[{'username':'Hemchandhar','work':'Text Summarisation'},
		   {'username':'Harish','work':'Speech'}
		   ]
	return render_template('index.html',title='Home Page',posts=post)

@app.route('/login',methods=['GET','POST'])
def login():
	if(current_user.is_authenticated):
		return redirect(url_for('index'))
	form=LoginForm()
	if(form.validate_on_submit()):
		user=User.query.filter_by(username=form.username.data).first()
		if((user is None) or not (user.check_password(form.password.data))):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user,remember=form.remember_me.data)
		next_page=request.args.get('next')
		if(not next_page or url_parse(next_page).netloc!=''):
			next_page=url_for('index')
			return redirect(url_for(next_page))
		return redirect(next_page)
	return render_template('login.html',title='Sign In',form=form)	

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.shell_context_processor
def make_shell_context():
	return {'db':db,'User':User,'Post':Post}











