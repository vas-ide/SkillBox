import datetime
import random
import vk_api
import logging
from logging.config import dictConfig

import handlers
import info
from info import dict_questions

try:
    import settings
except ImportError:
    exit(f"Copy 'settings.py.default' to settings.py and set token")

from log_src.logging_config import log_config

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

logging.config.dictConfig(log_config)
errors_log = logging.getLogger('errors')
chat_log = logging.getLogger('chat')


class UserState:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    """
    Echo bot for vk.com

    We use Python 3.12.1
    """

    def __init__(self, community_id, token):
        """
        :param community_id: group_id vk.com
        :param token: secret token from vk.com
        """
        self.community_id = community_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.community_id)
        self.api = self.vk.get_api()
        self.user_states = dict()

    def run(self):
        """
        Run the bot.
        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                # errors_log.exception("Exception occurred")
                pass

    def on_event(self, event: VkBotEventType):
        """
        Analyse event and send message.
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            chat_log.info("Message received type-%s----->Unable to process this type of massages", event.type)
            return

        user_id = event.object.message["peer_id"]
        text = event.object.message["text"]

        if user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id, text)
        else:
            for intent in info.INTENTS:
                if any(token in text for token in intent["token"]):
                    if intent["answer"]:
                        text_to_send = intent["answer"]
                    else:
                        self.start_scenario(user_id, intent["scenario"])
                    break
            else:
                text_to_send = info.DEFAULT_ANSWER

        self.api.messages.send(
            message=f"{text}",
            random_id=random.randint(0, 2 ** 20),
            peer_id=event.object.message["peer_id"],
        )

    def start_scenario(self, user_id, scenario_name):
        scenario = info.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step["text"]
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = info.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.step_name]

        handler = getattr(handlers, step["handler"])
        if handler(text=text, context=state.context):
            next_step = steps[step["next_step"]]
            text_to_send = next_step["text"].format(**state.context)
            if next_step["next_step"]:
                state.step_name = step["next_step"]
            else:
                self.user_states.pop(user_id)
        else:
            text_to_send = step["failure_text"].format(**state.context)
        return text_to_send

    # def on_event(self, event: VkBotEventType):
    #     """
    #     Analyse event and send message.
    #     """
    #     cur_date = datetime.datetime.now(datetime.UTC).strftime("%b %d %Y %H:%M:%S")
    #     if event.type == VkBotEventType.MESSAGE_NEW:
    #
    #         message_received = f"{event.object.message["text"]}"
    #         # chat_log.debug("Message received %s", message_received)
    #         message_reply = None
    #         if message_received.split()[0].lower() in dict_questions:
    #             message_reply = dict_questions[message_received.split()[0].lower()]
    #         self.api.messages.send(
    #             message=f"{cur_date}\n"
    #                     f"{message_reply}",
    #             random_id=random.randint(0, 2 ** 20),
    #             peer_id=event.object.message["peer_id"],
    #         )
    #         # chat_log.debug("Message received %s", message_reply)
    #     elif event.type == VkBotEventType.MESSAGE_REPLY:
    #         # chat_log.debug("Message received type-%s----->Unable to process this type of massages", event.type)
    #         pass
    #     else:
    #         # chat_log.info("Message received type-%s----->Unable to process this type of massages", event.type)
    #         raise ValueError
    #         pass


if __name__ == '__main__':
    bot = Bot(community_id=settings.COMMUNITY_ID, token=settings.TOKEN)
    bot.run()
    pass
