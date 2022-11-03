import Estructura
valor=500

def depositoCuenta(deposito):
    global valor
    
    if(deposito%100==0):
        valor=valor+deposito
 
        return valor
    else:
        print("error en el deposito")



def retiroCuenta(retiro):
    global valor
   
    if(retiro%100==0):
        valor=valor-retiro
        return valor 
    else:
        print("error al retirar dinero en la cuenta")

 



def mostrarCuenta():
    global valor
    print( "el saldo de la cuenta es de: ",valor )


 
