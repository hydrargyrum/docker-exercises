FROM debian:stable

RUN apt-get update
RUN apt-get install --no-install-recommends --yes python3-bottle
COPY hello.wsgi /

CMD python3 /hello.wsgi

EXPOSE 8080
