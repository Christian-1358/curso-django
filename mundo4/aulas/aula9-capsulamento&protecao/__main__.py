from conta import ContaBancaria

def main():
    c1 = ContaBancaria(111, "maria", 5_999)
    c1.depositar(1000)
    c1.titular = 'pedro' #ele deixa mais n deixa, pois "aldutos tao consentindo"
    c1.saldo = 0
    print(c1)
    
    
if __name__ == '__main__':
    main()