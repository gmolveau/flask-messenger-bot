FROM alpine

RUN apk update && \
    apk add --no-cache python3 && \
    mkdir /flask_app

ADD . /flask_app
WORKDIR /flask_app
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["/usr/bin/gunicorn", "/flask_app/app:app"]
