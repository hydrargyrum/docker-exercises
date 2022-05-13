#### solution

Hôte :

```shell=
docker build -t mywsgi .
docker run -p 5678:8080 mywsgi
```

Hôte :

    curl http://localhost:5678

