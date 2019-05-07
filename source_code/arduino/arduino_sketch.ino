#include <FastLED.h>

#define NUM_LEDS 88

#define R_INDEX 0
#define G_INDEX 1
#define B_INDEX 2


#define LED_PIN 8
#define MICROPHONE_PIN 5

CRGB leds[NUM_LEDS];
byte serialArrived[3];
byte microphoneValue = 0;
int color[6][3];

void setup() 
{
  Serial.begin(9600);
  while (!Serial) continue;

  FastLED.addLeds<WS2811, LED_PIN, GRB>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.setBrightness(100);
  pinMode(LED_PIN, OUTPUT);
  
  color[1][R_INDEX] = 255;
  color[1][G_INDEX] = 0;
  color[1][B_INDEX] = 0;

  color[2][R_INDEX] = 0;
  color[2][G_INDEX] = 255;
  color[2][B_INDEX] = 0;

  color[3][R_INDEX] = 0;
  color[3][G_INDEX] = 0;
  color[3][B_INDEX] = 255;

  color[4][R_INDEX] = 148;
  color[4][G_INDEX] = 0;
  color[4][B_INDEX] = 211;

  color[5][R_INDEX] = 0;
  color[5][G_INDEX] = 0;
  color[5][B_INDEX] = 0;
}

void loop() 
{
  
  if (Serial.available() > 0) 
  {
    for (int i = 0; i < 3; i++)
    {
        serialArrived[i] = Serial.read();
    }
    
    if (serialArrived[0] == 255)
    {
      switch(serialArrived[1]) 
      {
        case 128: clearPixels(); break;
        case 129: fillColor(0, color[serialArrived[2]][R_INDEX], color[serialArrived[2]][G_INDEX], color[serialArrived[2]][B_INDEX]); break;
        case 130: fillColor(1, color[serialArrived[2]][R_INDEX], color[serialArrived[2]][G_INDEX], color[serialArrived[2]][B_INDEX]); break;
        case 131: fillColor(2, color[serialArrived[2]][R_INDEX], color[serialArrived[2]][G_INDEX], color[serialArrived[2]][B_INDEX]); break;
        case 132: fillColor(3, color[serialArrived[2]][R_INDEX], color[serialArrived[2]][G_INDEX], color[serialArrived[2]][B_INDEX]); break;
      }
      
    } 
    if (serialArrived[0] < NUM_LEDS && serialArrived[1] < NUM_LEDS)
    {
      setPixel(serialArrived[0], serialArrived[1], serialArrived[2]);
    }
  }
  delay(500);
}

void setPixel(byte indexTurnOn, byte indexTurnOff, byte colorIndex) 
{
    if (indexTurnOn == -1 || indexTurnOff == -1 || colorIndex == -1 || indexTurnOn == 255 || indexTurnOff == 255) {
      Serial.print("e\n");
      return;
    }
      
    leds[indexTurnOff].r = 0;
    leds[indexTurnOff].g = 0;
    leds[indexTurnOff].b = 0;
    
    leds[indexTurnOn].r = color[colorIndex][R_INDEX];
    leds[indexTurnOn].g = color[colorIndex][G_INDEX];
    leds[indexTurnOn].b = color[colorIndex][B_INDEX];
    
    FastLED.show();
}

void clearPixels()
{
  for (int i = 0; i < NUM_LEDS; i++) 
  {
    leds[i].r = 0;
    leds[i].g = 0;
    leds[i].b = 0;
  }
  FastLED.show();
}

void fillColor(int stripeNumber, int red, int green, int blue)
{
  digitalWrite(12, HIGH);
  for (int i = 0; i < 200000; i++) 
  {
    microphoneValue = digitalRead(MICROPHONE_PIN);
    
    if (microphoneValue) break;
  }
  digitalWrite(12, LOW);
    if (!microphoneValue) {
      Serial.write('2');
      delay(500);
      return;
    }
    Serial.write('1');
    delay(500);

    while(Serial.available() > 0)
    {
      Serial.read();
    }
    
     for (int i = (stripeNumber + 1) * 22 - 1; i >= stripeNumber * 22; i-- )
    {
      delay (50);
      leds[i].r = red;
      leds[i].g = green;
      leds[i].b = blue;
      FastLED.show();
    }

    for (int i = (stripeNumber + 1) * 22 - 1; i >= stripeNumber * 22; i-- )
    {
      delay (50);
    
      leds[i].r = 0;
      leds[i].g = 0;
      leds[i].b = 0;
    
      FastLED.show();
    }
      delay(100);
    for (int i = (stripeNumber + 1) * 22 - 1; i >= stripeNumber * 22; i-- )
    {
      leds[i].r = red;
      leds[i].g = green;
      leds[i].b = blue;
    }
    FastLED.show();
    delay(100);
    for (int i = (stripeNumber + 1) * 22 - 1; i >= stripeNumber * 22; i-- )
    {
      leds[i].r = 0;
      leds[i].g = 0;
      leds[i].b = 0;
    }
    FastLED.show();
      delay (100);
      for (int i = (stripeNumber + 1) * 22 - 1; i >= stripeNumber * 22; i-- )
    {
      leds[i].r = red;
      leds[i].g = green;
      leds[i].b = blue;
    }
    FastLED.show();
}
