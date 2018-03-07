#-*- coding:utf-8 -*-
import os
import hashlib


def hash_password(password, salt=None):
    hash = hashlib.sha256()
    if salt == None:
        salt = os.urandom(8)
    hash.update(salt + password)
    return salt, hash.hexdigest()


if __name__ == '__main__':
    passwd_old = raw_input('Please input your password:')
    salt, hashed = hash_password(passwd_old)
    while 1:
        passwd_new = raw_input('Please input your password to confirm:')
        if hash_password(passwd_new,salt)[1] == hashed:
            print 'Yes'
        else:
            print 'No'
