import ipaddress


def parse_input(ip_input):
    try:
        # Parse IP address or CIDR notation
        ip = ipaddress.ip_interface(ip_input)
        return ip.network
    except ValueError as e:
        print("Error:", e)
        return None


def subnet_calc(ip_network, prefix_size):
    # Calculate subnets based on the given prefix size
    ip = ipaddress.ip_network(f'{ip_network}/{prefix_size}', strict=False)
    subnets = list(ip.subnets())

    print(f"Prefix Size: /{prefix_size}")
    print(f"Network Mask: {ip.netmask}")
    print(f"Usable IP Count: {subnets[0].num_addresses - 2}")  # Excluding network and broadcast addresses

    print("\nSubnets:")
    for i, subnet in enumerate(subnets):
        print(f"\nSubnet {i + 1}:")
        print(f"Start IP: {subnet.network_address}")
        print(f"End IP: {subnet.broadcast_address}")
        print(f"Total IP Count: {subnet.num_addresses}")
        print(f"Usable IP Count: {subnet.num_addresses - 2}")


# Get input from the user
ip_input = input("Enter IP Address or CIDR notation (e.g., 192.168.1.0/24): ")

# Parse and process the input
ip_network = parse_input(ip_input)
if ip_network:
    prefix_size = int(input("Enter prefix size (e.g., 24): "))
    subnet_calc(ip_network.network_address, prefix_size)
