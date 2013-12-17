import urllib
import httplib2 # for easy header/cookie handling

from bs4 import BeautifulSoup
from config import * # import passwords & URLs

http = httplib2.Http() # making this prettier

# logs in user, returns header info with cookie
def login():
	
	# setup variables, ones in CAPS from config.py
	url = LOGIN_URL
	body = {'username': USERNAME, 'password': PASSWORD, 'rememberme': 'on'}
	headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
	
	# submit credentials and store response & content
	response, content = http.request(url, 'POST', headers = headers, body = urllib.urlencode(body))
	
	headers['Cookie'] = response['set-cookie']
	
	return headers
	
headers = login()
print headers