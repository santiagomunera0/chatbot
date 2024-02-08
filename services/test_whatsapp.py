import unittest
from whatsapp import button_reply_message

class TestWhatsApp(unittest.TestCase):

    def test_button_reply_message(self):
        number = "1234567890"
        options = ["Option 1", "Option 2", "Option 3"]
        body = "Hello, please select an option:"
        footer = "Powered by WhatsApp"
        sedd = "abcd1234"

        expected_data = '{"messaging_product": "whatsapp", "recipient_type": "individual", "to": "1234567890", "type": "interactive", "interactive": {"type": "button", "body": {"text": "Hello, please select an option:"}, "footer": {"text": "Powered by WhatsApp"}, "action": {"buttons": [{"type": "reply", "reply": {"id": "abcd1234_btn_1", "title": "Option 1"}}, {"type": "reply", "reply": {"id": "abcd1234_btn_2", "title": "Option 2"}}, {"type": "reply", "reply": {"id": "abcd1234_btn_3", "title": "Option 3"}}]}}}'
        
        result = button_reply_message(number, options, body, footer, sedd)

        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()