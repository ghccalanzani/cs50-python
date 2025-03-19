resposta = input('Qual a resposta para a vida, universo e tudo mais?')
resposta = resposta.lower().strip()

if resposta == '42' or resposta == 'forty-two' or resposta == 'forty two':
    print('Yes')
else:
    print('No')