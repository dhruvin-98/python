from flask import *
from database import get_connection

app = Flask(__name__)

app.secret_key="dhruivn"


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
        cursor.close()

        return redirect('/')
    return render_template('register.html')


#login

@app.route('/login',methods=['POST'])
def login():

    un = request.form.get('un')
    pwd = request.form.get('pwd')

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT fn,ln,loginpassword
        FROM loginmaster
        WHERE loginusername = %s
        """,
        (un,)
    )

    user = cursor.fetchone();
    cursor.close();
    connection.close();


    return render_template(
        'welcome.html',
        fn=user[0],
        ln=user[1]
        )



if __name__ == "__main__":
    app.run(debug=True)
            


