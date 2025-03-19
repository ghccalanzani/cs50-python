nomeArquivo = input('Nome do arquivo: ')
nomeArquivo = nomeArquivo.strip().lower()

if nomeArquivo.endswith('.gif'):
    print('image/gif')
elif nomeArquivo.endswith('.jpg') or nomeArquivo.endswith('.jpeg'):
    print('image/jpeg')
elif nomeArquivo.endswith('.png'):
    print('image/png')
elif nomeArquivo.endswith('.pdf'):
    print('application/pdf')
elif nomeArquivo.endswith('.txt'):
    print('text/plain')
elif nomeArquivo.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')