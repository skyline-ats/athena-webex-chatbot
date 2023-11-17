import unittest
from src.webex_chatbot import app


class WebexChatbotTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_webhook_response(self):
        # Add your tests for the webhook response here
        pass


if __name__ == '__main__':
    unittest.main()
