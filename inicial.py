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

#---------------------------------CREACION_DIRECTORIOS------------------------------------------------------------##



if(os.path.isdir("%s/__RESULTADOS__INICIAL"%ruta) or os.path.isdir("%s\__RESULTADOS__INICIAL"%ruta) ):
	shutil.rmtree("__RESULTADOS__INICIAL")


if(os.path.isdir("%s/__RESULTADOS__OBJECT"%ruta) or os.path.isdir("%s\__RESULTADOS__OBJECT"%ruta) ):
	shutil.rmtree("__RESULTADOS__OBJECT")



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


if __name__ == "__main__":
	mk("__RESULTADOS__INICIAL")
	mk("%s/__RESULTADOS__INICIAL/CARTAS_INICIAL"%ruta)

else:
	mk("__RESULTADOS__OBJECT")
	mk("%s/__RESULTADOS__OBJECT/CARTAS__OBJECT"%ruta)


#---------------------------------CREACION_ARCHIVO_BASE_DATOS------------------------------------------------------##

def baase_datos_txt(path, mode):
	lista=op(path,mode)

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



#-----------------------------------LECTURA_DE_DATOS---------------------------------------------------------------##

def lista_listas(path,mode):

	arr=op(path,mode)

	lista_lineas=[0 for v in range(30)]
	for i in range (0,30):
		lista_lineas[i]=arr.readline()
	return lista_lineas





#-----------------------------------FUNCIONES_COMUNES--------------------------------------------------------------##

## Logging y time
def time_count_logging(fun_0,):
	import logging 
	if __name__ == "__main__":
		logging.basicConfig(filename="%s/__RESULTADOS__INICIAL/logging_profiling.txt"%ruta,level=logging.INFO)
	else:
		logging.basicConfig(filename="%s/__RESULTADOS__OBJECT/logging_profiling.txt"%ruta,level=logging.INFO)
	import time
	def wrapper(*args,**kwargs):
		t1=time.time()
		result=fun_0(*args,**kwargs)
		t2=time.time()-t1
		logging.info("#{} Ran with: args {}___Kwargs \n {}___takes {}seconds\n".format(fun_0.__name__,args,
		kwargs,t2))
		return result
	return wrapper


## Escribir Carta
def escribir_carta(fl,nombre,fdp,coste,tamor):
		fl.write("""<p><!DOCTYPE html></p>""")
		fl.write("""<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head>""")
		fl.write("""<p><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></p>""")
		fl.write("""<body leftmargin="30" rightmargin = "300" topmargin="60" >""")
		fl.write("""<p><div align=right>Le&oacute;n, %s </div><br><H4>Estimado Se&ntilde;or/Se&ntilde;ora:"""
	        """<br></H4>Nos ponemos en contacto con usted para informarle de los  beneficios economicos que  """
		"""obtendria por la mejora del factor de potencia de su instalacion '%s'.<br>Su f.d.p actual es"""
		""" %.2f para mejorarlo hasta 0.95 con la instalacion de una bateria condensadores, """
		"""necesitaria una inversion inicial para la compra e instalacion de los equipos de %.2f&euro;."""
		""" El tiempo de amortizacion seria de %.2f meses, teniendo en cuenta la cantidad mensual que"""
		""" ahorraria en su factura nueva con respecto a la anterior.<br><br> No tenga reparos"""
		""" en contactar con nosotros para mas detalles. <br><br><br>Reciba un cordial saludo.<br></p>"""
		%(date,nombre,fdp,coste,tamor))

## Crear Carta
def crear_cartas(path,fl,nombre,fdp,coste,tamor):	
	fl=op("%s/%s.html"%(path,nombre),"w")
	escribir_carta(fl,nombre,fdp,coste,tamor)
	fl.close()



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






def main():


	#mk("__RESULTADOS__INICIAL")
	#mk("%s/__RESULTADOS__INICIAL/CARTAS_INICIAL"%ruta)
	baase_datos_txt("%s/__RESULTADOS__INICIAL/Base de datos inicial.txt"%ruta,"w")
	lista_lineas=lista_listas("%s/__RESULTADOS__INICIAL/Base de datos inicial.txt"%ruta,"r")






#------------------------------GENERACION DE LISTA DE SELECCIONADOS Y CARTAS----------- ---------------------------##

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


#craccion lista
	pathI="%s/__RESULTADOS__INICIAL/Lista_seleccionados.html"%ruta
	crear_lista(pathI)
	for i in L2:
		add_to_list(pathI,i[0],i[1],i[2],i[3],i[4],i[5])


#creaccion cartas
	for i in L2:
		crear_cartas("%s/__RESULTADOS__INICIAL/CARTAS_INICIAL"%ruta,"f",i[0],i[3],i[4],i[5])



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


if __name__ == "__main__":
	main()


