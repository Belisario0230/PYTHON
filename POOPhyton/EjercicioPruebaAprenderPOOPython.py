class Vehiculo:
    contador_vehiculos = 0  # Atributo de clase para contar el número de vehículos creados

    def __init__(self, marca, modelo, año):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia
        self.año = año  # Atributo de instancia
        Vehiculo.contador_vehiculos += 1  # Incrementar el contador de vehículos

    @classmethod
    def obtener_total_vehiculos(cls):
        """Método de clase para obtener el número total de vehículos."""
        return cls.contador_vehiculos

    @staticmethod
    def tipo_vehiculo():
        """Método estático para indicar que es un vehículo."""
        return "Este es un vehículo."

    @property
    def edad(self):
        """Propiedad para calcular la edad del vehículo."""
        from datetime import datetime
        return datetime.now().year - self.año

    def descripcion(self):
        """Método de instancia para describir el vehículo."""
        return f"{self.marca} {self.modelo}, {self.año}"

    def __str__(self):
        """Método mágico para representar el objeto como cadena."""
        return self.descripcion()

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.puertas = puertas  # Atributo específico de Coche

    def descripcion(self):
        """Método de instancia sobreescrito para describir el coche."""
        return f"{super().descripcion()} con {self.puertas} puertas"

    @property
    def es_deportivo(self):
        """Propiedad que indica si el coche es deportivo basado en el modelo."""
        deportivos = ["Ferrari", "Lamborghini", "Porsche"]
        return self.modelo in deportivos


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.tipo = tipo  # Atributo específico de Motocicleta

    def descripcion(self):
        """Método de instancia sobreescrito para describir la motocicleta."""
        return f"{super().descripcion()} tipo {self.tipo}"

    @property
    def es_de_aventura(self):
        """Propiedad que indica si la motocicleta es de aventura basado en el tipo."""
        return self.tipo.lower() == "aventura"

def main():
    # Crear instancias de Vehiculo, Coche y Motocicleta
    coche1 = Coche("Ferrari", "488", 2020, 2)
    coche2 = Coche("Toyota", "Corolla", 2018, 4)
    moto1 = Motocicleta("BMW", "GS", 2021, "Aventura")
    moto2 = Motocicleta("Yamaha", "MT-07", 2022, "Deportiva")

    # Mostrar información de los vehículos
    print(coche1)  # Utiliza el método __str__
    print(coche2)
    print(moto1)
    print(moto2)

    # Mostrar propiedades específicas
    print(f"¿El {coche1.modelo} es deportivo? {'Sí' if coche1.es_deportivo else 'No'}")
    print(f"¿La {moto1.modelo} es de aventura? {'Sí' if moto1.es_de_aventura else 'No'}")

    # Mostrar total de vehículos
    print(f"Total de vehículos creados: {Vehiculo.obtener_total_vehiculos()}")

if __name__ == "__main__":
    main()
