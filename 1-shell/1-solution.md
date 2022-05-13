## Start container

Run on host:

```shell
docker run -it debian:oldstable
```

## Check content, create a file, exit

Run in container:

```shell
cat /etc/debian_version
echo foo > /foo
exit
```

## Start container

Run:

```shell
docker run -it debian:oldstable
```

## Verify file was lost

Run in container:

```shell
cat /foo
```
