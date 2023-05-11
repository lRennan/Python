'''
Exercício Python 094:Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de cada pessoa em
um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Error!,  RESPONDA APENAS S ou N.')
    if resp == 'N':
        break
print('-='* 30)
print(f' A) ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.0f}anos. ')
print('C) As mulheres cadastradas foram', end='')
for p in galera:
    if p ['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista de pessoas que estao acima da media: ')
for p in galera:
    if p ['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<<< ENCERRADO >>>')

