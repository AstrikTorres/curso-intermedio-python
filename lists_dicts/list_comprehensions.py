def run():
    squares = []
    for i in range(1, 101):
        squares.append(i ** 2)

    print(squares)

    # [element for element in iterable if condition]
    squares_comprehensions = [i ** 2 for i in range(1, 101) if i % 3 != 0]


def reto():
    # Reto: Crear un list comprhension de todos los multiplos de 4 que a la vez
    # también son múltiplos de 6 y de 9, hasta 5 dígitos
    list_comprehension = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(list_comprehension)


if __name__ == '__main__':
    run()
    reto()
