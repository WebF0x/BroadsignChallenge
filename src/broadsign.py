from src.domain import Domain


def main():
    print('Question 1')
    print('Creating a domain with id=123, name="Broadsign", mac_addresses=[]')
    id = 123
    name = 'Broadsign'
    mac_addresses = []
    domain = Domain(id, name, mac_addresses)
    print(f'Actual content: id={domain.id}, name="{domain.name}", mac_addresses={domain.mac_addresses}')

    print('Question 2')
    d1 = Domain(43690, 'domain 1', [])
    d2 = Domain(48059, 'domain 2', [])
    d3 = Domain(52428, 'domain 3', [])


if __name__ == '__main__':
    main()
