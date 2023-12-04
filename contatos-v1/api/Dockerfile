FROM node:21

# Cria diretorio
WORKDIR api-contados/usr/src/app

COPY ./package*.json ./

RUN npm install

#Copia arquivos de instalaç"ao
COPY ./ .

# Define porta
EXPOSE 3000

#Comando para iniciar servidor
CMD [ "node", "index.js" ]
