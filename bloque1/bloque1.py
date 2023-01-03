#Ángel Fernández-Getino, Ana Garcia, Abril Ontoria 

import sys
import json
import time
from subprocess import call
call(["sudo apt-get update"], shell=True)
#call(["echo 'y' | sudo apt-get update"], shell=True) #El eco para el mensaje por pantalla
call(["sudo apt install python3-pip"], shell=True)	#Para poder usar pip (install)
#call(["echo 'y' | sudo apt install python3-pip"], shell=True) #El eco para el mensaje por pantalla
call(["git clone https://github.com/CDPS-ETSIT/practica_creativa2.git"], shell=True)
#---------------------------------------------------------
call(["sudo pip3 install urllib3"], shell=True)
call(["sudo pip3 install flask_bootstrap"], shell=True)
call(["sudo pip3 install chardet"], shell=True)
call(["sudo pip3 install jaeger_client"], shell=True)
call(["sudo pip3 install opentracing_instrumentation"], shell=True)
call(["sudo pip3 install json2html"], shell=True)
#-----------------------------------------------------------
call(["pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt"],shell=True) #-r obliga a sobreescribir al copiar
call(["pip3 install --upgrade requests"], shell=True)
call(["sudo apt-get update"], shell=True)

print("------------------HOLAAAAAAAAAAA todo instalado------------------")

#Nos ponemos a modificar lo del group_number
fin = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", 'r') # in file
fout = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py", 'w') # out file
for line in fin:
  if "reviewsHostname = "+r'"'+"reviews"+r'"'+" if (os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+") is None) else os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+")" in line :
   fout.write(line+ "\nos.environ['GROUP_NUMBER']="+r'"'+"Equipo 47"+r'"'+" \n")
  elif "'title': 'The Comedy of Errors'," in line :
    fout.write("'title': 'The Comedy of Errors ' +os.environ['GROUP_NUMBER'],")
  elif "'author': book['authors'][0]," in line :
    fout.write(line + "        'equipo' : os.environ['GROUP_NUMBER'],\n")
  else:
   fout.write(line)
fin.close()
fout.close()
               
call(["sudo","cp","practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py","practica_creativa2/bookinfo/src/productpage/productpage_monolith.py"])
call(["sudo","rm","practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py"])
 

#-------------------------------------------------------------------------------

#Nos ponemos a modificar el titulo del html
fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html",'r')
fout = open("practica_creativa2/bookinfo/src/productpage/templates/productpage2.html",'w')

for line in fin:
	if "{% block title %}Simple Bookstore App{% endblock %}" in line:
	#r, raw para poner caracteres tal cual
	
		fout.write("{% block title %}Simple Bookstore App{{details.equipo}}{% endblock %}")
	
	else:
		fout.write(line)
fin.close()
fout.close()

call(["sudo cp practica_creativa2/bookinfo/src/productpage/templates/productpage2.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html"], shell= True)
call(["sudo rm practica_creativa2/bookinfo/src/productpage/templates/productpage2.html"], shell= True)

call(["sudo python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080"],shell=True)





