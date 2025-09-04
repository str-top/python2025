class Packet:
    def __init__(self, src_mac, dst_mac, data, broadcast=False):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.data = data
        self.broadcast = broadcast
    
    def __str__(self):
        if self.broadcast:
            return f"Broadcast Packet from {self.src_mac}: {self.data}"
        return f"Packet from {self.src_mac} to {self.dst_mac}: {self.data}"

class Router:
    def __init__(self):
        self.devices = {}
    
    def connect(self, device):
        self.devices[device.mac_address] = device
        print(f"Устройство {device.name} (MAC: {device.mac_address}) подключено к роутеру")
    
    def route(self, packet):
        if packet.broadcast:
            print(f"Роутер: Широковещательная рассылка от {packet.src_mac}")
            for mac, device in self.devices.items():
                if mac != packet.src_mac:
                    device.receive(packet)
        elif packet.dst_mac in self.devices:
            print(f"Роутер: Пересылаю пакет от {packet.src_mac} к {packet.dst_mac}")
            self.devices[packet.dst_mac].receive(packet)
        else:
            print(f"Роутер: Ошибка! Устройство с MAC {packet.dst_mac} не найдено")

class Computer:
    def __init__(self, name, router):
        self.name = name
        self.router = router
        self.mac_address = self._generate_mac_address()
    
    def _generate_mac_address(self):
        mac_parts = []
        for i in range(6):
            char_code = ord(self.name[i % len(self.name)]) if self.name else 0
            mac_part = (char_code + i * 17) % 256
            mac_parts.append(f"{mac_part:02x}")
        return ":".join(mac_parts)
    
    def _validate_packet(self, packet):
        if not packet.src_mac or packet.src_mac.strip() == "":
            print(f"ОШИБКА: Пустой MAC-адрес отправителя в пакете!")
            exit(1)
        if not packet.data or packet.data.strip() == "":
            print(f"ОШИБКА: Пустое сообщение в пакете от {packet.src_mac}!")
            exit(1)
        return True
    
    def send(self, dst_mac, data):
        print(f"{self.name} ({self.mac_address}): Отправляю сообщение для {dst_mac}")
        packet = Packet(self.mac_address, dst_mac, data)
        self.router.route(packet)
    
    def send_broadcast(self, data):
        print(f"{self.name} ({self.mac_address}): Отправляю широковещательное сообщение")
        broadcast_packet = Packet(self.mac_address, "ff:ff:ff:ff:ff:ff", data, broadcast=True)
        self.router.route(broadcast_packet)
    
    def receive(self, packet):
        self._validate_packet(packet)
        if packet.broadcast:
            print(f"{self.name} ({self.mac_address}): Получено широковещательное сообщение от {packet.src_mac}: '{packet.data}'")
        else:
            print(f"{self.name} ({self.mac_address}): Получено сообщение от {packet.src_mac}: '{packet.data}'")

router = Router()

pc1 = Computer("PC1", router)
pc2 = Computer("PC2", router)
pc3 = Computer("PC3", router)
pc4 = Computer("PC4", router)

router.connect(pc1)
router.connect(pc2)
router.connect(pc3)
router.connect(pc4)

pc1.send(pc3.mac_address, "Привет от PC1!")
pc3.send(pc1.mac_address, "Ответ от PC3!")
pc2.send(pc4.mac_address, "PC2 здесь.")
pc4.send(pc2.mac_address, "Принято!")
pc2.send_broadcast("Всем привет! Это широковещательное сообщение от PC2!")

try:
    invalid_packet = Packet(pc1.mac_address, pc2.mac_address, "")
    pc2.receive(invalid_packet)
except SystemExit:
    print("Программа завершена из-за некорректного пакета")
