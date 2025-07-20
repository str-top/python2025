class Packet:
    
    def __init__(self,src,dst,data):
        self.src = src
        self.dst = dst
        self.data = data
        
class Computer:
    
    def __init__(self,name_comp,router_link):
        self.name_comp = name_comp
        self.router_link = router_link

    def send(self,dst,data):
        packet = Packet(self.name_comp,dst,data)
        self.router_link.route(packet)
    
    def receive(self,packet):
        if not packet.src or not packet.data:
            raise ValueError("Некорректный пакет: поле src или data пустое")
        print(packet.data)

class Router:
    
    def __init__(self):
        self.devices = {}
    
    def connect(self,device):
        self.devices[device.name_comp] = device

    
    def route(self,packet):
        if str(packet.dst) in self.devices:
            self.devices[str(packet.dst)].receive(packet)
            
            
router = Router()
pc1 = Computer('pc1', router)
pc2 = Computer('pc2', router)
pc3 = Computer('pc3', router)
pc4 = Computer('pc4', router)
router.connect(pc1)
router.connect(pc2)
router.connect(pc3)
router.connect(pc4)

pc1.send('pc3', 'Привет от PC1!')
pc3.send('pc1', 'Ответ от PC3!')
pc2.send('pc4', 'PC2 здесь')
pc4.send('pc2', 'Принято')

bad_packet = Packet("src", "dst", "")  
pc1.receive(bad_packet)
