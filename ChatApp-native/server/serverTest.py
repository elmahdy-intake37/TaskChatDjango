#!/usr/bin/env python
# import logging
# logger = logging.getLogger('websockets')
# logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler())
import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

connected = set()

async def handler(websocket, path):
    global connected
    # Register.
    connected.add(websocket)
    try:
        # Implement logic here.
        await asyncio.wait([ws.send("Hello!") for ws in connected])
        await asyncio.sleep(10)
    finally:
        # Unregister.
        connected.remove(websocket)


start_Server = websockets.serve(handler, '127.0.0.1', 5678)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_Server)

asyncio.get_event_loop().run_forever()


# async def consumer_handler(websocket, path):
#     async for message in websocket:
#         await consumer(message)
# async def producer_handler(websocket, path):
#     while True:
#         message = await producer()
#         await websocket.send(message)
# async def handler(websocket, path):
#     consumer_task = asyncio.ensure_future(consumer_handler(websocket))
#     producer_task = asyncio.ensure_future(producer_handler(websocket))
#     done, pending = await asyncio.wait(
#         [consumer_task, producer_task],
#         return_when=asyncio.FIRST_COMPLETED,
#     )
#
#     for task in pending:
#         task.cancel()
