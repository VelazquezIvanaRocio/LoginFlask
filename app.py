from flask import Flask 
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL , MySQLdb

app= Flask(__name__, template_folder="template")

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='login'
app.config['MYSQL_CURSOR']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/admin')
def admin(): 
    return render_template ('admin.html')

#FUNCION DE LOGIN
@app.route("/acceso-login", methods =["POST", "GET"])
def login():
   
    if request.method== 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form: 
        _correo= request.form ['txtCorreo']
        _password=request.form['txtPassword'] 
        
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s', (_correo, _password,))
        account = cur.fetchone() 
        print(account)
           
        if account :
            session['logueado']=True
            session['id']=account['id']
            print(account)
            return render_template("admin.html")
            print(account)
        else:
            return render_template('index.html', mensaje='usuario incorrecto')
    return render_template ('index.html')

if __name__== '__main__': 
    app.secret_key="rociov"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
    