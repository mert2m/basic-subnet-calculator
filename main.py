import ipaddress

def parse_input(ip_input):
    try:
        # IP adresini veya CIDR notasyonunu ayrıştır
        ip = ipaddress.ip_interface(ip_input)
        return ip.network
    except ValueError as e:
        print("Hata:", e)
        return None

def subnet_calc(ip_network, prefix_size):
    # Verilen prefix boyutuna göre alt ağları hesapla
    ip = ipaddress.ip_network(f'{ip_network}/{prefix_size}', strict=False)
    subnets = list(ip.subnets())

    print(f"Prefix Boyutu: /{prefix_size}")
    print(f"Network Maskesi: {ip.netmask}")
    print(f"Kullanılabilir IP Sayısı: {subnets[0].num_addresses - 2}")  # Network ve Broadcast adresleri hariç

    print("\nAlt Ağlar:")
    for i, subnet in enumerate(subnets):
        print(f"\nAlt Ağ {i+1}:")
        print(f"Başlangıç IP: {subnet.network_address}")
        print(f"Bitiş IP: {subnet.broadcast_address}")
        print(f"Toplam IP Sayısı: {subnet.num_addresses}")
        print(f"Kullanılabilir IP Sayısı: {subnet.num_addresses - 2}")

# Kullanıcıdan bilgileri al
ip_input = input("IP Adresi veya CIDR notasyonu girin (örn. 192.168.1.0/24): ")

# Girdiyi analiz et ve işle
ip_network = parse_input(ip_input)
if ip_network:
    prefix_size = int(input("Prefix boyutu girin (örn. 24): "))
    subnet_calc(ip_network.network_address, prefix_size)
