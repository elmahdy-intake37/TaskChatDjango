import signal
import functools
import sys
import asyncio
import aiohttp
import json
import websockets
import random
from mongodb import *


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError:
    return False
  return True

async def login(websocket, path):
    data = await websocket.recv()
    print(is_json(data))
    if is_json(data):
        j = json.loads(data)
        for i in j:
            if i == 'email':
                email = j[i]
            if i == "pass":
                password = j[i]
            if i == "reg":
                data = await websocket.recv()
                users_data = users.insert_one(j).inserted_id
            user = users.find_one({"email":email})
            if user == None:
                msg = 400
            else:
                msg = 200
            await websocket.send(str(msg))
    else:
            await handler(websocket, path)



async def consumer_handler(websocket):
    global glob_messagech
    while True:
        message = await websocket.recv()
        await glob_message.put(message)
        print("this went in glob_message: {}".format(message))

async def producer_handler(websocket):
    global glob_message
    while True:
        message = await glob_message.get()
        await websocket.send(message)

async def handler(websocket, path):
    producer_task = asyncio.ensure_future(producer_handler(websocket))
    consumer_task = asyncio.ensure_future(consumer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()

async def test(websocket, path):
    try:
        await login(websocket, path)
        return False
    except:
        await handler(websocket, path)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    glob_message = asyncio.Queue()
    start_Server = websockets.serve(login, '127.0.0.1', 5678)
    loop.run_until_complete(start_Server)
    loop.run_forever()
    loop.stop()
