resposta = input('Greeting: ')
resposta = resposta.lower().strip()

if resposta.startswith('hello'):
    print('$0')
elif resposta.startswith('h'):
    print('$20')
else:
    print('$100')
