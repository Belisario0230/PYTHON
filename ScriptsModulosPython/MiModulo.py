def my_sum(*numbers):
    """
    Funcion que suma los elementos que introduzcamos por parametro
    """
    result = 0
    for n in numbers:
        result += n
  
    return result
  
def my_prod(*numbers):
    """
    Funcion que multiplica los elementos que introduzcamos por parametro
    """
    result = 1
    for n in numbers:
        result *= n
  
    return result
    
def my_description():
    print("Este mÃ³dulo tiene 3 funciones: ")
    print("\t- la que muestra la descripciÃ³n del mÃ³dulo")
    print("\t- la que suma los nÃºmeros que introduzcamos por parÃ¡metro")
    print("\t- la que multiplica los nÃºmeros que introduzcamos por parÃ¡metro")
    
sum1to10 = my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
prod1to10 = my_prod(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)