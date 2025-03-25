texto = input("Input: ")
novoTexto = ''

for t in texto:
    if t in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
        continue
    else:
        novoTexto += t

print('Output: ' + novoTexto)