import threading
import traceback
import uuid
from json import JSONDecodeError

import ssdpServer
import asyncio
import websockets
import json
import argparse
import sys
from sqlitedict import SqliteDict

from lib.getIp import get_network_interface_ip_address
from lib.upnp_http_server import UPNPHTTPServer
from ssdpServer import SimpleSsdpServer
from cecController import CecController
from fakeCecController import FakeCecController

parser = argparse.ArgumentParser(description='TV remote server')
parser.add_argument('--fakecec', help="Use Fake CEC client", action='store_true')
parser.add_argument('--fakewebsocket',
                    help="Read commands from command line instead of listening for websocket commands",
                    action='store_true')
parser.add_argument('--interface',
                    help="network interface",
                    default="wlan0")

args = parser.parse_args()
useFakeCec = args.fakecec
useFakeWebsocket = args.fakewebsocket

networkInterface = args.interface
print(f"using interface {networkInterface}")

config = SqliteDict('./config.sqlite', autocommit=True)

# start ssdp listener
SimpleSsdpServer(networkInterface).start()

# start ssdp web server
device_uuid = uuid.uuid4()

local_ip_address = get_network_interface_ip_address(networkInterface)

http_server = UPNPHTTPServer(8088,
                             friendly_name="TV Remote",
                             manufacturer="Frank D",
                             manufacturer_url='',
                             model_description='FrankDs TV remote',
                             model_name="TV Remote",
                             model_number="1",
                             model_url="",
                             serial_number="1",
                             uuid=device_uuid,
                             presentation_url="http://{}:8765/".format(local_ip_address))
http_server.start()

# start HDMI cec server
connected = set()
if (useFakeCec):
    cecController = FakeCecController()
else:
    cecController = CecController()


async def handleCecUpdateAsync(cecState):
    print("handling cec update async")
    cecState['name'] = config.get("name", "Unknown")
    # print(f"handling CEC update {cecState}")
    # print(f"connected devices: {len(connected)}")
    for websocket in connected:
        await websocket.send(json.dumps(cecState))
        print(f"sending {json.dumps(cecState)} to {websocket.remote_address}")


# start Websocket server

async def handleConnection(websocket, path):
    print("Client connected")
    connected.add(websocket)
    await websocket.send(json.dumps(cecController.currentStatus()))
    try:
        async for message in websocket:
            await handleMessageAsync(message)
            await websocket.send(json.dumps(cecController.currentStatus()))

    finally:
        connected.remove(websocket)


async def handleMessageAsync(message):
    handleMessage(message)


def handleMessage(message):
    print(f"< {message}")
    try:
        messageDict = json.loads(message)
        command = messageDict['command']
        target = messageDict.get('target', None)
        if (command == "play"):
            cecController.play()
        elif (command == "pause"):
            cecController.pause()
        elif (command == "status"):
            cecController.currentStatus()
        elif (command == "power_on"):
            cecController.powerOn()
        elif (command == "power_off"):
            cecController.powerOff()
        elif (command == "volume_up"):
            cecController.powerOff()
        elif (command == "volume_down"):
            cecController.powerOff()
        elif (command == "switch"):
            cecController.switchToDevice(target)
        elif (command == "rename"):
            newName = messageDict.get("new_name", None)
            if (newName != None and not newName.isspace()):
                config["name"] = newName

    except JSONDecodeError as e:
        print(e)
    except KeyError as e:
        print(e)


async def make_iter():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    def put(*args):
        loop.call_soon_threadsafe(queue.put_nowait, args)

    async def get():
        while True:
            yield queue.get()

    return get(), put


async def main():
    print("starting server")
    await websockets.serve(handleConnection, '', 8765)

    cecController.start()

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    def put(*args):
        loop.call_soon_threadsafe(queue.put_nowait, args)

    async def get():
        while True:
            result = await queue.get()
            print("got item from queue")
            yield result

    cecController.addCallback(put)

    async for state in get():
        cecController.requestCurrentStatus()
        await handleCecUpdateAsync(cecController.currentStatus())


if (not useFakeWebsocket):
    print("running event loop forever")
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_forever()

else:
    for line in sys.stdin:
        handleMessage(line.rstrip())
