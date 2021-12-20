FROM python:3.8.8-buster

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

RUN apt-get update && apt-get install -y nginx supervisor netcat libc6-dev
RUN apt-get -y --purge autoremove && apt-get -y clean && rm -rf /var/lib/apt/lists/*

COPY custom/profiler.conf /etc/nginx/sites-available/
COPY custom/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/profiler.conf /etc/nginx/sites-enabled/profiler.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf && chown -R www-data:www-data /var/log

WORKDIR /var/www/

COPY requirements.txt /var/www/requirements.txt

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 5000 9001

ENTRYPOINT ["sh", "./entrypoint.sh"]