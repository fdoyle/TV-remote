import asyncio
import threading


class FakeCecController:

    def start(self):
        pass


    async def eventStream(self):
        stream_get, stream_put = await make_iter()
        threading.Timer(1000, stream_put).start()
        async for event in stream_get:
            yield event

    def cb(self, event, *args):
        print("Got event", event, "with data", args)

    def log_cb(self, event, level, time, message):
        print("CEC Log message:", message)

    def switchToDevice(self, physicalAddress):
        print(f"Switched to device {physicalAddress}")

    def play(self):
        print("playing")

    def pause(self):
        print("pausing")

    def volumeUp(self):
        print("volume up")

    def volumeDown(self):
        print("volume down")

    def toggleMute(self):
        print("toggling mute")

    def powerOn(self):
        print("powering on")
    
    def powerOff(self):
        print("powering off")

    def currentStatus(self):
        return {
            "devices":[]
        }


    def requestCurrentStatus(self):
        status = {
            "name":"unknown",
            "devices":[]
        }
        return status


async def make_iter():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()
    def put(*args):
        loop.call_soon_threadsafe(queue.put_nowait, args)
    async def get():
        while True:
            yield queue.get()
    return get(), put