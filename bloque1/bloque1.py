#Ángel Fernández-Getino, Ana Garcia, Abril Ontoria 

import sys
import json
import time
from subprocess import call
call(["sudo apt-get update"], shell=True)
#call(["echo 'y' | sudo apt-get update"], shell=True) #El eco para el mensaje por pantalla
call(["sudo apt install python3-pip"], shell=True)	#Para poder usar pip (install)
#call(["echo 'y' | sudo apt install python3-pip"], shell=True) #El eco para el mensaje por pantalla
call(["git clone https://github.com/angelfergen/practica2_bloque1.git"], shell=True)
#python3 -m pip= pip3

call(["pip3 install -r practica2_bloque1/bookinfo/src/productpage/requirements.txt"],shell=True) #-r obliga a sobreescribir al copiar
call(["pip3 install --upgrade requests"], shell=True)
call(["sudo apt-get update"], shell=True)

print("------------------HOLAAAAAAAAAAA todo instalado------------------")

#Nos ponemos a modificar lo del group_number
fin = open("practica2_bloque1/bookinfo/src/productpage/productpage_monolith.py",'r')
fout = open("practica2_bloque1/bookinfo/src/productpage/productpage_monolith2.py",'w')

for line in fin:

#     |--------NOTA TEORICA---------------------------------------------------------------------------------------------|
#     |	os.getenv() does not raise an exception, but returns None					            						|
#     |	os.environ.get() similarly returns None							                                                |
#     |	os.environ[] raises an exception if the environmental variable does not exist	               			        |
#     |-----------------------------------------------------------------------------------------------------------------|

	if "reviewsHostname = "+r'"'+"reviews"+r'"'+" if (os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+") is None) else os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+")" in line :
	#r, raw para poner caracteres tal cual
		fout.write(line+ "\nos.environ['GROUP_NUMBER']="+r'"'+"Equipo 02"+r'"'+" \n")
		#Lo que hace es sacar del entorno la variable group number y se sustituye por Equipo 02. Para modifcar sacandola del entorno es \os.environ[]
	#reviewsHostname = "reviews" if (os.environ.get("REVIEWS_HOSTNAME") is None) else os.environ.get("REVIEWS_HOSTNAME"), linea 62 de github, no tiene sentido cambiar ni el service, ni el detail ni el rating
	elif "'title': 'The Comedy of Errors'," in line :
    		fout.write("'title': 'The Comedy of Errors ' + os.environ['GROUP_NUMBER'],")
		#OJO QUE NO SE SI TENEMOS QUE USAR LO DEL RAW
		#Tenemos que cambiar el nombre del autor????Si, para hacer el titulo del equipo
	elif "'author': book['authors'][0]," in line :
    		fout.write(line + "        'equipo' : os.environ['GROUP_NUMBER'],\n")		
	else:
		fout.write(line)
fin.close()
fout.close()

call(["sudo cp practica2_bloque1/bookinfo/src/productpage/productpage_monolith2.py practica_creativa2/bookinfo/src/productpage/productpage_monolith.py"], shell= True)
call(["sudo rm practica2_bloque1/bookinfo/src/productpage/productpage_monolith2.py"], shell= True)

#-------------------------------------------------------------------------------

#Nos ponemos a modificar el titulo del html
fin = open("practica2_bloque1/bookinfo/src/productpage/templates/productpage.html",'r')
fout = open("practica2_bloque1/bookinfo/src/productpage/templates/productpage2.html",'w')

for line in fin:
	if "{% block title %}Simple Bookstore App{% endblock %}" in line:
	#r, raw para poner caracteres tal cual
	
		fout.write("{% block title %}Simple Bookstore App{{details.equipo}}{% endblock %}")
	
	else:
		fout.write(line)
fin.close()
fout.close()

call(["sudo cp practica2_bloque1/bookinfo/src/productpage/templates/productpage2.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html"], shell= True)
call(["sudo rm practica2_bloque1/bookinfo/src/productpage/templates/productpage2.html"], shell= True)

call(["sudo python3 practica2_bloque1/bookinfo/src/productpage/productpage_monolith.py 9080"],shell=True)
