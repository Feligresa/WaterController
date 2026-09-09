import sys

BASE_URL = "http://192.168.189.22"
INTERVAL_SECONDS = 900
WATERING_DUR_SECONDS = 10

# If the pump is low pressure, set to True.
# Will water each plant sequentially to avoid uneven watering.
PUMP_LOW_PRESSURE = False

PUMP_GPIO = 0
# Plant IDs are sorted low to high
VALVE_GPIO1 = 0
VALVE_GPIO2 = 0
VALVE_GPIO3 = 0
VALVE_GPIO4 = 0

try:
    with open('ApiKey.txt', 'r') as f:
        API_KEY = f.read()
except FileNotFoundError:
    print('Missing ApiKey.txt')
    sys.exit(1)
