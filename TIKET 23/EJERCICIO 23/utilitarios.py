def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

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