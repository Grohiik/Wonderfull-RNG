#include <Arduino.h>

int analog_pin = 14;    // used for ESP32
bool posetive_edge = false;

unsigned long oldTime = 0;
int numberOfCycles = 0;

#define upperlevel 2200
#define lowerlevel 2000


void setup() {
  Serial.begin(115200);
}

void loop() {
  int analogInput = analogRead(analog_pin);
  unsigned long currentTime = micros();

  
  if (analogInput > 2200 && !posetive_edge) {
    posetive_edge = true;
    numberOfCycles++;
  } else if (analogInput < 2000){
    posetive_edge = false;
  }

  if (numberOfCycles >= 5) {
    numberOfCycles = 0;
    Serial.println(currentTime-oldTime);
    oldTime = currentTime;
  }
}