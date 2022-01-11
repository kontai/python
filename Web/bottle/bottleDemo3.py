from bottle import run, route, static_file


@route('/')
def home():
    return static_file('index.html', root='.')


@route('/e/<thing>')
def echo(thing):
    return "Say hello to my little friend %s!" % thing



run(host='localhost', port=9999,reloader=True,debug=True)
'''
    debug: 如果有HTTP錯誤,debug=Ture會建立一個除錯網頁
    reloader: 當修改任何Python程式,reloader=True會在瀏覽器重新載入網頁
'''
