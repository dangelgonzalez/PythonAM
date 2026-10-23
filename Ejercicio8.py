nombre = input("¿Cual es tu nombre?")
edad = int(input("¿Cual es tu edad?"))

print("Hola", nombre, "tienes que ingresar 3 notas")
nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
nota3 = float(input("Nota 3:"))
suma = nota1 + nota2 + nota3
division = suma / 3
print("Hola", nombre, "tienes", edad, "años y tu promedio es:", division)
