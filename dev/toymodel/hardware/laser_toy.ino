//**************************************************************//
//  Name    : laser_toy                      //
//  Author  : porcherface                                       //
//  Date    : may 2021                                  //
//  Version : 1.0                                               //
//  Notes   : just a toy   //
//          :                                                   //
//**************************************************************//

int b1_pin = 40;
int b2_pin = 42;
int l1_pin = 30;
int l2_pin = 32;

String to_pollo = "$s01$pollo$";
String to_station = "$pollo$s01$";

void setup() {

pinMode(b1_pin, INPUT);
pinMode(b2_pin, INPUT);

pinMode(l1_pin, OUTPUT);
pinMode(l2_pin, OUTPUT);

digitalWrite(l1_pin, LOW);
digitalWrite(l2_pin, HIGH);
  
Serial.begin(115200);
Serial.println("$s01$pollo$init_successful$0xbadcacca");

}

void loop(){
  delay(1000);
  digitalWrite(l1_pin, HIGH);
  Serial.println("$s01$pollo$L1_high$0xbadcacca");
  delay(1000);
  digitalWrite(l1_pin, LOW);
  Serial.println("$s01$pollo$L1_low$0xbadcacca");
}
