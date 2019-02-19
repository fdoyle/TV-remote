import uuid
from lib.ssdp import SSDPServer
from lib.getIp import get_network_interface_ip_address

NETWORK_INTERFACE = "en0"


class SimpleSsdpServer:
    def start(self):
        device_uuid = uuid.uuid4()
        local_ip_address = get_network_interface_ip_address(NETWORK_INTERFACE)
        ssdp = SSDPServer()
        print("Starting SSDP server on {local_ip_address}")
        ssdp.register('local',
                      'uuid:{}::urn:Lacronicus:remote'.format(device_uuid),
                      'urn:Lacronicus:remote',
                      'http://{}:8765'.format(local_ip_address))
        ssdp.run()
        print("Running SSDP server...")
