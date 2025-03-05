#include <OneWire.h>
#include <DallasTemperature.h>

// Pin Definitions
#define ONE_WIRE_BUS 2   // Data pin connected to DS18B20
#define LED_ABOVE_THRESHOLD 7   // LED for temp above threshold
#define LED_BELOW_THRESHOLD 4  // LED for temp below threshold

// Temperature threshold
const float temperatureThreshold = 22;

// Setup OneWire and DallasTemperature
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  
  // Enable internal pull-up resistor on the DS18B20 data pin
  pinMode(ONE_WIRE_BUS, INPUT_PULLUP);

  // Initialize the temperature sensor
  sensors.begin();

  // Set up LEDs
  pinMode(LED_ABOVE_THRESHOLD, OUTPUT);
  pinMode(LED_BELOW_THRESHOLD, OUTPUT);
}

void loop() {
  sensors.requestTemperatures(); // Request temperature from DS18B20
  float temperatureC = sensors.getTempCByIndex(0); // Get temperature

  if (temperatureC == DEVICE_DISCONNECTED_C) {
    Serial.println("Error: No DS18B20 sensor found!");
    Serial.println(DEVICE_DISCONNECTED_C);
    return;
  }

  // Debug output to Serial Monitor
  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.println(" °C");

  // LED Logic: Only one LED is on at a time
  if (temperatureC >= temperatureThreshold) {
    digitalWrite(LED_ABOVE_THRESHOLD, HIGH);
    digitalWrite(LED_BELOW_THRESHOLD, LOW);
  } else {
    digitalWrite(LED_ABOVE_THRESHOLD, LOW);
    digitalWrite(LED_BELOW_THRESHOLD, HIGH);
  }

  delay(1000); // Read temperature every second
}
