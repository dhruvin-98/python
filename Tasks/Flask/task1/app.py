from flask import *

app = Flask(__name__)

app.secret_key = "dhruvin"

users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

#Register

@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        fn=request.form.get('fn')
        ln=request.form.get('ln')
        un=request.form.get('un')
        pw=request.form.get('pw')

        users[un]={

            'fn':fn,
            'ln':ln,
            'pw':pw

        }

        return redirect(url_for('login'))
    return render_template('register.html')


#login

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST' :

        un = request.form.get('un')
        pw = request.form.get('pw')

        if un in users and users[un]['pw'] == pw :
            return redirect(url_for(
                'welcome',
                fn=users[un]['fn'],
                ln=users[un]['ln']
            ))

        else:
            flash("Invalid USERNAME or PASSWORD")
            return redirect(url_for('login'))

    return render_template('login.html')

#welcome

@app.route('/welcome',methods = ['GET','POST'])
def welcome():

    fn=request.args.get('fn')
    ln=request.args.get('ln')

    return render_template('welcome.html',fn=fn,ln=ln)


if __name__ == "__main__":
    app.run(debug=True)