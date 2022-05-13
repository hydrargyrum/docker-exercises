
## Provision file

```shell
cat > myprovision.sql << EOF
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE tab (col TEXT);
INSERT INTO tab(col) VALUES("foo bar");
EOF
```

## Write Dockerfile

Host:

```shell
cat > Dockerfile << EOF
FROM mariadb

ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes

COPY myprovision.sql /docker-entrypoint-initdb.d
EOF
```

## Build image and run container

Host:

```
docker build -t mymaria .
container=$(docker run -d mymaria)
```

## Verify provisioned data was loaded

Host:

```shell
docker exec -it "$container" mariadb --protocol=tcp --user=root --port=1234 mydb --execute='SELECT * FROM tab'
```
