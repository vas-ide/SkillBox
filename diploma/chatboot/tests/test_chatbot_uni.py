from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

from src.bot import Bot


class TestChatBotUni(TestCase):
    def test_chatbot(self):
        count = 5
        # obj = {"item": 1}
        # events = [obj] * count
        events = [{}] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot("", "")
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called_colled()
                bot.on_event.assert_any_call({})
                bot.on_event.call_count == count
