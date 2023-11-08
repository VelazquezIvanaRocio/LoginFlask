from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'tu_usuario'
app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
app.config['MYSQL_DB'] = 'login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']

        # Hash de la contraseña antes de guardarla en la base de datos
        hashed_password = bcrypt.generate_password_hash(_password).decode('utf-8')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (correo, password) VALUES (%s, %s)", (_correo, hashed_password))
        mysql.connection.commit()
        cur.close()

        return "Usuario registrado exitosamente"

if __name__ == '__main__':
    app.run(debug=True)
