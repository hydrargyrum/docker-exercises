
## Start container

Host:

```shell
container=$(docker run -d -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -p 1234:3306 mariadb)
echo "$container"
docker ps
```

## Run client

Host:

```shell
mariadb --protocol=tcp --user=root --port=1234
```

MariaDB shell:

```sql
CREATE DATABASE mydb;
QUIT;
```

## Stop container

Host:

```shell
docker ps
docker container stop "$container"
```
