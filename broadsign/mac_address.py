import re
from textwrap import wrap

from broadsign.exceptions import MacAddressTooSmallError

DOMAIN_ID_CHAR_LENGTH = len('00:00')


def is_valid_mac_address(mac_address, nb_bytes_in_mac_address):
    regexp_string = '(?:[0-9a-fA-F]:?){%s}' % (nb_bytes_in_mac_address * 2)
    mac_address_regexp = re.compile(regexp_string)
    return mac_address_regexp.match(mac_address)


def int_to_mac_address(int_address, nb_bytes_in_mac_address):
    hex_address = format(int_address, 'X')
    left_padded_hex_address = hex_address.zfill(nb_bytes_in_mac_address * 2)
    address_bytes = wrap(left_padded_hex_address, 2)
    return ':'.join(address_bytes)


def get_mac_address_char_length(nb_bytes_in_mac_address):
    nb_digits = nb_bytes_in_mac_address * 2
    nb_colons = nb_bytes_in_mac_address - 1 if nb_bytes_in_mac_address else 0
    return nb_digits + nb_colons


def get_sub_mac_address_char_length(nb_bytes_in_mac_address):
    if nb_bytes_in_mac_address < 2:
        raise MacAddressTooSmallError()
    if nb_bytes_in_mac_address == 2:
        return 0
    return get_mac_address_char_length(nb_bytes_in_mac_address) - DOMAIN_ID_CHAR_LENGTH - 1


def get_domain_id_from_mac_address(mac_address):
    domain_string = mac_address[:5]
    domain_id_hex = domain_string.replace(':', '')
    return int(domain_id_hex, 16)
