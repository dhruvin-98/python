from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymysql import MySQLError
from database import get_connection

app = Flask(__name__)

app.secret_key = 'dhruivn'


#home

@app.route('/')
def home():
    return render_template('login.html')

#register

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        fn=request.form.get('fn')
        ln=request.form.get('ln')
        un=request.form.get('un')
        pw=request.form.get('pw')


        #empty field
        if not fn or not ln or not un or not pw:
            return render_template(
                'register.html',error="All fields are required!"
            )

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO loginmaster
                (fn,ln,loginUsername,loginPassword)
                VALUES
                (%s,%s,%s,%s)
                """,
                (fn,ln,un,pw)
            )
            connection.commit()
        except MySQLError:
            connection.rollback()
            return render_template(
                'register.html',
                error="Registration failed. Please try another username."
            )
        finally:
            cursor.close()
            connection.close()

        return redirect('/')
    return render_template('register.html')


#login

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    un = request.form.get('un')
    pw = request.form.get('pw')

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT fn,ln,loginpassword
        FROM loginmaster
        WHERE loginUsername = %s AND loginPassword = %s
        """,
        (un,pw)
    )

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user is None:
        flash('Invalid username or password.')
        return redirect(url_for('login'))

    session['username'] = un
    session['first_name'] = user[0]
    session['last_name'] = user[1]


    return redirect(url_for('welcome'))

#for welcome
@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template(
        'welcome.html',
        fn=session['first_name'],
        ln=session['last_name']
    )

#for logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(debug=True)
            


