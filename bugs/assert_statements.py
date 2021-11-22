# Assert statements
# Es una manera poco usual de manejar los errores en python
# Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python,
# si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.
def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número:")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Termino mi programa de divisores")
    print(palindrome(""))


if __name__ == '__main__':
    run()
