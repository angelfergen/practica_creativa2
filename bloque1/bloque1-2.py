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
call(["export GROUP_NUMBER=02"],shell=True)
call(["echo ${GROUP_NUMBER}"],shell=True)
call(["python3 -m venv cdps-c2-env"],shell=True)
call(["source cdps-c2-env/bin/activate"],shell=True)
call(["pip3 install -r practica2_bloque1/bookinfo/src/productpage/requirements.txt"],shell=True) #-r obliga a sobreescribir al copiar
call(["pip3 install --upgrade requests"], shell=True)
call(["sudo apt-get update"], shell=True)

print("------------------HOLAAAAAAAAAAA todo instalado------------------")

call(["sudo python3 practica2_bloque1/bookinfo/src/productpage/productpage_monolith.py 9080"],shell=True)





