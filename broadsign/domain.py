import netaddr
from netaddr import EUI

from broadsign.exceptions import InvalidMacAddressFormat, InvalidMacAddressDomain
from broadsign.mac_address import MAC_ADDRESS_CHAR_LENGTH, DOMAIN_ID_CHAR_LENGTH, int_to_mac_address


class Domain(object):
    def __init__(self, id, name, mac_addresses):
        self.id = id
        self.name = name
        self.mac_addresses = mac_addresses

    def add_mac_address(self, mac_address):
        try:
            eui_mac_address = EUI(mac_address)
        except netaddr.core.AddrFormatError:
            raise InvalidMacAddressFormat()
        if len(mac_address) != MAC_ADDRESS_CHAR_LENGTH:
            raise InvalidMacAddressFormat()
        if not self.is_mac_address_matching_id(mac_address):
            raise InvalidMacAddressDomain()
        self.mac_addresses.append(eui_mac_address)

    def is_mac_address_matching_id(self, mac_address):
        domain_id = mac_address[:DOMAIN_ID_CHAR_LENGTH]
        hexadecimal_domain_id = domain_id.replace(':', '')
        return int(hexadecimal_domain_id, 16) == self.id

    def get_next_unique_mac_address(self):
        min_address = self.id * 16 ** 8
        max_address = (self.id + 1) * 16 ** 8 - 1
        for potential_next_address in range(min_address, max_address + 1):
            if potential_next_address not in self.mac_addresses:
                return int_to_mac_address(potential_next_address)
        raise Exception()
