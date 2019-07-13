#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import websockets
sstr = ''
async def consumer_handler(websocket):
    global glob_message
    while True:
        message = await websocket.recv()
        sstr +=  message
        print("this went in glob_message: {}".format(message))

async def producer_handler(websocket):
    global glob_message
    while True:
        message = await glob_message.get()
        await websocket.send(sstr)

async def handler(websocket, path):
    producer_task = asyncio.ensure_future(producer_handler(websocket))
    consumer_task = asyncio.ensure_future(consumer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()

if __name__ == '__main__':
    glob_message = asyncio.Queue()
    start_server = websockets.serve(
            handler,
            '127.0.0.3', 5680)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
