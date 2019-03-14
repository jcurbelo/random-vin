# Random VIN Barcodes Generator

A simple python script that fetches __real__ VIN numbers from [randomvin.com](http://randomvin.com/) and generates barcodes with [python-barcodes](https://github.com/WhyNotHugo/python-barcode).

## How to use it

Use [pipenv](https://pipenv.readthedocs.io/en/latest/) for install all project's dependencies.

```bash
# install all dependencies
$ pipenv install

# fetch real VIN numbers
$ python fetch-vins.py

# generate barcodes in SVG format
$ python generate.py
```

Enjoy it!