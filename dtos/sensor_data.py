from ..main import (VALVE_GPIO1, VALVE_GPIO2, VALVE_GPIO3, VALVE_GPIO4)

class SensorData:
    def __init__(self, s1: int, s2: int, s3: int, s4: int) -> None:
        self.sensor1 = {"data": s1, "valvegpio": VALVE_GPIO1}
        self.sensor2 = {"data": s2, "valvegpio": VALVE_GPIO2}
        self.sensor3 = {"data": s3, "valvegpio": VALVE_GPIO3}
        self.sensor4 = {"data": s4, "valvegpio": VALVE_GPIO4}