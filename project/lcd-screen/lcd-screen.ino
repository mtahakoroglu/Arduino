#include <LiquidCrystal.h>

//with the arduino pin number it is connected to
const int rs = 13, en = 12, d4 = 11, d5 = 10, d6 = 9, d7 = 8;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

//int analogPin = A0;
//bool flag = true;
//byte k = 0;

void setup()
{
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  //pinMode(10, INPUT_PULLUP);
  //set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  //Print a message to the LCD.
  lcd.print("Binary counter");
}  
 
void loop()
{
  // if (digitalRead(10) == LOW) // continue counting
  //   flag = !flag;
  //while (flag) {
    for(byte i=0; i<256; i++) {
      byte a = i%2;      
      byte b = i/2 %2;     
      byte c = i/4 %2;        
      byte d = i/8 %2;
      byte e = i/16 %2;
      byte f = i/32 %2;
      byte g = i/64 %2;
      byte h = i/128 %2;

      digitalWrite(0,a);
      digitalWrite(1,b);
      digitalWrite(2,c);
      digitalWrite(3,d);
      digitalWrite(4,e);
      digitalWrite(5,f);
      digitalWrite(6,g);
      digitalWrite(7,h);

      //set the cursor to column 0, line 1
      //(note: line 1 is the second row, since counting begins with 0):
      lcd.setCursor(0, 1);
      // print the number of seconds since reset:
      char buffer[50];
      sprintf(buffer, "%i%i%i%i%i%i%i%i - %i", h, g, f, e, d, c, b, a, i);
      lcd.print(buffer);

      delay(500);
      // if (digitalRead(10) == LOW) // anahtara basarsak
      // {
      //   delay(250);
      //   flag = !flag;
      //   k = i;
      //   break;
      // }
    }
  //}
}