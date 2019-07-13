import signal
import functools
import sys
import asyncio
import aiohttp
import json
import websockets
import random
from mongodb import *

loop = asyncio.get_event_loop()
async def register(websocket, path):
    data = await websocket.recv()
    j = json.loads(data)
    users_data = users.insert_one(j).inserted_id


start_Server = websockets.serve(register, '127.0.0.2', 5679)
loop.run_until_complete(start_Server)
loop.run_forever()
loop.close()
