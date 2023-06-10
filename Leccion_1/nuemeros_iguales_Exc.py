from numerosIguales_Exc import numerosIguales_Exc

resultado = None

try:
    a = print(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise numerosIguales_Exc('Son numeros iguales')
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