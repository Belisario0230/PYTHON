#Ejercicio N° 1
s1 = ("Había una vez, " )
s2 = ("un barquito chiquitito ") 
s3 = ("que no podía, ") 
s4 = ("que no podía navegar.")

print((s1+s2)*2+(s3*2+s4))
print()

#Ejercicio N° 2
s5 = "Érase un hombre a una nariz pegado," "\n"
s6 = "Érase una nariz superlativa," "\n"
s7 = "Érase una alquitara medio viva," "\n"
s8 = "Érase un peje espada mal barbado" "\n"

print(s5 + s6 +s7 +s8)
print()

#Ejercicio N° 3
s = ("me encantan las matematicas")
resultado = s.upper()
print(resultado)
print()

#Ejercicio N° 4
s = "Mi pasión por el chocolate es superior a mis fuerzas"
s = len(s)
print(s)
print()

#Ejercicio 5
s = "Mi pasión por el chocolate es superior a mis fuerzas"

inicio=s.find("chocolate")
final=inicio+len("chocolate")
s_sub=s[inicio:(final+1)]
print(s_sub)

inicio1 = s.find("superior")
final1 = inicio1+len("superior")
s_sub1 = s[inicio1:(final1+1)]
print(s_sub1)

inicio2 = s.find("fuerzas")
final2=inicio2+len("fuerzas")
s_sub2 = s[inicio2:(final2+1)]
print(s_sub2)

#Ejercicio 6
nombre = input("Dijite su Nombre ")
print(nombre)

#Ejerciico 7 
nombre = input("Dijite su Nombre ")
apellidos = input("Dijite sus apellidos ")
print("Hola mi nombre es + {} + y mis apellidos son {}".format(nombre,apellidos))
print()

#Ejercicio 8
nombre = input("Dijite su nombre ")
apellidos = input("Dijite sus apellidos ")
edad = input("Dijite su edad ")
print("Mi nombre es {} y mis apelldios son {} y mi edad es {}".format(nombre,apellidos,edad))


#Ejercicio 9 y 10
nombre = input("Dijite su nombre ")
apellidos = input("Dijite sus apellidos ")
edad = input("Dijite su edad ")
ciudad = input("Dijite la ciudad donde vive ")
print("Mi nombre es {} y mis apelldios son {} y mi edad es {} y la ciudad donde vivo actualmente es {}".format(nombre,apellidos,edad,ciudad))


