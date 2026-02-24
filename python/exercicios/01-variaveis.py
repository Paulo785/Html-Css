faturamento=997 #int
custo=300 #int
imposto=0.2 #float
lucro1=faturamento-custo-imposto*faturamento 

faturamento=600
lucro2=faturamento-custo-imposto*faturamento
print(lucro1)
print(lucro2)

# Tipos de variáveis
# int: números inteiros
# float: números com casas decimais
# string: texto
# booleanos: Verdadeiro ou Falso (True / False)

print('O lucro do primeiro mês foi:', lucro1)
print('O lucro do segundo mês foi:', lucro2)

print('O lucro da loja foi de', lucro1, 'para o primeiro mês')

margem_lucro=lucro2/faturamento
print('Margem de lucro de', margem_lucro)

meta=0.5
bateu_meta= margem_lucro >= meta #booleana
print(bateu_meta)

# mod % (resto da divisão)
# // (parte inteira da divisão)
duracao_contrato= 140 #meses

anos= duracao_contrato // 12 
meses_sobra= duracao_contrato % 12

print('O contrato tem', anos, 'anos e', meses_sobra, 'meses')
