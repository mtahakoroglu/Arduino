// https://www.youtube.com/watch?v=188hO4R7eN0
int led[] = {2,3,4,5,6,7,8,9};
int n = 8; // number of leds
int delayTime = 50;

void setup() {
  for(int i=0; i<n; i++)
    pinMode(led[i], OUTPUT);
}

void loop() {
  for(int i=0; i<n; i++){
    digitalWrite(led[i], HIGH);
    delay(delayTime);
    digitalWrite(led[i], LOW);
  }
  for(int j=n-1; j>-1; j--){
    digitalWrite(led[j], HIGH);
    delay(delayTime);
    digitalWrite(led[j], LOW);
  }
}