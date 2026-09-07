from classes.app import App

BASE_URL = ""
PUMP_GPIO = 0
VALVE_GPIO1 = 0
VALVE_GPIO2 = 0
VALVE_GPIO3 = 0
VALVE_GPIO4 = 0

if __name__ == "__main__":
    app = App()
    app.start()