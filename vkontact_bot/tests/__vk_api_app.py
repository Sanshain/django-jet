from vk_api import vk_api

# https://github.com/python273/vk_api/blob/master/examples/auth_by_code.py
# https://vk.com/editapp?id=7881679

code = 'bf623d89bf623d89bf623d8983bf1a7e46bbf62bf623d89dfa8158f42dbe2a2dee34136'        # ?? - сервисный не подошел
redirect_url = 'http://example.com'
app = 7881679
secret = '2ueIRERfyBflTkTmZSBM'

vk_session = vk_api.VkApi(app_id=app, client_secret=secret)

try:
    vk_session.code_auth(code, redirect_url)

    print(vk_session.token['user_id'])
    print(vk_session.token['access_token'])

except vk_api.AuthError as error_msg:
    print(error_msg)

