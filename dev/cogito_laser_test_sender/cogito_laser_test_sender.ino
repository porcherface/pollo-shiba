#include <Arduino.h>
String init_message = "$S01$pollo$INIT$0x0404";

String on_message = "$S01$pollo$E01_HI$0x0404";

void setup() {
  // put your setup code here, to run once:
  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);
  Serial.begin(115200);
  Serial.println(init_message);

  delay(15000);
}

void loop() {
  // put your main code here, to run repeatedly:
}
