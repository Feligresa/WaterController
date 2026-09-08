class TestGPIO:
    IN = 0
    OUT = 1
    BOARD = 10
    BCM = 11

    def setmode(self, mode: int):
        mode_str = {10: "BOARD", 11: "BCM"}.get(mode, "UNKNOWN")
        print(f"GPIO setmode: {mode_str}")

    def setup(self, pin: int, mode: int):
        mode_str = {10: "BOARD", 11: "BCM"}.get(mode, "UNKNOWN")
        print(f"GPIO setup: Pin {pin}, Mode {mode_str}")

    def output(self, pin: int, state: bool):
        print(f"GPIO output: Pin {pin} -> {state}")

    def cleanup(self):
        print("GPIO cleanup")