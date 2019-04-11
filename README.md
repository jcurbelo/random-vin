# Random VIN Barcodes Generator

A simple python script that fetches __real__ VIN numbers from [randomvin.com](http://randomvin.com/) and then generates an HTML page with their barcodes representation using [TEC-IT](https://www.tec-it.com).

## How to use it

Use [pipenv](https://pipenv.readthedocs.io/en/latest/) to install all project's dependencies.

```bash
# install all dependencies
$ pipenv install

# fetch real VIN numbers
$ python fetch-vins.py

# generate HTML page with barcodes as <img>
$ python generate.py
```

Enjoy it!