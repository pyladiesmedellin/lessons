# -*- coding: utf-8 -*-

# recurso de referencia: http://www.tutorialspoint.com/python/python_lists.htm
lista_de_asignaturas_teoricas = [ 'matematicas', 'lengua castellana']
lista_de_asignaturas_laboratorio = ['fisica', 'biologia', 'programacion']

""" Concatenar listas"""
print "lista_de_asignaturas_teoricas + lista_de_asignaturas_laboratorio: "
todas_las_asignaturas = lista_de_asignaturas_teoricas + lista_de_asignaturas_laboratorio
print todas_las_asignaturas
# ['matematicas', 'lengua castellana', 'fisica', 'biologia', 'programacion']

""" Repeticion de elementos"""
print "asignaturas_repetidas: "
asignaturas_repetidas = lista_de_asignaturas_teoricas * 3
print asignaturas_repetidas
# ['matematicas', 'lengua castellana', 'matematicas', 'lengua castellana', 'matematicas', 'lengua castellana']

""" Encontrar elementos en la lista """
print "la materia matemátias se encuentra en la lista lista_de_asignaturas_teoricas?"
print "matematicas" in lista_de_asignaturas_teoricas
# True

print "la materia inglés se encuentra en la lista lista_de_asignaturas_teoricas?"
print "inglés" in lista_de_asignaturas_teoricas
# print False




