import configparser

config = configparser.ConfigParser()

# ---------------------------------------------查
print(config.sections())  # []

config.read('example.ini')

print(config.sections())  # ['bitbucket.org', 'topsecret.server.com']

print('bytebong.com' in config)  # False

print(config['bitbucket.org']['User'])  # hg

print(config['DEFAULT']['Compression'])  # yes

print(config['topsecret.server.com']['ForwardX11'])  # no

for key in config['bitbucket.org']:
    print(key)

# user
# serveraliveinterval
# compression
# compressionlevel
# forwardx11


print(
    config.options('bitbucket.org'))  # ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
print(config.items(
    'bitbucket.org'))  # [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]

print(config.get('bitbucket.org', 'compression'))  # yes

# ---------------------------------------------删,改,增(config.write(open('i.cfg', "w")))


config.add_section('yuan')

config.remove_section('topsecret.server.com')
config.remove_option('bitbucket.org', 'user')

config.set('bitbucket.org', 'k1', '11111')

config.write(open('i.cfg', "w"))
