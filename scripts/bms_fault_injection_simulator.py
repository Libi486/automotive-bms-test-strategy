def inject_fault(fault_type):
    print(f"Injecting fault: {fault_type}")
    if fault_type == "overvoltage":
        print("Simulating voltage > 4.2V")
    elif fault_type == "undervoltage":
        print("Simulating voltage < 3.0V")
    elif fault_type == "sensor_failure":
        print("Simulating sensor disconnection")
    else:
        print("Unknown fault")

if __name__ == "__main__":
    inject_fault("overvoltage")
    inject_fault("undervoltage")
    inject_fault("sensor_failure")
