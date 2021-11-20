def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 == 0:
            continue
        my_dict[i] = i ** 3

    print(my_dict)

    # { key:value for value in iterable if condition }
    my_dict_comprehension = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict_comprehension)


def challenge():
    # Crear con un dictionary comprehension,un diccionario cuyas llaves sean los
    # 1000 primeros números naturales con sus raíces cuadradas como valores
    dict_square_root = {i: i ** 0.5 for i in range(1, 1001)}
    print(dict_square_root)


if __name__ == '__main__':
    run()
    challenge()
