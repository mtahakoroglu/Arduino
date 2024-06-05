int analogPin = A0; 
volatile bool counting = true; // Counter state (start/stop)
volatile unsigned long lastDebounceTime = 0; // Debounce time tracking
const unsigned long debounceDelay = 200; // Debounce delay
byte i = 0; // Counter variable

void setup() {
  // Set LED pins as output
  for (int pin = 2; pin <= 9; pin++) {
    pinMode(pin, OUTPUT);
  }

  // Set push-button pin as input with pull-up resistor
  pinMode(10, INPUT_PULLUP);

  // Attach interrupt to pin 10, triggered on falling edge
  attachInterrupt(digitalPinToInterrupt(10), toggleCounting, FALLING);

  // Initialize Serial Monitor for debugging
  Serial.begin(9600);
}

void loop() {
  if (counting) {
    // Display the binary count on LEDs
    for (int bit = 0; bit < 8; bit++) {
      digitalWrite(2 + bit, (i >> bit) & 0x01);
    }

    // Increment the counter
    i++;
    delay(analogRead(analogPin)); // Adjust speed with potentiometer

    // Reset counter after reaching 255
    if (i >= 256) {
      i = 0;
    }
  }

  // Debugging output to Serial Monitor
  Serial.print("Counting: ");
  Serial.println(counting);
  delay(500); // Small delay for readability in Serial Monitor
}

// Interrupt Service Routine to toggle counting state
void toggleCounting() {
  unsigned long currentTime = millis();
  // Debounce: ignore if interrupt happened within debounceDelay
  if (currentTime - lastDebounceTime > debounceDelay) {
    counting = !counting;
    lastDebounceTime = currentTime;
    Serial.println("Button pressed! Toggling counting state.");
  }
}
