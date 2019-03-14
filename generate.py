import json
from barcode import generate


def main():
    try:
        with open('vins.json', 'r') as f:
            vins = json.load(f)
        for vin in vins:
            generate('CODE39', vin, output='barcodes/{}'.format(vin))
    except FileNotFoundError:
        print('"vins.json" file not found.')


main()
