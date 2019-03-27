FROM python:3.6.8

EXPOSE 8000
EXPOSE 80

RUN apt-get update -y && \
    apt-get install -y nginx gettext \
    build-essential binutils-doc \
    autoconf flex bison libjpeg-dev \
    libfreetype6-dev zlib1g-dev libzmq3-dev \
    libgdbm-dev libncurses5-dev \
    automake libtool libffi-dev curl git tmux

ADD front/ /taiga-front/

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/taiga.conf /etc/nginx/conf.d/default.conf

WORKDIR /taiga

ADD backend/requirements.txt /taiga/

RUN pip install -r requirements.txt && pip install gunicorn

ADD ./backend/ /taiga/

COPY ./docker-settings.py /taiga/settings/local.py
COPY ./conf-front.json ./taiga-front/dist/conf.json

ENTRYPOINT ["/taiga/docker-entrypoint.sh"]

CMD gunicorn taiga.wsgi:application --bind 0.0.0.0:8000

