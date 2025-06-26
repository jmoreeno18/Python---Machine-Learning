# Variables Suma
numero1 = 5
numero2 = 7
suma = numero1 + numero2

# Variables String
var1 = 'Hola'
var2 = 'Mundo'
var = var1 + ' ' + var2

# Concatenar con format
profesion = 'Hola soy {} y mi profesión es {}'
profesion2 = profesion.format('Javier', 'Desarrolladoe de aplicaciones web')
print(profesion2)

# Upper, lower y cappitalize
texto = 'es un texto de prueba en minusculas'
textoMayusculas = texto.upper()
print(textoMayusculas)

# split → Separa una frase como si fuera una lista
# replace → Cambia una palabra de una frase por otra palabra

lista = 'Hola Javier'
lista2 = lista.split(' ')
print(lista2)
lista3 = lista.replace('Javier', 'Carlos')
print(lista3)

# Boolean
bol = True
not bol # Pasa a falso

# Estructuras (listas, tuplas y diccionarios)

# Listas
nombres = ['Javier', 'Carlos', 'Paco']
print(len(nombres))
nombres.sort()
print(nombres)
nombres.sort(reverse=True)
print(nombres)
nombres.reverse()
print(nombres)

# Tuplas → No se pueden alterar
nombres2 = ('limon', 'aguacate', 'pera', 'manzana')

# Diccionarios
nombres3 = {'agua': 3, 'aceite': 2, 'harina': 6, 'azucar': 5}
nombres3.keys()
print(list(nombres3.keys()))

# If else
edad_persona = 20
mayoria_edad = 18

if(edad_persona > mayoria_edad):
    print('Eres mayor de edad')
elif(edad_persona == mayoria_edad):
    print('Tienes 18 años')
else:
    print('No eres mayor de edad')
    
# While
edad_persona2 = 10
while(edad_persona2 < mayoria_edad):
    print(edad_persona2)
    edad_persona2+=1
    
# FOR
numeros5 = [i**2 for i in range(1,11)]
print(numeros5)

# Funciones
import math as mt
def pitagoras(a, b):
    """
    Dado los catetos de un triangulo, devuelve el valor de la hipotenusa
    """
    c = mt.sqrt(a**2 + b**2)
    return c

# Programacion Orientada a Objetos
class humano(): 
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def presentar(self):
        return f'Hola soy {self.nombre}'
persona = humano('Javier', 24, '11111111Y')
print(persona.presentar())