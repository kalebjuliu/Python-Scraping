from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.enterkomputer.com/vga.php')

span_name = r.html.find('span.prd-name')
span_price = r.html.find('span.harga')

for price in span_price:
	print(price.text)
	
for name in span_name:
	print(name.text)