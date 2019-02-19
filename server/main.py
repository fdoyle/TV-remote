from json import JSONDecodeError

import ssdpServer
import asyncio
import websockets
import json
import argparse
import sys
from sqlitedict import SqliteDict
from ssdpServer import SimpleSsdpServer
from cecController import CecController
from fakeCecController import FakeCecController

parser = argparse.ArgumentParser(description='TV remote server')
parser.add_argument('--fakecec', help="Use Fake CEC client", action='store_true')
parser.add_argument('--fakewebsocket',
                    help="Read commands from command line instead of listening for websocket commands",
                    action='store_true')
args = parser.parse_args()
useFakeCec = args.fakecec
useFakeWebsocket = args.fakewebsocket

config = SqliteDict('./config.sqlite', autocommit=True)

# start ssdp listener
# SimpleSsdpServer().start() # Flutter has *extremely* poor multicast support, and no working out of the box SSDP library anyway. We'll just use hard-coded ip's for now

# start HDMI cec server
connected = set()
if (useFakeCec):
    cecController = FakeCecController()
else:
    cecController = CecController()


def handleCecUpdate(cecState):
    cecState['name'] = config.get("name", "Unknown")
    for websocket in connected:
        websocket.send(json.dumps(cecState))


cecController.start(handleCecUpdate)


# start Websocket server

async def handleConnection(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            await handleMessage(message)
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

if (not useFakeWebsocket):
    start_server = websockets.serve(handleConnection, 'localhost', 8765)
else:
    for line in sys.stdin:
        handleMessage(line.rstrip())
