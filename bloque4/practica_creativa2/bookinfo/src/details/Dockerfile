FROM ruby:2.7.1-slim
COPY details.rb /opt/microservices/
WORKDIR /opt/microservices/
#Aqui faltan los ARG que son los que van a ser llamados en las llamada del DockerCompose
ARG service_version
ARG enable_external_book_service
#Ahora vamos a especificar el valor de las variables de entorno
ENV SERVICE_VERSION ${service_version:-v1}
ENV ENABLE_EXTERNAL_BOOK_SERVICE ${enable_external_book_service:-true}
#Estas variables, las hemos rellenado de esta manera para que se vayan escribiendo en el DockerCompose
EXPOSE 9080
CMD ["ruby", "details.rb", "9080"]
