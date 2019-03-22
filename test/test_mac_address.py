import pytest

from broadsign.mac_address import make_mac_address, int_to_mac_address
from broadsign.exceptions import InvalidMacAddressFormat


def test_make_valid_mac_address():
    assert make_mac_address('00:00', '00:00:00:00') == '00:00:00:00:00:00'
    assert make_mac_address('00:01', '00:00:00:00') == '00:01:00:00:00:00'
    assert make_mac_address('00:00', '00:00:00:01') == '00:00:00:00:00:01'
    assert make_mac_address('AB:CD', '00:00:00:00') == 'AB:CD:00:00:00:00'
    assert make_mac_address('00:00', 'AB:CD:EF:FF') == '00:00:AB:CD:EF:FF'
    assert make_mac_address('00:00', 'FF:FF:FF:FF') == '00:00:FF:FF:FF:FF'


def test_make_mac_address_with_bad_domain_id_raises_invalid_mac_address_format_exception():
    with pytest.raises(InvalidMacAddressFormat):
        make_mac_address('GG:GG', '00:00:00:00')
    with pytest.raises(InvalidMacAddressFormat):
        make_mac_address('00', '00:00:00:00')


def test_make_mac_address_with_bad_sub_mac_address_raises_invalid_mac_address_format_exception():
    with pytest.raises(InvalidMacAddressFormat):
        make_mac_address('00:00', 'GG:GG:GG:GG')
    with pytest.raises(InvalidMacAddressFormat):
        make_mac_address('00:00', '00')


# We want to avoid the case where concatenating a bad domain id and a bad sub MAC address would create a valid result
def test_add_mac_address_with_both_bad_parameters_raises_invalid_mac_address_format_exception():
    with pytest.raises(InvalidMacAddressFormat):
        make_mac_address('00:00:00', '00:00:00')


def test_convert_int_to_mac_address():
    assert int_to_mac_address(0) == '00:00:00:00:00:00'
    assert int_to_mac_address(16) == '00:00:00:00:00:10'
    assert int_to_mac_address(20) == '00:00:00:00:00:14'
