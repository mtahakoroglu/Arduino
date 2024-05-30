#include <MPU6050_ZUPT.h>

MPU6050 mpu6050(Wire);

void setup() {
  Serial.begin(57600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
}

void loop() {
  mpu6050.update();
  float roll = mpu6050.getAngleX();
  float pitch = mpu6050.getAngleY();
  float yaw = mpu6050.getAngleZ();
  Serial.print("Roll: "); Serial.print(roll);
  Serial.print(" Pitch: "); Serial.print(pitch);
  Serial.print(" Yaw: "); Serial.println(yaw);
}