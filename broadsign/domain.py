from broadsign.exceptions import MacAddressFormatError, MacAddressDomainError
from broadsign.mac_address import DOMAIN_ID_CHAR_LENGTH, int_to_mac_address, \
    is_valid_mac_address


class Domain(object):
    def __init__(self, id, name, mac_addresses, nb_bytes_in_mac_address=6):
        self.id = id
        self.name = name
        self.mac_addresses = mac_addresses
        self.nb_bytes_in_mac_address = nb_bytes_in_mac_address

    def add_mac_address(self, mac_address):
        if not is_valid_mac_address(mac_address, self.nb_bytes_in_mac_address):
            raise MacAddressFormatError()
        if not self.is_mac_address_matching_id(mac_address):
            raise MacAddressDomainError()
        self.mac_addresses.append(mac_address)

    def is_mac_address_matching_id(self, mac_address):
        domain_id = mac_address[:DOMAIN_ID_CHAR_LENGTH]
        hexadecimal_domain_id = domain_id.replace(':', '')
        return int(hexadecimal_domain_id, 16) == self.id

    def get_next_unique_mac_address(self):
        for potential_next_address in range(self.get_min_address(), self.get_max_address() + 1):
            mac_address_string = int_to_mac_address(potential_next_address, self.nb_bytes_in_mac_address)
            if mac_address_string not in self.mac_addresses:
                return mac_address_string
        return None

    def get_min_address(self):
        return self.id * 256 ** (self.nb_bytes_in_mac_address - 2)

    def get_max_address(self):
        return (self.id + 1) * 256 ** (self.nb_bytes_in_mac_address - 2) - 1
