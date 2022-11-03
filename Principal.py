from Funciones import *



def UsuarioCuenta():

    nombreTarjeta="pipito1234"
    pincuenta=1234
    nombre=input("Digite el nombre de la cuenta: ")
    pin=int(input("Digite su ping de cuenta: "))
    if(nombreTarjeta==nombre and pin==pincuenta):
        print("digito de manera correcta")
        return True
    else:
        print("datos mal indicado")
        return False
    
def Deposito():
    depos=int(input("Digite el valor a ser depositado: "))
    depositoCuenta(depos)
    print(valor)
def RetirodeDinero():
    reti=int(input("Digite el valor a retirar: "))
    retiroCuenta(reti)
    print(reti)


def menu():
            print("1. Depositar dinero: ")
            print("2. Retirar Dinero: ")
            print("3. Mostrar cuenta: ")
            print("4. Salir.")
            op = int(input("Escriba el # de la opcion: "))
            return op


def main():
    if(UsuarioCuenta()==True):
        op = 0
        while(op != 4):
            op = menu()
            if(op==1): Deposito()
            elif(op==2): RetirodeDinero()
            elif(op==3): mostrarCuenta()
            elif(op==4): print("Ciao, ciao...")
            else: print("Opcion Invalida...")


    else:
        print("digite bien su mierda")

main()