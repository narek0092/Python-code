#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import shutil
import datetime

#Fecha
date=datetime.datetime.now()
date=date.strftime("%Y-%m-%d")

#Ruta
ruta=os.getcwd()

#Factores de coste y amortizacion
fp=20  
am=200 

#Nº Consumidores
n=30

#Valor de mejora del f.d.p
fdpmax=0.80


##------------------------------------------------------GENERACION DE LOS DIRECTORIOS------------------------------------------------##


if(os.path.isdir("%s/__RESULTADOS__"%ruta) or os.path.isdir("%s\__RESULTADOS__"%ruta) ):
	shutil.rmtree("__RESULTADOS__")
os.mkdir("__RESULTADOS__")

#posibilita aceder a directorios en SO windows o linux
def mk(path):
	try:
		os.mkdir(path)
	except:
		path2=path.replace("/","\\")
		os.mkdir(path2)	

def op(path,m):
	try:
		arx=open(path,m)		
	except:
		path2=path.replace("/","\\")
		arx=open(path2,m)		
	return arx

mk("%s/__RESULTADOS__/OBJET_ORIENTED"%ruta)
mk("%s/__RESULTADOS__/PROCEDURAL"%ruta)
mk("%s/__RESULTADOS__/OBJET_ORIENTED/CARTAS_CLASS"%ruta)
mk("%s/__RESULTADOS__/PROCEDURAL/CARTAS_STAND"%ruta)

pathC="%s/__RESULTADOS__/OBJET_ORIENTED/Lista_seleccionados.html"%ruta
pathI="%s/__RESULTADOS__/PROCEDURAL/Lista_seleccionados.html"%ruta



##--------------------------------------------------------GENERACION BASE DE DATOS INICIAL--------------------------------------##
lista=op("%s/__RESULTADOS__/Base de datos inicial.txt"%ruta,"w")


pot=[0 for v in range(0,n)]
fdp=[0 for v in range(0,n)]

for i in range(0,n):
	num=random.randrange(1.00,100.00)
	num2=num/100.00
	fdp[i]=num2
	num3=random.randrange(15,300,10)
	pot[i]=num3
	
for i in range(n):
	lista.write("nombre%s telf%s %.2f %.2f\n"%(i,i,pot[i],fdp[i]))
lista.close()


##---------------------------------------------LECTURA DE DATOS DEL ARCHIVO BASE DE DATOS INICIAL--------------------------------##

arr=op("%s/__RESULTADOS__/Base de datos inicial.txt"%ruta,"r")

lista_lineas=[0 for v in range(30)]
for i in range (0,30):
	lista_lineas[i]=arr.readline()

##--------------------------------------------------------------FUNCION COMUNES-----------------------------------------------##

## Logging y time
def time_count_logging(fun_0):
	import logging 
	logging.basicConfig(filename="%s/__RESULTADOS__/TIME_LOG.txt"%(ruta),level=logging.INFO)
	import time
	def wrapper(*args,**kwargs):
		t1=time.time()
		result=fun_0(*args,**kwargs)
		t2=time.time()-t1
		logging.info("#{} Ran with: args {}___Kwargs {}___takes {}seconds\n".format(fun_0.__name__,args,kwargs,t2))
		return result
	return wrapper


## Escribir Carta
@time_count_logging
def escribir_carta(nom_archivo,nombre,fdp,coste,tamor):
		nom_archivo.write("""<p><!DOCTYPE html></p>""")
		nom_archivo.write("""<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head>""")
		nom_archivo.write("""<p><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></p>""")
		nom_archivo.write("""<body leftmargin="30" rightmargin = "300" topmargin="60" >""")
		nom_archivo.write("""<p><div align=right>Le&oacute;n, %s </div><br><H4>Estimado Se&ntilde;or/Se&ntilde;ora:"""
                """<br></H4>Nos ponemos en contacto con usted para informarle de los  beneficios economicos que  obtendria por"""
                """ la mejora del factor de potencia de su instalacion '%s'.<br>Su f.d.p actual es %.2f para mejorarlo hasta %.2f"""
                """ con una instalacion auxiliar de condensadores o inductores, necesitaria una inversion inicial para la compra"""
                """ e instalacion de los equipos de %.2f&euro;. El tiempo de amortizacion seria de %.2f meses, teniendo en cuenta"""
                """ la cantidad mensual que ahorraria en su factura nueva con respecto a la anterior.<br><br> No tenga reparos en contactar"""
                """ con nosotros para mas detalles. <br><br><br>Reciba un cordial saludo.<br></p>"""%(date,nombre,fdp,fdpmax,coste,tamor))

## Crear Carta
@time_count_logging
def crear_cartas(path,nom_archivo,nombre,fdp,coste,tamor):	
	nom_archivo=op("%s/%s.html"%(path,nombre),"w")
	escribir_carta(nom_archivo,nombre,fdp,coste,tamor)
	nom_archivo.close()



