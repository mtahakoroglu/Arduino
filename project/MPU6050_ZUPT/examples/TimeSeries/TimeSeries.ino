#include <MPU6050_ZUPT.h>

MPU6050 mpu6050(Wire);


void setup() {
  Serial.begin(57600);
  Wire.begin();
  mpu6050.begin(); // setting sampling rate as f = 200Hz
  mpu6050.calcGyroOffsets(true);
}

void loop() {
  mpu6050.update();
  Serial.print("temp: "); Serial.print(mpu6050.getTemp());
  Serial.print("\tTime: "); Serial.print(mpu6050.getTimestamp());
  Serial.print("\taccX : "); Serial.print(mpu6050.getAccX());
  Serial.print("\taccY : "); Serial.print(mpu6050.getAccY());
  Serial.print("\taccZ : "); Serial.print(mpu6050.getAccZ());

  Serial.print("\tgyroX : "); Serial.print(mpu6050.getGyroX());
  Serial.print("\tgyroY : "); Serial.print(mpu6050.getGyroY());
  Serial.print("\tgyroZ : "); Serial.print(mpu6050.getGyroZ());
  
  Serial.print("\tangleX : "); Serial.print(mpu6050.getAngleX());
  Serial.print("\tangleY : "); Serial.print(mpu6050.getAngleY());
  Serial.print("\tangleZ : "); Serial.println(mpu6050.getAngleZ());
}