import random
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from bot import Bot
from vk_api.bot_longpoll import VkBotMessageEvent


class TestChatBotUni(TestCase):
    RAW_EVENT = {'group_id': 224818713, 'type': 'message_new',
                 'event_id': '88c5aae293730e37291740ab0205e1ee2a624eb1',
                 'v': '5.199', ''
                               'object': {
            'message': {'date': 1709404596, 'from_id': 851440434, 'id': 346, 'out': 0, 'version': 10001228,
                        'attachments': [], 'conversation_message_id': 344, 'fwd_messages': [], 'important': False,
                        'is_hidden': False, 'peer_id': 851440434, 'random_id': 0, 'text': 'Hello'},
            'client_info': {
                'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'open_photo', 'callback',
                                   'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True,
                'inline_keyboard': True,
                'carousel': True, 'lang_id': 0}}}

    def test_run_chatbot(self):
        count = 5
        obj = {"item": 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot("", "")
                bot.on_event = Mock()
                bot.run()
                pass

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    def test_on_event_chatbot(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot("", "")
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)
        send_mock.assert_called_once()

        send_mock.assert_called_once_with(
            # message=self.RAW_EVENT["object"]["message"]["text"],
            # message = "Mar 02 2024 19:05:14\nHow are you?",
            message=ANY,
            random_id=ANY,
            peer_id=self.RAW_EVENT["object"]["message"]["peer_id"],
        )
