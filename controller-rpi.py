# file: temp_led_control.py
import os
import glob
import time
import RPi.GPIO as GPIO

# GPIO Pin Definitions
LED_ABOVE_THRESHOLD = 17  # GPIO17 / Pin 11
LED_BELOW_THRESHOLD = 27  # GPIO27 / Pin 13
TEMPERATURE_THRESHOLD = 22.0  # Celsius

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ABOVE_THRESHOLD, GPIO.OUT)
GPIO.setup(LED_BELOW_THRESHOLD, GPIO.OUT)

# Initialize 1-Wire Sensor (DS18B20)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]  # Auto-detect sensor folder
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        return f.readlines()

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        return float(temp_string) / 1000.0  # Celsius
    return None

try:
    while True:
        temperatureC = read_temp()
        if temperatureC is None:
            print("Error: No DS18B20 sensor found!")
            GPIO.output(LED_ABOVE_THRESHOLD, GPIO.LOW)
            GPIO.output(LED_BELOW_THRESHOLD, GPIO.LOW)
        else:
            print(f"Temperature: {temperatureC:.2f} °C")

            if temperatureC >= TEMPERATURE_THRESHOLD:
                GPIO.output(LED_ABOVE_THRESHOLD, GPIO.HIGH)
                GPIO.output(LED_BELOW_THRESHOLD, GPIO.LOW)
            else:
                GPIO.output(LED_ABOVE_THRESHOLD, GPIO.LOW)
                GPIO.output(LED_BELOW_THRESHOLD, GPIO.HIGH)

        time.sleep(1)

except KeyboardInterrupt:
    print("Shutting down...")
    GPIO.cleanup()
