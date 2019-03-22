from textwrap import wrap

import netaddr
from netaddr import EUI

from broadsign.exceptions import InvalidMacAddressFormat

MAC_ADDRESS_CHAR_LENGTH = len('00:00:00:00:00:00')
DOMAIN_ID_CHAR_LENGTH = len('00:00')
SUB_MAC_ADDRESS_CHAR_LENGTH = len('00:00:00:00')


def make_mac_address(domain_id, sub_mac_address):
    if len(domain_id) != DOMAIN_ID_CHAR_LENGTH:
        raise InvalidMacAddressFormat()
    if len(sub_mac_address) != SUB_MAC_ADDRESS_CHAR_LENGTH:
        raise InvalidMacAddressFormat()
    try:
        return EUI(domain_id + ':' + sub_mac_address)
    except netaddr.core.AddrFormatError:
        raise InvalidMacAddressFormat()


def int_to_mac_address(int_address):
    hex_address = format(int_address, 'X')
    left_padded_hex_address = hex_address.zfill(12)
    address_bytes = wrap(left_padded_hex_address, 2)
    return ':'.join(address_bytes)
