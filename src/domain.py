import netaddr
from netaddr import EUI

from src.exceptions import InvalidMacAddressFormat


class Domain(object):
    def __init__(self, id, name, mac_addresses):
        self.id = id
        self.name = name
        self.mac_addresses = mac_addresses

    def add_mac_address(self, mac_address):
        try:
            self.mac_addresses.append(EUI(mac_address))
        except netaddr.core.AddrFormatError:
            raise InvalidMacAddressFormat()
