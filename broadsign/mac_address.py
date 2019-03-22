import netaddr
from netaddr import EUI

from broadsign.exceptions import InvalidMacAddressFormat

SUB_MAC_ADDRESS_CHAR_LENGTH = 11
DOMAIN_ID_CHAR_LENGTH = 5
MAC_ADDRESS_CHAR_LENGTH = len('00:00:00:00:00:00')


def make_mac_address(domain_id, sub_mac_address):
    if len(domain_id) != DOMAIN_ID_CHAR_LENGTH:
        raise InvalidMacAddressFormat()
    if len(sub_mac_address) != SUB_MAC_ADDRESS_CHAR_LENGTH:
        raise InvalidMacAddressFormat()
    try:
        return EUI(domain_id + ':' + sub_mac_address)
    except netaddr.core.AddrFormatError:
        raise InvalidMacAddressFormat()
