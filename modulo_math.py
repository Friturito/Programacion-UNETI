def sum(n1, n2):
    print(n1 + n2)


def rest(n1, n2):
    print(n1 - n2)


def multi(n1, n2):
    print(n1 * n2)


def div(n1, n2):
    try:
        print(n1 / n2)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
