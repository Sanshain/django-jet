import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

# https://github.com/python273/vk_api/blob/master/examples/longpoll.py

psw = input('')     # 314...

vk_session = vk_api.VkApi('digital-mag@ya.ru', psw)
# vk_session.auth()
vk_session.auth(token_only=True)

vk = vk_session.get_api()


print(vk.wall.post(message='лучший день!'))
print(vk.wall.get(count=1))


# longpoll = VkLongPoll(vk_session)                 # не работает

# callback:
# https://github.com/python273/vk_api/blob/master/examples/callback_bot.py
