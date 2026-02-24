print('Olá, coloque o seu nome aqui antes de qualquer coisa')
nome = input('Digite o seu nome aqui: ')
print('Olá', nome, 'seja bem-vindo(a)')
print('Escolha uma dessas opções')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = input('Digite o número da operação escolhida: ')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if opcao == '1':
    resultado = num1 + num2
    print('O resultado da soma é:', resultado)

if opcao == '2':
    resultado = num1 - num2
    print('O resultado da subtração é:', resultado)   

if opcao == '3':
    resultado = num1 * num2
    print('O resultado da multiplicação é:', resultado)   

if opcao == '4':
    resultado = num1 / num2
    print('O resultado da divisão é:', resultado)    

    
