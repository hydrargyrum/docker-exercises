
## Start detached container

Host:

```shell
container=$(docker run -d -e MYSQL_ALLOW_EMPTY_PASSWORD=yes mariadb)
```

## Attach to container, run a mariadb client

Host:

```shell
docker ps
echo "$container"
docker exec -it "$container" mariadb
```

Mysql shell:

```sql
CREATE DATABASE mydb;
QUIT;
```

## Stop container

Host:

```shell
docker container stop "$container"
```
