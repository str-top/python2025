class Observer:
    def update(self, temperature):
        raise NotImplementedError("Метод update должен быть переопределен")

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature):
        print(f"\n[WeatherStation] Новая температура: {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"[PhoneDisplay] Новая температура: {temperature}°C")

class WebDisplay(Observer):
    def update(self, temperature):
        print(f"[WebDisplay] Новая температура: {temperature}°C")


station = WeatherStation()

phone = PhoneDisplay()
web = WebDisplay()

station.add_observer(phone)
station.add_observer(web)

station.set_temperature(27)
station.set_temperature(34)

station.remove_observer(phone)
station.set_temperature(44)
