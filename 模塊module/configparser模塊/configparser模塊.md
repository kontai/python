来看一个好多软件的常见文档格式如下：

    [DEFAULT]
    ServerAliveInterval = 45
    Compression = yes
    CompressionLevel = 9
    ForwardX11 = yes
     
    [bitbucket.org]
    User = hg
     
    [topsecret.server.com]
    Port = 50022
    ForwardX11 = no

如果想用python生成一个这样的文档怎么做呢？

    import configparser
     
    config = configparser.ConfigParser()
    config["DEFAULT"] = {'ServerAliveInterval': '45',
                          'Compression': 'yes',
                         'CompressionLevel': '9'}
     
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Host Port'] = '50022'     # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'

    with open('example.ini', 'w') as configfile:
       config.write(configfile)

