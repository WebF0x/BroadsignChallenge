import pytest

from broadsign.domain import Domain

from broadsign.exceptions import InvalidMacAddressFormat


def test_constructor():
    id = 123
    name = 'Broadsign'
    mac_addresses = []
    domain = Domain(id, name, mac_addresses)
    assert domain.id == 123
    assert domain.name == 'Broadsign'
    assert domain.mac_addresses == []


def test_add_valid_mac_address():
    domain = Domain(None, None, [])
    domain.add_mac_address('00:00:00:00:00:00')
    assert domain.mac_addresses[0] == '00:00:00:00:00:00'
    domain.add_mac_address('00:00:00:00:00:01')
    assert domain.mac_addresses[1] == '00:00:00:00:00:01'
    domain.add_mac_address('FF:FF:FF:FF:FF:FF')
    assert domain.mac_addresses[2] == 'FF:FF:FF:FF:FF:FF'


def test_add_mac_address_with_invalid_character_raises_invalid_mac_address_format_exception():
    domain = Domain(None, None, [])
    with pytest.raises(InvalidMacAddressFormat):
        domain.add_mac_address('GG:GG:GG:GG:GG:GG')


def test_add_mac_address_with_too_few_characters_raises_invalid_mac_address_format_exception():
    domain = Domain(None, None, [])
    with pytest.raises(InvalidMacAddressFormat):
        domain.add_mac_address('00:00:00')
