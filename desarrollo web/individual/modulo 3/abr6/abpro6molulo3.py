"""Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario.
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir
en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’."""



import time 



def listado():
    while True:
        print("\nPor favor escriba su nombre: ")
        nombre = input('ingresar un nombre:')
        print("\nPor favor escriba su contraseña: ")
        contraseña = input('ingrese la contreseña')
        break

listado()        