def calcul_plus_mol():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    did = input('Введите действие "+" или "*": ')

    if did == '+':
        plus = num1 + num2
        print(plus)
        return plus

    elif did == '*':
        mol = num1 * num2
        print(mol)
        return mol

    else:
        print('Произошла ошибка')


calcul_plus_mol()