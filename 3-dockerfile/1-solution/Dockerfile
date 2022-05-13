FROM mariadb

ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes

COPY myprovision.sql /docker-entrypoint-initdb.d
