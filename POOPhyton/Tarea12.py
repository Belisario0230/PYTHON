#Ejercicio 1
# A lo largo de toda esta taraea vas a construir la clase Date. 
# Empieza con el constructor, que recibe por parámetros el día (day),
#  mes (month) y año (year). Los 3 parámetros son de tipo int y por defecto 
# todos valen 1.

class Date():
    def __init__(self, day = 1, month = 1, year = 1):
        self.day = day
        self.month = month
        self.year = year

#Ejercicio 2
#Configura el método .__str__() para que muestre la fecha en formato day 
# / month / year. Si el valor del día o el mes son menores a 10, mostrar
#  el valor con un 0 delante. Por ejemplo, si day = 8, month = 7 y year = 1998, 
# entonces se debería mostrar 08 / 07 / 1998.
#En el caso del año, si el año es menor a 1000, mostrar con un cero 
# delante; si es menor a 100, mostrar con 2 ceros delante; y si es menor 
# a 10, mostrar con 3 ceros delante.

#PISTA: Puedes crear una función que dado un número entero y el número de
#  cifras que debe tener, rellene con ceros a la izquierda hasta completar 
# el número de cifras indicado.

def agregar_ceros_izquierda(numero, cifras_totales=2):
    """
    Agrega ceros a la izquierda hasta completar la cantidad de cifras especificada.
    Args:
        numero: Número entero positivo
        cifras_totales: Número entero positivo (total de cifras que debe tener el número)
    Returns:
        Cadena con las cifras completadas
    """
    for i in range(cifras_totales - 1, 0, -1):
        if numero < 10 ** (cifras_totales - i):
            return "0" * i + str(numero)
    else:
        return str(numero)


class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return "{} / {} / {}".format(
            agregar_ceros_izquierda(self.dia),
            agregar_ceros_izquierda(self.mes),
            agregar_ceros_izquierda(self.año, 4),
        )


# Ejemplo de uso
fecha_ejemplo = Fecha(5, 9, 1978)
print(fecha_ejemplo)

#Ejercicio 3
#Implementa el método de instancia .isLeap() que diga si el año es bisiesto o no.

def agregar_ceros_izquierda(numero, cifras_totales=2):
    """
    Añade ceros adicionales a la izquierda hasta completar la cantidad de cifras especificada.
    Args:
        numero: Número entero positivo
        cifras_totales: Número entero positivo (total de cifras que debe tener el número)
    Returns:
        Cadena con las cifras completadas
    """
    for i in range(cifras_totales - 1, 0, -1):
        if numero < 10 ** (cifras_totales - i):
            return "0" * i + str(numero)
    else:
        return str(numero)


class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return "{} / {} / {}".format(
            agregar_ceros_izquierda(self.dia),
            agregar_ceros_izquierda(self.mes),
            agregar_ceros_izquierda(self.año, 4),
        )

    def es_bisiesto(self):
        if self.año % 4 == 0:
            if self.año % 100 == 0:
                if self.año % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


# Ejemplo de uso
fecha_ejemplo = Fecha(5, 2, 2024)
print(fecha_ejemplo)
print(fecha_ejemplo.es_bisiesto())

#Ejercicio 4
#• Implementa un método de instancia .totalMonthDays() que diga el número de 
# días del mes. Ten en cuenta que en los años bisiestos, Febrero tiene 29 días. 
# • Implementa el método de instancia .validDate() que determine si una fecha es
#  válida. Modifica el constructor para que si la fecha introducida no es válida, 
# devuelva un mensaje indicando “¡¡¡La fecha introducida no es una fecha 
# válida!!!”.
# Definir la clase Fecha
class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año

        if not self.fecha_valida():
            print("¡¡¡La fecha introducida no es válida!!!")

    def __str__(self):
        return "{}/{}/{}".format(
            agregar_ceros_izquierda(self.dia),
            agregar_ceros_izquierda(self.mes),
            agregar_ceros_izquierda(self.año, 4),
        )

    def es_bisiesto(self):
        if self.año % 4 == 0:
            if self.año % 100 == 0:
                if self.año % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def total_dias_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            if self.es_bisiesto():
                return 29
            else:
                return 28

    def fecha_valida(self):
        if self.año < 0:
            return False
        if self.mes <= 0 or self.mes > 12:
            return False
        if self.dia <= 0 or self.dia > self.total_dias_mes():
            return False
        return True


