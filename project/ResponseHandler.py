from ResponseHandlerInterface import ResponseHandlerInterface

class ResponseHandler(ResponseHandlerInterface):
    def get_balance(self, response) -> float:
        balance_number = response.split(':')[1]
        return float(balance_number)

    def get_activation_number(self, phone_response_data) -> int:
        activation_number = phone_response_data.split(':')[1]
        return int(activation_number, base=10)

    def get_phone_number(self, phone_response_data) -> str:
        phone_number = phone_response_data.split(':')[2]
        return phone_number
    
    def get_verification_code(self, message_response_data) -> int:
        text_message = message_response_data.split(':')[1]
        print(text_message)
        verification_code = text_message.split(' ')[1]
        return verification_code