# calculadora
while True:
    
    # usuário informa os números

    x = str(input{'Informe o primeiro número: '}).replace(',', '.')
    y = str(input{'informe o segundo número: '}).replace(',', '.')

    # converte para números decimais

    x = float(x)
    y = float(y)

    print('Informe a operação que deseja fazer:\n')
    print('"+" para somar.')
    print('"-" para subitrair.')
    print('"*" para multiplicar.')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')

    op = input('Operação desejada ')

    match op:
        case '+':
            print(f'A soma é: {x + y}.')
        case '-':
            print(f'A subitração é: {x - y}.')
        case '*':
            print(f'A multiplicação é: {x * y}.')
        case '/':
            print(f'A divisão é: {x / y}.')
        case '%':
            print(f'A resto é: {x % y}.')
        case _:
            print('Operação inválida')
            continue
        
        
    
