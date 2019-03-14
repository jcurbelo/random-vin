import json
from barcode import generate

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
	<title>VINs</title>
</head>
<body>
{}
</body>
</html>
"""


def main():
    try:
        with open('vins.json', 'r') as f:
            img_html_tags = []
            vins = json.load(f)
        for vin in vins:
            name = generate('CODE39', vin, output='barcodes/{}'.format(vin))
            img_html_tags.append('<img src="{0}" alt={0}/>'.format(name))
    except FileNotFoundError:
        print('"vins.json" file not found.')

    # generates html
    output = HTML_TEMPLATE.format(''.join(img_html_tags))
    # writes html file
    with open('index.html', 'w') as f:
        f.write(output)


main()
