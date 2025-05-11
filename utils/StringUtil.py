def getmd5(password):
    import hashlib
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()
