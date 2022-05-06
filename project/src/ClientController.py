import names

from ApiHandler import ApiHandler
from FileHandler import FileHandler
from ResponseHandler import ResponseHandler
from TelegramHandler import TelegramHandler
from Account import Account

class ClientController():
    def __init__(self):
        self.telegram_handler = TelegramHandler()
        self.api_handler = ApiHandler()
        self.response_handler = ResponseHandler()
        self.file_handler = FileHandler()

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

        first_name = names.get_first_name()
        last_name = names.get_last_name()

        await self.telegram_handler.sign_up_client_with_full_name(verification_code,
                                                                  first_name,
                                                                  last_name)

        await self.telegram_handler.add_client_to_pin_group()

        account = Account(first_name, phone_id, phone_number)

        self.file_handler.write_single_account_json_file(account)    

    def get_balance(self):
        print(self.api_handler.request_balance())