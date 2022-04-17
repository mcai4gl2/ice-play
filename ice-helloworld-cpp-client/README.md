# Ice Hello World C++ Client and Python Server

To build the docker image, run:
```
docker build . -t ice-latest
```

To run docker interactively and test, run:
```
docker run -it -v --rm ice-latest /bin/bash
```

Or use the pre-built image:
```
docker run -it -v --rm mcai4gl2/ice-helloworld-cpp-client:latest /bin/bash
```

Inside the docker image, run:
```
python server.py &
./client
```

The expected output is:
```
Reply from server: Hello test

```
