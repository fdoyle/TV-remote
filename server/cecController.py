import asyncio

import cec
import json
import socket

# cec.transmit(destination, opcode, parameters)

def addressStringToBytes(physicalAddressString):
    split = physicalAddressString.split(".")  # ["1","2","3","4"]
    splitInt = [int(str) for str in split]  # [1,2,3,4]
    b1 = splitInt[0]
    b2 = splitInt[1]
    b3 = splitInt[2]
    b4 = splitInt[3]
    first = int(str(b1 * 10 + b2), 16)
    second = int(str(b3 * 10 + b4), 16)
    return bytes([first, second])

class CecController:
    updateListener = None

    currentCecState = None

    def start(self):
        cec.init()
        # cec.add_callback(lambda event, *args: self.cb(event, args), cec.EVENT_ALL & ~cec.EVENT_LOG)
        # cec.add_callback(lambda event, level, time, message: self.log_cb(event, level, time, message), cec.EVENT_LOG)
        self.requestCurrentStatus()

    def addCallback(self, cb):
        cec.add_callback(lambda event, *args: cb(event), cec.EVENT_ALL & ~cec.EVENT_LOG)


    def log_cb(self, event, level, time, message):
        print("CEC Log message:", message)

    def switchToDeviceByBytes(self, physicalAddress):
        print(f"Switching to device byte {physicalAddress}")
        cec.transmit(cec.CECDEVICE_BROADCAST, cec.CEC_OPCODE_ACTIVE_SOURCE, physicalAddress)



    def switchToDevice(self, physicalAddress):
        print(f"Switching to device {physicalAddress}")
        self.switchToDeviceByBytes(addressStringToBytes(physicalAddress))

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

    def requestCurrentStatus(self):
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
        self.currentCecState = status


