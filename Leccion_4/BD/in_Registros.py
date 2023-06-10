import psycopg2 # Es para poder conectarnos a Postredsql

conexion = psycopg2.connect(
    user = 'postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_basedatos',
)  # El codigo se puede poner en una sola linea, pero yo lo dejo asi.

try:
    with conexion:

    with conexion.cursor() as cursor:
      sentencia ='INSER INTO perosna(nombre, apellido, email) VALUES(%s,  %s, %s)'  # Pasamos parametros %
      entrada = input('Digite los id-persona a buscar (separados por comas): ')
      valores = ('Carlos', 'Lara', ' clara@mail.com ') # Esto es una tupla
      cursor.execute (sentencia, valores)#(sentencia, (id_persona,)) # De esta manera ejecutamos la sentencia
      #cursor,commit() Se utiliza para guardar los cambios en la base de datos
      #registros = cursor.fetchall() #Recuperamos todos los registros que seran una lista.
      registros_insertados = cursor.rowcount
      print(f' los registros insertados son : {registros_insertados}') # estamos insertado la tupla con la informacion de la sentencia
      #for registro in registros:
      print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# https//www.psycopg.org/docs/usage.html  para buscar documentacion

SEGUIR CON EL VIDEO 6 DE LA  CALSE 5