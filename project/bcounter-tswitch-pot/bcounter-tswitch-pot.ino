int analogPin = A0;
bool flag = true;
byte k = 0;

void setup()
{
  for (int pin = 2; pin <= 9; pin++) {
    pinMode(pin, OUTPUT);
  }
  pinMode(10, INPUT_PULLUP);
}
 
void loop()
{
  if (digitalRead(10) == LOW) // continue counting
    flag = !flag;
  while (flag) {
    for(byte i=k; i<256; i++) {
      byte a = i%2;      
      byte b = i/2 %2;     
      byte c = i/4 %2;        
      byte d = i/8 %2;
      byte e = i/16 %2;
      byte f = i/32 %2;
      byte g = i/64 %2;
      byte h = i/128 %2;

      digitalWrite(2, a);
      digitalWrite(3, b);
      digitalWrite(4, c);
      digitalWrite(5, d);
      digitalWrite(6, e);
      digitalWrite(7, f);
      digitalWrite(8, g);
      digitalWrite(9, h);

      delay(analogRead(analogPin));
      if (digitalRead(10) == LOW) // anahtara basarsak
      {
        delay(500);
        flag = !flag;
        k = i;
        break;
      }
    }
  }
}