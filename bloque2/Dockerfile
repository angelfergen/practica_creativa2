FROM python:3.7
RUN git clone https://github.com/angelfergen/practica2_bloqueX.git
WORKDIR practica2_bloqueX
ENV GROUP_NUMBER 'Grupo 02'
RUN pip3 install -r practica2_bloqueX/bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "practica2_bloqueX/bookinfo/src/productpage/productpage_monolith.py", "9080"]
