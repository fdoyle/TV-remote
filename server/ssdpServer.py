import threading
import uuid
from lib.ssdp import SSDPServer
from lib.getIp import get_network_interface_ip_address

NETWORK_INTERFACE = "en0"


class SimpleSsdpServer(threading.Thread):
    def run(self):
        device_uuid = uuid.uuid4()
        local_ip_address = get_network_interface_ip_address(NETWORK_INTERFACE)
        ssdp = SSDPServer()
        print(f"Starting SSDP server on {local_ip_address}")
        ssdp.register('localhost',
                      'uuid:{}::upnp:rootdevice'.format(device_uuid),
                        'upnp:lacronicus',
              'http://{}:8088/remote.xml'.format(local_ip_address))
        ssdp.run()
        print("Running SSDP server...")