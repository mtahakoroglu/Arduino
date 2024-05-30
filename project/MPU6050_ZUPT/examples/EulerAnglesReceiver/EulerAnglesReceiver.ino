#include <Wire.h>

// Define variables to store Euler angles
float roll, pitch, yaw;

void setup() {
  // Initialize serial communication
  Serial.begin(57600);
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    // Read the incoming data
    String data = Serial.readStringUntil('\n');
    
    // Parse the data and extract roll, pitch, and yaw
    int rollIndex = data.indexOf("Roll: ");
    int pitchIndex = data.indexOf("Pitch: ");
    int yawIndex = data.indexOf("Yaw: ");
    
    // Extract the Euler angles from the string
    roll = data.substring(rollIndex + 6, pitchIndex).toFloat();
    pitch = data.substring(pitchIndex + 8, yawIndex).toFloat();
    yaw = data.substring(yawIndex + 6).toFloat();
    
    // Print the received Euler angles
    Serial.print("Received Euler Angles: ");
    Serial.print("Roll: ");
    Serial.print(roll);
    Serial.print(" Pitch: ");
    Serial.print(pitch);
    Serial.print(" Yaw: ");
    Serial.println(yaw);
  }
}
