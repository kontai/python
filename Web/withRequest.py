import requests

# url = 'https://www.programmableweb.com/api/i-heart-quotes-rest-api'
url = '0.0.0.0:8000'
resp = requests.get(url)
print(resp)
print(resp.text)
