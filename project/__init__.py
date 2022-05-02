import asyncio
from ClientController import ClientController

async def main():
    client_controller = ClientController()
    await asyncio.gather(client_controller.sign_up_client())
  
if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
