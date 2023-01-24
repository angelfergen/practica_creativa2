FROM python:3.7
RUN git clone https://github.com/angelfergen/practica2_bloqueX.git
WORKDIR practica2_bloqueX
ENV GROUP_NUMBER 'Grupo 02'
RUN pip3 install -r ./bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "./bookinfo/src/productpage/productpage.py", "9080"]
