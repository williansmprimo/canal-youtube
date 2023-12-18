FROM node:21 as build 

WORKDIR /usr/local/app

COPY . .

RUN npm install

RUN npm run build

FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html

COPY --from=build /usr/local/app/dist/cadastro/browser .

EXPOSE 8081

CMD nginx -g 'daemon off;'
