import requests

resp = requests.get('http://localhost:9999/e/haha')
if resp.status_code == 200 and \
        resp.text == 'Say hello to my little friend haha':
    print('It worked! The almost never happens!')
else:
    print('Argh,got this:', resp.text)
