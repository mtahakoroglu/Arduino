void setup() {
  for (int pin = 2; pin <= 9; pin++) {
    pinMode(pin, OUTPUT);
  }
}

void loop() {
  for (byte i = 0; i < 256; i++) {
    byte bits = i;
    for (int pin = 2; pin <= 9; pin++) {
      digitalWrite(pin, bits & 1);
      bits = bits >> 1;
    }
    delay(250);
  }
}