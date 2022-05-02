import requests

from ApiHandlerInterface import ApiHandlerInterface
from Status import Status

class ApiHandler(ApiHandlerInterface):
    BASE_URL = 'http://api.sms-man.com/stubs/handler_api.php'

    # Info@payitnow.io acount api key
    key = 'mPeOymYGK30laHMO-BP_oPpu3vJTFqm7'

    def request_balance(self) -> str:
        query_params = {
            'action': 'getBalance',
            'api_key': self.key
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.text
    
    def request_available_numbers(self) -> str:
        query_params = {
            'action': 'getPrices',
            'api_key': self.key
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.json()
    
    def request_phone_number(self, country_code: int) -> str:
        query_params = {
            'action': 'getNumber',
            'api_key': self.key,
            'service': 'tg',
            'country': country_code
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.text

    def request_activation_status(self, phone_id: int) -> str:
        query_params = {
            'action': 'getStatus',
            'api_key': self.key,
            'id': phone_id
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.text

    def change_activation_status(self, phone_id: str, status: Status) -> str:
        query_params = {
            'action': 'setStatus',
            'api_key': self.key,
            'id': phone_id,
            'status': status
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.text

    def request_all_countries(self) -> str:
        query_params = {
            'action': 'getCountries',
            'api_key': self.key
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.json()
    
    def request_all_services(self) -> str:
        query_params = {
            'action': 'getServices',
            'api_key': self.key
        }
        response = requests.get(f'{self.BASE_URL}',
                                params=query_params)
        return response.json()