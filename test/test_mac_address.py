import pytest

from broadsign.exceptions import MacAddressTooSmallError
from broadsign.mac_address import int_to_mac_address, get_mac_address_char_length, \
    get_sub_mac_address_char_length


def test_convert_int_to_mac_address():
    assert int_to_mac_address(0, 6) == '00:00:00:00:00:00'
    assert int_to_mac_address(16, 6) == '00:00:00:00:00:10'
    assert int_to_mac_address(20, 6) == '00:00:00:00:00:14'


def test_get_mac_address_char_length():
    assert get_mac_address_char_length(0) == 0
    assert get_mac_address_char_length(1) == 2
    assert get_mac_address_char_length(2) == 5
    assert get_mac_address_char_length(3) == 8
    assert get_mac_address_char_length(6) == 17


def test_get_sub_mac_address_char_length():
    assert get_sub_mac_address_char_length(2) == 0
    assert get_sub_mac_address_char_length(3) == 2
    assert get_sub_mac_address_char_length(4) == 5
    assert get_sub_mac_address_char_length(5) == 8


def test_get_sub_mac_address_char_length_raises_error_when_too_few_bytes():
    with pytest.raises(MacAddressTooSmallError):
        get_sub_mac_address_char_length(0)
    with pytest.raises(MacAddressTooSmallError):
        get_sub_mac_address_char_length(1)
