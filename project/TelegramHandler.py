import asyncio
import time
import names

from telethon import TelegramClient
from telethon import errors
from telethon.tl.functions.channels import JoinChannelRequest

class TelegramHandler():
    id = '15075009'
    hash = '1b3f35183a1865d05a169f8f60106151'

    client = TelegramClient('tester', id, hash)

    def __init__(self):
        self.client.connect()

    async def request_sms_verification(self, phone_number):
        try:
            await self.client.send_code_request(phone_number)
        except errors.rpcerrorlist.FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds)
            self.request_sms_verification(phone_number)

    async def sign_up_client_with_full_name(self, verification_code):
        first_name = names.get_first_name()
        last_name = names.get_last_name()

        await self.client.sign_up(
                            code=verification_code, 
                            first_name=first_name,
                            last_name=last_name)

    async def add_client_to_pin_group(self):
        await self.client(JoinChannelRequest('PayItNow_PIN'))
        self.client.disconnect()