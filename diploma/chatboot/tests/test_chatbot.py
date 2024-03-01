# import pytest
# from mock import patch
# import mock


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

# class TestChatbot:
#     def test_chatbot(self, monkeypatch):
#         count = 5
#         event = [{}] * count


# long_poller_mock = mock.Mock(return_value=event)
# long_poller_listen_mock = mock.Mock()
# long_poller_listen_mock.listen = long_poller_mock

# with mocker.patch("bot.vk_api.VkApi"):
#     with mocker.patch("bot.VkbotLongPoll", return_value=event):
#         bot = Bot("", "")
#         bot.on_event = mock.Mock()
#         bot.run()

# bot.on_event.assert_called_once()
# bot.on_event.assert_called_with({})
# bot.on_event.assert_called() == count

# def test_chatbot_add(self):
#     count = 5
#     event = [{}] * count
#     long_poller_mock = mock.MagicMock(return_value=event)
#     long_poller_listen_mock = mock.MagicMock()
#     long_poller_listen_mock.listen = long_poller_mock
#
#     with patch("bot.vk_api.VkApi"):
#         with patch("bot.VkbotLongPoll", return_value=long_poller_mock):
#             bot = Bot("", "")
#             bot.on_event = mock.MagicMock()
#             bot.run()
#
#             bot.on_event.assert_has_calls(count)
#             # bot.on_event.assert_called_with({})
#             # bot.on_event.assert_called() == count


# import pytest
# from mock import patch
#
# import mock
#
# from src.bot import Bot
# class TestChatbot:
#     def test_chatbot(self):
#         count = 5
#         event = [{}] * count
#         long_poller_mock = mock.Mock(return_value=event)
#         long_poller_listen_mock = mock.Mock()
#         long_poller_listen_mock.listen = long_poller_mock
#
#         with patch("bot.vk_api.VkApi"):
#             with patch("bot.VkbotLongPoll", return_value=long_poller_mock):
#                 bot = Bot("", "")
#                 bot.on_event = mock.Mock()
#                 bot.run()
#
#                 bot.on_event.assert_called_once()
#                 bot.on_event.assert_called_with({})
#                 bot.on_event.assert_called() == count
#
#     def test_chatbot_add(self):
#         count = 5
#         event = [{}] * count
#         long_poller_mock = mock.MagicMock(return_value=event)
#         long_poller_listen_mock = mock.MagicMock()
#         long_poller_listen_mock.listen = long_poller_mock
#
#         with patch("bot.vk_api.VkApi"):
#             with patch("bot.VkbotLongPoll", return_value=long_poller_mock):
#                 bot = Bot("", "")
#                 bot.on_event = mock.MagicMock()
#                 bot.run()
#
#                 bot.on_event.assert_has_calls(count)
#                 # bot.on_event.assert_called_with({})
#                 # bot.on_event.assert_called() == count
