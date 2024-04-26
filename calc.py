def calculadora(num1, num2, op):
    if op == 1:
        print(f'El resultado final de {num1} más {num2}, amigo mio, es: {num1 + num2}')
    elif op == 2:
        print(f'El resultado final de {num1} menos {num2}, amigo mio, es: {num1 - num2}')
    elif op == 3:
        print(f'El resultado final de {num1} por {num2}, amigo mio, es: {num1 * num2}')
    elif op == 4:
        print(f'El resultado final de {num1} entre {num2}, amigo mio, es: {num1 / num2}')
    else:
        print('te has equivocado de opción!')

variable1 = float(input('Introduzca el primer valore: '))
variable2 = float(input('Introduzca el segundo valore: '))

print(calculadora(variable1, variable2, 1))
print(calculadora(variable1, variable2, 2))
print(calculadora(variable1, variable2, 3))
print(calculadora(variable1, variable2, 4))