import re
import requests
from bs4 import BeautifulSoup

def get_companies_by_url(url=None):
	url = url
	headers = {'User-Agent':'Mozilla/5.0'}
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	regex = re.compile('company-name')
	content_lis = soup.find_all('h3', attrs={'class': regex})
	content = []
	for a in content_lis:
	    content.append(a.text.split('\n')[1])
	print(content)

get_companies_by_url("https://clutch.co/in/agencies/ui-ux/delhi?page=1")