from broadsign.domain import Domain
from broadsign.mac_address import get_domain_id_from_mac_address


def fill_domain_with_n_unique_mac_addresses(domain, nb_unique_addresses):
    for _ in range(nb_unique_addresses):
        mac_address = domain.get_next_unique_mac_address()
        domain.add_mac_address(mac_address)


def print_domain(domain):
    print(f'Domain: "{domain.name}"')
    for i, mac_address in enumerate(domain.mac_addresses):
        print(f'\tAdress #{i}: {mac_address}')


def main():
    print('Question 1')
    print('Creating a domain with id=123, name="Broadsign", mac_addresses=[]')
    id = 123
    name = 'Broadsign'
    mac_addresses = []
    domain = Domain(id, name, mac_addresses)
    print(f'Actual content: id={domain.id}, name="{domain.name}", mac_addresses={domain.mac_addresses}')

    print('Question 2')
    print('\tAssumption: A domain ID is always between 0x0000 and 0xFFFF to fit in the 2 first bytes')
    print('\tAssumption: We want to prevent adding an invalid address or an address to the wrong domain')
    print('Creating the 3 domains')
    d1 = Domain(43690, 'domain 1', [])
    d2 = Domain(48059, 'domain 2', [])
    d3 = Domain(52428, 'domain 3', [])
    print('Filling domains with 10 MAC addresses each')
    fill_domain_with_n_unique_mac_addresses(d1, 10)
    fill_domain_with_n_unique_mac_addresses(d2, 10)
    fill_domain_with_n_unique_mac_addresses(d3, 10)
    print_domain(d1)
    print_domain(d2)
    print_domain(d3)
    print('From a MAC address we can obtain its domain ID')
    print('For example, here is the domain ID of the MAC address "BB:BB:42:42:42:42"')
    domain_id = get_domain_id_from_mac_address('BB:BB:42:42:42:42')
    print(f'ID: {domain_id}')


if __name__ == '__main__':
    main()