## Open list
@time_count_logging
def crear_lista(path):
	f=op(path,"w")
	f.write("""<body leftmargin="50" rightmargin = "300" topmargin="60" >"""
                """<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>"""
                """<div align=left>Le&oacute;n, %s""" 
                """</div><br><br><table><tr><th>NOMBRE_EMPRESA_______</th><th>TELEFONO_______</th><th>"""
                """POTENCIA(KW)_______</th><th>FDP_______</th><th>COSTE(&euro;)_______</th><th>TIEMPO<br>AMORTIZACION(meses)"""
                """</th></tr>"""%date)
	f.close()

## Add costumers to list
@time_count_logging
def add_to_list(path,nombre,tel,pot,fdp,coste,tamor):
	f=op(path,"a")
	f.write("""<tr><td>%s</td><td>%s</td><td><div align=center>%.2f</div></td><td>%.2f</td>"""
        """<td>%.2f</td><td><div align=center>%.2f</div></td></tr>"""%(nombre,tel,pot,fdp,coste,tamor))
	f.close()


##--------------------------------------------------------------------IMPERATIVO---------------------------------------------##

L=[[] for v in range(len(lista_lineas))]

for i in range(len(lista_lineas)):
	for k in range(len(lista_lineas[i])): 
		
		if lista_lineas[i][k] == " ":
			nom=lista_lineas[i][0:k]
			L[i].append(nom)
			k += 1
			k2=k
			while lista_lineas[i][k] != " ":
				k += 1

		if lista_lineas[i][k] == " ":
			tlf=lista_lineas[i][k2:k]
			L[i].append(tlf)
			k += 1
			k2=k
			while lista_lineas[i][k] != " ":
				k += 1
				
		if lista_lineas[i][k] == " ":
			pot=float(lista_lineas[i][k2:k])
			L[i].append(pot)	
			k += 1
			k2=k
			while lista_lineas[i][k] != "\n":
				k += 1	
		
		if lista_lineas[i][k] == "\n":
			fdp=float(lista_lineas[i][k2:k])
			L[i].append(fdp)		
			break

#consumidores seleccionados que pueden obtener rentabilidad de la mejora de su fdp
L2=[v for v in L if (v[3] > 0.30 and v[3] < fdpmax+0.01 and v[2] > 80) ]

#coste de la instalacion en funcion de la potencia
coste=[(v[2]*fp) for v in L2]

#tiempo de amortizacion en funccion del ahorro mensual

tamor=[v/am for v in coste]

#lista de seleccionados ampliada con el coste y tiempo de amortizacion
for i in range(0,len(L2)):
	L2[i].append(coste[i])
	L2[i].append(tamor[i])

crear_lista(pathI)
for i in L2:
	add_to_list(pathI,i[0],i[1],i[2],i[3],i[4],i[5])

for i in L2:
	crear_cartas("%s/__RESULTADOS__/PROCEDURAL/CARTAS_STAND"%ruta,"f",i[0],i[3],i[4],i[5])



##--------------------------------------------------------------CLASS------------------------------------------------------##



c=[("c%s"%i) for i in range(n)]

class consumidor():
	@time_count_logging
	def __init__(self,nom,tel,pot,fdp):
		self.nom=nom
		self.tel=tel
		self.pot=pot
		self.fdp=fdp
	
	@classmethod
	@time_count_logging
	def generador_clientes(cls,string):
		string=string.replace("\n","")
		nom,tel,pot,fdp=string.split(" ")
		return cls(nom,tel,float(pot),float(fdp))

#Ejecucion del metodo para agregar los clientes como objetos a la clase
for i in range(n):
	c[i]=consumidor.generador_clientes(lista_lineas[i])

#subclase con los clientes seleccionados y calculo del coste y tiempo amortizacion
crear_lista(pathC)
class consumidores_seleccionados(consumidor):
	@time_count_logging
	def __init__(self,nom,tel,pot,fdp):
		consumidor.__init__(self,nom,tel,pot,fdp)
		self.coste=float(self.pot)*fp
		self.tamor=float(self.coste)/am
		add_to_list(pathC,self.nom,self.tel,self.pot,self.fdp,self.coste,self.tamor)
		crear_cartas("%s/__RESULTADOS__/OBJET_ORIENTED/CARTAS_CLASS"%ruta,"f",self.nom,self.fdp,self.coste,self.tamor)

	@staticmethod
	@time_count_logging
	def seleccion():
		for i in range(len(c)):
			if (c[i].fdp > 0.30 and c[i].fdp < fdpmax+0.01 and c[i].pot > 80.00):
		 		c[i]=consumidores_seleccionados(c[i].nom,c[i].tel,float(c[i].pot),float(c[i].fdp))

#ejecucion del metodo para agregar los clientes con fdp deseado como objetos a la clase
consumidores_seleccionados.seleccion()


print("**************************************************************************************************************************************")
print ('\nEn la carpeta RESULTADOS ubicada en %s encontrara el archivo txt con la lista total de clientes' 
       ' y un archivo html con los datos de los clientes seleccionados y una carpeta CARTAS con la carta de'
       ' notificacin generada para cada cliente'%ruta)
print("\n**************************************************************************************************************************************")



#print (lista_lineas)






	