# Ejemplo de uso
fecha_ejemplo = Fecha(dia=29, mes=2, año=2024)
print(fecha_ejemplo)  # Salida: "29/02/2024"
print(fecha_ejemplo.total_dias_mes())  # Salida: 29 (porque 2024 es bisiesto)
print(fecha_ejemplo.fecha_valida())  # Salida: True

fecha_invalida = Fecha(dia=31, mes=4, año=2022)  # Fecha inválida
# Salida: "¡¡¡La fecha introducida no es válida!!!"

#Ejercicio 5
#Implementa la propiedad .monthName que devuelva el nombre del mes en inglés. 
# Por ejemplo, si nuestra fecha es day = 8, month = 7 y year = 1998, la propiedad
#  debe devolver July.
# Definir la clase Fecha
class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año

        if not self.fecha_valida():
            print("¡¡¡La fecha introducida no es válida!!!")

    def __str__(self):
        return "{}/{}/{}".format(
            agregar_ceros_izquierda(self.dia),
            agregar_ceros_izquierda(self.mes),
            agregar_ceros_izquierda(self.año, 4),
        )

    def es_bisiesto(self):
        if self.año % 4 == 0:
            if self.año % 100 == 0:
                if self.año % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def total_dias_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            if self.es_bisiesto():
                return 29
            else:
                return 28

    def fecha_valida(self):
        if self.año < 0:
            return False
        if self.mes <= 0 or self.mes > 12:
            return False
        if self.dia <= 0 or self.dia > self.total_dias_mes():
            return False
        return True

    @property
    def nombre_mes(self):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return meses[self.mes - 1]


# Crear una instancia de Fecha para el mes actual
mes_actual = Fecha(mes=7, año=2024)
print(f"El mes actual es {mes_actual.nombre_mes.capitalize()} de {mes_actual.año}.")


#Ejercicio 6
#• Implementa el método estático .areEqual(), que dadas dos fechas diga si son 
# iguales. • Implementa el método estático .isLater(), que dadas dos fechas diga 
# si la primera es posterior a la segunda. • Implementa el método estático 
# .isPrevious(), que dadas dos fechas diga si la primera es anterior a la segunda.
class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año

        if not self.fecha_valida():
            print("¡¡¡La fecha introducida no es válida!!!")

    def __str__(self):
        return "{}/{}/{}".format(
            agregar_ceros_izquierda(self.dia),
            agregar_ceros_izquierda(self.mes),
            agregar_ceros_izquierda(self.año, 4),
        )

    def es_bisiesto(self):
        if self.año % 4 == 0:
            if self.año % 100 == 0:
                if self.año % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def total_dias_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            if self.es_bisiesto():
                return 29
            else:
                return 28

    def fecha_valida(self):
        if self.año < 0:
            return False
        if self.mes <= 0 or self.mes > 12:
            return False
        if self.dia <= 0 or self.dia > self.total_dias_mes():
            return False
        return True

    @property
    def nombre_mes(self):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return meses[self.mes - 1]

    @staticmethod
    def areEqual(d1, d2):
        return d1.año == d2.año and d1.mes == d2.mes and d1.dia == d2.dia

    @staticmethod
    def isLater(d1, d2):
        if d1.año > d2.año:
            return True
        elif d1.año == d2.año:
            if d1.mes > d2.mes:
                return True
            elif d1.mes == d2.mes:
                return d1.dia > d2.dia
        return False

    @staticmethod
    def isPrevious(d1, d2):
        return not Fecha.isLater(d1, d2) and not Fecha.areEqual(d1, d2)


