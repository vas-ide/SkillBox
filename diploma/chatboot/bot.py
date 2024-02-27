

import datetime
import random
import vk_api
import logging

from _token import token
from info import community_id, dict_questions

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

log = logging.getLogger("bot")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

file_handler = logging.FileHandler("logging/log.txt")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

log.addHandler(stream_handler)
log.addHandler(file_handler)
log.setLevel(logging.DEBUG)


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
                log.exception("Exception occurred")
                pass

    def on_event(self, event):
        cur_date = datetime.datetime.now(datetime.UTC)
        if event.type == VkBotEventType.MESSAGE_NEW:

            message_received = f"{event.object.message["text"]}"
            log.debug("Message received %s", message_received)
            message_reply = None
            if message_received.split()[0].lower() in dict_questions:
                message_reply = dict_questions[message_received.split()[0].lower()]
            self.api.messages.send(
                message=f"{cur_date.date()}\n"
                        f"{message_reply}",
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.message["peer_id"],
                # peer_id=event.object.message["from_id"],

            )
            log.debug("Message received %s", message_reply)
        elif event.type == VkBotEventType.MESSAGE_REPLY:
            log.debug("Message received type-%s----->Unable to process this type of massages", event.type)
            pass
        else:
            log.debug("Message received type-%s----->Unable to process this type of massages", event.type)
            pass


if __name__ == '__main__':
    bot = Bot(community_id=community_id, token=token)
    bot.run()
    pass
