
#jercicio 10
#Pide al usuario un número complejo. Para dicho número, crea una tupla donde la primera entrada sea dicho 
# número complejo, la segunda, su opuesto y, la tercera, su conjugado.

real_part = float(input("Introduce la parte real de un número complejo: "))
imag_part = float(input("Introduce la parte imaginaria de un número complejo: "))
z = complex(real_part, imag_part)

print((z, -z, z.conjugate()))