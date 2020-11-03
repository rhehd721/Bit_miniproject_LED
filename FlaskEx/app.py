import os
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from models import db
from models import Myuser

from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm

app=Flask(__name__)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')
        print("login_sumit")
        return redirect('/')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

# /127.0.0.1 '/register' URI address
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if request.method=='POST':
        if form.validate_on_submit():
            myuser = Myuser()
            myuser.userid = form.data.get('userid')
            myuser.username = form.data.get('username')
            myuser.password = form.data.get('password')

            db.session.add(myuser)
            db.session.commit()

            return redirect('/')
        else:
            print('retry')

    return render_template('register.html', form=form)


# html을 컨트롤러에서 만들어서 View로 전달하는데 컨트롤러와 View를 분리
# /127.0.0.1 '/'
@app.route('/')
def hello():
    userid = session.get('userid', None)
    print(userid)
    return render_template('hello.html',userid=userid)

if __name__ == "__main__":

    basedir=os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile=os.path.join(basedir,'db.sqlite')
    print('file:{}'.format(dbfile))

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SECRET_KEY']='dkjghdfakgjhdfkg'  #임의의 문자열 넣는다.

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)





