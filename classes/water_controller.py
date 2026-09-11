import time

from gpiozero import DigitalOutputDevice

from config import PUMP_GPIO, WATERING_DUR_SECONDS, PUMP_LOW_PRESSURE
from dtos.sensor_data import SensorData


class WaterController:
    def __init__(self):
        self.pump = DigitalOutputDevice(PUMP_GPIO, initial_value=False)
        self.valves: dict[int, DigitalOutputDevice] = {}

    def water(self, sensor_data: SensorData):
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
                self.toggle_pump()
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

        self.pump.close()
        for valve in self.valves.values():
            valve.close()

    def toggle_valve(self, valve: int):
        device = self.valves.setdefault(
            valve, DigitalOutputDevice(valve, initial_value=False)
        )
        if device.is_active:
            device.off()
        else:
            device.on()

    def toggle_pump(self):
        if self.pump.is_active:
            self.pump.off()
        else:
            self.pump.on()