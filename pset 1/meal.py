def main():
    tempoSTRING = input("Que horas são? ")
    horario = convert(tempoSTRING)
    
    if 7 <= horario <= 8:
        print('breakfast time')
    elif 12 <= horario <= 13:
        print('lunch time')
    elif 18 <= horario <= 19:
        print('dinner time')

def convert(tempoSTRING):
    h, m = tempoSTRING.split(":")
    m = float(m) / 60
    horario = float(h) + m
    return horario

if __name__ == "__main__":
    main()