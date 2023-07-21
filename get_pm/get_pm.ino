#define DHTPIN 3
#include "Arduino_SensorKit.h"

#define Environment Environment_I2C

int dust_pin = 8;
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 30000; // sample 30 seconds
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;

float calc_concentration(float ratio) {
  return 1.1*pow(ratio, 3) - 3.8*pow(ratio, 2) + 520*ratio + 0.62;
}

void setup() {
  Serial.begin(9600);
  Wire.begin();
  Environment.begin();
  pinMode(dust_pin, INPUT);
  starttime = millis();
}

void loop() {
  duration = pulseIn(dust_pin,  INPUT);
  lowpulseoccupancy = lowpulseoccupancy + duration;
  if ((millis() - starttime) > sampletime_ms) {
    ratio = lowpulseoccupancy/(sampletime_ms * 10.0);
    concentration = calc_concentration(ratio);
    float temp = Environment.readTemperature();
    float humidity = Environment.readHumidity();
    Serial.print(millis());
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.print(humidity);
    Serial.print(",");
    Serial.println(concentration);
    lowpulseoccupancy = 0;
    starttime = millis();

  }

}