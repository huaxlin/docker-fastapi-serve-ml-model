# docker-fastapi-serve-ml-model

## Usage Guide

### Create a ML model from scratch

> the `music_recommender` demo reference to:
> 
> [🎞 Python Machine Learning Tutorial (Data Science)](https://youtu.be/7eh4d6sabA0)

#### create ML development docker image

build ML development docker image:

```shell
$ docker build -t music-recommender:dev-python3.9 -f Dockerfile.dev .
```

#### developing a ML model

##### run ML development docker image

```shell
$ docker run -d --rm --name music-recommender-dev \
  -v $PWD/venv39:/venv39 \
  -v $PWD:/code \
  music-recommender:dev-python3.9
b8fefb7fca0d...
$ docker exec -ti b8fefb7fca0d bash
root@b8fefb7fca0d:/code#
```

##### prepare ML development (python)environment

create python environment:

```shell
root@b8fefb7fca0d:/code# python -m venv --copies --system-site-packages /venv39
...
```

setup python environment for ML development:

```shell
root@b8fefb7fca0d:/code# /venv39/bin/python -m pip install -r requirements.txt
...
root@b8fefb7fca0d:/code#
root@b8fefb7fca0d:/code# source /venv39/bin/activate
(venv39) root@b8fefb7fca0d:/code#
```

##### tran ML model

```shell
(venv39) root@b8fefb7fca0d:/code# python -m music_recommender.train
(venv39) root@b8fefb7fca0d:/code# ls -alFht
-rw-r--r-- 1 root root 2.6K Dec 12 11:47 music_recommender.joblib
...
```

##### test ML model

```shell
(venv39) root@b8fefb7fca0d:/code# python -m music_recommender.test
metrics = {'accuracy': 1.0}
```

#### using ML model to make prediction

```shell
(venv39) root@b8fefb7fca0d:/code# echo -n '{"age": 10, "gender": 1}' |
  python -m music_recommender
{'class': 'HipHop'}
```

### Serving the prediction ML model with FastAPI

#### create service docker image

build service docker image:

```shell
$ docker build -t music_recommender:prd-2022-12-12 -f Dockerfile.service .
```

#### serve ML model

run service docker image:

```shell
$ docker run -d --name serve-ml-model-with-fastapi \
  -p 8080:8080 \
  music_recommender:prd-2022-12-12
dfd48661c592...
```

> stop service and remove it:
> 
> ```shell
> $ docker stop dfd48661c592
> $ docker rm dfd48661c592
> ```

#### validate prediction server

```shell
$ echo -n '{"age": 10, "gender": 0}' | http POST localhost:8080/predict
HTTP/1.1 200 OK
content-length: 17
content-type: application/json
date: Mon, 12 Dec 2022 06:03:29 GMT
server: uvicorn

{
    "class": "Dance"
}
```

> install `http` command by: `pip install httpie`

