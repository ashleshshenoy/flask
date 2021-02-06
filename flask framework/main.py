from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from werkzeug.utils import secure_filename





app=Flask(__name__)
app.secret_key='hello'
UPLOAD_FOLDER='/UPLOAD_FOLDER'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
permanent_session_lifetime=timedelta(days=5)

@app.route("/")
def home():
	return render_template('second.html',content='contact us ')


@app.route('/login/',methods=['POST','GET'])
def login():
	
	if request.method == 'POST':
		user=request.form["nm"]
		age=request.form['ae']
		address=request.form['add']
		#session.permanent=True            #session for storing more than once 
		session["user"]=user
		session['address']=address
		session["age"]=age
		return redirect(url_for("user"))

	else:
		return render_template('login.html')

@app.route('/user')
def user():
	if 'user' in session:
		user=session["user"]
		add=session['address']
		age=session['age']
		session.pop("user")
		session.pop("address")
		session.pop("age")
		check1=True
		flash('your data has been saved successfully','info')
		file=open('website.txt','a')
		file.write(f'log:{user},{age},{add}')
		return render_template('user.html',content=f'user details: {user} is {age} old and lives in {add}')
	else:
		return redirect(url_for('login'))



@app.route('/form',methods=['POST','GET'])
def servey():
	check3=False
	if request.method=="POST":
		f=request.files['file']
		f.save(secure_filename(f.filename))
		check3=True
	return render_template('form.html',check=check3)



if __name__=="__main__" :
	#app.jinga_env.auto_reload=True 
	#FLASK_ENV=development
	#app.config['TEMPLATE_AUTO_RELOAD']=True 
	app.run(debug=True )






