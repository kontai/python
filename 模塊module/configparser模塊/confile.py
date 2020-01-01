import configparser

config = configparser.ConfigParser()     #config={}




config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}



config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here



with open('example.ini', 'w') as f:
    config.write(f)


#------------------------------------------------------增删改查、
import configparser

config = configparser.ConfigParser()

#---------------------------------------------查
# print(config.sections())   #[]
#
config.read('example.ini')
# #
# print(config.sections())   #['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config)# False
# #
# print(config['bitbucket.org']['User']) # hg
# #
# print(config['DEFAULT']['Compression']) #yes
# #
# print(config['topsecret.server.com']['ForwardX11'])  #no
#
#
# for key in config['bitbucket.org']:
#     print(key)    #預設[DEFAUL]內容也會打印出來（無論是否指定）
#

#
#
#print(config.options('bitbucket.org'))#['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
#print(config.items('bitbucket.org'))  #[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]

#print(config.get('bitbucket.org','compression'))#yes
#
#
# #---------------------------------------------删,改,增(config.write(open('i.cfg', "w")))
#
#
config.add_section('yuan')      #增加塊
config.set('yuan','k1','11111') #塊,鍵,值

config.remove_section('topsecret.server.com')  #移除塊
config.remove_option('bitbucket.org','user')   #移除值d11
#

config.write(open('i.cfg', "w"))