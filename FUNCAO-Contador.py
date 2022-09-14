def contagem(ini, fim, pas):
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    if pas == 0:
        pas = 1
    if ini >= fim:
        ajuste = -1
        if pas > 0:
            pas = pas * -1
    else:
        ajuste = 1
        if pas < 0:
            pas = pas * -1
    for i in range(ini, fim + ajuste, pas):
        print(f'{i} ', end='')
    print('FIM!')

ini = fim = pas = 0
print('=-' * 30)
contagem(1, 10, 1)
print('=-' * 30)
contagem(10, 0, 2)
print('=-' * 30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contagem(ini, fim, pas)