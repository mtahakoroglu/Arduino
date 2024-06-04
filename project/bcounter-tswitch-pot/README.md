## Geliştirilmiş İkili Sistem Sayıcı

## Improved Binary Counter

### ChatGPT diyaloğu

<b>Hoca</b>

<p align="justify">Selam ChatGPT. İnternetten yardım alarak bir Arduino kodu yazdım. Bu kod ile Arduino'nun dijital pinlerinden 2, 3, 4, 5, 6, 7, 8, 9 numaralı olanlara bağladığım sekiz adet led ile ikili (binary) sayıcı oluşturdum. Tasarladığım sayıcı (counter) 0'dan 255'e kadar sayabiliyor. Yâni bir byte'lık bir aralığa sâhip. Bu anlattığım kod aşağıda veriliyor.</b>

```
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}  
 
void loop()
{
  for(byte i=0; i<256; i++) {
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
    delay(250); // milliseconds
  }
}
```

<p align="justify">Bu deneyi ve kodu, sayıcıyı istediğim zaman durdurup devam ettirerek ve sayıcı hızını değiştirerek geliştirmek istiyorum. Sayıcı hızını değiştirmek için analog bir girişten okuduğum potansiyometre değerini delay() fonksiyonunda kullanacağım. Bu şekilde sayıcı hızını değiştirebilirim. Aşağıdaki iki satır kodu yukarıdaki kodda uygun yerlere ekleyerek sayıcı hızını değiştirmeyi başardım.</p>

```
int analogPin = A0;
delay(analogRead(analogPin));
```

<p align="justify">Üstten basmalı anahtar (push-button switch) yardımıyla sayıcıyı durdurup devam ettirme konusunda ise istediğim şeyi başaramadım. Bunun için D10 pini diye bilinen Arduino'nun 10 numaralı dijital pinini setup() fonksiyonunun içerisinde</p> 

```
pinMode(10, INPUT_PULLUP);
```

<p align="justify">şeklinde dijital giriş olarak tanımlamak istiyorum. Üstten basmalı anahtarın bir bacağını D10 pinine öbür bacağını GND denilen toprağa bağlacağım. Bu şekilde anahtara bastığımda D10 pini GND olurken anahtardan elimi çektiğimde D10 pini logic 1 yâni 5V olacaktır. Aşağıdaki kodu denedim ama anahtara bastığımda sayıcı durmasına rağmen anahtardan elimi çektiğimde bazen sayıcı saymaya devam ettiği hâlde bazen devam etmedi.</p>

```
int analogPin = A0;
bool flag = true;
byte k = 0;

void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
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

      digitalWrite(2,a);
      digitalWrite(3,b);
      digitalWrite(4,c);
      digitalWrite(5,d);
      digitalWrite(6,e);
      digitalWrite(7,f);
      digitalWrite(8,g);
      digitalWrite(9,h);

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
```

<p align="justify">Bana gömülü sistemler literatüründe kesme denilen İngilizce'de INTERRUPT SERVICE ROUTINE yani ISR olarak geçen mikrodenetleyici programlama tekniğini kullanarak üstten basmalı anahtara (push-button switch) bastığımda sayıcıyı durduran ve yine anahtara (serbest bıraktıktan sonra) tekrar bastığımda sayma işlemini devam ettiren bir Arduino kodu yazabilir misin?</p>