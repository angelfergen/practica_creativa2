FROM node:12.18.1-slim #Imagen base a utilizar
#RUN git clone https://github.com/angelfergen/practica_creativa2
COPY package.json /opt/microservices/
COPY ratings.js /opt/microservices/
WORKDIR /opt/microservices/
ARG service_version
ENV SERVICE_VERSION ${service_version:-v1}
RUN npm install #Para instalar las dependencias de node
EXPOSE 9080
CMD ["node", "ratings.js", "9080"]
