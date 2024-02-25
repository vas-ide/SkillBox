import datetime, random, time
from _token import token
from info import community_id, dict_questions
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api


class Bot:
    def __init__(self, community_id, token):
        self.community_id = community_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=self.community_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as err:
                print(err)
        pass

    def on_event(self, event):
        cur_date = datetime.datetime.now(datetime.UTC)
        # print(event.type, event.object)
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(f"{event.type:<35}\n{event.object}\n{event.object.message["text"]}")
            message_request = f"{event.object.message["text"]}"
            message_reply = None
            if message_request in dict_questions:
                message_reply = dict_questions[message_request]
            self.api.messages.send(
                message=f"{cur_date.date()} {cur_date.time()} ___{message_reply}",
                random_id=random.randint(0, 2 ** 20),
                # peer_id=event.object.massage["peer_id"],
                peer_id=event.object.message["from_id"],

            )
        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print(f"{event.type:<35}-{event.object["text"]}")
        else:
            print(event.type, event)


if __name__ == '__main__':
    bot = Bot(community_id=community_id, token=token)
    bot.run()
    pass
