def get_lines(url):
    from bs4 import BeautifulSoup as soup
    import requests

    url = requests.get(url)
    page = url.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links


if __name__ == '__main__':
    import sys
    url = 'http://www.google.com'
    print('Link in',url)
    for num,Link in enumerate(get_lines(url),1):
        print(num,Link)


