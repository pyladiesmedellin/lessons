# -*- coding: utf-8 -*-

# recurso de referencia: http://www.tutorialspoint.com/python/python_lists.htm
lista_de_asignaturas = ['fisica', 'biologia', 'matematicas', 'programacion', 'quimica']

"Invierte el orden de los elementos de la lista"
lista_de_asignaturas.reverse()
print "lo elementos de la lista en orden invertido son"
print lista_de_asignaturas
# ['quimica', 'programacion', 'matematicas', 'biologia', 'fisica']

lista_con_elementos_repetidos = ['fisica', 'biologia', 'matematicas', 'fisica', 'biologia', 'fisica']

"Cantidad coincidencias en la lista segun un elemento dando"
print "Cuantas veces está física en la lista?"
print lista_con_elementos_repetidos.count("fisica")
# 3

"Ordena elementos en lista"
lista_de_numeros = [1, 2, 3, 4, 2, 5, 6, 3, 8, 1]
print "Organiza los elementos de menor a mayor"
lista_de_numeros.sort()
print lista_de_numeros
# [1, 1, 2, 2, 3, 3, 4, 5, 6, 8]
