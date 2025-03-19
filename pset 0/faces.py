def convert(textoOriginal):
    textoOriginal = textoOriginal.replace(":)", "🙂").replace(":(", "🙁")
    return textoOriginal

def main():
    texto = input()
    print(convert(texto))

main()
