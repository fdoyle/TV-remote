class FakeCecController:

    def start(self, ul):
        print("I started")

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


    def _requestCurrentStatus(self):
        devices = cec.listDevices()
        status = {
            "name":"unknown",
            "devices":[]
        }
        return status;