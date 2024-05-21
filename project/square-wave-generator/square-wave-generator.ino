int analogPin = A0;
void setup() {
  pinMode(13, OUTPUT);
}
void loop() {
  digitalWrite(13, HIGH);
  delayMicroseconds(analogRead(analogPin));
  digitalWrite(13, LOW);
  delayMicroseconds(analogRead(analogPin));
}