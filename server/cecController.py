
#cec.transmit(destination, opcode, parameters)


class CecController:
    updateListener = None

    def start(ul):
        updateListener = ul
        cec.init()
        cec.add_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
        cec.add_callback(log_cb, cec.EVENT_LOG)

    def cb(event, *args):
        print("Got event", event, "with data", args)
        currentCecState = _requestCurrentStatus()
        if(updateListener != None):
            updateListener(currentCecState)

    def log_cb(event, level, time, message):
        print("CEC Log message:", message)

    def switchToDevice(physicalAddress):
        cec.transmit(cec.CECDEVICE_BROADCAST, cec.CEC_OPCODE_ACTIVE_SOURCE, target)

    def play():
        cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_PLAY)

    def pause():
        cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_PAUSE)

    def volumeUp():
        cec.volume_up();

    def volumeDown():
        cec.volume_down();

    def toggleMute():
        cec.toggle_mute();

    def powerOn():
        cec.Device(cec.CECDEVICE_TV).power_on()
    
    def powerOff():
        cec.Device(cec.CECDEVICE_TV).standby()

    def currentStatus():
        return currentCecState


    def _requestCurrentStatus():
        devices = cec.listDevices()
        status = {
            "name":"unknown",
            "devices":map(lambda device: {
                "name":"unknown",
                "powered":device.is_on(),
                "active":device.is_active(),
                "address":device.address,
                "physical_address":device.physical_address,
                "osd_string":device.osd_string
            })
        }
        return status;