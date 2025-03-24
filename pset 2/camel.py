palavra = input("Camel case: ")
palavraSnakeCase = ""

for p in palavra:
    if p.isupper():
        palavraSnakeCase = palavraSnakeCase + '_' + p.lower()
    else:
        palavraSnakeCase = palavraSnakeCase + p

print(palavraSnakeCase)