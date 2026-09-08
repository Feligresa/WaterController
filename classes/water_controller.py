import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO. Fallback to test.")
    from .test_gpio import TestGPIO
    GPIO = TestGPIO()

from ..main import PUMP_GPIO, WATERING_DUR_SECONDS
from ..dtos.sensor_data import SensorData


class WaterController:
    def water(self, sensor_data: SensorData):
        GPIO.setmode(GPIO.BOARD)

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

        for valve in openvalves:
            self.toggle_valve(valve)

        self.toggle_pump()
        time.sleep(WATERING_DUR_SECONDS * len(openvalves))
        self.toggle_pump()

        for valve in openvalves:
            self.toggle_valve(valve)
        
        GPIO.cleanup()

    def toggle_valve(self, valve: int):
        if GPIO.output(valve, False):
            GPIO.output(valve, True)
        else:
            GPIO.output(valve, False)

    def toggle_pump(self):
        if GPIO.output(PUMP_GPIO, False):
            GPIO.output(PUMP_GPIO, True)
        else:
            GPIO.output(PUMP_GPIO, False)