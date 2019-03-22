import netaddr
from netaddr import EUI

from broadsign.exceptions import InvalidMacAddressFormat
from broadsign.mac_address import MAC_ADDRESS_CHAR_LENGTH


class Domain(object):
    def __init__(self, id, name, mac_addresses):
        self.id = id
        self.name = name
        self.mac_addresses = mac_addresses

    def add_mac_address(self, mac_address):
        if len(mac_address) != MAC_ADDRESS_CHAR_LENGTH:
            raise InvalidMacAddressFormat()
        try:
            self.mac_addresses.append(EUI(mac_address))
        except netaddr.core.AddrFormatError:
            raise InvalidMacAddressFormat()
