# from flask import Flask, request, render_template, session
# from flask_mysqldb import MySQL
# from flask_bcrypt import generate_password_hash
# import os 

# from flask import Flask, request, render_template, session
# from flask_mysqldb import MySQL
# from flask_bcrypt import Bcrypt

# app = Flask(__name__, template_folder="template")
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'login'

# # Inicializar la extensión MySQL
# mysql = MySQL(app)

# # Inicializar la extensión Bcrypt
# bcrypt = Bcrypt(app)

# @app.route("/")
# def index():
#     # Hash de la contraseña "sixitse2023"
#     hashed_password = bcrypt.generate_password_hash("sixitse2023").decode('utf-8')
#     return "Contraseña hash para 'sixitse2023': " + hashed_password

# @app.route('/admin')
# def admin(): 
#     return render_template('admin.html')

# # Función de inicio de sesión
# @app.route("/acceso-login", methods=["POST", "GET"])
# def login():
#     if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form: 
#         _correo = request.form['txtCorreo']
#         _password = request.form['txtPassword'] 
        
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM usuarios WHERE correo = %s', (_correo,))
#         account = cur.fetchone()
#         cur.close()
           
#         if account and bcrypt.check_password_hash(account['password'], _password):
#             session['logueado'] = True
#             session['id'] = account['id']
#             return render_template('admin.html')
#         else:
#             return render_template('index.html', mensaje='Usuario incorrecto')
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.secret_key = "rociov"
#     app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
from flask import Flask, request,render_template, config, redirect, session, url_for
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['SECRET_KEY']=config.HEX_SEC_KEY
app.config['MYSQL_HOST']=config.MYSQL_HOST
app.config['SECRET_USER']=config.MYSQL_USER
app.config['SECRET_PASSWORD']=config.MYSQL_PWD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql=MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email=request.form['email']
    password=request.form['password']
    
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE email=%s AND password=%s', (email,password))
    user=cur.fetchone()
    cur.close()
    
    if user is not None:
        session['email']=email
        session['name']=user[1]
        session['surnames']= user[2]
        
        return redirect(url_for('task'))
    else:
        return render_template('index.html', message="Las credenciales no son correctos")
    
@app.route('/task', methods=['GET'])
def task():
    return render_template('task.html')
    
if __name__=='__main__':
    app.run(debug= True)