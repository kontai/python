用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
    import hashlib
     
    m=hashlib.md5()# m=hashlib.sha256()
     
    m.update('hello'.encode('utf8'))
    print(m.hexdigest())  #5d41402abc4b2a76b9719d911017c592
     
    m.update('alvin'.encode('utf8'))
     
    print(m.hexdigest())  #92a7e713c30abbb0319fa07da2a5c4af
     
    m2=hashlib.md5()
    m2.update('helloalvin'.encode('utf8'))
    print(m2.hexdigest()) #92a7e713c30abbb0319fa07da2a5c4af

以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。

    import hashlib
     
    # ######## 256 ########
     
    hash = hashlib.sha256('898oaFs09f'.encode('utf8'))
    hash.update('alvin'.encode('utf8'))
    print (hash.hexdigest())#e79e68f070cdedcfe63eaf1a2e92c83b4cfb1b5c6bc452d214c1b7e77cdfd1c7
    
python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密:

    import hmac
    h = hmac.new('alvin'.encode('utf8'))
    h.update('hello'.encode('utf8'))
    print (h.hexdigest())#320df9832eab4c038b6c1d7ed73a5940