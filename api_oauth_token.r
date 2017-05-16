library(httr)
library(rjson)
library(jsonlite)

url_token = "PATH/oauth/token"
payload = 'grant_type=password&client_id=<ID>&client_secret=<SECRET>&username=<USERNAME>&password=<PASSWORD>'

req = httr::POST(url_token,
                 httr::add_headers(
                   'accept'='application/json',
                   'content-type'='application/x-www-form-urlencoded'
                 ),
                 body=payload)
# get token
token = httr::content(req)$access_token

# get data
url = '<URL>'
request = httr::GET(url, httr::add_headers(Authorization=paste('Bearer', token)))
json = httr::content(request, as='text')
json = jsonlite::fromJSON(json, simplifyDataFrame = TRUE)

