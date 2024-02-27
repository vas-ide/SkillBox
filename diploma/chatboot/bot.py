import datetime
import random
import vk_api
import logging
from logging.config import dictConfig

from _token import token
from info import community_id, dict_questions
from log_crf.logging_config import log_config

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

logging.config.dictConfig(log_config)
errors_log = logging.getLogger('errors')
chat_log = logging.getLogger('chat')


class Bot:
    def __init__(self, community_id, token):
        self.community_id = community_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.community_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                errors_log.exception("Exception occurred")
                pass

    def on_event(self, event):
        cur_date = datetime.datetime.now(datetime.UTC).strftime("%b %d %Y %H:%M:%S")
        if event.type == VkBotEventType.MESSAGE_NEW:

            message_received = f"{event.object.message["text"]}"
            chat_log.debug("Message received %s", message_received)
            message_reply = None
            if message_received.split()[0].lower() in dict_questions:
                message_reply = dict_questions[message_received.split()[0].lower()]
            self.api.messages.send(
                message=f"{cur_date}\n"
                        f"{message_reply}",
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.message["peer_id"],
                # peer_id=event.object.message["from_id"],

            )
            chat_log.debug("Message received %s", message_reply)
        elif event.type == VkBotEventType.MESSAGE_REPLY:
            chat_log.debug("Message received type-%s----->Unable to process this type of massages", event.type)
            pass
        else:
            chat_log.info("Message received type-%s----->Unable to process this type of massages", event.type)
            raise ValueError
            pass


if __name__ == '__main__':
    bot = Bot(community_id=community_id, token=token)
    bot.run()
    pass
