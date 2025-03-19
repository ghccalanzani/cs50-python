def convert(textoOriginal):
    while ":)" in textoOriginal or ":(" in textoOriginal:
        textoOriginal = textoOriginal.replace(":)", "🙂").replace(":(", "🙁")
    return textoOriginal

def main():
    texto = input()
    print(convert(texto))

main()
