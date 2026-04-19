from flask import Flask , render_template, request, redirect, url_for, session
import re
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost:3306/gmk_caterers?charset=utf8'
db=SQLAlchemy(app)
app.secret_key = "mykey"

class User_info(db.Model):
    __tablename__="user_info"
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String(20), nullable=False)
    contact_number=db.Column(db.String, nullable=False)
    username=db.Column(db.String(20), primary_key=True)
    password=db.Column(db.String(20), nullable=False)
    confirm_password=db.Column(db.String(20), nullable=False)

class Contact(db.Model):
    __tablename__="contact"
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String(20), primary_key=True)
    message=db.Column(db.String, nullable=False)

class Feedback(db.Model):
    __tablename__="feedback"
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String(20), primary_key=True)
    message=db.Column(db.String, nullable=False)

class Order(db.Model):
    __tablename__="order"
    name=db.Column(db.String(30), nullable=False)
    email=db.Column(db.String(30), primary_key=True)
    event=db.Column(db.String(30), nullable=False)
    date=db.Column(db.Date, nullable=False)
    venue=db.Column(db.String(100), nullable=False)
    add_info=db.Column(db.String(200), nullable=False)

txt=r'^[A-Za-z]{3,}$'
phonep = r'^07[0-9]{9}$'
user=r'^[A-Za-z0-9_$@]{8,20}$'
passs = r'^[A-Z][A-Za-z0-9_$@]{7,19}$'
mail = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/wedding')
def wedding():
    return render_template('wedding.html')
@app.route('/corporate')
def corporate():
    return render_template('corporate.html')
@app.route('/privatep')
def paties():
    return render_template('privatep.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/testimonial', methods=['POST', 'GET'])
def testimonial():
    if request.method=='GET':
        return render_template("testimonial.html")
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get("email")
        message=request.form.get("message")
        if not name or not email or not message:
            msg="Please fill empty fields"
            return render_template("testimonial.html", msg=msg)
        if not re.fullmatch(txt, name):
            msg="Name should contain 3+ characters"
            return render_template("testimonial.html", msg1=msg)
        if not re.fullmatch(mail, email):
            msg="Email should be in this format xyz@xyz.xyz"
            return render_template("testimonial.html", msg2=msg)
        else:
            entry= Feedback(name=name, email=email, message=message)
            db.session.add(entry)
            db.session.commit()
            msg='Feedback Sent Successfully'
            return render_template("testimonial.html", smsg=msg)
    else:
        print("error")
        
@app.route("/feedbacks")
def feedbacks():
    feed=Feedback.query.all()
    return render_template('testimonial.html', feed=feed)
@app.route("/order", methods=['POST', 'GET'])
def order():
    if request.method=='GET':
        return render_template("order.html")
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get('mail')
        event=request.form.get("event")
        date=request.form.get('date')
        venue=request.form.get("venue")
        # menu=request.form.getlist("items")
        add_info=request.form.get("info")
        if not name or not email or not event or not date or not venue:
            msg="please fill empty fields"
            return render_template("order.html", error=msg)
        if not re.fullmatch(txt, name):
            msg="Name should contain 3 or more characters"
            return render_template("order.html", error=msg)
        if not re.fullmatch(mail, email):
            msg="username should contain 8 or more characters can include numbers and special characters(_,@,$)"
            return render_template("order.html", error=msg)
        else:
            entry=Order(name=name, email=email, event=event, date=date, venue=venue, add_info=add_info)
            db.session.add(entry)
            db.session.commit()
            msg='Order booked successfully'
            return render_template("order.html", msg=msg)
    else:
        print ("error")

@app.route('/profile')
def profile():
    user = User_info.query.filter_by(username=session['username']).first()
    return render_template("profile.html", user=user)
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method=='GET':
        return render_template('contact.html')
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get("email")
        message=request.form.get("msg")
        if not name or not email or not message:
            msg="Please fill empty fields"
            return render_template("contact.html", msg=msg)
        if not re.fullmatch(txt, name):
            msg="Name should contain 3+ characters"
            return render_template("contact.html", msg1=msg)
        if not re.fullmatch(mail, email):
            msg="Email should be in this format xyz@xyz.xyz"
            return render_template("contact.html", msg2=msg)
        else:
            entry= Contact(name=name, email=email, message=message)
            db.session.add(entry)
            db.session.commit()
            msg='Message Sent Successfully'
            return render_template("contact.html", smsg=msg)
    else:
        print("error")

