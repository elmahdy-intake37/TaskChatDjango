import asyncio
import json
import websockets
from mongodb import *


class WebSocketRequest:
    def __init__(self, websocket):
        self.websocket = websocket

    async def login(self):
        data = await self.websocket.recv()
        j = json.loads(data)
        for i in j:
            if i == 'email':
                email = j[i]
            if i == "pass":
                password = j[i]
        user = users.find_one({"email":email})
        if user == None:
            msg = 400
        else:
            msg = 200
        await websocket.send(str(msg))

    async def register(self):
        data = await self.websocket.recv()
        j = json.loads(data)
        print(j)

    async def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.ensure_future(self.login())
        asyncio.ensure_future(self.register())
        loop.run_forever()

class WebsocketServer:
    def __init__(self, localhost,port):
        self.localhost = localhost
        self.port = port


    async def hello(self, websocket, path):
        req = WebSocketRequest(websocket)
        await req.run()

    def run(self):
        print("opening")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        start_server = websockets.serve(self.hello, self.localhost, self.port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
if __name__=='__main__':
    localhost, port = '127.0.0.1', 5678
    web = WebsocketServer(localhost, port)
    web.run()
