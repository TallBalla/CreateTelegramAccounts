import asyncio

from TelegramHandler import TelegramHandler
from ApiHandler import ApiHandler

async def sign_up_client():
    return 'hello'

async def main():
    await asyncio.gather(sign_up_client())
  

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    # api_handler = ApiHandler()
    # print(api_handler.request_all_countries())


