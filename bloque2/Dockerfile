FROM python:3.7
RUN git clone https://github.com/angelfergen/practica_creativa2
WORKDIR practica_creativa2
ENV GROUP_NUMBER 'Grupo 02'
RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"]
