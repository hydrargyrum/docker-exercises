## Start container with persistence

On the host:

```shell
mkdir /tmp/test-persistence
docker run -it -v /tmp/test-persistence:/host debian:stable
```

## Create file within container

In container:

```shell
echo 42 > /host/foo
exit
```

## Check file exists on host

On host:

```shell
cat /tmp/test-persistence/foo
```
