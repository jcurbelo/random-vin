import json

IMG_BASE_URL = 'https://barcode.tec-it.com/barcode.ashx?data={}&code=Code39&dpi=96&dataseparator='

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>

<head>
	<title>VINs</title>
	<style>
		img {{
			margin: 10px;
			width: 100%;
			max-width: 250px;
		}}
	</style>
</head>

<body>
	{}
	<footer>
		<a href='https://www.tec-it.com' title='Barcode Software by TEC-IT'>
			Barcode generated with TEC-IT Barcode Software
		</a>
	</footer>
</body>

</html>
"""


def main():
    try:
        print('parsing "vins.json".')
        with open('vins.json', 'r') as f:
            img_html_tags = []
            vins = json.load(f)
            for vin in vins:
                img_link = IMG_BASE_URL.format(vin)
                img_html_tags.append(
                    '<img src="{}" alt="Barcode Generator TEC-IT"/>'.format(img_link))
    except FileNotFoundError:
        print('"vins.json" file not found.')

    # generates html
    output = HTML_TEMPLATE.format(''.join(img_html_tags))
    # writes html file
    print('writing output into "index.html"...')
    with open('index.html', 'w') as f:
        f.write(output)
    print('done!')


main()
