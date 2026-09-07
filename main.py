import sys
from classes.app import App

BASE_URL = ""
PUMP_GPIO = 0
# Plant IDs are sorted low to high
VALVE_GPIO1 = 0
VALVE_GPIO2 = 0
VALVE_GPIO3 = 0
VALVE_GPIO4 = 0

try:
    with open('ApiKey.txt', 'r') as f:
        API_KEY = f.read()
except:
    print('Missing ApiKey.txt')
    sys.exit(1)


if __name__ == "__main__":
    app = App()
    app.start()