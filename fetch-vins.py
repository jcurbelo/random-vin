import requests
import json

BASE_URL = 'http://randomvin.com/getvin.php?type=real'
COUNT = 100


def main():
    print('making {} requests...'.format(COUNT))
    vins = []
    failed_attempts = 0
    for i in range(COUNT):
        try:
            print('request {} of {}.'.format(i + 1, COUNT))
            r = requests.get(BASE_URL)
            if r and r.text:
                vins.append(r.text)
                print('fetched VIN: {}.'.format(r.text))
        except Exception as e:
            print('error:', str(e))
            failed_attempts += 1

    print('{} successful attempts'.format(len(vins)))
    print('{} failed attempts'.format(len(vins)))
    print('saving to file...')
    with open('vins.json', 'w') as f:
        json.dump(vins, f)
    print('done!')


main()
