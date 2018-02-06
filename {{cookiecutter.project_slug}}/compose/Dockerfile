FROM alpine:latest

ENV PYTHONUNBUFFERED 1

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
  && apk --no-cache --update add python3 py3-psycopg2 \
  && cd /usr/bin/ \
  && ln -s pydoc3 pydoc \
  && ln -s python3 python \
  && ln -s pip3 pip

# alpine linux 添加用户和组的命令略有不同 See: https://github.com/mhart/alpine-node/issues/48
RUN addgroup -S django \
    && adduser -S -g django django

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com\
    && rm -rf /requirements

COPY ./compose/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh
RUN chown django /gunicorn.sh

COPY ./compose/start-celeryworker.sh /start-celeryworker.sh
RUN sed -i 's/\r//' /start-celeryworker.sh
RUN chmod +x /start-celeryworker.sh

COPY ./compose/start-celerybeat.sh /start-celerybeat.sh
RUN sed -i 's/\r//' /start-celerybeat.sh
RUN chmod +x /start-celerybeat.sh

COPY ./compose/start-flower.sh /start-flower.sh
RUN sed -i 's/\r//' /start-flower.sh
RUN chmod +x /start-flower.sh

COPY . /code

RUN chown -R django /code

USER django

WORKDIR /code

CMD ["/gunicorn.sh"]