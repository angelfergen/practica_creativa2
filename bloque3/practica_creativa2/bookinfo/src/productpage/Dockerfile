FROM python:3.7
RUN git clone https://github.com/angelfergen/practica2_bloqueX.git
WORKDIR practica2_bloqueX
ARG GROUP_NUMBER
ENV GROUP_NUMBER 'Grupo 02'
RUN pip3 install -r practica2_bloqueX/bookinfo/src/productpage/requirements.txt
#RUN sed -i 's/texto_a_buscar/texto_a_reemplazar/g' fichero_a_reemplazar
RUN sed -i 's/Simple Bookstore App/Simple Book Store Grupo 02/g' practica2_bloqueX/bookinfo/src/productpage/templates/productpage.html
RUN sed -i 's/{{ product.title }}/{{ product.title }} Grupo 02/g' practica2_bloqueX/bookinfo/src/productpage/templates/productpage.html
EXPOSE 9080
CMD ["python3", "practica2_bloqueX/bookinfo/src/productpage/productpage.py", "9080"]
