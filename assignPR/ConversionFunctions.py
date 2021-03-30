# A função characteristic atribui a parte inteira de uma string númerica
# para a variável intNumber
#
# @param numString, string númerica que será convertida
# @param intNUmber, recebe o valor inteiro da conversão da string númerica
# @return True, se a conversão for bem sucedida e False, caso não consiga converter
#
def characteristic(numString, intNumber):
    try:
        intNumber[0] = int(float(numString))
        return True
    except:
        return False

# A função mantissa atribui a parte decimal de uma string númerica a variável numerator,
# e calcula o logartimo baseado no numerador
#
# @param numString, string númerica que será convertida
# @param numerator, recebe um inteiro do valor decimal da conversão da string númerica
# @param denominator, recebe o logartimo do numerator
# @return True, se o calculo for bem sucedido e False, caso não consiga calcular
#
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

# Método principal
def main():
    number = '123.456'
    intNumber = [0]
    numerator = [0]
    denomiator = [0]

    if (characteristic(number, intNumber) and mantissa(number, numerator, denomiator)):
        print(number)
        print(intNumber[0])
        print(numerator[0])
        print(denomiator[0])
    else:
        print('O número informado é inválido!')

if __name__ == "__main__":
    main()
