import cec
import json
import socket

# cec.transmit(destination, opcode, parameters)


class CecController:
    updateListener = None

    def start(self, ul):
        self.updateListener = ul
        cec.init()
        cec.add_callback(lambda event, *args: self.cb(event, args), cec.EVENT_ALL & ~cec.EVENT_LOG)
        # cec.add_callback(lambda event, level, time, message: self.log_cb(event, level, time, message), cec.EVENT_LOG)
        self._requestCurrentStatus()

    def cb(self, event, *args):
        print("Got event", event, "with data", args)
        self.currentCecState = self._requestCurrentStatus()
        if (self.updateListener != None):
            self.updateListener(self.currentCecState)

    def log_cb(self, event, level, time, message):
        print("CEC Log message:", message)

    def switchToDeviceByBytes(self, physicalAddress):
        cec.transmit(cec.CECDEVICE_BROADCAST, cec.CEC_OPCODE_ACTIVE_SOURCE, physicalAddress)

    def switchToDevice(self, physicalAddress):
        self.switchToDeviceByBytes(socket.inet_aton(physicalAddress))

    def play(self):
        cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_PLAY)

    def pause(self):
        cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_PAUSE)

    def volumeUp(self):
        cec.volume_up();

    def volumeDown(self):
        cec.volume_down();

    def toggleMute(self):
        cec.toggle_mute();

    def powerOn(self):
        cec.Device(cec.CECDEVICE_TV).power_on()

    def powerOff(self):
        cec.Device(cec.CECDEVICE_TV).standby()

    def currentStatus(self):
        return self.currentCecState

    def _requestCurrentStatus(self):
        deviceStatuses = [{
                "name": "unknown",
                "powered": device.is_on(),
                "active": device.is_active(),
                "address": device.address,
                "physical_address": device.physical_address,
                "osd_string": device.osd_string
            } for index, device in cec.list_devices().items()]
        status = {
            "name": "unknown",
            "devices": deviceStatuses
        }
        print(f"current status \n{json.dumps(status)}")
        return status
