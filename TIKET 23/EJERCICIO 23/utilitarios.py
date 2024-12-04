def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

<<<<<<< HEAD
def consultarMulta(valor): 
    if valor == 1:
        return 10 / 100 * 100
    elif valor == 2:
        return 15 / 100 * 100
    elif valor == 3:
        return 20 / 100 * 100
    elif valor == 4:
        return 30 / 100 * 100
    else:
        return -1
     
        
    
=======
def calcularSubtotal(val1,val2,val3):
    subtotalSinDescuento=val1*val2
    calculo=subtotalSinDescuento*(val3/100)
    subtotal1=subtotalSinDescuento-calculo
    return subtotal1

def calcularValorDescuento(val1,val2):
    calculo=val1*(val2/100)
    descuento1=val1-calculo
    return descuento1

def calcularValorHora(val1):
    valorhora1=460/val1
    return valorhora1
>>>>>>> cf92a62a06cd589079e9504101fb99c5add1ed8b
