from io import open
import numpy as np
import subprocess
import matplotlib.pyplot as plt

#funcion para escribir los datos a un fichero llamado datosint.txt
def datos (E,R,C,T):
	
	escribir=open("datosint.txt","w")
	datos=""+E+"\n"+R+"\n"+C+"\n"+T
	escribir.write(datos)
	escribir.close()
#funcion que Grafica la Corriente 
def grafic():
	#obtiene el tiempo del archivoint.txt
	tiem=open("datosint.txt","r")
	tq=tiem.readlines()
	#t1 es la variable donde guardo el tiempo
	t1=tq[3]
	tiem.close()
	#subprocess arranca un script para ejecutar la funciones de haskell que crean el archvio DatosGraficarI.txt
	subprocess.run(['bash','graficadora_C'])
	#Lee el archvio DatosGraficarI.txt y lo guarda en una lista que tiene por nombre texto
	archivo_text=open("DatosGraficarI.txt","r")
	texto=archivo_text.readlines()
	
	#la variable mat es la lista que con el for me pasa los datos de la lista texto que son String a Float
 
	mat=[None]*50
	t=0
	for i in texto:
		mat[t]=float(i)
		t=t+1

	
	archivo_text.close()
	gg=0
	#Ve si el tiempo es entero o un float para poder combertirlo
	for i in t1:
		if i==".":
			gg=1
	#condicion para elegir si es float o sino a un entero
	if gg==1:
		T1=float(t1)
	else:
		T1=int(t1)
	print(T1)
	#t es la lista de 0 al tiempo que se tiene que graficar
	t=np.linspace(0,T1)
	#le da las propiedades al objeto plt que es el de la grafica de matplolib como el tiempo que es el eje X y la lista mat es el eje Y
	plt.plot(t,mat,'b.-')
	plt.grid(True)
	#se le coloca el titulo que va a tener el eje X
	plt.xlabel('Tiempo (s)')
	#se le coloca el titulo que va a tener el eje Y
	plt.ylabel('Corriente (A)')
	#el titulo de la grafica
	plt.title('Comportamiento de la Corriente del Capacitor')
	#donde me muestra la grafica
	plt.show()
	

if __name__ == '__main__':
	grafic()
  
	
    






































































































































