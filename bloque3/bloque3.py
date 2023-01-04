import sys
import os
import json
from subprocess import call
#Está sin terminar esta vaina
#REVIEWS VERSION 1

call(["pwd"])   #Esto se usa para llamar a la base de datos con las contraseñas que se necesita para la siguiente linea
call(["docker run --rm -u root -v " + r' " ' + "$(pwd)"+ r' " ' + ":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"],shell=True)
    #EL raw, lo he hecho para poder poner las comillas de $(pwd)

#REVIEWS VERSION 2
call(["pwd"])
call(["docker run --rm -u root -v " + r' " ' + "$(pwd)"+ r' " ' + ":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"],shell=True)
    #EL raw, lo he hecho para poder poner las comillas de $(pwd)

#REVIEWS VERSION 3
call(["pwd"])
call(["docker run --rm -u root -v " + r' " ' + "$(pwd)"+ r' " ' + ":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"],shell=True)
    #EL raw, lo he hecho para poder poner las comillas de $(pwd)

