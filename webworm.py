#爬虫部分

import requests
import sqlite3 as sql

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'

def get_HTML(address):
    url = address
    headers = {
		'User-Agent' : 
	}
    req = requests.get()