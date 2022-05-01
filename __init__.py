import asyncio
from smsactivate.api import SMSActivateAPI

from telethon import TelegramClient
from telethon import errors

# for getting numbers from sms_api
# sms_api_key = '1bde5d8A7931c38880dc7ecf97332cA6'
# sms_api = SMSActivateAPI(sms_api_key)
# phone number = sms_api.getNumber(service='tg')

telegram_api_id = '15075009'
telegram_api_hash = '1b3f35183a1865d05a169f8f60106151'

# TODO get phone number from sms_api
phone_number = '14138894178'

client = TelegramClient('tester',
                        telegram_api_id,
                        telegram_api_hash)

async def create_new_client():
    await client.connect()
    await send_sms_verification_code()

    # TODO get verification code from phone number
    # code collected from the sms message
    verification_code  = input("enter the code: ")
    await sign_up_client_to_telegram(verification_code)

async def send_sms_verification_code():
    try:
        await client.send_code_request(phone_number)
    except Exception as e:
        print(e)
        # TODO handle errors correctly 
        # sometimes get error "A wait of 45460 seconds is required before requesting another code"
        # sometimes phone numbers are blocked as well

async def sign_up_client_to_telegram(verification_code):
    # await client.sign_in(phone_number, verification_code)
    await client.sign_up(code=verification_code, first_name="test", last_name="er")

async def main():
    await asyncio.gather(create_new_client())

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