# Ejemplo de uso
fecha1 = Fecha(dia=15, mes=7, año=2024)
fecha2 = Fecha(dia=20, mes=7, año=2024)

print(f"¿Son iguales las fechas? {Fecha.areEqual(fecha1, fecha2)}")
print(f"¿La primera fecha es posterior a la segunda? {Fecha.isLater(fecha1, fecha2)}")
print(f"¿La primera fecha es anterior a la segunda? {Fecha.isPrevious(fecha1, fecha2)}")

#Ejercicio 7
#• Implementa el método de clase .firstDayOfTheYear() que dado un año cree 
#  objeto Date con la fecha correspondiente al primer día del año indicado. •
#  Implementa el método de clase .lastDayOfTheYear() que dado un año cree un
#  objeto Date con la fecha correspondiente al último día del año indicado. •
#  Implementa el método de instancia .plusDay() que incremente un día la fecha. 
# Ten en cuenta que si estamos en el último día del mes y añadimos un día, 
# tendremos que cambiar de mes (pasar al siguiente). Y lo mismo si estamos en el
#  último día del año (tendremos que pasar al siguiente año). • Implementa el
#  método de instancia .minusDay() que decremente un día la fecha. Ten en cuenta 
# que si estamos en el primer día del mes y restamos un día, tendremos que 
# cambiar de mes (pasar al anterior). Y lo mismo si estamos en el primer día 
# del año (tendremos que pasar al año anterior).
class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año

        if not self.fecha_valida():
            print("¡¡¡La fecha introducida no es válida!!!")

    def __str__(self):
        return "{}/{}/{}".format(
            agregar_ceros_izquierda(self.dia),
            agregar_ceros_izquierda(self.mes),
            agregar_ceros_izquierda(self.año, 4),
        )

    def es_bisiesto(self):
        if self.año % 4 == 0:
            if self.año % 100 == 0:
                if self.año % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def total_dias_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            if self.es_bisiesto():
                return 29
            else:
                return 28

    def fecha_valida(self):
        if self.año < 0:
            return False
        if self.mes <= 0 or self.mes > 12:
            return False
        if self.dia <= 0 or self.dia > self.total_dias_mes():
            return False
        return True

    @property
    def nombre_mes(self):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return meses[self.mes - 1]

    @classmethod
    def firstDayOfTheYear(cls, año):
        return cls(dia=1, mes=1, año=año)

    @classmethod
    def lastDayOfTheYear(cls, año):
        return cls(dia=31, mes=12, año=año)

    def plusDay(self):
        if self.dia < self.total_dias_mes():
            self.dia += 1
        else:
            self.dia = 1
            if self.mes < 12:
                self.mes += 1
            else:
                self.mes = 1
                self.año += 1

    def minusDay(self):
        if self.dia > 1:
            self.dia -= 1
        else:
            if self.mes > 1:
                self.mes -= 1
                self.dia = self.total_dias_mes()
            else:
                self.mes = 12
                self.dia = 31
                self.año -= 1
                
# Crear una instancia de Fecha
mi_fecha = Fecha(7, 7, 2024)

# Ejemplo de uso de los métodos
print("Nombre del mes:", mi_fecha.nombre_mes)
print("Primer día del año:", Fecha.firstDayOfTheYear(2024))
print("Último día del año:", Fecha.lastDayOfTheYear(2024))

# Avanzar un día y mostrar la fecha actualizada
mi_fecha.plusDay()
print("Fecha después de avanzar un día:", mi_fecha)

# Retroceder un día y mostrar la fecha actualizada
mi_fecha.minusDay()
print("Fecha después de retroceder un día:", mi_fecha)

#Ejercicio 8
#• Implementa el método de clase .copy() que dado un objeto Date, devuelva otro 
# objeto Date con los mismos atributos. • Implementea el método estático 
# .difference() que dadas dos fechas devuelva el número de días que hay entre 
# ellas.

