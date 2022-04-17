# Ice Hello World

To build the docker image, run:
```
docker build . -t ice-latest
```

To run docker interactively and test, run:
```
docker run -it -v --rm ice-latest /bin/bash
```

Inside the docker image, run:
```
python server.py &
python client.py
```

The expected output is:
```
Reply from server: Hello World!

```
