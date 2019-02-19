class FakeCecController:

    def start(ul):
        print("I started")

    def cb(event, *args):
        print("Got event", event, "with data", args)

    def log_cb(event, level, time, message):
        print("CEC Log message:", message)

    def switchToDevice(physicalAddress):
        print("Switched to device {physicalAddress}")

    def play():
        print("playing")

    def pause():
        print("pausing")

    def volumeUp():
        print("volume up")

    def volumeDown():
        print("volume down")

    def toggleMute():
        print("toggling mute")

    def powerOn():
        print("powering on")
    
    def powerOff():
        print("powering off")

    def currentStatus():
        return {
            "devices":[]
        }


    def _requestCurrentStatus():
        devices = cec.listDevices()
        status = {
            "name":"unknown",
            "devices":[]
        }
        return status;