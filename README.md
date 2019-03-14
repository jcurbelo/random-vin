# Random VIN Barcodes generator

A simple python script that fetches __real__ VIN numbers from [randomvin.com](http://randomvin.com/) and generates barcodes with [python-barcodes](https://github.com/WhyNotHugo/python-barcode).

## How to use it

Use [pipenv](https://pipenv.readthedocs.io/en/latest/) for install all project's dependencies.

```bash
# installs all dependencies
$ pipenv install

# fetches real VIN numbers
$ python fetch-vins.py

# generates barcodes in SVG
$ python generate.py
```

Enjoy it!