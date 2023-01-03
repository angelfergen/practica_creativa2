FROM ruby:2.7.1-slim
#RUN git clone https://github.com/angelfergen/practica_creativa2
COPY details.rb /opt/microservices/
WORKDIR /opt/microservices/
#Aqui faltan los ARG que son los que van a ser llamados en las llamada del DockerCompose
ARG service_version
ARG enable_external_book_service
#Ahora vamos a especificar el valor de las variables de entorno
ENV SERVICE_VERSION ${service_version:-v1}
ENV ENABLE_EXTERNAL_BOOK_SERVICE ${enable_external_book_service:-true}
#Estas variables, las hemos rellenado de esta manera para que se vayan escribiendo en el DockerCompose
#Tenemos duda, no sabemos si se puede escribir así:
#ENV SERVICE_VERSION 'v1'
#ENV ENABLE_EXTERNAL_BOOK_SERVICE 'true'
#RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["ruby", "details.rb", "9080"]
