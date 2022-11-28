FROM nginx:alpine

COPY src/ /usr/share/nginx/html/
COPY docker/server/api/ /usr/share/nginx/server/api/
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
