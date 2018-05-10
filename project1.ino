//#include <MQ135.h>


#include <dht.h>

dht DHT;

#define DHT11_PIN 7

int airquality = 0;
void setup()
{
  Serial.begin(9600);

}
void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print(DHT.temperature);
  Serial.print(" ");
  Serial.print(DHT.humidity);
  int sensorValue = analogRead(A0);
  Serial.print(" ");
  Serial.print(sensorValue);
  Serial.println();
  delay(2000);
}


