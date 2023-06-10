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
      #sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # Placeholder
      sentencia ='SELECT * FROM persona WHERE id_persona = %$'  # Placeholder
      #entrada = input('Digite los id_persona a buscar (separadoos por coma ): ')
      id_persona = input('Digite un numero para el id-persona: ')
      llaves_primarias = (tuple(entrada.split( ' ,')), )
     # id_persona = input('Digite un número para el id_persona: ')
      cursor.execute (sentencia, llaves_primarias)#(sentencia, (id_persona,)) # De esta manera ejecutamos la sentencia
      registros = cursor.fetchone() #Recuperamos todos los registros que seran una lista.
      #for registro in registros:
      print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# https//www.psycopg.org/docs/usage.html  para buscar documentacion
