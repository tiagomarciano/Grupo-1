def characteristic(numString, c):
    try:
        c[0] = int(float(numString))
        return True
    except:
        return False

def mantissa(numString, numerator, denominator):
    try:
        aux = numString.split('.', 1)[1]
        numerator[0] = int(aux)
        cont = 1

        for x in aux:
            cont *= 10

        denominator[0] = cont

        return True
    except:
        return False

def main():
    number = '123.456'
    c = [0]
    n = [0]
    d = [0]

    if (characteristic(number, c) and mantissa(number, n, d)):
        print(number)
        print(c[0])
        print(n[0])
        print(d[0])
    else:
        print('O número informado é inválido!')

if __name__ == "__main__":
    main()