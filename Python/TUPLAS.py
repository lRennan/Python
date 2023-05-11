lanche = ('HAMBURGUER,' ' suco', 'PIZZA', 'pudim', 'Batata frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')


for pos,comida in enumerate(lanche):
    print(f'eu vou comer{comida} na posiçao {pos}')
print('Comi pra caramba!')
