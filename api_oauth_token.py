import json
import urllib2
import requests
from pandas.io.json import json_normalize

def get_access_token():
	'''
	get an oauth access token
	'''
	url = "PATH/oauth/token"
	payload = "grant_type=password&client_id=<ID>&client_secret=<SECRET>&username=<USERNAME>&password=<PASSWORD>"
	headers = {'accept': "application/json",
				'content-type': '<CONTENT-TYPE>'}
	response = requests.request("POST", url, data=payload, headers=headers)
	response_data = json.loads(response.text)
	access_token = response_data['access_token'].encode("ascii", "ignore")
	return access_token


def get_response_json_object(url):
	'''
	get json info
	'''
	access_token = get_access_token()
	req = urllib2.Request(url, None, {"Authorization": "Bearer %s" % access_token})
	response = urllib2.urlopen(req)
	html = response.read()
	json_obj = json.loads(html)
	return json_obj

url = '<URL>'
data = get_response_json_object(url)
df = json_normalize(data['result'])

