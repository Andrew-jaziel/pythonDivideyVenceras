import Estructura
valor=500

def depositoCuenta(deposito):
    global valor
    
    if(deposito%100==0):
        valor=valor+deposito
 
    else:
        print("error en el deposito")
    return valor

def retiroCuenta(retiro):
    global valor
   
    if(retiro%100==0):
        valor=valor-retiro
     
    else:
        print("error al retirar dinero en la cuenta")
    return valor 

def mostrarCuenta():
    global valor
    print( "el saldo de la cuenta es de: ",valor )


 
