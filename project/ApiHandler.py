import requests

class ApiHandler():
    url = 'http://api.sms-man.com/stubs/handler_api.php?'

    # Info@payitnow.io acount api key
    key = 'mPeOymYGK30laHMO-BP_oPpu3vJTFqm7'

    def request_balance(self):
        return 'balance'
    
    def request_available_numbers(self):
        return 'available_numbers'
    
    def request_phone_number(self):
        return 'phone_number'

    def request_activation_status(self):
        return 'activation status'