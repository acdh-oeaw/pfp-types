FROM nginx
RUN sed -i 's/80;/5000;/g' /etc/nginx/conf.d/default.conf
COPY html /usr/share/nginx/html
