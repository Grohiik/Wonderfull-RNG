#include <Arduino.h>

int analog_pin = 14;    // used for ESP32

uint8_t number = 0;
int previous_input = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  for (int i = 0; i < 8; i++) {
    int analogInput = analogRead(analog_pin);
    number = number << 1;

    number = number | (analogInput >= previous_input);

    previous_input = analogInput;
  }
    Serial.println(number);
    number = 0;
}