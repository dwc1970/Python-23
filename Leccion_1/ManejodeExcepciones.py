# 1.2 Procesamiento de excepciones
# 1.3 Procesar clases de exception más específicas
# 1.4 Más de procedimientos de excepciones
# 1.5 Bloques else y finally al manejar excepciones
# 1.6 Creación de clases de Exception personalizadas

resultado = None
a = '10'
b = 0
try:
    resultado = a / b # modificamos
except ZeroDivisionError as e:
    print(f'ocurrio un error: {e}')

print(f'El resultado es: {resultado}')
print('seguimos...')

##################################################
resultado = None
a = 7
b = 5
try:
    resultado = a / b # modificamos
except TypeError as e:
    print(f' typeError - ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {Type(e)}')
except Exception as e:
    print(f' Exception - Ocurrio un error: {e}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# 1.5 Bloques else y finally al manejar excepciones

resultado = None

try:
    a = print(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    resultado = a / b # modificamos
except TypeError as e:
    print(f' typeError - ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {Type(e)}')
except Exception as e:
    print(f' Exception - Ocurrio un error: {Type(e)}')
else:
    print("No se arrojo ninguna excepcion")
finally: #Siempre se va a ejecutar
    print("Ejecucion de este bloque finallyu")

print(f'El resultado es: {resultado}')
print('seguimos...')