# #Anderson
# # CALCULA TOTAL A PAGAR TAXI
# #custokmrodado = float(input("Entre com o valor do KM rodado: "))
#Constante sao os valores que estao fixos dentro do programa, nao podendo ser alterados pelo usuario
custokmrodado = 6.0
#Variaveis podem ser alteradas pelo usuario
quantidadekmrodado = float(input("Entre com o total de KM rodado: "))
#
# totalapagar = round((custokmrodado * quantidadekmrodado), 2)
#
# print("O total a pagar é: R$",totalapagar)

#Toshio
#custo
custo = float(input('Qual é o custo por quilometro?'))

#Quilometragem
quilometro = float(input('Quantos quilometros você percorreu?'))

cliente = input("Enre com o seu nome: ")
#Valor a pagar
preco = custo * quilometro

#Exemplos de Formatacao
print('1',cliente, 'esta corrida custou: R$', preco)
print('2','{} esta corrida custou: R${} '.format(cliente, preco))
print('3','{} esta corrida custou: R${:.2f} '.format(cliente, preco))
print('4','{} o custo do kilometro é R${}, e voce percorreu {}KM por isso esta corrida custou: R${} '.format(cliente, custo, quilometro, preco))
print('5',f'{cliente} o custo do kilometro é R${custo}, 1e voce percorreu {quilometro}KM por isso esta corrida custou: R${round(preco, 2)} ')

print("Adicionada nova linha")