@app.route('/login', methods=['POST', 'GET'])
def log():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        uname=request.form.get("username")
        passw=request.form.get("password")
        if not uname or not passw:
            msg="please fill empty fields"
            return render_template("login.html", error=msg)
        if not re.fullmatch(user, uname):
            msg="username should contain 8 or more characters can include numbers and special characters(_,@,$)"
            return render_template("login.html", error=msg)
        if not re.fullmatch(passs, passw):
            msg="Password should be 8 or more characters and must include capital letter in begining"
            return render_template("login.html", error=msg)
        
        user = User_info.query.filter_by(username=uname, password=passw).first()
        if user:
            session['username'] = user.username
            msg="Login successful"
            # profile="Profile"
            return render_template("index.html", msg=msg, profile=profile)
        else:
            msg="Invalid username or password"
            return render_template("login.html", error=msg)

@app.route('/sign', methods=['POST', 'GET'])
def reg():
    if request.method=='GET':
        return render_template("sign.html") 
    if request.method=='POST':
        # data=request.form.values()
        name=request.form.get("name")
        email=request.form.get("email")
        cnum=request.form.get("cnumber")
        uname=request.form.get("uname")
        password=request.form.get("pass")
        cpassword=request.form.get("cpass")
        if not name or not email or not cnum or not uname or not password or not cpassword:
            msg="please fill empty fields"
            return render_template("sign.html", error=msg)
        if not re.fullmatch(txt, name):
            msg="Name should contain 3 or more characters"
            return render_template("sign.html", error=msg)
        if not re.fullmatch(phonep, cnum):
            msg="Phone number must have 10 digits and start with 07"
            return render_template("sign.html", error=msg)
        if not re.fullmatch(user, uname):
            msg="username should contain 8 or more characters can include numbers and special characters(_,@,$)"
            return render_template("sign.html", error=msg)
        if not re.fullmatch(passs, password):
            msg="Password should be 8 or more characters and must include capital letter in begining"
            return render_template("sign.html", error=msg)
        if password!=cpassword:
            msg="password not match"
            return render_template("sign.html", error=msg)
        if not re.fullmatch(mail, email):
            msg="email should be in this xyz@xyz.xyz"
            return render_template("sign.html", error=msg)
        else:
            entry= User_info(name=name, email=email, contact_number=cnum, username=uname, password=password, confirm_password=cpassword)
            db.session.add(entry)
            db.session.commit()
            mess="Resigtration Successful"
            return render_template("login.html", mesg=mess)
    else:
        print("error")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("index.html")

@app.route('/edit', methods=['POST', 'GET'] )
def edit():
        if 'username' not in session:
            return render_template("login.html")
        
        user = User_info.query.filter_by(username=session['username']).first()
        if request.method == 'POST':
            user.name = request.form.get('uname')
            user.email = request.form.get('uemail')
            user.contact_number = request.form.get('unum')
            user.username=request.form.get("usname")
            user.password=request.form.get("upass")
            user.confirm_password=request.form.get("upass")
            if not user.name or not user.email or not user.contact_number or not user.username or not user.password:
                msg="please fill empty fields"
                return render_template('edit.html', msg=msg)
            db.session.commit()
            session['username'] = user.username
            return render_template("profile.html", user=user)
        else:
            return render_template("edit.html", user=user)

@app.route('/delete')
def delete():
    if 'username' not in session:
        return render_template("login.html")
    user = User_info.query.filter_by(username=session['username']).first()
    db.session.delete(user)
    db.session.commit()
    session.pop('username', None)
    mesg="Account deleted Successfully!"
    return render_template("sign.html", mesg=mesg)

if __name__=="__main__": 
    app.run(debug=True)