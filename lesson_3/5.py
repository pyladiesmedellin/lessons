# -*- coding: utf-8 -*-

importe_a_pagar = int(input("Ingrese el importe"))

if importe_a_pagar > 100:
    tasa_descunto = 0.10
    descuento = importe_a_pagar * tasa_descunto
    total_a_pagar = importe_a_pagar - descuento
    print "El total a pagar es: %d" % (total_a_pagar)
else:
    print "El total a pagar es: %d" % (importe_a_pagar)