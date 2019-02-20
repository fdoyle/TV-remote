import asyncio
import threading


class FakeCecController:

    def start(self):
        pass

    def addCallback(self, cb):
        self._startTimer(cb)

    def _startTimer(self,cb):
        cb()
        threading.Timer(1, self._startTimer, [cb]).start()


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