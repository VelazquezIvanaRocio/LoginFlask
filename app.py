from flask import Flask, request, render_template, session
from flask_mysqldb import MySQL
from flask_bcrypt import generate_password_hash
import os 

from flask import Flask, request, render_template, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder="template")
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

# Inicializar la extensión MySQL
mysql = MySQL(app)

# Inicializar la extensión Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    # Hash de la contraseña "sixitse2023"
    hashed_password = bcrypt.generate_password_hash("sixitse2023").decode('utf-8')
    return "Contraseña hash para 'sixitse2023': " + hashed_password

@app.route('/admin')
def admin(): 
    return render_template('admin.html')

# Función de inicio de sesión
@app.route("/acceso-login", methods=["POST", "GET"])
def login():
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form: 
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword'] 
        
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s', (_correo,))
        account = cur.fetchone()
        cur.close()
           
        if account and bcrypt.check_password_hash(account['password'], _password):
            session['logueado'] = True
            session['id'] = account['id']
            return render_template('admin.html')
        else:
            return render_template('index.html', mensaje='Usuario incorrecto')
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = "rociov"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
