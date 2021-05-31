
def divisors(n):
    l = [i for i in range(1,n+1) if n%i==0]
    return l
def run_assert():
    print("*****Probando assert*****")
    n = int(input("Ingresa un numero:\n"))
    assert n > 0, "Debes ingresar un numero positivo"
    d = divisors(n)
    print(f'Los divisores de {n} son {d}')

def run_try():
    print("***+Probando Try , raise and except****")
    try:
        n = int(input("Ingresa un numero:\n"))
        if n<0:
            raise Exception('negative')
        d = divisors(n)
        print(f'Los divisores de {n} son {d}')
    except Exception as E:
        print("El numero debe ser positivo")

if __name__=='__main__':
    run_assert()
    run_try()
