def convert(textoOriginal):
    textoOriginal = textoOriginal.replace(":)", "🙂").replace(":(", "🙁") #if in é desnecessário
    return textoOriginal

def main():
    texto = input()
    print(convert(texto))

main()
