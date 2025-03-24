def main():
    saldoDevido = 50
    while True:
        moedaInserida = int(input(f"Amount Due: {saldoDevido}\n"))
        if moedaInserida in (25, 10, 5):
            saldoDevido -= moedaInserida
            if saldoDevido <= 0:
                print(f"Change Owed: {abs(saldoDevido)}")
                break
            print(f"Amount Due: {saldoDevido}")
                
            
main()