// mandy wu

#include <Arduino.h>
#include <MeMCore.h> 

MeUltrasonicSensor ultrasonic(PORT_3);

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("Distance :");
  Serial.print(ultrasonic.distanceCm()); 
  Serial.println(" cm");
}
