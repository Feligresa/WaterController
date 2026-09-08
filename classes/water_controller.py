import time

try:
    import RPi.GPIO as gpio # type: ignore
except RuntimeError:
    print("Error importing RPi.GPIO. Fallback to test.")
    from .test_gpio import TestGPIO
    gpio = TestGPIO()

from ..main import PUMP_GPIO, WATERING_DUR_SECONDS, PUMP_LOW_PRESSURE
from ..dtos.sensor_data import SensorData


class WaterController:
    def water(self, sensor_data: SensorData):
        gpio.setmode(gpio.BOARD)

        sensors = [sensor_data.sensor1,
                   sensor_data.sensor2,
                   sensor_data.sensor3,
                   sensor_data.sensor4]
        openvalves: list[int] = []

        for sensor in sensors:
            if sensor.get('data') == 1:
                valve = sensor.get('valvegpio')
                if valve is not None:
                    openvalves.append(valve)

        if PUMP_LOW_PRESSURE:
            for valve in openvalves:
                self.toggle_valve(valve)
                self.toggle_pump
                time.sleep(WATERING_DUR_SECONDS)
                self.toggle_pump()
                self.toggle_valve(valve)
        else:
            for valve in openvalves:
                self.toggle_valve(valve)

            self.toggle_pump()
            time.sleep(WATERING_DUR_SECONDS * len(openvalves))
            self.toggle_pump()

            for valve in openvalves:
                self.toggle_valve(valve)
        
        gpio.cleanup()

    def toggle_valve(self, valve: int):
        if gpio.output(valve, False):
            gpio.output(valve, True)
        else:
            gpio.output(valve, False)

    def toggle_pump(self):
        if gpio.output(PUMP_GPIO, False):
            gpio.output(PUMP_GPIO, True)
        else:
            gpio.output(PUMP_GPIO, False)