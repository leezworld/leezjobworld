from bs4 import BeautifulSoup

#test beatifulsoup
print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))