# чтобы произвести подтверждение, нужен selenium или pypetter
# https://vk.com/dev/implicit_flow_user
import logging

from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id

logger = logging.getLogger(__name__)

let = 'https://oauth.vk.com/authorize?client_id=7881679&display=page&scope=2&response_type=token&state=oookooo&revoke=1'
# requests.get(
#     'https://oauth.vk.com/authorize?client_id=7881679&display=page&scope=2&response_type=token&state=oookooo&revoke=1'
# )


# берем отсюда https://vkhost.github.io/
# token = '9c4644cc3f7355a8f7d81def9c17013b1413bf27516c53a5de555351924bc3dd1053f846b8ce8da832835'
# token = '429b8049a2ce89220cc2b98ceb0ca221007b1d40f3d7283a91bdcf704bb3025438955a67ad03d4ce35933'


psw = input('')  # 314...


class Listener:
    token = '429b8049a2ce89220cc2b98ceb0ca221007b1d40f3d7283a91bdcf704bb3025438955a67ad03d4ce35933'

    def __init__(self):
        self.vk_session = vk_api.VkApi('digital-mag@ya.ru', psw, token=self.token, app_id=2685278)
        # vk_session = vk_api.VkApi(token=token)
        self.vk_session.auth(self.token)

        # longpoll = VkBotLongPoll(vk_session)            # требует group_id
        self.longpoll = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api()

    def start(self):

        for event in self.longpoll.listen():

            m_type = event.type.name.lower()  # .split('.').pop()

            print(m_type)
            logger.info(msg=m_type)

            if event.type.name == VkBotEventType.MESSAGE_NEW.name:

                print('Новое сообщение:')

                if event.from_me:
                    print('От меня для: ', end='')
                elif event.to_me:
                    print('Для меня от: ', end='')

                peer_id = None
                if event.from_user:
                    print(f' From user {event.user_id} ')
                    peer_id = event.user_id
                    continue
                elif event.from_chat:
                    print(event.user_id, 'в беседе', event.chat_id)
                    peer_id = 2000000000 + event.chat_id
                elif event.from_group:
                    print('группы', event.group_id)
                    peer_id = - event.group_id
                    continue

                print('Текст: ', event.text)

                if '123' in event.text:
                    result = self.vk.messages.send(
                        message='Hello World!',
                        random_id=get_random_id(),
                        peer_id=peer_id,                    # from_id = data['object']['from_id']
                        reply_to=event.message_id
                        # chat_id=
                        # forward_messages=
                    )
                    print('success')
                elif 'хуй' in event.text:
                    result = self.vk.messages.send(
                        message='warn',
                        random_id=get_random_id(),
                        peer_id=peer_id,                    # from_id = data['object']['from_id']
                        reply_to=event.message_id
                    )
                    self.vk.messages.delete(
                        message_ids=(event.message_id,),
                        delete_for_all=1,
                        peer_id=peer_id
                    )
                    r = self.vk.messages.removeChatUser(
                        chat_id=event.chat_id,
                        user_id=event.user_id
                    )

                print()


Listener().start()

# https://github.com/python273/vk_api/blob/master/examples/callback_bot.py
# https://github.com/python273/vk_api/blob/master/examples/longpoll.py
# https://vk-api.readthedocs.io/en/latest/bot_longpoll.html
