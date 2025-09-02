class Packet:
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data
    
    def __str__(self):
        return f"Пакет из {self.src} в {self.dst}: {self.data}"
        
class Computer:
    def __init__(self, name, router):
        self.name = name
        self.router = router
        router.connect(self)

    def send(self, dst, data):
        packet = Packet(self.name, dst, data)
        print(f"{self.name}: Отправка в {dst} - '{data}'")
        self.router.route(packet)

    def receive(self, packet):
        if not packet.src or not packet.data:
            raise ValueError("Некорректный пакет: поле src или data пустое")
        print(f"{self.name}: Получено из {packet.src} - '{packet.data}'")
        
class Router:
    def __init__(self):
        self.devices = {}
        
    def connect(self, device):
        self.devices[device.name] = device
        print(f"Router: {device.name} связанный")
    
    def route(self, packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"Маршрутизатор: Пункт назначения '{packet.dst}' не найден!")
            
router = Router()
pc1 = Computer("PC1", router)
pc2 = Computer("PC2", router)
pc3 = Computer("PC3", router)
pc4 = Computer("PC4", router)
pc1.send("PC3", "Привет от PC1!")
pc3.send("PC1", "Ответ от PC3!")
pc2.send("PC4", "PC2 здесь.")
pc4.send("PC2", "Принято!")

try:
    bad_packet = Packet("", "PC1", "Пустой отправитель")
    pc1.receive(bad_packet)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    bad_packet = Packet("PC2", "PC1", "")
    pc1.receive(bad_packet)
except ValueError as e:
    print(f"Ошибка: {e}")
