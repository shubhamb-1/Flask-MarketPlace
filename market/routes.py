from flask import render_template,flash,redirect,url_for
from market import app
from market import db
from market.models import Item,User
from market.forms import RegisterForm,LoginForm
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('base.html')

@app.route('/market')
def market_page():
    items=Item.query.all()
    return render_template('market.html',items=items)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data):
            flash(f'You have been logedin Successfully as {attempted_user.username}',category="success")
            login_user(user)
            return redirect(url_for('market_page'))
        else:
            flash(f'Username/Password is Wrong.Please try again',category="danger")
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create= User(username=form.username.data,
                             email_address=form.email_address.data,
                             password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(f"Account created Successfully,You are now LogedIn as {user_to_create.username}",category="success")
        return redirect(url_for('market_page'))
    if form.errors != {} :
        for err in form.errors.values():
            flash(f"There was an error with Creating User {err}",category="danger")

    return render_template('register.html',form=form)