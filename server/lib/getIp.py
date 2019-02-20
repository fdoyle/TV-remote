import netifaces as ni

# NETWORK_INTERFACE = "en0"
def get_network_interface_ip_address(interface='eth0'):
    """
    Get the first IP address of a network interface.
    :param interface: The name of the interface.
    :return: The IP address.
    """
    while True:
        if interface not in ni.interfaces():
            print('Could not find interface %s.' % (interface,))
            exit(1)
        interface = ni.ifaddresses(interface)
        if (2 not in interface) or (len(interface[2]) == 0):
            print('Could not find IP of interface %s. Sleeping.' % (interface,))
            continue
        return interface[2][0]['addr']
