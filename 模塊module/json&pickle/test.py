import shelve

f = shelve.open(r'shelve1')  # 目的：将一个字典放入文本 f={}

f['stu1_info'] = {'name': 'alex', 'age': '18'}
f['stu2_info'] = {'name': 'alvin', 'age': '20'}
f['school_info'] = {'website': 'oldboyedu.com', 'city': 'beijing'}
# f.close()

print(f.get('stu1_info')['age'])
