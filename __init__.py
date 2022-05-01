import asyncio
import names
import time
import requests
from tkinter import E
from requests import get
from smsactivate.api import SMSActivateAPI

from telethon import TelegramClient
from telethon import errors
from telethon.tl.functions.channels import JoinChannelRequest


# Info@payitnow.io acount api key
sms_api_key = '769b7fA2cA8b5191d3c382cf46784db1'


sms_api = SMSActivateAPI(sms_api_key)
sms_api.debug_mode = True

telegram_api_id = '15075009'
telegram_api_hash = '1b3f35183a1865d05a169f8f60106151'

client = TelegramClient('tester',
                        telegram_api_id,
                        telegram_api_hash)

# 
async def main():
    await asyncio.gather(create_new_client())

async def create_new_client():
    phone_meta_data = get_sms_api_response()
    await client.connect()
    await send_sms_verification_code(phone_meta_data)
    message_meta_data = get_message_meta_data(phone_meta_data)
    # verification_code  = input("enter the code: ")
    verification_code = get_verification_code(message_meta_data)
    await sign_up_client_to_telegram(verification_code)
    await add_client_to_pin_group()

def get_sms_api_response():
    sms_api_response = sms_api.getNumber(service='tg')
    # sms_api_response = sms_api.getRentNumber(service='tg')
    phone_meta_data = sms_api_response.get('phone')
    if phone_meta_data is None:
        get_sms_api_response()

    return phone_meta_data

async def send_sms_verification_code(phone_meta_data):
    phone_number = phone_meta_data.get('number')
    try:
        await client.send_code_request(phone_number)
    except errors.rpcerrorlist.FloodWaitError as e:
        print('Have to sleep', e.seconds, 'seconds')
        time.sleep(e.seconds)
        await send_sms_verification_code(phone_meta_data)

def get_message_meta_data(phone_meta_data):
    phone_id = phone_meta_data.get('activation_id')
    # phone_id = phone_meta_data.get('id')
    message_meta_data = sms_api.getStatus(phone_id)
    # message_meta_data = sms_api.getRentStatus(phone_id)

    if message_meta_data.get('status') == 'error':
        get_message_meta_data(phone_meta_data)

    return message_meta_data

def get_verification_code(message_meta_data):
    values = message_meta_data.get('values')
    first_message = values.get('0')
    verification_code = first_message.get('text')

    # removes the word 'code' from the message
    return verification_code.split()[-1]              

async def sign_up_client_to_telegram(verification_code):
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    await client.sign_up(code=verification_code, 
                         first_name=first_name,
                         last_name=last_name)
    print(first_name)
    print(last_name)

async def add_client_to_pin_group():
    await client(JoinChannelRequest('PayItNow_PIN'))

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
