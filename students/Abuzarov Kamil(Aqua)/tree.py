def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance
 
@singleton
class Configuration:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        # Загрузка конфигурации
 
# Использование
config = Configuration('settings.json')
