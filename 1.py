#Elaborar un programa en python que capture la siguiente informacion codigo,nombre,apellidos,contacto,correo,edad
#Solo se registra los estudiantes que cumplan los siguientes criterios 
#Sexo masculino.EDAD:15-25,estracto socio economico 1 y 2 
#Sexo femenino 20-35 estracto 1 y 4 en caso que no aplique guardar su contacto en una lista guardar el contacto en una lista llamda pendiente 

import os

class Estudiante:
    def __init__(self, codigo, nombre, apellidos, contacto, correo, edad, sexo, estrato):
        self.codigo = codigo
        self.nombre = nombre
        self.apellidos = apellidos
        self.contacto = contacto
        self.correo = correo
        self.edad = edad
        self.sexo = sexo
        self.estrato = estrato

def capturar_estudiante():
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellidos = input("Ingrese los apellidos del estudiante: ")
    contacto = input("Ingrese el número de contacto del estudiante: ")
    correo = input("Ingrese el correo electrónico del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    sexo = input("Ingrese el sexo del estudiante (M/F): ").upper()
    estrato = int(input("Ingrese el estrato socioeconómico del estudiante: "))
    return Estudiante(codigo, nombre, apellidos, contacto, correo, edad, sexo, estrato)

estudiantes_registrados = []
estudiantes_pendientes = []

while True:
    nuevo_estudiante = capturar_estudiante()
    
    if nuevo_estudiante.sexo == 'M' and 15 <= nuevo_estudiante.edad <= 25 and nuevo_estudiante.estrato in [1, 2]:
        estudiantes_registrados.append(nuevo_estudiante)
        print("Estudiante registrado exitosamente.")
    elif nuevo_estudiante.sexo == 'F' and 20 <= nuevo_estudiante.edad <= 35 and nuevo_estudiante.estrato in [1, 4]:
        estudiantes_registrados.append(nuevo_estudiante)
        print("Estudiante registrado exitosamente.")
    else:
        estudiantes_pendientes.append(nuevo_estudiante.contacto)
        print("Estudiante no cumple con los criterios y ha sido puesto en la lista de pendientes.")
    
    continuar = input("¿Desea registrar otro estudiante? (s/n): ").lower()
    if continuar != 's':
        break

print("\nEstudiantes registrados:")
for estudiante in estudiantes_registrados:
    print(f"Código: {estudiante.codigo}, Nombre: {estudiante.nombre} {estudiante.apellidos}, Contacto: {estudiante.contacto}, Correo: {estudiante.correo}, Edad: {estudiante.edad}, Sexo: {estudiante.sexo}, Estrato: {estudiante.estrato}")

print("\nEstudiantes pendientes:")
for contacto in estudiantes_pendientes:
    print(contacto)
