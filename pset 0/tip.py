def main():
    dollars = dollars_to_float(input("Qual o valor da refeicao? "))
    percent = percent_to_float(input("Qual a porcentagem da gorjeta? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip('$')
    return float(d)

def percent_to_float(p):
    p = p.strip('%')
    return float(p)/100

main()