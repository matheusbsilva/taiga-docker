FROM python:3.6.8

EXPOSE 8000

RUN apt-get update -y && \
    apt-get install -y nginx 

ADD front/ /taiga-front/

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/taiga.conf /etc/nginx/conf.d/default.conf

WORKDIR /taiga

ADD backend/requirements.txt /taiga/

RUN pip install -r requirements.txt

ADD ./backend/ /taiga/

ENTRYPOINT ["/taiga/docker-entrypoint.sh"]
