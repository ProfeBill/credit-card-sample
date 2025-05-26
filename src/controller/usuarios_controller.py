
import sys
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2

from model.Usuario import Usuario
import SecretConfig

class ControladorUsuarios :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        with open( "sql/crear-usuarios.sql", "r"  ) as archivo:
            consulta = archivo.read()

        cursor.execute( consulta )
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""drop table if exists usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarUsuario( usuario : Usuario ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        cursor = ControladorUsuarios.ObtenerCursor()
        try:
            cursor.execute( f"""insert into usuarios (cedula, nombre, apellido, 
                                direccion, correo, telefono, 
                                codigo_municipio, codigo_departamento) 
                            values ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}',  
                                '{usuario.direccion}', '{usuario.correo}', '{usuario.telefono}',
                                '{usuario.codigo_municipio}', '{usuario.codigo_departamento}')""" )

            cursor.connection.commit()
            
        except psycopg2.IntegrityError as e:
            cursor.connection.rollback()
            raise Exception("La cédula ya existe") from e

    def BuscarUsuario( cedula ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""select cedula, nombre, apellido, direccion, correo, telefono, codigo_departamento, codigo_municipio
        from usuarios where cedula = '{cedula}'""" )
        fila = cursor.fetchone()
        resultado = Usuario(cedula=fila[0], nombre=fila[1], apellido=fila[2], direccion=fila[3], correo=fila[4],
                            telefono=fila[5],codigo_departamento=fila[6], codigo_municipio=fila[7]   )
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
