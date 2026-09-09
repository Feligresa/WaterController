import time
from config import INTERVAL_SECONDS
from classes.water_controller import WaterController
from classes.fetcher import Fetcher

class App:
    def __init__(self):
        self.fetcher = Fetcher()
        self.water_controller = WaterController()

    def start(self):
        while True:
            sensor_data = self.fetcher.get_latest_sensors()

            self.water_controller.water(sensor_data)

            time.sleep(INTERVAL_SECONDS)