#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     01.07.2020
# Copyright:   (c) User 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import base64
from itertools import chain

class Secure:

    class Stub:
        Encrypt = staticmethod(lambda s,n: s)
        Decrypt = staticmethod(lambda s,n: s)

    class Simplest:

        abc = [chr(c) for c in chain(range(48,58), range(65,91),range(97,123))]

        @staticmethod
        def Encrypt(s, n):
            abc = Secure.Simplest.abc

            res = ''
            for c in s:
                res += abc[(abc.index(c) + n) % len(abc)]
            return res

        @staticmethod
        def Decrypt(s,n):
            abc = Secure.Simplest.abc

            res = ''
            for c in s:
                res += abc[(abc.index(c) - n) % len(abc)]
            return res


    approach = Simplest

    @staticmethod
    def Encrypt(s, n): return Secure.approach.Encrypt(s, n)

    @staticmethod
    def Decrypt(s,n): return Secure.approach.Decrypt(s, n)








def Sniffer(func):
    def wrapper(*args, **kwargs):
        #  + func.__name__ + ' on '
        # tp = 'out' if args[0].__class__.__name__ == 'Server' else 'in'

        print ("steal request to server: " + str(args[1:]))
        return_value = func(*args, **kwargs)
        print ("steal server response: " + str(return_value))
        return return_value
    return wrapper



class Server: # (object)
    username = "asa"
    password = "111111"
    token = None
    Content = 'secure content'

    def _encrypt(self, value, key):
        if ' ' in value:
            name, value = value.split(' ')
            rez = name + ' ' + Secure.Encrypt(value, key)
        else: rez = Secure.Encrypt(value, key)

        return rez

    def _decrypt(self, key, value):
        if value is tuple: value = value[1]
        elif value is str: value = value

        rez = Secure.Decrypt(value, key)
        return rez


    def Auth(self, name_password, key):
        name_password = name_password.split(':')
        if len(name_password) != 2: return 'wrong auth data'
        else:
            name, password = name_password

        self.token = "Non authorizated"
        if (self.username == name and self.password == self._decrypt(key, password)):
            self.token = "token " + base64.b64encode(self.username + self.password)
            print 'token pushed: ' + self.token
            key = 6
            token = self._encrypt(self.token, key)
            return token, key
        # encrypt
        return self.token


    def token_auth(self, token, key):

        tkn = token.split(' ')
        if len(tkn) == 2:
            token = ' '.join((tkn[0], self._decrypt(key, tkn[1])))

        if self.token == token: return '> ' + self.Content
        else:
            return "Non authorizated"


class Client(object):

    server = Server()
    token = None


    def input_and_auth(self, name, password):
        key = 5
        cry_password = Secure.Encrypt(password, key)
        token, key = self.request_for_auth(':'.join((name, cry_password)), key)
        if token == "Non authorizated":
            print "Non authorizated/ no token"
            return None
        else:
            self.token = token.split(' ')[0] + ' ' + Secure.Decrypt(token.split(' ')[1], key)
            return self.token


    def get_secure_content(self, token):
        realm, token = token.split(' ')
        key = 7
        cry_token = Secure.Encrypt(token, key)
        return self.request_for_content(realm + ' ' + cry_token, key)


    @Sniffer
    def request_for_auth(self, name_password, key):

        token, key = self.server.Auth(name_password, key)
        return token, key

    @Sniffer
    def request_for_content(self, token, key):

        return self.server.token_auth(token, key)




def main():
    s = Client()
    token = s.input_and_auth("asa","111111")
    s.get_secure_content(token)
    s.get_secure_content(token)

    # print token
    # print base64.b64decode(token.split(' ')[1])

if __name__ == '__main__':
    main()


