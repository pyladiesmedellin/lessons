# -*- coding: utf-8 -*-

compra = int(input("ingresa el valor de la compra"))

if compra <= 100:
    print "Pago en efectivo"
elif compra > 100:
    print "Pago con tarjeta débito"
else:
    print "Pago con tarjeta crédito"