
## Run the detached container with a volume

Host:

```shell
container=$(docker run -d -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -v /tmp/test-persistence:/var/lib/mysql mariadb)
```

## Attach to the container to start a mariadb client

Host:

```
docker ps
docker exec -it "$container" mariadb
```

MariaDB shell:

```sql
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE tab (col TEXT);
INSERT INTO tab(col) VALUES("foo bar");
QUIT;
```

## Stop the container

Host:

```
docker ps
docker stop "$container"
```

## Start a new container

Host:

```
container=$(docker run -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -v /tmp/test-persistence:/var/lib/mysql mariadb)
```

## Attach again to check if table still exists

Host:

```
docker exec -it "$container" mariadb mydb --execute='SELECT * FROM tab'
```

## Stop the container

Host:

```
docker ps
docker stop "$container"
```