def addLeftZero(n, m=2):
    """Añade ceros adicionales a la izquierda hasta completar las m cifras.
    
    Args:
        n: Número entero positivo.
        m: Número entero positivo (cifras totales que debe tener n).
    
    Returns:
        String con m cifras.
    """
    for i in range(m - 1, 0, -1):
        if n < 10**(m - i):
            return "0" * i + str(n)
    return str(n)


class Date:
    def __init__(self, d=1, m=1, y=1):
        self.day = d
        self.month = m
        self.year = y
        if not self.validDate():
            print("¡¡¡La fecha introducida no es una fecha válida!!!")

    def __str__(self):
        return "{} / {} / {}".format(
            addLeftZero(self.day),
            addLeftZero(self.month),
            addLeftZero(self.year, 4)
        )

    def isLeap(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def totalMonthDays(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if self.month in [4, 6, 9, 11]:
            return 30
        if self.month == 2:
            if self.isLeap():
                return 29
            else:
                return 28

    def validDate(self):
        if self.year < 0:
            return False
        if self.month <= 0 or self.month > 12:
            return False
        if self.day <= 0 or self.day > self.totalMonthDays():
            return False
        return True

    @property
    def monthName(self):
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[self.month - 1]

    @staticmethod
    def areEqual(d1, d2):
        if d1.year == d2.year and d1.month == d2.month and d1.day == d2.day:
            return True
        return False

    @staticmethod
    def isLater(d1, d2):
        if d1.year > d2.year:
            return True
        elif d1.year == d2.year:
            if d1.month > d2.month:
                return True
            elif d1.month == d2.month:
                if d1.day > d2.day:
                    return True
        return False

    @staticmethod
    def isPrevious(d1, d2):
        if not Date.isLater(d1, d2) and not Date.areEqual(d1, d2):
            return True
        return False

    @classmethod
    def firstDayOfTheYear(cls, year):
        if year > 0:
            return cls(1, 1, year)
        print("El año introducido no es válido")

    @classmethod
    def lastDayOfTheYear(cls, year):
        if year > 0:
            return cls(31, 12, year)
        print("El año introducido no es válido")

    def plusDay(self):
        if Date.areEqual(self, Date.lastDayOfTheYear(self.year)):
            self.day = 1
            self.month = 1
            self.year += 1
        elif self.day == self.totalMonthDays():
            self.day = 1
            self.month += 1
        else:
            self.day += 1

    def minusDay(self):
        if Date.areEqual(self, Date.firstDayOfTheYear(self.year)):
            self.day = 31
            self.month = 12
            self.year -= 1
        elif self.day == 1:
            self.month -= 1
            self.day = self.totalMonthDays()
        else:
            self.day -= 1

    @classmethod
    def copy(cls, d):
        """Dado un objeto Date, devuelve otro objeto Date con los mismos atributos."""
        return cls(d.day, d.month, d.year)

    @staticmethod
    def difference(d1, d2):
        """Dadas dos fechas, devuelve el número de días que hay entre ellas."""
        if Date.areEqual(d1, d2):
            return 0
        elif Date.isLater(d1, d2):
            count = 0
            d2_copy = Date.copy(d2)
            while not Date.areEqual(d1, d2_copy):
                count += 1
                d2_copy.plusDay()
            return count
        else:
            count = 0
            d2_copy = Date.copy(d2)
            while not Date.areEqual(d1, d2_copy):
                count += 1
                d2_copy.minusDay()
            return count

# Pruebas
if __name__ == "__main__":
    date1 = Date(1, 1, 2023)
    date2 = Date(1, 1, 2024)
    date3 = Date(15, 8, 2023)

    # Prueba de copy
    copied_date = Date.copy(date1)
    print(f"Original date: {date1}")
    print(f"Copied date: {copied_date}")

    # Prueba de difference
    days_between = Date.difference(date1, date2)
    print(f"Días entre {date1} y {date2}: {days_between} días")

    days_between = Date.difference(date3, date1)
    print(f"Días entre {date3} y {date1}: {days_between} días")


#Ejercicio 9
#Implementa el método de clase .randomDate() que cree una fecha aleatoria 
# válida.
import random

def addLeftZero(n, m=2):
    """Añade ceros adicionales a la izquierda hasta completar las m cifras.
    
    Args:
        n: Número entero positivo.
        m: Número entero positivo (cifras totales que debe tener n).
    
    Returns:
        String con m cifras.
    """
    for i in range(m - 1, 0, -1):
        if n < 10**(m - i):
            return "0" * i + str(n)
    return str(n)


class Date:
    def __init__(self, d=1, m=1, y=1):
        self.day = d
        self.month = m
        self.year = y
        if not self.validDate():
            print("¡¡¡La fecha introducida no es una fecha válida!!!")

    def __str__(self):
        return "{} / {} / {}".format(
            addLeftZero(self.day),
            addLeftZero(self.month),
            addLeftZero(self.year, 4)
        )

    def isLeap(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def totalMonthDays(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if self.month in [4, 6, 9, 11]:
            return 30
        if self.month == 2:
            if self.isLeap():
                return 29
            else:
                return 28

    def validDate(self):
        if self.year < 0:
            return False
        if self.month <= 0 or self.month > 12:
            return False
        if self.day <= 0 or self.day > self.totalMonthDays():
            return False
        return True

    @property
    def monthName(self):
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[self.month - 1]

    @staticmethod
    def areEqual(d1, d2):
        if d1.year == d2.year and d1.month == d2.month and d1.day == d2.day:
            return True
        return False

    @staticmethod
    def isLater(d1, d2):
        if d1.year > d2.year:
            return True
        elif d1.year == d2.year:
            if d1.month > d2.month:
                return True
            elif d1.month == d2.month:
                if d1.day > d2.day:
                    return True
        return False

    @staticmethod
    def isPrevious(d1, d2):
        if not Date.isLater(d1, d2) and not Date.areEqual(d1, d2):
            return True
        return False

    @classmethod
    def firstDayOfTheYear(cls, year):
        if year > 0:
            return cls(1, 1, year)
        print("El año introducido no es válido")

    @classmethod
    def lastDayOfTheYear(cls, year):
        if year > 0:
            return cls(31, 12, year)
        print("El año introducido no es válido")

    @classmethod
    def randomDate(cls):
        """Genera una fecha aleatoria entre el año 0 y 3000."""
        year = random.randint(0, 3000)
        month = random.randint(1, 12)
        random_date = cls(1, month, year)
        random_date.day = random.randint(1, random_date.totalMonthDays())
        return random_date

    def plusDay(self):
        if Date.areEqual(self, Date.lastDayOfTheYear(self.year)):
            self.day = 1
            self.month = 1
            self.year += 1
        elif self.day == self.totalMonthDays():
            self.day = 1
            self.month += 1
        else:
            self.day += 1

    def minusDay(self):
        if Date.areEqual(self, Date.firstDayOfTheYear(self.year)):
            self.day = 31
            self.month = 12
            self.year -= 1
        elif self.day == 1:
            self.month -= 1
            self.day = self.totalMonthDays()
        else:
            self.day -= 1

    @classmethod
    def copy(cls, d):
        """Dado un objeto Date, devuelve otro objeto Date con los mismos atributos."""
        return cls(d.day, d.month, d.year)

    @staticmethod
    def difference(d1, d2):
        """Dadas dos fechas, devuelve el número de días que hay entre ellas."""
        if Date.areEqual(d1, d2):
            return 0
        elif Date.isLater(d1, d2):
            count = 0
            d2_copy = Date.copy(d2)
            while not Date.areEqual(d1, d2_copy):
                count += 1
                d2_copy.plusDay()
            return count
        else:
            count = 0
            d2_copy = Date.copy(d2)
            while not Date.areEqual(d1, d2_copy):
                count += 1
                d2_copy.minusDay()
            return count

# Pruebas
if __name__ == "__main__":
    # Creación de fechas de prueba
    date1 = Date(1, 1, 2023)
    date2 = Date(1, 1, 2024)
    date3 = Date(15, 8, 2023)

    # Prueba de copy
    copied_date = Date.copy(date1)
    print(f"Original date: {date1}")
    print(f"Copied date: {copied_date}")

    # Prueba de difference
    days_between = Date.difference(date1, date2)
    print(f"Días entre {date1} y {date2}: {days_between} días")

    days_between = Date.difference(date3, date1)
    print(f"Días entre {date3} y {date1}: {days_between} días")

    # Prueba de randomDate
    random_date = Date.randomDate()
    print(f"Fecha aleatoria generada: {random_date}")


#Ejercicio 10
#Implementa el método de clase .toDate() que dado un string con el formato 
# "01 January 0001" devuelva el objeto fecha correspondiente a day = 1, month = 1,
#  year = 1. Por ejemplo, si se pasa por parámetro 05 July 1985, el método debería devolver el objeto Date con los atributos day = 5, month = 7, year = 1985.
#2

import random

def agregarCerosIzquierda(numero, totalCifras=2):
    """Añade ceros adicionales a la izquierda hasta completar las cifras requeridas.
    
    Args:
        numero: Número entero positivo.
        totalCifras: Número entero positivo (cifras totales que debe tener el número).
    
    Returns:
        Cadena con las cifras completas.
    """
    for i in range(totalCifras - 1, 0, -1):
        if numero < 10**(totalCifras - i):
            return "0" * i + str(numero)
    return str(numero)


class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        self.dia = dia
        self.mes = mes
        self.año = año
        if not self.esFechaValida():
            print("¡¡¡La fecha introducida no es una fecha válida!!!")

    def __str__(self):
        return "{} / {} / {}".format(
            agregarCerosIzquierda(self.dia),
            agregarCerosIzquierda(self.mes),
            agregarCerosIzquierda(self.año, 4)
        )

    def esAñoBisiesto(self):
        if self.año % 4 == 0:
            if self.año % 100 == 0:
                if self.año % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def obtenerDiasDelMes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if self.mes in [4, 6, 9, 11]:
            return 30
        if self.mes == 2:
            if self.esAñoBisiesto():
                return 29
            else:
                return 28

    def esFechaValida(self):
        if self.año < 0:
            return False
        if self.mes <= 0 or self.mes > 12:
            return False
        if self.dia <= 0 or self.dia > self.obtenerDiasDelMes():
            return False
        return True

    @property
    def nombreDelMes(self):
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        return meses[self.mes - 1]

    @staticmethod
    def sonIguales(fecha1, fecha2):
        if fecha1.año == fecha2.año and fecha1.mes == fecha2.mes and fecha1.dia == fecha2.dia:
            return True
        return False

    @staticmethod
    def esPosterior(fecha1, fecha2):
        if fecha1.año > fecha2.año:
            return True
        elif fecha1.año == fecha2.año:
            if fecha1.mes > fecha2.mes:
                return True
            elif fecha1.mes == fecha2.mes:
                if fecha1.dia > fecha2.dia:
                    return True
        return False

    @staticmethod
    def esAnterior(fecha1, fecha2):
        if not Fecha.esPosterior(fecha1, fecha2) and not Fecha.sonIguales(fecha1, fecha2):
            return True
        return False

    @classmethod
    def primerDiaDelAño(cls, año):
        if año > 0:
            return cls(1, 1, año)
        print("El año introducido no es válido")

    @classmethod
    def ultimoDiaDelAño(cls, año):
        if año > 0:
            return cls(31, 12, año)
        print("El año introducido no es válido")

    @classmethod
    def fechaAleatoria(cls):
        """Genera una fecha aleatoria entre el año 0 y 3000."""
        año = random.randint(0, 3000)
        mes = random.randint(1, 12)
        fecha_aleatoria = cls(1, mes, año)
        fecha_aleatoria.dia = random.randint(1, fecha_aleatoria.obtenerDiasDelMes())
        return fecha_aleatoria

    @classmethod
    def convertirACadena(cls, cadena):
        """Convierte una cadena en formato 'DD Mes YYYY' a un objeto Fecha.
        
        Args:
            cadena: Cadena en formato 'DD Mes YYYY'.
        
        Returns:
            Un objeto Fecha si la cadena es válida; 'NULL' si el formato es incorrecto o el mes no es válido.
        """
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        
        partes_fecha = cadena.split(" ")
        if len(partes_fecha) != 3:
            print("Formato de fecha incorrecto. Debe ser 'DD Mes YYYY'.")
            return "NULL"
        
        try:
            dia = int(partes_fecha[0])
            nombre_mes = partes_fecha[1]
            año = int(partes_fecha[2])
            
            if nombre_mes in meses:
                mes = meses.index(nombre_mes) + 1
            else:
                print("No has introducido un mes válido")
                return "NULL"
            
        except ValueError:
            print("Error en la conversión de la fecha. Asegúrate de que el día y el año sean números.")
            return "NULL"

        return cls(dia, mes, año)

    def siguienteDia(self):
        if Fecha.sonIguales(self, Fecha.ultimoDiaDelAño(self.año)):
            self.dia = 1
            self.mes = 1
            self.año += 1
        elif self.dia == self.obtenerDiasDelMes():
            self.dia = 1
            self.mes += 1
        else:
            self.dia += 1

    def diaAnterior(self):
        if Fecha.sonIguales(self, Fecha.primerDiaDelAño(self.año)):
            self.dia = 31
            self.mes = 12
            self.año -= 1
        elif self.dia == 1:
            self.mes -= 1
            self.dia = self.obtenerDiasDelMes()
        else:
            self.dia -= 1

    @classmethod
    def copiar(cls, fecha):
        """Dado un objeto Fecha, devuelve otro objeto Fecha con los mismos atributos."""
        return cls(fecha.dia, fecha.mes, fecha.año)

    @staticmethod
    def diferencia(fecha1, fecha2):
        """Dadas dos fechas, devuelve el número de días que hay entre ellas."""
        if Fecha.sonIguales(fecha1, fecha2):
            return 0
        elif Fecha.esPosterior(fecha1, fecha2):
            conteo = 0
            fecha2_copia = Fecha.copiar(fecha2)
            while not Fecha.sonIguales(fecha1, fecha2_copia):
                conteo += 1
                fecha2_copia.siguienteDia()
            return conteo
        else:
            conteo = 0
            fecha2_copia = Fecha.copiar(fecha2)
            while not Fecha.sonIguales(fecha1, fecha2_copia):
                conteo += 1
                fecha2_copia.diaAnterior()
            return conteo

# Pruebas
if __name__ == "__main__":
    # Creación de fechas de prueba
    fecha1 = Fecha(1, 1, 2023)
    fecha2 = Fecha(1, 1, 2024)
    fecha3 = Fecha(15, 8, 2023)

    # Prueba de copiar
    fecha_copiada = Fecha.copiar(fecha1)
    print(f"Fecha original: {fecha1}")
    print(f"Fecha copiada: {fecha_copiada}")

    # Prueba de diferencia
    dias_entre = Fecha.diferencia(fecha1, fecha2)
    print(f"Días entre {fecha1} y {fecha2}: {dias_entre} días")

    dias_entre = Fecha.diferencia(fecha3, fecha1)
    print(f"Días entre {fecha3} y {fecha1}: {dias_entre} días")

    # Prueba de fechaAleatoria
    fecha_aleatoria = Fecha.fechaAleatoria()
    print(f"Fecha aleatoria generada: {fecha_aleatoria}")

    # Prueba de convertirACadena
    fecha_str = "05 Julio 1985"
    fecha_desde_cadena = Fecha.convertirACadena(fecha_str)
    print(f"Fecha convertida desde cadena '{fecha_str}': {fecha_desde_cadena}")

    fecha_invalida_str = "31 MesInvalido 2024"
    fecha_invalida = Fecha.convertirACadena(fecha_invalida_str)
    print(f"Fecha convertida desde cadena inválida '{fecha_invalida_str}': {fecha_invalida}")
