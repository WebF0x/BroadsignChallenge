import pytest

from broadsign.domain import Domain

from broadsign.exceptions import MacAddressFormatError, MacAddressDomainError
from broadsign.mac_address import int_to_mac_address


def test_constructor():
    id = 123
    name = 'Broadsign'
    mac_addresses = []
    domain = Domain(id, name, mac_addresses)
    assert domain.id == 123
    assert domain.name == 'Broadsign'
    assert domain.mac_addresses == []


def test_add_valid_mac_address():
    domain = Domain(int('1234', 16), None, [])
    domain.add_mac_address('12:34:56:78:9A:BC')
    assert domain.mac_addresses[0] == '12:34:56:78:9A:BC'


def test_add_mac_address_with_invalid_character_raises_invalid_mac_address_format_exception():
    with pytest.raises(MacAddressFormatError):
        Domain(None, None, []).add_mac_address('GG:GG:GG:GG:GG:GG')


def test_add_mac_address_with_too_few_characters_raises_invalid_mac_address_format_exception():
    with pytest.raises(MacAddressFormatError):
        Domain(None, None, []).add_mac_address('00:00:00')


def test_prevent_adding_mac_addresses_that_do_not_match_the_domain_id():
    with pytest.raises(MacAddressDomainError):
        Domain(int('0000', 16), None, []).add_mac_address('00:01:00:00:00:00')
    with pytest.raises(MacAddressDomainError):
        Domain(int('0000', 16), None, []).add_mac_address('FF:FF:00:00:00:00')
    with pytest.raises(MacAddressDomainError):
        Domain(int('FFFF', 16), None, []).add_mac_address('FF:FE:00:00:00:00')


def test_get_next_unique_mac_address_when_domain_is_empty():
    domain = Domain(int('1234', 16), None, [])
    assert domain.get_next_unique_mac_address() == '12:34:00:00:00:00'


def test_get_next_unique_mac_address_when_domain_contains_addresses_already():
    domain = Domain(int('1234', 16), None, [])
    domain.add_mac_address('12:34:00:00:00:00')
    domain.add_mac_address('12:34:00:00:00:01')
    domain.add_mac_address('12:34:00:00:00:02')
    assert domain.get_next_unique_mac_address() == '12:34:00:00:00:03'


def test_get_next_unique_mac_address_when_domain_is_full_raises_exception():
    domain = Domain(int('1234', 16), None, [], 3)
    for mac_address in range(int('123400', 16), int('123500', 16)):
        domain.add_mac_address(int_to_mac_address(mac_address, 3))
    assert domain.get_next_unique_mac_address() is None


def test_get_min_address():
    assert Domain(int('0000', 16), None, [], 3).get_min_address() == 0
    assert Domain(int('0001', 16), None, [], 3).get_min_address() == 256


def test_get_max_address():
    assert Domain(int('0000', 16), None, [], 3).get_max_address() == 255
    assert Domain(int('0001', 16), None, [], 3).get_max_address() == 511
