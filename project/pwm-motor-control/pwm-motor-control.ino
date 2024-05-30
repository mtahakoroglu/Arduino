#include <Servo.h>
Servo motor;
int analogPin = A2;

void setup() {
  motor.attach(9);
}

void loop() {
   int x = analogRead(analogPin);
   // int y = map(x, 0, 1023, 0, 180);
   int z = map(x, 50, 1023, 1000, 2000);
   // motor.write(y);
   motor.writeMicroseconds(z);
}