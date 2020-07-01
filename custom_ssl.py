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


class Secure:

    class Stub:
        Encrypt = staticmethod(lambda s,n: None)
        Decrypt = staticmethod(lambda s,n: None)

    class Simplest:

        abc = [chr(c) for c in range(48,58)+ range(65,91)+range(97,123)]

        @staticmethod
        def Encrypt(s, n):
            abc =Simplest.abc

            res = ''
            for c in s:
                res += abc[(abc.index(c) + n) % len(abc)]
            return res

        @staticmethod
        def Decrypt(s,n):
            abc =Simplest.abc

            res = ''
            for c in s:
                res += abc[(abc.index(c) - n) % len(abc)]
            return res


    approach = Simplest

    @staticmethod
    def Encrypt(s, n): approach.Encrypt(s, n)

    @staticmethod
    def Decrypt(s,n): approach.Decrypt(s, n)








def Sniffer(func):
    def wrapper(*args, **kwargs):

        print ("Sniffer: "+ str(args[1:]))
        return_value = func(*args, **kwargs)
        return return_value
    return wrapper



class Server: # (object)
    username = "asa"
    password = "111111"
    token = None
    Content = 'secure content'

    def _crypt(key, value):
        if value is tuple:
            name, psw = value
        elif value is str:
            value = Crypto.Simplest.encrypt()

    def Auth(self, name, password):
        self.token = "Non authorizated"
        if (self.username == name and self.password == password):
            self.token = "token " + base64.b64encode(self.username + self.password)

        return self.token

    def token_auth(self, token):

        if self.token == token: return self.Content
        else:
            return "Non authorizated"


class Client:

    server = Server()
    token = None

    @Sniffer
    def Auth(self, name, password):

        self.token = self.server.Auth(name, password)
        return self.token


    @Sniffer
    def token_auth(self, token):
        return self.server.token_auth(token)




def main():
    s = Client()
    token = s.Auth("asa","111111")
    print s.token_auth(token)

    # print token
    # print base64.b64decode(token.split(' ')[1])

if __name__ == '__main__':
    main()


