import re

s='<div><a href="https://support.google.com/chrome/?p=ui_hotword_search" target="_blank">更多</a><a href="">123</a><p>dfsl</p></div>'
print(re.search(r'<a.*>(.*)</a>',s).group(0))
