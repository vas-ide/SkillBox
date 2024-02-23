

from _token import token
from info import community_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api

class Bot:
    def __init__(self, community_id, token):
        self.community_id = community_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=self.community_id)


    def run(self):
        for event in self.long_poller.listen():
            print(f"полученно событие")
            try:
                self.on_event(event)
            except Exception as err:
                print(err)
        pass
    def on_event(self, event):
        print(event.type,event.object)
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(f"{event.object.message["text"]}")




if __name__ == '__main__':
    bot = Bot(community_id=community_id, token=token)
    bot.run()
    pass























