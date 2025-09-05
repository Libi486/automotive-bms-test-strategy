import random
import time

def read_voltage():
    return round(random.uniform(3.0, 4.2), 2)

def monitor_battery(cycles=10):
    print("Monitoring BMS Voltage Levels...")
    for _ in range(cycles):
        voltage = read_voltage()
        status = "OK" if 3.2 <= voltage <= 4.1 else "ALERT"
        print(f"Voltage: {voltage}V - Status: {status}")
        time.sleep(1)

if __name__ == "__main__":
    monitor_battery()
