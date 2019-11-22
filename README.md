# Simple guillotina server

This is an exampe of how simple it is to define and start a server
application on top of guillotina.


## To download and install

``` shell
git clone git@github.com:lferran/guillotina-simpleserver.git
cd guillotina-simpleserver
pip install -e .
```

## Run the server

``` shell
g -c config.json
```

And then you already have the new `GET /@double/{value}` service available:

``` shell
curl -XGET "http://localhost:8080/@double/3"                               ~
{"value": 6}
```

## To run the tests

``` shell
pip install -e '.[test]'
pytest tests
```
