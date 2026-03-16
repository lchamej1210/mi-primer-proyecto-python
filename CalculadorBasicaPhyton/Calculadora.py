# Calculadora Básica
# Hecha por Luis Chaparro Mejías, alumno de 2ºSMR
# Proyecto empezado el 16 de Marzo de 2026 y acabado el 16 de Marzo de 2026

print("Bienvenid@ a mi calculadora basica")
print("Aqui vas a tener que empezar poniendo un numero, luego otro numero y luego su operacion logica")

numero1 = float(input("Ingrese un numero 1: ")) 
numero2 = float(input("Ingrese un numero 2: "))
operacion = input("Ingrese la operacion logica (suma, resta, multiplicacion, division): ")
total = 0

if operacion == "suma":
    total = numero1 + numero2
elif operacion == "resta": 
    total = numero1 - numero2
elif operacion == "multiplicacion":
    total = numero1 * numero2
elif operacion == "division": 
    total = numero1 / numero2
else:
    print("Ingrese la operacion logica adecuada (suma, resta, multiplicacion, division)")

print(f"El resultado de {numero1} {operacion} {numero2} es {total}")   