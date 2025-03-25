def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not plate.isalnum(): #Garante que só há letras e números
        return False
    if  len(plate) < 2 or len(plate) > 6: #Garante tamanho entre 2 e 6 caracteres
        return False
    if not plate[:2].isalpha(): #Garante que começa com pelo menos 2 letras
        return False
    if any(char.isdigit() for char in plate): #Verifica que há numeros
        reverso = "".join(reversed(plate))
        contador = 0 
        for x in range(len(plate) - 1):
            if reverso[x].isdigit() and reverso[x+1].isalpha():
                contador += 1
        if contador > 1:
            return False
    return True

main()