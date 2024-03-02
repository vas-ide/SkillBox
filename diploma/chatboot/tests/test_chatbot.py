# import pytest
# from mock import patch
# import mock
# from bot import Bot
#
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
#                 # bot.on_event.assert_called_once()
#                 # bot.on_event.assert_called_with({})
#                 # bot.on_event.assert_called() == count
# #
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
#                 # bot.on_event.assert_has_calls(count)
#                 # bot.on_event.assert_called_with({})
#                 # bot.on_event.assert_called() == count
