from flask_login import UserMixin
import bcrypt

class Usuario(UserMixin):
    
    def __init__(self,id=None,usuario=None,password=None):
        self.id=id,
        self.usuario=usuario,
        self.password=password
        
        
    @classmethod
    def revisar_contraseña_hasheada(self, hash, password):
        try:
            #  print("Hash almacenado:", hash)
            #  print("Contraseña proporcionada:", password)
            #  print("estoy en revisar contraseña ")
            return bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8"))
        except Exception as ex:
            print("Error:", ex)
            return False

    @classmethod
    def generar_contraseña_hasheada(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    
    @classmethod
    def obtenerUsuario_por_usuario( cls,db, username):
        try:
            cur = db.connection.cursor()
            consulta = "SELECT idusuario, usuario, password, tipo FROM usuario WHERE usuario = %s"
            cur.execute(consulta, [username])
            user = cur.fetchone()
            if user:
                user = Usuario(user[0],user[1],user[2])
                return user
            else:
                return None
        except Exception as ex:
            return user
        
        
        
    @classmethod
    def obtenerUsuario_por_id( cls,db, id):
        try:
            cur = db.connection.cursor()
            consulta = "SELECT * FROM usuario WHERE id = %s"
            cur.execute(consulta, [id])
            user = cur.fetchone()
            print(user, "en obtenerporuid")
            if user:
                user = Usuario(user[0],user[1],user[2])
            else:
                return None
        except Exception as ex:
            return None
        
#print(Usuario.generar_contraseña_hasheada('sixitse2023'))