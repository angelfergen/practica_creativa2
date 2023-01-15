FROM python:3.7
RUN git clone https://github.com/angelfergen/practica2_bloque1.git
WORKDIR practica2_bloque1
ENV GROUP_NUMBER 'Grupo 02'
RUN pip3 install -r ./bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "./bookinfo/src/productpage/productpage.py", "9080"]
