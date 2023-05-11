print('{:=^40}'.format('LOJAS Rennan '))
preco = float(input('preco das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartao 
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('qual é a opçao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela  =  total / 2
    print('sua compra vai ser parcelada em 2x de R${:.2f} SEM JUROS '.format(parcela))
elif opcao == 4:
    total = preco + ( preco * 20 / 100)
    totalparc= int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('OPCAO INVALIDA de pagamento. Tente novamente!')
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
