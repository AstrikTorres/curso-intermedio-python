def divisors(num):
    try:
        if num < 0 or num == 0:
            raise ValueError
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError:
        print('Ingresa un número positivo')


def run():
    try:
        num = int(input("Ingresa un número:"))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()
