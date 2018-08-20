#!/usr/bin/env python
# -*- coding: utf-8 -*-


from inicial import *




baase_datos_txt("%s/__RESULTADOS__OBJECT/Base de datos inicial.txt"%ruta,"w")
lista_lineas=lista_listas("%s/__RESULTADOS__OBJECT/Base de datos inicial.txt"%ruta,"r")

c=[("c%s"%i) for i in range(n)]

class consumidor():
	def __init__(self,nom,tel,pot,fdp):
		self.nom=nom
		self.tel=tel
		self.pot=pot
		self.fdp=fdp
	
	@classmethod
	def generador_clientes(cls,string):
		string=string.replace("\n","")
		nom,tel,pot,fdp=string.split(" ")
		return cls(nom,tel,float(pot),float(fdp))

#Ejecucion del metodo para agregar los clientes como objetos a la clase
for i in range(n):
	c[i]=consumidor.generador_clientes(lista_lineas[i])

#subclase con los clientes seleccionados y calculo del coste y tiempo amortizacion
crear_lista("%s/__RESULTADOS__OBJECT/Lista_seleccionados.html"%ruta)
class consumidores_seleccionados(consumidor):

	def __init__(self,nom,tel,pot,fdp):
		consumidor.__init__(self,nom,tel,pot,fdp)
		self.coste=float(self.pot)*fp
		self.tamor=float(self.coste)/am
		add_to_list("%s/__RESULTADOS__OBJECT/Lista_seleccionados.html"
		%ruta,self.nom,self.tel,self.pot,self.fdp,self.coste,self.tamor)
		crear_cartas("%s/__RESULTADOS__OBJECT/CARTAS__OBJECT/"
		%ruta,"f",self.nom,self.fdp,self.coste,self.tamor)

	@staticmethod
	@time_count_logging
	def seleccion():
		for i in range(len(c)):
			if (c[i].fdp > 0.30 and c[i].fdp < fdpmax+0.01 and c[i].pot > 80.00):
		 		c[i]=consumidores_seleccionados(c[i].nom,c[i].tel,float(c[i].pot),float(c[i].fdp))

#ejecucion del metodo para agregar los clientes con fdp deseado como objetos a la clase
consumidores_seleccionados.seleccion()



print("**************************************************************************************************************************************")
print ('En la carpeta RESULTADOS__INICIAL ubicada en %s encontrara:\n\nBase de datos inicial.txt(Es el base'
' de datos generada, donde se encuentran los datos de todos los consumidores)\n\nLista_seleccionados.html(Lista con'
' los consumidores seleccionados para la mejora del factor de potencia, se indican los datos de cada consumidor'
' incluyendo el coste y tiempo de amortización)\n\n' 
'logging_profiling.txt(Registro en un archivo txt de las llamadas, variables y tiempo de ejecucion de las funciones'
' o metodos deseados)\n\n'
'carpeta CARTAS_INICIAL(Carpeta que contiene la carta generada para cada consumidor, para informarle de los beneficios'
' que obtendría al mejorar su factor de potencia)'%ruta)
print("\n**************************************************************************************************************************************")



