# Son funciones que reciben como parámetro a otra función.
def saludo(func):
    func()


def hola():
    print("¡Hola!")


def adios():
    print("¡Adios!")

# Funciones de orden superior de importancia:

# 1. filter
# recibe una función filtro (anónima) y un iterable (lista, tupla, etc)
# devolviendonos un iterador: objeto optimizado recorrer elemento a elemento (iterar)
# por lo que no lo podemos inprimir de manera directa (para ello lo convertimos a una lista),
# su sintaxis es: filter(<funcion filtro>, <iterable>)


def my_filter():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    my_list_filter = list(filter(lambda x: x % 2 !=0, my_list))
    print(my_list_filter)


# 2. map
#  al igual que filter recibe una función anónima y un iterable como parámetros pero en este caso
#  map ejecuta la función sobre cada uno de los elementos del iterable,
#  sintaxis: map(<funcion>, <iterable>)


def my_map():
    my_list = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, my_list))
    print(squares)


# 3. reduce
# tenemos que importar esta función desde functools para poder usarla, tiene los mismos argumentos
# que las anteriores funciones, reduce el iterable por medio de la función anonima,
# su sintaxis es: reduce(<funcion reduccion>, <iterable>)
# la función de reducción necesita de dos parámetros, uno que almacena el resultado
# (o el primer valor del iterable) y otro que opera con el siguiente valor del iterable:
# lambda a,b: <expresión>


def my_reduce():
    from functools import reduce
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print(all_multiplied)


if __name__ == '__main__':
    saludo(hola)
    saludo(adios)
    my_filter()
    my_map()
    my_reduce()
