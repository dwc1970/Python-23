import psycopg2 # Es para poder conectarnos a Postredsql

conexion = psycopg2.connect(
    user = 'postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_basedatos',
)

try:
   # with conexion:

    with conexion.cursor() as cursor:
      sentencia = 'SELECT * FROM persona WHERE id_persona IN %$' # Placeholder
      entrada = input('Digite los id_persona a buscar  (separados por coma): ')
      llaves_primarias = (tuple(entrada.split(', ')), ) # con una coma es una tupla de tuplas
      cursor.execute(sentencia, llaves_primarias)
      #id_persona = input('Digite un número para el id_persona: ')
      #cursor.execute(sentencia, (id_persona,)) # De esta manera ejecutamos la sentencia
      registros = cursor.fetchall() #Recuperamos todos los registros que seran una lista.
      for  registro in registros:
          print(registro)
      print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# https//www.psycopg.org/docs/usage.html
