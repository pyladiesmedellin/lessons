# -*- coding: utf-8 -*-

lista_de_asignaturas = ['fisica', 'biologia', 'matematicas', 'programacion']

""" tamaño variable """
# imprime lista de asignaturas
print lista_de_asignaturas
# ['fisica', 'biologia', 'matematicas', 'programacion']

lista_de_asignaturas_mas_extensa = ['fisica', 'biologia', 'matematicas', 'programacion', 'quimica']
print lista_de_asignaturas_mas_extensa
# ['fisica', 'biologia', 'matematicas', 'programacion', , 'quimica']

""" buscar elementos en la lista """

# imprime la primera asignatura
print "la primera asignaturas es: ", lista_de_asignaturas[0]
# la primera asignaturas es:  fisica

# imprime la segunda asignatura
print "la segunda asignaturas es: ", lista_de_asignaturas[1]
# la segunda asignaturas es:  biologia

# imprime la ultima asignatura
print "la ultima asignaturas es: ", lista_de_asignaturas[-1]
# la ultima asignaturas es:  programacion

# imprime los elementos incluídos desde la posición 1(incluido 1) a la posición 2(excluyendo 2)
print "los elementos incluídos desde la posición 1 a la posición 2: ", lista_de_asignaturas[1:2]
# los elementos incluídos desde la posición 1 a la posición 2:  ['biologia']

# imprime los elementos incluídos desde la posición 1(incluido 1) a la posición 3(excluyendo 3)
print "los elementos incluídos desde la posición 1 a la posición 3: ", lista_de_asignaturas[1:3]
# los elementos incluídos desde la posición 1 a la posición 3:  ['biologia', 'matematicas']

