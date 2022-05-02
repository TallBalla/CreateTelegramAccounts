from TelegramHandler import TelegramHandler
from ApiHandler import ApiHandler
from ResponseHandler import ResponseHandler
import project

class ClientController():
    telegram_handler = TelegramHandler()
    api_handler = ApiHandler()
    response_handler = ResponseHandler()

    async def sign_up_client(self):
        phone_response_data = self.api_handler.request_phone_number(31)
        # TODO handle exceptions before information is passed down

        phone_id = self.response_handler \
                                .get_activation_number(phone_response_data)

        # TODO handle exceptions before information is passed down
        phone_number = self.response_handler \
                           .get_phone_number(phone_response_data)

        await self.telegram_handler.request_sms_verification(phone_number)

        message_response_data = self.api_handler.request_activation_status(phone_id)

        verification_code = self.response_handler \
                                .get_verification_code(message_response_data)

        await self.telegram_handler.sign_up_client_with_full_name(verification_code)

        await self.telegram_handler.add_client_to_pin_group()

    def save_to_json_file():
        # TODO save to json file or database
        return 'hello'