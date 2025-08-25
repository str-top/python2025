class Watcher:
    def on_change(self, value):
        raise NotImplementedError("Нужно реализовать в дочернем классе")

class Thermometer:
    def __init__(self):
        self._watchers = []
        self._current_temp = 20
    
    def subscribe(self, watcher):
        if watcher not in self._watchers:
            self._watchers.append(watcher)
    
    def unsubscribe(self, watcher):
        if watcher in self._watchers:
            self._watchers.remove(watcher)
    
    def change_temp(self, new_temp):
        print(f"Термометр показывает: было {self._current_temp}C, стало {new_temp}C")
        self._current_temp = new_temp
        self._alert_watchers()
    
    def _alert_watchers(self):
        for watcher in self._watchers:
            watcher.on_change(self._current_temp)

class MobileApp(Watcher):
    def on_change(self, value):
        print(f"На телефоне: {value}C")

class BrowserWidget(Watcher):
    def on_change(self, value):
        print(f"В браузере: {value}C")

class SmartWatch(Watcher):
    def on_change(self, value):
        print(f"На часах: {value}C")

if __name__ == "__main__":
    main_thermometer = Thermometer()
    
    phone_app = MobileApp()
    browser_app = BrowserWidget()
    watch_app = SmartWatch()
    
    main_thermometer.subscribe(phone_app)
    main_thermometer.subscribe(browser_app)
    main_thermometer.subscribe(watch_app)
    
    main_thermometer.change_temp(13)
    main_thermometer.change_temp(25)
    
    main_thermometer.unsubscribe(phone_app)
    
    main_thermometer.change_temp(26)
